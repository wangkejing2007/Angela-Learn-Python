# Flask

###### 一、程式架構

```python
from flask import Flask #基本架構
app = Flask(__name__)

@app.route('/hello') #建立路由
def hello():
    return '這裡是回應的訊息!'

if __name__ == '__main__':
    app.run()
```

二、執行Flask程式

```python
D:\flask>python hello.py
```

