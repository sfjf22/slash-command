#!/usr/bin/env python

import json
import random
import sys
import time
import BaseHTTPServer

HOST_NAME   = '127.0.0.1'
PORT_NUMBER = 8080

# function listening to the request
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

        if 'drawrandomcard' in s.path:
            num = draw_random_playing_card()
            print "Num drawn : %s" % str(num)
            s.wfile.write("Card drawn: %s" % str(num))

def draw_random_playing_card():
    return random.randint(0, 51)

if __name__ == '__main__':
    server = BaseHTTPServer.HTTPServer
    httpd  = server((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Listening - %s:%s" % (HOST_NAME, PORT_NUMBER)

    try:
        httpd.serve_forever()
    except:
        print "Error : ", sys.exc_info()[0]
    httpd.server_close()
    sys.exit(0)

