
from property import Property
from utilities import get_valid_input


class House(Property):
	def __init__(self, number_stories='', garage='', fenced='', pool='', *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.pool = pool
		self.fenced = fenced
		self.garage = garage
		self.number_stories = number_stories
		
	def display(self):
		super().display()
		print(f'Number of Stories: {self.number_stories}\n'
		      f'Garage: {self.garage}\n'
		      f'Fenced: {self.fenced}\n'
		      f'Pool: {self.pool}')
		
	def prompt_init():
		parent_init = Property.prompt_init()
		
		number_stories = input('How many stories do you want?')
		garage = get_valid_input(
			'Do you want to garage',
			('attach', 'detached', 'none')
		)
		fenced = get_valid_input(
			'Do you prefer to fenced?',
			('yes', 'no')
		)
		pool = get_valid_input(
			'Do you prefer to pool?',
			('yes', 'no')
		)
		
		parent_init.update({
			'number_stories': number_stories,
			'garage': garage,
			'fenced': fenced,
			'pool': pool
		})
		
		return parent_init
	
	prompt_init = staticmethod(prompt_init)