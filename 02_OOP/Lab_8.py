
from abc import ABC, abstractmethod


class Logger(ABC):
	@abstractmethod
	def log_operation(self) -> str: pass
	
	
class Creator(ABC):
	@abstractmethod
	def creator_method(self) -> Logger: pass
	
	
class PLS_Logger(Logger):
	def log_operation(self) -> str:
		return 'PLS logs data were logged..!'
	
	
class System_Logger(Logger):
	def log_operation(self) -> str:
		return 'System logs data were logged..!'
	
	
class PLS_Logger_Creator(Creator):
	def creator_method(self) -> Logger:
		return PLS_Logger()
	
	
class System_Logger_Creator(Creator):
	def creator_method(self) -> Logger:
		return System_Logger()
	
	
def main():
	print('Application launching the system log..!')
	system_log = System_Logger_Creator()
	print(system_log.creator_method().log_operation())
	print('===============================')
	
	print('Application launching the PLS log..!')
	pls_log = PLS_Logger_Creator()
	print(pls_log.creator_method().log_operation())
	print('===============================')
	
	
main()