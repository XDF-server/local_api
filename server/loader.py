# *-* coding:utf-8 *-*

from base import Base
from base import Logger
from base import Configer
from doit import Doit

class Loader(object):
	
	@staticmethod
	def load():

		configer = Configer('../config.ini')

		log_info = configer.get_configer('LOG','info')
		log_path = configer.get_configer('LOG','path')
		log_format = '%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s'

		logger = Logger(info = log_info,path = log_path,format = log_format)
		LOG = logger.get_logger()

		doit = Doit()
