# -*- coding: utf-8 -*-

"""
   程式說明請參閱《超圖解Python物聯網實作入門》17-31頁
"""

from machine import Pin
import socket, gc

passcode = 'zzzzz'   # 請自行修改程式碼
passed = False

led = Pin(2, Pin.OUT, value=1)

HOST = '0.0.0.0'
PORT = 80

httpHeader = b"""\
HTTP/1.0 200 OK

Welcome to MicroPython!
"""

feedback = b'''\
HTTP/1.1 200 OK

OK!
'''

def err(socket, code, msg):
    socket.write("HTTP/1.1 "+code+" "+msg+"\r\n\r\n")
    socket.write("<h1>"+msg+"</h1>")

def parse(str):
    arr = str.split('&')
    args = {}

    for item in arr:
        data = item.split('=')
        args[data[0]] = data[1]
    
    return args

def query(client, path):
    cmd, qstr = path.split('?')

    if cmd == 'sw':
        args = parse(qstr)
                
        try:
            key = args['key']
            state = args['led']

            if key == passcode:
                if state == 'on':
                    led.value(0)
                else:
                    led.value(1)
                    
                client.send(feedback)
            else:
                err(client, "400", "Bad Request")
        except:
            err(client, "400", "Bad Request")

    else:
        err(client, "400", "Bad Request")

def handleRequest(client):
    req = client.recv(1024).decode('utf-8')
    firstLine = req.split('\r\n')[0]
    print(firstLine)
    
    httpMethod = ''
    path = ''

    try:
        httpMethod, path, httpVersion = firstLine.split()

        print('Method:', httpMethod)
        print('Path:', path)
        print('Version:', httpVersion)

        del httpVersion
    except:
        pass

    del firstLine
    del req

    if httpMethod == 'GET':
        queries = path.strip('/')

        if '?' in queries:
            query(client, queries)
        else:
            client.send(httpHeader)
    else:
        err(client, "501", "Not Implemented")

def main():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    print('Web server running on port', PORT)

    while True:
        client = s.accept()[0]
        handleRequest(client)
        client.close()
        
        print('Free RAM before GC:', gc.mem_free())
        gc.collect()
        print('Free RAM after GC:', gc.mem_free())

main()