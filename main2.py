#36
print("#36")
tpl = (1, 2, 3)
print(tpl)
print(tpl[0])

#37
print("#37")
tpl = (1, 2)+(3,4)
print(tpl)
print(len(tpl))

#38
print("#38")
st = {1, 2, 3}
st.add(1)
print(st)
st.add(4)
print(st)
st.remove(1)
st.remove(4)
print(st)

#39
print("#39")
x = {1,2,3}
y = {3,4,5}
print(x.union(y))
print(x.intersection(y))

#40
print("#40")
st = {1,2,3}
for i in st :
    print(i)

#41
print("#41")
dct = {'id': '0001', 'name': 'guest'}
dct['key'] ='value' #代入
print(dct['name'],dct['key'])

#42
print("#42")
dct =  {'id': '0001', 'name': 'guest'} 
for key, value in dct.items():
    print(key, value)

for x in dct.items():
    print(x)

#43
print("#43")
result = [i for i in range(1,10) if i % 2 == 0]
print(result)

#44
print("#44")
x = "1, 2, 3"
print(x.replace(",","&"))

#45
print("#45")
x = "1, 2, 3"
lst = x.split(",")
print(lst)
y = "&".join(lst)
print(y)

#46
print("#46")
x = 10
y =3
print(x*y)
print(float(x/y))
print(int(x/y))
print(x//y)
print(x%y)

#47
print("#47")
lst = [1, 2, 3] 
print(max(lst))

#48
print("#48")
x = 0
try:
    print(1/x)
except ZeroDivisionError:
    print("ゼロ除算エラーが発生しました")

#49
print("#49")
x = None
try:
    print(x*2)
except TypeError as e:
    print("エラー内容:" + str(e))

#50
print("#50") 
x = -1 
if x < 0 :
   raise ValueError( "負の値が入力されました" )
