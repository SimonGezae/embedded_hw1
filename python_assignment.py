# #question 1

# def if_function(condition, true_result, false_result):
#     if condition:
#         return true_result
#     else:
#         return false_result

# print(if_function(True, 2, 3))
# print(if_function(2==3, 2, 3))
# print(if_function(3>2, 5-1, 3))

# #question 2
# def sum_odd(num):
#     sum = 0
#     for i in range(num+1):
#         if i%2 != 0:
#             sum = sum + i
    
#     return sum

# print(sum_odd(7))

# # question 3
# def foo(a, b, c, d):
#     list_input = sorted([a, b, c, d])
#     result = list_input[0]**2 + list_input[1]**2
#     return result

# print(foo(2,7,4,2))

# # question 4
# def df(a, b, c):
#     lista = [a,b,c]
#     for i in lista:
#         for j in lista:
#             if i-j in lista:
#                 return True
#     return False

# print(df(7,2,3))

# # question 5
# def lrgst_factor(m):
#     if m <= 1:
#         return "Please enter greater 1"
#     factors = []
#     for i in range(1, m):
#         if m%i == 0:
#             factors.append(i)
#     return max(factors)
    
# print(lrgst_factor(15))

# # question 6
# def pfct_num(m):
#     sum = 0
#     for i in range(1,m):
#         if m%i == 0:
#             sum += i
#     if sum == m:
#         return True
#     return False

# print(pfct_num(8))

# # question 7
# def same_ord(a, b):
#     a = str(a)
#     b = str(b)
#     if len(a) == len(b):
#         return True
#     return False

# print(same_ord(678,100))

# # question 8
# def double_5(n):
#     list_n =[int(x) for x in str(n)]
#     for i in range(len(list_n)-1):
#         if list_n[i] == list_n[i+1] and list_n[i] == 5:
#             return True
#     return False

# print(double_5(505505))

# # question 9
# def uniq_digits(x):
#     list_x = [int(i) for i in str(x)]
#     uniq_digit = []
#     for num in list_x:
#         if num not in uniq_digit:
#             uniq_digit.append(num)
#     return len(uniq_digit)

# print(uniq_digits(1231234))

# # question 10
def sum_proper(num):
    sum = 0
    for i in range(1,num):
        if num%i == 0:
            sum += i
    return sum

def amc(n):
    while True:
        n += 1
        sum_n = sum_proper(n)
        sum_m = sum_proper(sum_n)
        if n != sum_n and n == sum_m:
            return n
        
print(amc(5))



    
    







