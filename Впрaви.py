print('Вправа 1')
print(60*60)

print('Вправа 2')
#1 варіант
seconds_per_hour=(60*60)
print(seconds_per_hour)
#2 варіант
hour= int(input('Скільки годин:'))
print('2variant',hour*60*60)
print('Вправа 3')
print(seconds_per_hour*24)

print('Вправа 4')
seconds_per_day=60*60*24
print(seconds_per_day)

print('Вправа 5')
print(seconds_per_day / seconds_per_hour)

print('Вправа 6')
print(seconds_per_day // seconds_per_hour)

print('Вправа 7')
print(5 + 7)
print(15 - 3)
print(60 / 5)
print(2 * 6)

print('Вправа 8')
a=('16')
print('Моє улюблене число',a,)

print('Вправа 9')
name= 'Vitalik'
print(str.lower(name))
print(str.upper(name))
print(str.swapcase(name))

print('Вправа 10')  #Вправа з поемою
poem ='''Yes, I'll smile, indeed, through tears and weeping
Sing my songs where evil holds its sway,
Hopeless, a steadfast hope forever keeping,
I shall live! You thoughts of grief, away!'''
print(poem)
print(poem[:15])  #1
print(len(poem))  #2
print(poem.startswith('Yes')) #3
print(poem.endswith('I shall live!')) #4
print(poem.find(',')) #5
print(poem.rfind(','))  #6
print(poem.count(',')) #7
print(poem.isalnum()) #8
