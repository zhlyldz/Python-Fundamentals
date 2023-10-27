
from property import Property
from utilities import get_valid_input


class Apartment(Property):
	def __init__(self, balcony='', laundry='', *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.laundry = laundry
		self.balcony = balcony
		
	def display(self):
		super().display()
		print(f'Balcony: {self.balcony}\n'
		      f'Laundry: {self.laundry}')
		
	def prompt_init():
		parent_init = Property.prompt_init()
		
		balcony = get_valid_input(
			'Does apartment have a balcony?',
			('yes', 'no')
		)
		laundry = get_valid_input(
			'What laundry type do you prefer?',
			('coin', 'credit card', 'none')
		)
		
		parent_init.update({
			'laundry': laundry,
			'balcony': balcony
		})
		
		return parent_init
	
	prompt_init = staticmethod(prompt_init)
	