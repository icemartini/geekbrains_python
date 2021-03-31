# task 1 
a = 1
b = 1.5
c = 'text'
d = True
text1 = input('Enter something: ')
text2 = input('Enter something once more: ')
print(a, b, c, d, text1, text2)

# task 2
time = int(input('Enter time in seconds: '))
hours = time // 3600
minutes = (time // 60) % 60
seconds = time % 60
print('{:0=2}:{:0=2}:{:0=2}'.format(hours, minutes, seconds))

# task 3
n = input('Enter number: ')
print(int(n) + int(n + n) + int(n + n + n))

# task 4
number = int(input('Enter number: '))
max = 0
while(number > 0):
	if number % 10 > max:
		max = number % 10
	number //= 10
print(max)

# task 5
revenue = int(input('Enter revenue: '))
costs = int(input('Enter costs: '))
result = revenue - costs
if result > 0:
	profit = revenue / costs
	print('фирма отработала с прибылью')
	print('рентабельность составила', profit)
	employees = input('Enter number of employees: ')
	print('прибыль фирмы в расчете на одного сотрудника: ', result / int(employees))
elif result < 0:
	print('фирма отработала с убытком')
else:
	print('фирма отработала в ноль')

# task 6
a = int(input('Enter the distance: '))
b = int(input('Enter the final distance: '))
day = 1
while a < b:
	a *= 1.1
	day += 1
print(f'на {day} день спортсмен достиг результата — не менее {b} км')