# exercise

from __future__ import division
import json
import re
import datetime
import string
import os
import math
import random

"""
print(os.getcwd())
os.chdir("Python-programming-exercises")
print(os.getcwd())


with open("100+ Python challenging programming exercises.txt", "r") as rf:
    with open("Question.txt","w") as wf:
        f = rf.read()
        p = "Hints?:?[\s\S]+?Solution:?[\s\S]+?(?=#--)"
        new_text = re.sub(p,"", f)
        wf.write(new_text)

pattern = "Hints?:?[\s\S]+?Solution:?[\s\S]+?(?=#--)"


#12:07  "-30 mins.
"""
#1.


"""x = ', '.join(map(str,[n for n in range(2000, 3201) if (n%7==0) and not(n%5==0)]))
print x

#2.
def compute_fact():
    prod = 1
    outputs = []
    user_input = raw_input("enter a valid integer")
    nums = user_input.split()
    for num in nums:
        for i in range(1,int(num)+1):
            prod*=i
        outputs.append(prod)
        prod = 1
    return ", ".join(map(str, outputs))

print compute_fact()

#3
q3 = {i:i*i for i in range(1, int(raw_input())+1)}
print q3

#4
user_input = raw_input()
list_nums = list(user_input.split(","))
tuple_nums = tuple(user_input.split(","))
print list_nums
print tuple_nums

#5

class TwoMethods(object):

    def get_string(self):
        self.user_input = raw_input()
    def printstring(self):
        return self.user_input

    def test_class_methods(self):
        pass
#6

"Q = Square root of [(2 * C * D)/H]"
c = 50
h=30
d = raw_input().split(",")
output = ', '.join(map(str, ([math.sqrt((2*c*int(i))/h) for i in d])))
print output

#7

# works only if s and k are sperated with enter
s,k = (int(raw_input()),int(raw_input()))

i_out = []
for i in range(s):
    i_in = []
    for j in range(k):
        i_in.append(i*j)
    i_out.append(i_in)
print i_out

#8
user_input = raw_input()
print ', '.join(sorted(user_input.split()))

#1:28: break 3:30 release
#9
# while True:
#     user_input = raw_input("\n")
#     if user_input is "\n\n":
#         break
#     print user_input.upper()

#10
user_input = raw_input()
set_input = set(user_input.split())
output = ' '.join(sorted(set_input))
print output

#11
def binary_to_dec(n):
    return int(n,2)

print binary_to_dec("10001")

def check_divisibilit():
    user_input = raw_input().split(",")
    print user_input
    return ', '.join([n for n in user_input if int(n,2)%5==0])

#12
def check_if_digit_even(start_num, end_num):
    even_digit_num = []
    for x in range(start_num, end_num):
        even = True
        for y in str(x):
        
            if not y%2 == 0:
                even = False
        if even:
        num=x//10


#13
def count_letter_and_digit():
    digit = 0
    letter = 0
    user_input = raw_input()
    print
    for x in user_input:
        if x.isdigit():
            digit +=1
        elif x.isalpha():
            letter += 1
        else:
            continue
    return "LETTERS {0}{1}DIGIT {2}".format(letter, "\n", digit)

print count_letter_and_digit()


#14
upper_case = 0
lower_case = 0
for n in raw_input():
    if n.isupper():
        upper_case += 1
    elif n.islower():
        lower_case += 1
    else:
        continue
print "UPPER CASE {0}\nLOWER CASE {1}".format(upper_case, lower_case)

#15

def caculate_output(n):
    return int(str(n*4))+int(str(n*3))+int(str(n*2))+int(str(n))
print caculate_output("9")

#16
def find_odd_num(list_num):

    return ', '.join([num for num in list_num if not int(num)%2==0])

user_input = raw_input()
list_num = user_input.split(",")

print find_odd_num(list_num)

#17


class RaiseWithdrawlError():

    def __str__(self):
        return "Amount is not sufficient"

class ComputeAmount():

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def withdrawl(self, amount):
        if self.balance < int(amount):
            raise RaiseWithdrawlError
        self.balance -= int(amount)

    def deposite(self, amount):
        print 'in d in class'
        self.balance += int(amount)
        print self.balance

    def get_amount(self):
        return self.balance

c = ComputeAmount()
while True:
    transaction, amount = raw_input().split(' ')
    if transaction == "D":
        print('D got')
        c.deposite(amount)
    elif transaction == "W":
        c.withdrawl(amount)
    else:
        print c.get_amount()
        break"""

