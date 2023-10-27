
from property import Property
from utilities import get_valid_input
from apartment import Apartment
from house import House


class Rental(Property):
	def __init__(self, furnished='', extras='', rent='', *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.rent = rent
		self.extras = extras
		self.furnished = furnished
		
	def display(self):
		super().display()
		print(f'Rent Detail\n'
		      f'=================\n'
		      f'Rent: {self.rent}\n'
		      f'Furnished: {self.furnished}\n'
		      f'Extras: {self.extras}')
		
	def prompt_init():
		return dict(
			furnished=get_valid_input('Has apartment furnished', ('yes', 'no')),
			extras=input('What are the extras prefer?'),
			rent=input('What is the estimated montly rent?')
		)
	
	prompt_init = staticmethod(prompt_init)
	
	
class ApartmentRental(Apartment, Rental):
	def prompt_init():
		init = Apartment.prompt_init()
		init.update(Rental.prompt_init())
		
		return init
	
	prompt_init = staticmethod(prompt_init)
	
	
class HouseRental(House, Rental):
	def prompt_init():
		init = House.prompt_init()
		init.update(Rental.prompt_init())
		
		return init
		
	prompt_init = staticmethod(prompt_init)