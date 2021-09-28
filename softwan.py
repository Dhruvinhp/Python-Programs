names = ['Chris', 'Jack', 'John', 'Daman']
print(names[-1][-3:][::-1])

a= 10
b= 20
a, b = 20, 10
print(a, b)

dictionary1 = {'Google' : 1, 'Facebook' : 2, 'Microsoft' : 3}
dictionary2 = {'Google' : 2,'Youtube' : 3}
dictionary1.update(dictionary2)
for key, values in dictionary1.items():
    print(key, values)
    break
else:
    print("hello")

value = [1, 2, 3, 4, 5] 		
try: 
    value = ([value[10]] * 10 /0)
except ZeroDivisionError: 
    print('abc ', end = '') 
except IndexError: 
    print('abcc ', end = '') 		
else: 
    print('bc ', end = '') 	
finally: 		
    print('c ', end = '')

data = [1,5,7]	
temp = [[x for x in[data]] for x in range(3)]		
print(temp)

L1 = []
L1.append([1, [2, 3], 4])
L1.extend([7, 8, 9])
print(L1[0][1][1] + L1[2])

print("--------------------------------")
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class singly_linked_list:
    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0

    def iterate_item(self):
        current_item = self.tail
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val

    def append_item(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1

items = singly_linked_list()
items.append_item('Python')
for val in items.iterate_item():
    print(val)

print("--------------------------------------------")
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
