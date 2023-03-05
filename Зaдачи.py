('Задача 1') #+
a= ('Привіт')
print(a)
b= ('Пока')
a=b
print(a)

print('Задача 2') #+
#1 варіант Вибрати цифру від 1 до 4 і появиться ім'я
v =int(input('Виберіть Імя \n 1 Sasha \n 2 Dima \n 3 Maks \n 4 Ksyusha \n'))
if v == 1:
    p= ('Hello, Sasha, would you like to learn some Python today?')
if v == 2:
   p= ('Hello, Dima, would you like to learn some Python today?')
if v == 3:
    p =('Hello, Maks, would you like to learn some Python today?')
if v == 4:
   p = ('Hello, Ksyusha, would you like to learn some Python today?')
print(p)
#2 варіант Тут водити своє ім'я
name=input('Ведіть своє імя:')
print('Hello,',name,'would you like to learn some Python today?')
#3 варіант Тут уже вибране ім'я
Name='Vitalik'
print('Hello,',Name,'would you like to learn some Python today?')

print('Задача 3') #+
famous_person='Уолт Дісней'
message=' "Кращий спосіб почати робити – перестати говорити і почати робити." '
print(famous_person +' once said '+ message)

print('Задача 4')  #+
Namee=("  Vitali  ")
NameB=('\n Dima \t Vitalik \n Maks \t Masha ')
print(NameB)
g= Namee.lstrip()
y = Namee.rstrip()
z = Namee.strip()
print("gfjgh", g,"lstrip")
print("rgigr", y,"rstrip")
print("tghsi", z,"strip")
print('Задача 5')
print('Біляк Віталій \n Укріїна \n 5785 \n Чернівці́ \n Героїв Майдану \n 77')

print('Задача 6')  #+
m = float(input("Будь яке число щоб перевести "))
футах = m * 3.280840
дюйм = m * 39.370
мили = m * 0.00062137
ярди= m * 1.0936
print('метри',m ,'\nфутах',футах  ,'\n дюйм',дюйм,'\nмили',мили,'\nярди',ярди)

print('Задача 7')  #+
holi=14
h_ho=24*holi
h_min=60*h_ho
h_sec=60*h_min
print('Години {0:10}, Хвилини {1:10}, Секунди {2:10}' .format(h_ho, h_min, h_sec))
#11(7)     +
H_day= int(input('Ведіть число щоб узнати скільки секунд в канікулах: '))
H_mat= H_day*24*60*60
print('секунд канікул {:10}'.format(H_mat))

print('Задача 8') #+
C = int(input('Ведіть градус в ЦЕЛЬСІЯ:'))
F = C*32+9/5
K = C+273.15
print('Цельсія {:15,.2f}\n Фаренгейта {:15,.2f} \n Кельвіна  {:15,.2f}'.format(C,F,K))

print('Задача 9') #+
#1варіант
Num =int(input('Ведіть будь яке 4-ох значне число:'))
Тисячни= Num // 1000
Сотні= (Num % 1000) //100
Десятки= (Num % 100) //10
Одиниці=Num%10
Sum= Тисячни+Сотні+Десятки+Одиниці
print('{}+{}+{}+{}={}'.format(Тисячни,Сотні,Десятки,Одиниці,Sum))
#2варіан
n= input('Ведіть число будь яке число:')
O=[int(j) for j in n]
M=sum(O)
print(O)
print(M)

print('Задача 10')#+
import math
x1=39.9075000
y1 = 116.3972300
x2 = 50.4546600
y2 = 30.5238000
A1= math.radians(x1)
A2= math.radians(x2)
F1= math.radians(y1)
F2= math.radians(y2)

Дистанція = 6371.032 * math.acos(math.sin(A1) * math.sin(A2) + math.cos(A1) * math.cos(A2) * math.cos(F1 - F2))
print(f'{Дистанція:.3f}')
