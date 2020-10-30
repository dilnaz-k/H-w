# print('Hello world')
# a = -8
# b = 8
# if a > 56:
# print('КОД КРАСНЫЙ')
# elif a < 0:
# print('КОД КРАСНЫЙ')
# else:
# print('КОД СИНИЙ')
# a = [[1, 2, 3], [4, 3, 2]]
# b = [[9, 8, 7], [6, 5, 4]]
# Упражнение 1
# print("Упражнение 1. Заведите глубину елки")
# stars = int(input)
# Упражнение 2
# print('Упражнение 2')
# languages = ['C', 'Delphi', 'Python', 'HTML']
# if languages == 'Python':
# print('hi')
d = 19
c = 8
if d > c + 10:
    print('d больше чем c по крайней мере на 10')
g = 5
h = 5
if h > g:
    print('h больше чем g')
else:
    if h == g:
        print('h ровняется g')
    else:
        print('h меньше g')
name = 'Sean'
height = 1.67
weight = 90


# bmi = weight / (height * height)
# print('Индекс массы тела: ' + str(bmi))
# if bmi < 25:
# print("У " + name + " нет лишнего веса")
# else:
# print("У " + name + " есть лишний вес")
# print(10 < 51)
def function_1():
    print('Hello1')
    print('Hello2')


print('Hello world')

function_1()


def fun2(x):
    return 2 * x


a = fun2(5)
print(a)
print(fun2(3))


def fun3(x, y):
    return x + y


e = fun3(6, 85)
print(e)

name1 = "Tom"
height1 = 1.85
weight1 = 75

name2 = "Rey"
height2 = 1.90
weight2 = 100

name3 = "Anna"
height3 = 1.58
weight3 = 48


def bmi_calculator(name0, height0, weight0):
    bmi = weight0 / height0 ** 2

    print('Индекс массы тела: ' + str(bmi))

    if bmi < 25:
        return name0 + ' не имеет лишнего веса'
    else:
        return name0 + ' имеет лишний вес'


bmi1 = bmi_calculator(name1, height1, weight1)
bmi2 = bmi_calculator(name2, height2, weight2)
bmi3 = bmi_calculator(name3, height3, weight3)

print(bmi1)
print(bmi2)
print(bmi3)

# l1 = 6
# n1 = 4

# l2 = 7
# n2 = 5

# l3 = 8
# n3 = 8


# def area(l, n):
# s = l * n
# print("Площадь четырехугольника = " + str(s))


# area(l1, n1)
# area(l2, n2)
# area(l3, n3)

# m1 = 8
# m2 = 9
# m3 = 3

a = [3, 5, 20]
print(a)

a.append(15)
print(a)
a.append('hi')
print(a)
a.append([3, 5])
print(a)
a.pop()
print(a)
a.pop()
print(a)

print(a[0])
print(a[3])
print(a[-1])

a[0] = 100
print(a)

a.pop(2)
print(a)

b = ['hello', 'goodbye', 'hey']
temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)

b[0], b[2] = b[2], b[0]
print(b)

b[0], b[1], b[2] = b[2], b[0], b[1]
print(b)

word = 'Hello world'

for character in word:
    if character == 'l':
        print(character)
        break
    else:
        print('not an l')


i = 0

# while -5 < i < 5:
# print(i)
# break
#  i = i-1
# stars = '*'
# while stars == '*':
# print(str(stars)) stars = str(stars) + 1

a = ['hey', 'hello', 'bye']

for element in a:
    print(element)
b = [20, 30, 50, 60]
for num in b:
    print(num)
    print(num)
total_sum = 0
for e in b:
    total_sum = total_sum + e
print(total_sum)
range(1,5)
print(range(1, 5))
print(list(range(1, 5)))
for i in range(1, 5):
    print(i)


total_sum2 = 0
for i in range(1, 5):
    total_sum2 = total_sum2 + i
    total_sum2 += i
print(total_sum2)

print(list(range(1, 100)))
print(9 % 3)
for i in range(1, 100):
    if i % 3 == 0:
        print(i)

total_sum3 = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total_sum3 += i

print("Введите глубину елки:")
stars = int(input())
star = 1
while star < star+1:
    print(star * '*')
    star = star + 1



