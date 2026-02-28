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


