# задание 1
# def is_palindrome(s):
#     if len(s) < 2:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return is_palindrome(s[1:-1])

# print(is_palindrome("hello"))  
# print(is_palindrome("racecar")) 
# print(is_palindrome("abba"))

# задание 2 


# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(0))
# print(factorial(1))
# print(factorial(5))
# print(factorial(10))


# задание 3 
# rectangle_area = lambda length, width: length * width
# print(rectangle_area(2, 3))
# print(rectangle_area(5, 10))
# print(rectangle_area(8.5, 11))
# def rectangle_area(length, width):
#     return length * width

# задание 4 

# max_number = lambda x, y: x if x > y else y
# print(max_number(2, 3))  
# print(max_number(-5, 10))  
# print(max_number(8.5, 11))  
# def max_number(x, y):
#     return max(x, y)

# задание 5 
# def add_brackets(s):
#     if len(s) % 2 == 0:
#         # Для четной длины добавляем два символа в середину
#         half = len(s) // 2
#         s = s[:half] + '(' + s[half:half+2] + ')' + s[half+2:]
#     else:
#         # Для нечетной длины добавляем один символ в середину
#         half = len(s) // 2
#         s = s[:half] + '(' + s[half] + ')' + s[half+1:]
#     # Добавляем скобки по образцу
#     result = ''
#     for i, c in enumerate(s):
#         if i < len(s) // 2:
#             result += c + '('
#         else:
#             result += ')' + c
#     return result

# print(add_brackets('example'))
# print(add_brackets('card'))
# print(add_brackets('Python'))


# задание7


# import sys

# sys.setrecursionlimit(1000)

# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# limit = int(input("Введите лимит рекурсии: "))
# sys.setrecursionlimit(limit)

# n = int(input("Введите индекс числа Фибоначчи: "))
# print(f"Число Фибоначчи для индекса {n} равно {fibonacci(n)}")