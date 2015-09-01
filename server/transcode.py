# *-* coding:utf-8 *-*

import json
import urllib2
import time
from hashlib import sha1
from tornado import web

from base import Base
from gl import LOG
from doit import Doit

class Transcode(web.RequestHandler):
	
	def post(self):

		for i in range(1):
			LOG.info('API IN[%s]' % (self.__class__.__name__))
                        LOG.info('PARAMETER IN[%s]' % self.request.arguments)

                        ret = {'code':'','message':''}
			essential_keys = set(['filepath','timestamp','secret'])

			if Base.check_parameter(set(self.request.arguments.keys()),essential_keys):
				ret['code'] = 1
				ret['message'] = 'invalid parameter'
				LOG.error('ERROR[in parameter invalid]')
				break
			
			filepath = ''.join(self.request.arguments['filepath'])
			timestamp = ''.join(self.request.arguments['timestamp'])
			secret = ''.join(self.request.arguments['secret'])

			if Base.empty(filepath) or Base.empty(timestamp) or Base.empty(secret):
					ret['code'] = 1
					ret['message'] = 'invalid parameter'
					LOG.error('ERROR[parameter empty]')
					break
			
			key = filepath + timestamp
			secret_key = sha1(key).hexdigest()
			
			if secret == secret_key:
				doit = Doit()
				doit.transcode(filepath)
				LOG.info('QUEUE[put transcode task(%s)}' % filepath)

				ret['code'] = 0
				ret['message'] = 'success'
				break
                        else:
                                ret['code'] = 4
                                ret['message'] = 'secure key error'
                                LOG.error('ERR[secure key error]')
                                break

                self.write(json.dumps(ret))
                LOG.info('PARAMETER OUT[%s]' % ret)
                LOG.info('API OUT[%s]' % (self.__class__.__name__))
