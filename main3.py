#51
print("#51") 
for i in range(1,10):
    for j in range (1,10):
        print(f"{i} × {j} = {i*j}")


#52
print("#52") 
numb = 1 
while numb < 100:
    a = str(numb)
    if '3' in a :
        print(numb)
    numb += 1


#53
print("#53") 
i = 0
numb = 1 
while i < 100:
    a = str(numb)
    if '3' in a :
        print(numb)
        i += 1 
    numb += 1

#54
print("#54") 
list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for x in range(len(list_2d)):
    for y in range(len(list_2d[x])):
        print(2*list_2d[x][y])

for row in list_2d:
    for y in row:
        print(y*2)

#55
print("#55")
result =[ [ f"{i} - {j}" for j in range(10)] for i in range(10)]
print(result)

#56
print("#56")
ascii_dict = {'0x30': '0', '0x40': '@', '0x50': 'P'} 
reversed_dict = {value: key for key, value in ascii_dict.items()}
print(reversed_dict);

#57
print("#57")
target_text = "hello"
count_dic = {}
for i in target_text:
    if ( i in count_dic):
        count_dic[i] += 1
    else:
        count_dic[i] = 1
print(count_dic) 

#58
print("#58")
target_list =  [1, 2, 3, None, 5, None, 7]
#bad example
print("bad example")
a = ""
b = len(target_list)
c = 0
for i in target_list:
    c += 1
    if i is not None and c is not b:
        a = a + str(i) + "&"
    elif i is not None and c == b:
        a = a + str(i)
print(a)
#good example
print("good example")
filtered_list = [str(i) for i in target_list if i is not None]
result = '&'.join(filtered_list)
print(result)



