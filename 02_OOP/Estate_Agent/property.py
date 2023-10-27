

class Property:
	def __init__(self, square_feet='', bedrooms='', bathrooms='', *args, **kwargs):
		self.bathrooms = bathrooms
		self.bedrooms = bedrooms
		self.square_feet = square_feet
		
	def display(self):
		print(f'General Inforamtion\n'
		      f'===================\n'
		      f'Square Feet: {self.square_feet}\n'
		      f'Bedrooms: {self.bedrooms}\n'
		      f'Bathrooms: {self.bathrooms}')
		
	def prompt_init():
		return dict(
			square=input('Square Feet: '),
			bedrooms=input('Bedrooms: '),
			bathrooms=input('Bathrooms: ')
		)
	
	prompt_init = staticmethod(prompt_init)

