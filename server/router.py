#!/usr/bin/python2.7
# *-* coding:utf-8 *-* 

import os
import sys
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define,options

from loader import Loader

define('port',default = 8999,help='this is default port',type = int)

if __name__ == "__main__":
	
	Loader.load()

	from gl import LOG
	from transcode import Transcode

	tornado.options.parse_command_line()

	application = tornado.web.Application([
		(r'/transcode',Transcode),
	],)

	http_server = tornado.httpserver.HTTPServer(application)

        http_server.listen(options.port)

	LOG.info('local_api is started,port is [%s]' % options.port)

        tornado.ioloop.IOLoop.instance().start()

