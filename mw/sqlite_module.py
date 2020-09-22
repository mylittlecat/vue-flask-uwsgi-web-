# coding: UTF-8
import os, sqlite3, fcntl, logging
# from log_module import setup_logger
# from utility import load_config

# setup_logger('flask_engine')
# logger = logging.getLogger('flask_engine_log')

SQLITECON = None
sqlite_path = '/home/bijianyu/disk1/venv_flask_app/db/snacks.db'
def init_sqlite():
    '''
    初始化sqlite3数据库连接
    '''
    global SQLITECON
    if not SQLITECON:  # app_main和machine_state中都会初始化sqlite3,以防多次初始化,初始化前需要判断
        # sqlite_path = load_config('SQLITE', 'PATH')
        SQLITECON = sqlite3.connect(sqlite_path, check_same_thread=False)

g_sqlite_file_lock='/tmp/sqlite_file_lock'
def new_send_cmd(cmd, messageid):
    '''
    new_send_cmd function is send anything conf sql
    cmd: conf sql from web
    messageid: 1 is read sql(select), not 1 is write sql(insert, update, delete)
    '''
    global SQLITECON
    global g_sqlite_file_lock
    rows = None
    if not SQLITECON:  # app_main...machine_state..................sqlite3,.....................,.......
        # sqlite_path = load_config('SQLITE', 'PATH')
        SQLITECON = sqlite3.connect(sqlite_path, check_same_thread=False)
    try:
        if not os.path.exists(g_sqlite_file_lock):
            os.mknod(g_sqlite_file_lock)
    except:
        pass
        # logger.exception('Error')
    with open(g_sqlite_file_lock, 'r') as fp:
        fcntl.flock(fp.fileno(), fcntl.LOCK_EX)  # locks the file
        cur = SQLITECON.cursor()
        cmd = cmd.encode('utf-8')
        try:
            cur.execute(cmd)
            if messageid == 1:
                rows = cur.fetchall()
            else:
                SQLITECON.commit()
        except sqlite3.Error as e:
            pass
            # logger.exception("new_send_cmd oper db cmd=%s", cmd)
    if rows == None:
        rows = []
    return rows
