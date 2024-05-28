# # print('Hello, world!')

# # def Greet():
# #     print('Hello, ', input('Enter your name: '))

# # Greet()

# # Numbers
# print(type(10)) # int
# print(type(-10)) # int
# print(type(10.5)) # float
# print(type(-10.5)) # float
# print(type(5+4j)) # complex
# mycomplex = 5+4j # 5 + 4j
# print(mycomplex.real) # 5.0 
# print(mycomplex.imag) # 4.0

# # Operations
# print(5 +10 * 100) # 105
# print((5 +10) * 100) # 105
# print(25 % 5) # 0 modulus returns the remainder
# print(24 % 5) # 4 modulus returns the remainder
# # Floor division returns the quotient without the remainder
# print(25 // 5) # 5
# print(27 // 5) # 5
# print(24 // 5) # 4
# def count_positive_odd_numbers(n):
#     return n // 2 

# print(count_positive_odd_numbers(5))

# # Lists
# # [1] List Items Are Enclosed in Square Brackets
# # [2] List Are Ordered, To Use Index To Access Item
# # [3] List Are Mutable => Add, Delete, Edit
# # [4] List Items Is Not Unique
# # [5] List Can Have Different Data Types

# mylist = [1, 2, 3, 4, 5, "Hello", True]
# print(mylist[0]) # 1
# print(type(mylist)) # List
# print(type(mylist[-1])) # bool
# print(mylist[3:6]) # [4, 5, "Hello"] Slicing from index 3 to index 6
# print(mylist[:6]) # [1, 2, 3, 4, 5, "Hello"] Slicing from index 0 to index 6
# print(mylist[1:]) # [2, 3, 4, 5, "Hello"] Slicing from index 1 to end
# print(mylist[::2]) # [1, 3, 5, True] Slicing from index 0 to end with step 2
# print(mylist[::3]) # [1, 4, True] Slicing from index 0 to end with step 3
# mylist[1] = "Two"
# print(mylist) # [1, "Two", 3, 4, 5, "Hello", True] Changing index 1 to "Two"
# mylist[0:3:2] = ["One","Three"]
# print(mylist) # ['One', 'Two', 'Three', 4, 5, 'Hello', True] Changing index 0, 2 to "One", "Three"
# mylist[::2] = ["One","Three", "Five", True]
# print(mylist) # ['One', 'Two', 'Three', 4, 'Five', 'Hello', True] Changing index 0, 2, 4, 6 to "One", "Three", "Five", True
# mylist.append("World")
# print(mylist) # [1, "Two", 3, 4, 5, "Hello", True, "World"] Append "World" to list 

# # Given a string s, write a method (function) that will return true if its a valid single integer or floating number or false if its not.I
# def is_digit(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         return False