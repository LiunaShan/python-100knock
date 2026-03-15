#59
print("#59")
list =  [1, 2 , 3, None, 5] 

for a in list:
    try:
        print(a * 2)
    except TypeError as e:
        print(e)

#60
print("#60")
employees = [
    {'id': '0001', 'name': '田中', 'location_id': 'L01'},
    {'id': '0002', 'name': '山田', 'location_id': 'L02'},
    {'id': '0003', 'name': '小林', 'location_id': 'L01'},
    {'id': '0004', 'name': '藤本', 'location_id': 'L03'},
    {'id': '0005', 'name': '佐々木', 'location_id': 'L02'},
    {'id': '0006', 'name': '松田', 'location_id': 'L04'},
    {'id': '0007', 'name': '中村', 'location_id': 'L01'},
    {'id': '0008', 'name': '石川', 'location_id': 'L03'},
    {'id': '0009', 'name': '清水', 'location_id': 'L05'},
    {'id': '0010', 'name': '近藤', 'location_id': 'L02'}
]

for employee in employees:
    if  employee['location_id'] in {'L01', 'L02'}:
        print(employee['id'],employee['name']) 

#61
print("#61")
def sample():
    print('Hello World')
sample()
sample()
sample()

#62
print("#62")
def greet(name):
    print(f'こんにちは、{name}さん')

greet('テスト')

#63
print("#63")
def add(a,b):
    return a + b

print(add(1,2))

#64
print("#64")
def welcome_message(name =  'ゲスト'):
    print(f'こんにちは、{name}さん')

welcome_message()
welcome_message('管理者')

#65
print("#65")
def print_args(*args,**kwargs):
    print(args)
    print(kwargs)

print_args('A', 'B', key1='X', key2='Y')

#66
print("#66")
class SimpleClass:
    def __init__(self, name):
        print(f'名前が {name} のオブジェクトを作成しました')

x = SimpleClass('サンプル')

#67
print("#67")
class SimpleClass:
    def __init__(self, name):
        print(f'名前が {name} のオブジェクトを作成しました')
        self.name = name
    def print_name(self):
        print(self.name)

x = SimpleClass('サンプル')
x.print_name()

#68
print("#68")
class SimpleClass:
    count = 0
    def __init__(self, name):
        print(f'名前が {name} のオブジェクトを作成しました')
        self.name = name
        SimpleClass.count += 1
    
    @classmethod
    def print_count(cls):
        print(cls.count)
  
    def print_name(self):
        print(self.name)


x = SimpleClass('サンプル')
y = SimpleClass('サンプル２')
SimpleClass.print_count()

