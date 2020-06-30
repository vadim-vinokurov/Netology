import datetime
from time import sleep
class context_manager:

	def __enter__(self):
		self.begin_date_time = datetime.datetime.now()
		print(self.begin_date_time)
		sleep(10)
		self.end_date_time = datetime.datetime.now()
		print(self.end_date_time)
		self.result = self.end_date_time - self.begin_date_time
		return self

	def total_time(self):
		return self.result

	def __exit__(self, exc_type, exc_val, exc_tb):
		if exc_type == True:
			return exc_type

with context_manager() as manager:
	print(f'\nНа выполнение программы затратилось - {manager.total_time()} ')