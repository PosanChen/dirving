country = input('哪國人:')
age = input('年齡:')
age = float(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')