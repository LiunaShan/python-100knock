#1
print("#1")
print( "Hello, World!")
#2
print("#2")
print(1)
print(2)
print(3)
#3
print("#3")
print(123,"Hello")
#4
print("#4")
print(1)
#print(2)
print(3)
#5
print("#5")
"""
print(1)
print(2)
print(3)
"""


#6
print("#6")
x = 10
print(x)
#7
print("#7")
x = 1 + 2
print(x)

#8
print("#8")
x = "1" + "2"
print(x)

#9
print("#9")
print(str(10))
print(int("10"))

#10
print("#10")
print("1\n2\n3")

#11
print("#11")
print("C:\\test")

#12
print("#12")
print(r"C:\test")

#13
print("#13")
name = "Python"
print("Hello," + name + "!")

#14
print("#14")
x = "Python"
print(len(x))

#15
print("#15")
print(x[0],x[1])
print(x[0:2])

#16
print("#16")
x = None
print(x) 

#17
print("#17")
a = 10
b = 3.14
c = "Hello, Python!"
d = True
print(type(a),type(b),type(c),type(d))

#18
print("#18")
lst = [1, 2, 3]
print(lst)
print(lst[0])

#19
print("#19")
print(lst[1:2])

#20
print("#20")
lst.append(4)
print(lst)

#21
print("#21")
lst = [1, 2, 3]
print(len(lst))

#22
print("#22")
lst.remove(2)
print(lst)

#23
print("#23")
lst = [1,2] + [3,4]
print(lst)

#24
print("#24")
x = 15
if x > 10:
    print("xは10より大きい")

#25
print("#25")
x = 10
if x > 10:
    print("xは10より大きい")
elif x > 5:
    print("xは5より大きいが、10以下")
else:
    print("xは5以下")

#26
print("#26")
x = 10
y = 20
print(x > y)
print(x >= y)
print(x == y)
print(y >= x)
print(y > x)

#27
print("#27")
lst = [1, 2, 3]
print(2 in lst)

#28
print("#28")
y = None
print(y is None)

#29
print("#29")
x = 10
y = 20
print(x > 15 and y > 15)
print(x > 15 or y > 15)

#30
print("#30")
x = None
if x is not None:
    print("x は None ではない")
if not (x is None):
    print("x は None ではない")

#31
print("#31")
lst = [1, 2, 3]
for i in lst:
    print(i)

#32
print("#32")
for i in range(10):
    print(i)

#33
print("#33")
x = 5
for i in range(10):
    if i == x:
        break
    print(i)

#34
print("#34")
x = 5
for i in range(10):
    if i == x:
        continue
    print(i)

#35
print("#35")
x = 10
while x > 0:
    print(x)
    x -= 1 