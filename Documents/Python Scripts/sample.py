# from array import *

# a = array('l', [1,2,3,4,5])
# print(a[2], type(a[0]), id(a[0]))

# for i in range(10):
#     print('*'*(i+1))

# def rec(n, i):
#     if i<n:
#         print("*"*(i+1))
#         rec(n, i+1)

#     else:
#         print("Loop terminated!!!!")

# rec(10, 0)

'''LinkedLists---------------------------------------------------------'''
# class Node:
#     def __init__(self, data=None, next=None):
#         self.data=data
#         self.next=next


# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def insert_at_begining(self, data):
#         node=Node(data, self.head)
#         self.head=node

#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head=Node(data, None)
#             return

#         itr=self.head
#         while itr.next:
#             itr=itr.next

#         itr.next=Node(data, None)

#     def insert_list(self, data):
#         self.head=None
#         for elements in data:
#             self.insert_at_end(elements)

#     def count_list(self):
#         count=0
#         itr=self.head
#         while itr:
#             count+=1
#             itr=itr.next
#         return count

#     def insert_with_index(self, index, data):
#         if index == 0:
#             self.insert_at_begining(data)

#         count=0
#         itr=self.head
#         while itr:
#             if count==index-1:
#                 node=Node(data, itr.next)
#                 itr.next=node
#                 break
#             itr=itr.next
#             count+=1
        
#     def insert_after_value(self, data_after, data_to_insert):
#         # Search for first occurance of data_after value in linked list
#         itr=self.head
#         while itr:
#             if itr.data==data_after:
#                 node=Node(data_to_insert, itr.next)
#                 itr.next=node
#                 break
#             itr=itr.next
#         return

#     def remove_by_value(self, data):
#         # Remove first node that contains data
#         itr=self.head
#         while itr:
#             if itr.data==data:
#                 itr=itr.next
#                 itr.next=itr.next.next
#                 break
#             itr=itr.next
#         return

#     def print(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#         itr=self.head
#         llstr=''

#         while itr:
#             llstr += str(itr.data) + ' --> '
#             itr = itr.next

#         print(llstr)

# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.insert_list(['apple', 'banana', 'mango'])
#     ll.print()
#     ll.insert_with_index(2,'Orange')
#     ll.print()
#     ll.insert_after_value('Orange', 'Pine')
#     ll.print()
#     ll.remove_by_value('apple')
#     ll.print()
#     print('length: ', ll.count_list())

'''HashTables--------------------------------------------------'''
# def get_hash(key):
#     h=0
#     for keys in key:
#         h += ord(keys)
#     print(h%100)

# get_hash('march 9')
# get_hash('9 archm')

# class Father:
#     def __init__(self):
#         self.skills()

#     def Skills(self):
#         print("gardeninig, programming")

# class Mother:
#     def skills(self):
#         print("Cooking, art")

# class Child(Father, Mother):
#     def skills(self):
#         print("playing, studying")

# c = Child()
# print(c.Skills())

'''Stack-----------------------------------------------------------------'''

# s = []
# s.append('eins')
# s.append('zwei')
# s.append('drei')
# s.append('vier')
# s.append('funf')
# s.append('sechs')
# s.append('seben')

# for i in range(len(s)):
#     print(s, s.pop())

from collections import deque
# stack = deque()

# stack.append('erst')
# stack.append('zweite')
# stack.append('dritte')
# stack.append('vierte')
# print(stack, stack.pop())

# def reverse_string(string):
#     str1 = deque(string)
#     reverse = ''
#     for i in range(len(str1)):
#         reverse += str1.pop()

#     return reverse

# print(reverse_string('We will conquere COVID-19'))
    
# class Stack:
#     def __init__(self):
#         self.val = deque()

#     def push(self, value):
#         return self.val.append(value)

#     def Pop(self):
#         return self.val.pop()

#     def peek(self):
#         return self.val[-1]
    
#     def is_empty(self):
#         return len(self.val)==0

#     def size(self):
#         return len(self.val)

