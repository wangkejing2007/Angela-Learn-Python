## 在D:\microweb建立虛擬環境(env)
D:\microweb>python -m venv env #建立虛擬環境
D:\microweb>env\scripts\activate #啟動虛擬環境
(env) D:\microweb>deactivate #退出虛擬環境
### 在虛擬環境安裝flask套件(虛擬伺服器)
D:\microweb>env\scripts\activate #啟動虛擬環境
(env) D:\microweb>pip install flask #安裝flask
### 部署Python(產生requirements.txt檔案)
(env) D:\microweb\src>pip freeze > requirements.txt

## 部署Heroku空間檔案結構
D:\microweb\src>Procifile : web: gunicorn hello:app
D:\microweb\src>requirements.txt : gunicorn
D:\microweb\src>runtime.txt : python-3.8.3

## 用Git推送到Heroku空間
D:\microweb\src>git init #初始化本地端儲存庫
D:\microweb\src>heroku git:remote -a my-hello-bot #設定遠端儲存庫
D:\microweb\src>git add . #步驟1
D:\microweb\src>git commit -am "2020-01-15-1" #步驟2
D:\microweb\src>git push heroku master #步驟3
D:\microweb\src>heroku open #步驟4