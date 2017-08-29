#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@version: Python3.6
@author: yanlong.liang
@software: PyCharm
@file: vivol.py
@time: 2017/8/15 下午5:28

The very beginning mind itself is 
    the most accomplished mind of true enlightenment.
"""
#这仅仅是一个测试

from tornado import web, httpserver, ioloop

class LoginHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("vivol".center(100, '*'))

application = web.Application([
    (r'/', LoginHandler),
])

if __name__ == '__main__':
    application.listen(8888)
    ioloop.IOLoop.instance().start()




