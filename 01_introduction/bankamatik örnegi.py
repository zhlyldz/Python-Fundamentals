# Bankamaitk
burak_account = {
	'account_no': '12345',
	'full_name': 'burak yilmaz',
	'user_name': 'beast',
	'password': '123',
	'ballance': 3000,
	'additional_ballance': 1000
}

hakan_account = {
	'account_no': '67890',
	'full_name': 'hakan yilmaz',
	'user_name': 'bear',
	'password': '123',
	'ballance': 5000,
	'additional_ballance': 1000
}

ipek_account = {
	'account_no': '192837',
	'full_name': 'ipek yilmaz',
	'user_name': 'keko',
	'password': '123',
	'ballance': 8000,
	'additional_ballance': 1000
}

users = [burak_account, hakan_account, ipek_account]


def withdraw_money(account: dict, amount: int):
	# Çekilmek istenilen para bakiye tarafından karşılanıyor mu?
	# Miktar bakiye tarafındak karşılanamamasında ek hesap devreye girilsin
	# Ne bakiye ne ek hesap miktarı karşılayamama
	
	if account['ballance'] >= amount:
		account['ballance'] -= amount
		print("Don't fotget to take your money.")
		ballance_result(account)
	else:
		total_ballance = account['ballance'] + account['additional_ballance']
		
		if total_ballance >= amount:
			use_additianol_ballance = input('Insufficent ballance. Use additianol ballance?')
			
			if use_additianol_ballance == 'yes':
				amount_used_additional_account = amount - account['ballance']
				account['ballance'] = 0
				account['additional_ballance'] -= amount_used_additional_account
				ballance_result(account)
			elif use_additianol_ballance == 'no':
				print('Process has been cancaled.')
				ballance_result(account)
			else:
				print('Plase type "yes" or "no".')
		else:
			print('Insufficient total balance. Transaction cancelled.')
			ballance_result(account)


def ballance_result(account: dict) -> None:
	print(
		f"You have {account['ballance']} TL account number {account['account_no']}.\nAdditional ballance has {account['additional_ballance']} TL.")


def show_account_information(account: dict):
	print(f"Account Information\n"
	      f"===================\n"
	      f"Name: {account['full_name']}\n"
	      f"Account No: {account['account_no']}\n"
	      f"User Name: {account['user_name']}\n"
	      f"Password: {account['password']}\n"
	      f"Balance: {account['ballance']}\n"
	      f"Additional Balance: {account['additional_ballance']}")


def log_in(user_name: str, password: str) -> dict:
	account = {}
	for user in users:
		if user['user_name'] == user_name and user['password'] == password:
			account = user
			break
	
	return account


def menu(auth_account: dict) -> None:
	print(f"""
				Welcome, {auth_account['user_name']}
				====================================
				Withdrow Money      ==> 1
				Deposit             ==> 2
				Account Information ==> 3
				Show Balance        ==> 4
				EFT                 ==> 5
				Exit                ==> 6
				""")


def deposit_money(account: dict, amount: int) -> None:
	account['ballance'] += amount
	ballance_result(account)


def eft_process(sender_account: dict, receiver_account_no: str, amount: int):
	process_is_valid = False
	
	for user in users:
		if user['account_no'] == receiver_account_no:
			user['ballance'] += amount
			# Adamın hesabında ki para yetecek mi? yetmiyorsa ek hesap devereye girecek mi?
			# bütün parası yetecek mi?
			process_is_valid = True
			break
	
	if process_is_valid:
		ballance_result(sender_account)
	else:
		print('Process faild. Check your information.')


def main():
	auth_account = log_in(input('User Name: '), input('Password: '))
	while True:
		if auth_account != {}:
			menu(auth_account)
			
			process = input('Please choose a process: ')
			
			if process == '6':
				print('Exit.')
				break
			elif process == '3':
				show_account_information(auth_account)
			elif process == '4':
				ballance_result(auth_account)
			elif process == '1':
				withdraw_money(auth_account, int(input('Amount: ')))
			elif process == '2':
				deposit_money(auth_account, int(input('Amount: ')))
			elif process == '5':
				eft_process(auth_account,
				            input('Reveiver Account No: '),
				            int(input('Amount: ')))
		else:
			print('Check your information..!')


main()
