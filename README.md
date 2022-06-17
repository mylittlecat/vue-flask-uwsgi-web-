# vue-flask-uwsgi-web-
简单实现的web框架雏形，目标是搭建一个随自己喜好的风格只被自己定义的页面
- 安装vue依赖
> cd frontend
> 
> npm install
- 编译vue
> npm run build
- 前端软链到flask目录
> cd mw
> 
> ln -s ../frontend/dist/static ./
- 安装flask模块
> pip install flask
- 启动
> cd mw
> 
> ../uwsgi --http 127.0.0.1:8000 --master -p 4 -w snack:app
- 浏览器访问http://127.0.0.1:8000
