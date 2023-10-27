
# Kullanıcı final, ödev, vize notu ayrıca öğrencini adını ve soyadını giricek. girilen bu bilgieler "sinav_notlari.txt" dosyasında saklanılacak
# Örnek Format
# ad soyad:vize,final,ödev
# not hesaplanılacak
# hesaplanılan notlar "sonuclar.txt" dosyasında saklanılacak
# sınav sonuçları, ortalamlarını listle işlemleri yapıalcak

def create_exam_grades() -> None:
	file = open(file='exam_grades.txt', mode='w', encoding='utf-8')
	file.close()
	
	
def take_information():
	first_name = input('Please type into first name: ')
	last_name = input('Please type into last name: ')
	midterm = float(input('Midterm Grade: '))
	final = float(input('Final Grade: '))
	homework = float(input('Homework Grade: '))
	
	with open(file='exam_grades.txt', mode='a', encoding='utf-8') as file:
		file.write(f'{first_name} {last_name}:{midterm},{final},{homework}\n')


# Burak Yılmaz:34,56,78
# return Burak Yılmaz: FF
def calculate_grade(row: str) -> str:
	values = row.split(':')
	
	full_name = values[0]
	grades_list = values[1].split(',')
	
	ort = float(grades_list[0]) * 0.3 + float(grades_list[1]) * 0.6 + float(grades_list[2]) * 0.1
	
	if 90 <= ort <= 100:
		return f'{full_name}: AA'
	elif 85 <= ort <= 89:
		return f'{full_name}: BA'
	elif 80 <= ort <= 84:
		return f'{full_name}: BB'
	elif 75 <= ort <= 79:
		return f'{full_name}: CB'
	elif 70 <= ort <= 74:
		return f'{full_name}: CC'
	elif 65 <= ort <= 69:
		return f'{full_name}: CD'
	elif 60 <= ort <= 64:
		return f'{full_name}: DD'
	elif 55 <= ort <= 59:
		return f'{full_name}: DC'
	elif 50 <= ort <= 54:
		return f'{full_name}: FD'
	else:
		return f'{full_name}: FF'
	
	
def read_exam_grades() -> list:
	with open(file='exam_grades.txt', mode='r', encoding='utf-8') as file:
		lst = []
		for row in file:
			lst.append(calculate_grade(row))
	
	return lst


def register_result(lst: list):
	with open(file='result.txt', mode='w', encoding='utf-8') as file:
		for i in lst:
			file.write(i + "\n")
	print('Exam grades has been registerd.')


def read_exam_result():
	with open(file='result.txt', mode='r', encoding='utf-8') as file:
		for row in file:
			print(row)
		
		
def read_avarage_grades() -> None:
	with open(file='exam_grades.txt', mode='r', encoding='utf-8') as file:
		for row in file:
			print(row)
			
			
def take_process() -> str:
	process = input(f"""
	Read Grades      => 1
	Enter Grades     => 2
	Register Result  => 3
	Read Result      => 4
	Exit             => e
	Please choose a process:
	""")
	
	return process
	
	
def main():
	while True:
		process = take_process()
		
		if process == '1':
			read_avarage_grades()
		elif process == '2':
			take_information()
		elif process == '3':
			result = read_exam_grades()
			register_result(result)
		elif process == '4':
			read_exam_result()
		elif process == 'e':
			print('Application has been closed..!')
			break
		else:
			print('Please choose valid process..!')
	
	
main()





