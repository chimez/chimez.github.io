+++
title = "python 的 xmlrpc 简单用法"
date = 2019-10-02T00:00:00+08:00
tags = ["python"]
categories = ["计算机"]
draft = false
+++

## <span class="section-num">1</span> 服务端 {#服务端}

```python
from xmlrpc.server import SimpleXMLRPCServer

QUIT_SERVER = False


def is_even(n):
    return n % 2 == 0


def kill():
    global QUIT_SERVER
    QUIT_SERVER = True
    return 1


def main():
    server = SimpleXMLRPCServer(("localhost", 8000))
    print("Listening on port 8000...")
    server.register_function(is_even, "is_even")
    server.register_function(kill, "kill")
    global QUIT_SERVER
    while not QUIT_SERVER:
        server.handle_request()

if __name__ == '__main__':
    main()
```


## <span class="section-num">2</span> 客户端 {#客户端}

```python
import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("3 is even: %s" % str(proxy.is_even(3)))
    print(proxy.kill())
```