#     def is_balanced(self, input):
#         self.push(input)
#         count1, count2 = 0, 0
#         str1 = self.Pop()
#         for i in range(len(str1)):
#             popped = str1[i]
#             if popped in ('{', '[', '('):
#                     count1 += 1
#             if popped in ('}', ']', ')'):
#                 count2 += 1

#         return count1 == count2
    

# s = Stack()
# print(s.is_balanced('(a+b)'))


# def is_balanced(string):
#     count1, count2 = 0, 0
#     str1 = deque(string)
#     for i in range(len(str1)):
#         popped = str1.pop()
#         if popped in ('{', '[', '('):
#                 count1 += 1
#         if popped in ('}', ']', ')'):
#             count2 += 1
#     return count1 == count2

# print(is_balanced('((a+-b)'))

'''Trees------------------------------------------------------'''
# class  BinarySearchTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

#     def add_child(self, data):
#         if data == self.data:
#             return 'Node already exist'
        
#         if data < self.data:
#             if self.left:
#                 self.left.add_child(data)

#             else:
#                 self.left = BinarySearchTreeNode(data)

#         else:
#             if self.right:
#                 self.right.add_child(data)

#             else:
#                 self.right = BinarySearchTreeNode(data)

#     def search(self, val):
#         if self.data == val:
#             return True

#         if val < self.data:
#             if self.left:
#                 return self.left.search(val)

#             else:
#                 return False

#         if val > self.data:
#             if self.right:
#                 return self.right.search(val)

#             else:
#                 return False

#     def in_order_traversal(self):
#         elements = []
#         if self.left:
#             elements += self.left.in_order_traversal()

#         elements.append(self.data)

#         if self.right:
#             elements += self.right.in_order_traversal()

#         return elements

# def build_tree(elements):
#     print("Building trees with these elements", elements)
#     root = BinarySearchTreeNode(elements[0])

#     for i in range(1, len(elements)):
#         root.add_child(elements[i])

#     return root

# if __name__ == '__main__':
#     countries = ['India', 'Pakistan', 'Germany', 'USA', 'China', 'UK']
#     coountry_tree = build_tree(countries)

#     print('UK is in the list?', coountry_tree.search('UK'))
#     print('Sweden is in the list?', coountry_tree.search('Sweden'))

#     numbers_tree = build_tree([12, 3, 5, 20, 18, 24])
#     print('In order traversal gives this sorted list:', numbers_tree.in_order_traversal())


'''Tree_Code-----------------------------------------------------------'''

# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#         self.parent = None

#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)
    
#     def get_level(self):
#         level = 0 
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent

#         return level
    
#     def PrintTree(self):
#         spaces = '  ' * self.get_level() * 2
#         print(spaces + self.data)
#         if len(self.children) > 0:
#             for child in self.children:
#                 child.PrintTree()
#                 # print(child.data)

# def build_tree():
#     root = TreeNode("Electronics")

#     laptop = TreeNode('Laptop')
#     laptop.add_child(TreeNode('Mac'))
#     laptop.add_child(TreeNode('Surface'))
#     laptop.add_child(TreeNode('Thinkpad'))

#     cellphone = TreeNode('TV')
#     cellphone.add_child(TreeNode('iPhone'))
#     cellphone.add_child(TreeNode('Google Pixel'))

#     Tv = TreeNode('TV') 
#     Tv.add_child(TreeNode('Samsung'))
#     Tv.add_child(TreeNode('LG'))

#     root.add_child(laptop)
#     root.add_child(cellphone)
#     root.add_child(Tv)
    
#     return root

# if __name__ == '__main__':
#     root1 = build_tree() 
#     root1.PrintTree()

inputs = [1,2,1,3]

weights = [[0.5, 1, 2.5, 1],
            [1, -0.5, 2, 5],
            [1, -0.3, 2, 1.5]]   

bias  = [1,2,3,4]

for n_w, n_b in zip(weights, bias):
    print(n_w, n_b)

