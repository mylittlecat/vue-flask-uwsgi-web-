#!/usr/bin/python
# coding:utf-8
from flask import Flask, render_template, request, jsonify, Blueprint, session, send_from_directory,make_response, abort
from sqlite_module import new_send_cmd
import time
# import sqlite3
# conn = sqlite3.connect('example.db')

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/getAllSnack')
def getAllSnack():
    sqlStr = 'select snack_name from snacks'
    res = new_send_cmd(sqlStr, 1)
    rows = []
    for elem in res:
        row = {}
        row['value'] = elem[0]
        row['label'] = elem[0]
        rows.append(row)
    return jsonify({'status': 1, 'data': rows})

@app.route('/getGroupedSnack')
def getGroupedSnack():
    sqlStr = 'select pick_snack, count(pick_snack) from picks group by pick_snack;'
    res = new_send_cmd(sqlStr, 1)
    rows = []
    for elem in res:
        row = {}
        row['name'] = elem[0]
        row['hot'] = elem[1]
        rows.append(row)
    return jsonify({'status': 1, 'data': rows})


@app.route('/addSnack', methods = ['GET', 'POST'])
def addSnack():
    if request.method == 'GET':
        snacks = request.args.get('snacks')
        # loginuser = request.args.get('loginuser', '', type=str)
        # beginTimeFlag = request.args.get('beginTimeFlag', '', type=str)
    elif request.method == 'POST':
        post_data = request.get_json()
        # deviceType = post_data['deviceType']
        snacks = post_data['snacks']
        # beginTimeFlag = post_data.get('beginTimeFlag', '', type=str)

    sqlStr = 'select snack_name from snacks'
    res = new_send_cmd(sqlStr, 1)
    if len(res) != 0:
        snacklist = [elem[0] for elem in res]
        all_snacks = set(snacklist)
    new_snacks = set([elem for elem in snacks.split(',') if elem])
    new_add_snacks = [elem for elem in new_snacks if elem not in all_snacks]

    sqlStr2 = 'insert into snacks (snack_name) values (\'%s\')' % ("'),('".join(new_add_snacks))
    res2 = new_send_cmd(sqlStr2, 2)
    insertValueList = []
    for elem in new_add_snacks:
        insertValueList.append("('%s','%s')" % (elem, getTimePoint(),))
    sqlStr3 = 'insert into picks (pick_snack, pick_date) values %s' % (",".join(insertValueList))
    res3 = new_send_cmd(sqlStr3, 2)
    return jsonify({'status': 1})


def getTimePoint(*now):
    '''
    接受一个数值型时间值或默认为当前时间值
    返回一个时间字符串,格式形如:2017-12-26 10:22:13
    '''
    if len(now) == 1:
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now[0]))
    elif len(now) == 0:
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