#18
# def get_valid_password(passwords):
#     min_password_length = 6
#     max_password_length = 12
#     valid_passwords = []
#     for password in passwords:
#         if not len(password) < min_password_length or not len(password) > max_password_length:
#
#             alphabet_match = re.search(r'[A-Z]', password)
#             if alphabet_match:
#                 valid_passwords.append(alphabet_match)
#             alphabet_match = re.search(r'[a-z]', password)
#             if alphabet_match:
#                 valid_passwords.append(alphabet_match)
#             alphabet_match = re.search(r'[0-9]', password)
#             if alphabet_match:
#                 valid_passwords.append(alphabet_match)
#             alphabet_match = re.search(r'[@#$]', password)
#             if alphabet_match:
#                 valid_passwords.append(alphabet_match)
#             alphabet_match = re.search(r'[~A-z0-9@#$]', password)
#             if alphabet_match:
#                 break
#
#     return valid_passwords
#
# passwords = raw_input()
#
# print get_valid_password(passwords)
"""
#19

l = []
while True:
    user_input = raw_input()
    if not user_input:
        break
    name, age, height = user_input.split(",")
    l.append((name,age,height))

print sorted(l, key=lambda x:(x[0],x[1],x[2]))

#20

# class Generator(object):
#     def __init__(self, n):
#         (x for x in range(0,n) if x%7==0)


def generator(n):
    for i in range(n+1):
        if i%7==0:
            yield i

my_nums = generator(50)
for i in my_nums:
    print i

#21

x,y = 0,0
while True:
    user_input = raw_input()
    if not user_input:
        break
    direction, cordinate = user_input.split()
    if direction == "UP":
        y += int(cordinate)
    elif direction == "DOWN":
        y -= int(cordinate)
    elif direction == "LEFT":
        x -= int(cordinate)
    else:
        x += int(cordinate)
import math
distance = math.sqrt(x**2 + y**2)
print distance


#22
user_input = raw_input().split()
import collections
counter = collections.Counter(user_input)
for i,j in counter.items():
    print "%s:%s" %(i,j)


#method 2:
counter_dict = {}
for w in user_input:
    if w not in counter_dict:
        counter_dict[w] = 1
    else:
        counter_dict[w] += 1

for item in counter_dict:
    print "{0}:{1}".format(item, counter_dict[item])

#23
def calculate_square(num):
    return num*num


#24

def add_document_for_inbuilt_functions(func):
    print help(abs)
    print help(int)
    print help(raw_input)
    print help(func)

add_document_for_inbuilt_functions(reversed)

#25
class BasicClass(object):

    class_arg = "arg"
    
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

def compute_sum(x,y):
    return x+y

def convert_int_to_str(i):
    return str(i)

def compute_sum_str(x,y):
    return(int(x)+int(y))

def concatenate_two_strings(x,y):
    return str(x) + str(y)

def print_max_length_string(x,y):
    if len(str(x))>len(str(y)):
        return str(x)
    elif len(str(x))<len(str(y)):
        return str(y)
    else:
        return "{0}\n{1}".format(str(x),str(y))


def check_number(num):
    if num%2==0:
        print "It is an even number"
    else:
        print "It is an odd number"

def print_dict():
    return {i:i*i for i in range(1,4)}

def print_dict_and_square():
    return {i:i*i for i in range(1, 21)}

def print_dict_values():
    my_dict = {i:i*i for i in range(1, 21)}
    return ', '.join(map(str, my_dict.values()))

print print_dict_values()

def print_dict_keys():
    my_dict = {i:i*i for i in range(1, 21)}
    return ', '.join(map(str, my_dict.keys()))

def print_square_of_nums():
    return [num*num for num in range(1,21)]

def print_first_five_value_of_square_of_nums():
    return print_square_of_nums()[:5]

print print_first_five_value_of_square_of_nums()


def print_last_five_value_of_square_of_nums():
    return print_square_of_nums()[-6:-1]

print print_last_five_value_of_square_of_nums()

def print_all_except_first_five_value_of_square_of_nums():
    return print_square_of_nums()[5:]

def squre_of_tuples():
    return (num*num for num in range(1,21))

def print_tuple_slicing():
    my_tup =(1,2,3,4,5,6,7,8,9,10)
    first_half = my_tup[:(len(my_tup)//2)+1]
    second_half = my_tup[(len(my_tup)//2)+1:]
    return "{0}\n{1}".format(first_half,second_half)

given_tuple = (1,2,3,4,5,6,7,8,9,10)
print tuple([num for num in given_tuple if num%2==0])

user_input = raw_input()
print "Yes" if user_input in ["Yes", "YES", "yes"] else "NO"

print filter(lambda i:i%2==0, [1,2,3,4,5,6,7,8,9,10])

print map(lambda i:i*i, [1,2,3,4,5,6,7,8,9,10])

print map(lambda i:i*i, filter(lambda i:i%2==0,[1,2,3,4,5,6,7,8,9,10]))

print filter(lambda i: i%2==0, range(1,21))

print map(lambda x: x*x, range(1,21))


class American(object):

    @staticmethod
    def printNationality():
        return "Indian"

class NewYorker(American):
    pass

class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius**2


class Rectangle(object):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return 2*(self.length+self.width)

class Shape():

    def area(self):
        return 0


class Square(Shape):

    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length**2


#  User Defined Exception
class RuntimeException(Exception):

    def __str__(self):
        return "zero divisible error"


def divide(num):
    try:
        num/0

    except RuntimeException as e:
        return e


divide(5)


def get_user_name_from_email():
    user_input = raw_input().split("@")
    return user_input[0]


company_name = re.findall('@(.+?)\.com', raw_input())
print company_name[0]

#
print [digit for digit in raw_input().split() if digit.isdigit()]

#
print u'Hello world'
#
def compuate_result(n):
    sum = 0
    for i in range(1,n+1):
        sum += i/(i+1)
    return sum

print compuate_result(5)

#
def compute_funtion(n):
    if n == 0:
        return 0
    if n > 0:
        return compute_funtion(n-1) +100

user_input = int(raw_input())
print compute_funtion(user_input)

#
def compute_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return compute_fibonacci(n-1)+compute_fibonacci(n-2)


print compute_fibonacci(7)

user_input = int(raw_input())
f = ', '.join(map(str,[compute_fibonacci(x) for x in range(user_input+1)]))
print f

def even_nums(n):
    for i in range(n+1):
        if i%2 == 0:
            yield i

user_input = int(raw_input())
print ', '.join(map(str,[i for i in even_nums(user_input)]))

def check_divisible_by_five_and_seven(num):
    if (num%5 == 0) and (num%7 == 0):
        return True
    return False

def generate_nums(num):
    for x in range(num):
        if check_divisible_by_five_and_seven(x):
            yield x

u = int(raw_input())
print ", ".join(map(str,[x for x in generate_nums(u)]))


my_list = [2,4,6,8,10]
for i in my_list:
    assert i%2==0, "not even"


print eval("35/2")

# five random numbers with are divisible by 5 and 7
import random
random_nums = []

while len(random_nums)<5:
    random_num = random.randint(1, 1000)
    if random_num%5==0 and random_num%7==0:
        random_nums.append(random_num)
print random_nums

#
print random.randint(7,15)

#
import time
def timeit(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        f = func(*args, **kwargs)
        et = time.time()
        tt= et-st
        print tt
        return f
    return wrapper

@timeit
def count_time():
    for i in range(100):
        return 1+1

count_time()

#
li = [3,6,7,8]
random.shuffle(li)
print li

#
for i in ["I", "You"]:
    for j in ["Play", "Love"]:
        for k in ["Hockey", "Football"]:
            print "{0} {1} {2}".format(i, j, k)

#
odd_nums = [num for num in [5,6,77,45,22,12,24] if not num%2==0]
o_nums = filter(lambda x:x%2!=0, [5,6,77,45,22,12,24])
print odd_nums
print o_nums

#
nums = [num for num in [12,24,35,70,88,120,155] if not(num%5)==0 and not(num%7)==0]
print nums

#
li = [v for i,v in enumerate([12,24,35,70,88,120,155]) if i%2==0]
print li

#
# print 3*5*8 matrix

matrix = [[[0 for i in range(8)] for j in range(5)] for k in range(3)]
print matrix


li = [v for i, v in enumerate([12,24,35,70,88,120,155]) if i not in [0, 4, 5]]
print li

#
li = [l for l in [12,24,35,24,88,120,155] if not l is 24]
print li

#
l1 = [1,3,6,78,35,55]
l2 = [12,24,35,24,88,120,155]

l3 = list(set(l1)&set(l2))
print l3

#
l1 = [1,3,6,78,35,55]
l2 = [12,24,35,24,88,120,155]
l1.extend(l2)
l3 = list(set(l1))
print l3

x = list(set([12,24,35,24,88,120,155,88,120,155]))
print x[::-1]

#


class Person(object):

    def __init__(self, gender):
        self.gender = gender

    def getGender(self):
        return self.gender


class Male(Person):

    def getGender(self):
        return "Male"


class Female(Person):

    def getGender(self):
        return "Female"

#
user_input = raw_input()
freq = {}
for c in user_input:
    if c not in freq:
        freq[c] = 1
    else:
        freq[c] +=1
for f in freq:
    print "{0},{1}".format(f,freq[f])

#method2
freq2 = {}
for i in user_input:
    freq[i] = freq.get(i, 0)+1
print freq

#
user_input = raw_input()
r_string = ""
for s in user_input:
    r_string = s+r_string
print r_string

rev = [w[::-1] for w in user_input.split()]
print ' '.join(rev[::-1])

#
i = raw_input()
even_digits = ''.join([v for i,v in enumerate(i) if i%2==0])
print even_digits

#
li = [1,2,3]
pl = []

for l in li:
    for k in li:
        for m in li:
            pl.append([l,k,m])

print pl

import itertools
list(itertools.permutations([1, 2, 3]))


#
def chinese_puzzle(h=35, l=94):
    checken_legs = 2
    rabbit_legs = 4
    j = h-1

    for i in range(l):
        if i*rabbit_legs + j*checken_legs == 94:
            print i, j
            break

        j -= 1
chinese_puzzle()
    
# 2x + 4y = 94
# x + y = 35
# y = x-35
# 2x + 4(x-35) = 94
# 6x = 234


class CompressDecompress(object):
    def compres(self, strings, symbol):
        return "{0}{1}".format(strings.split(symbol)[0], symbol)

    def decompres(self, string):
        return string*4

cd = CompressDecompress()
print cd.compres("HelloWorld!HelloWorld!HelloWorld!","!")
print cd.decompres("HelloWorld!")

# import zlib
# s = 'hello world!hello world!hello world!hello world!'
# t = zlib.compress(s)
# print t
# print zlib.decompress(t)

li = [v for i,v in enumerate([12,24,35,70,88,120,155]) if i not in [0,2,4,6]]
print li

# By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

li = [v for i,v in enumerate([12,24,35,70,88,120,155]) if not i in [0,4,5]]
print li

# Binary Search

def calculate_middle_value(f, l):

    first_val = f
    last_val = l
    mid_val = (first_val+last_val)//2

    return mid_val


def binary_search(sorted_list,f,l, value):
    if len(sorted_list) > 1:

        if len(sorted_list) == 1:
            return 0
        middle_value = (f+l)//2
        if value == sorted_list[middle_value]:
            return middle_value
        elif value < sorted_list[middle_value]:

            # sorted_list = sorted_list[:middle_value]
            # middle_value = calculate_middle_value(0, len(sorted_list[middle_value]))
            return binary_search(sorted_list, 0, len(sorted_list[:middle_value]), value)
        else:
            # middle_value = calculate_middle_value(len(sorted_list[middle_value]), len(sorted_list))
            # sorted_list = sorted_list[middle_value:]
            return binary_search(sorted_list,len(sorted_list[:middle_value]), len(sorted_list), value)
    else:
        return "Not Found"
li = [1,2,3,4,5,6,7,8,9]
print binary_search(li, 0, len(li), 15)

#
print random.uniform(10, 100)"""
