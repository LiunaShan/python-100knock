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
