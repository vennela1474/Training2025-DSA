# a=5
# b=7
# print(a&b)
# print(a|b)
# print(~a)


# sum of even numbers in odd indexes

# n = [2,3,7,5,1,4,6,8,9]
# es = 0
# for i in range(1, len(n), 2):  
#     if n[i] % 2 == 0:         
#         es += n[i]
# print("Sum of even numbers at odd indices:", es)
#l = list(map(int, input("Enter numbers:").split()))
# es = 0
# for i in range(len(n)):
#     if i % 2 != 0 and n[i] % 2 == 0:
#         es += n[i]
# print("Sum of even numbers at odd indices:", es)

# sunlight on building programs

# max=0
# count=0
# for i in l:
#     if i>max:
#         max=i
#         count+=1
# print(count)

# vote 18>= and winner ,2 candidates same -1 

# n=int(input())
# v=list(map(int,input().split()))
# a=list(map(int,input().split()))
# c=max(v)*[0]
# for i in range(n):
#     if a[i]>=18:
#         c[v[i]-1]+=1
# m=max(c)
# temp=sorted(c,reverse=True)
# if temp[0]==temp[1]:
#     print(-1)
# else:
#     print(c.index(temp[0])+1)


#bit manipulation swapping

# a=7
# b=5
# a=a^b
# b=a^b
# a=a^b
# print(a)
# print(b)

# odd or even

# a=17
# if (a&1)==0:
#     print("even")
# else:
#     print("odd")

# l=[1,2,3,4,5,6,7]
# l.append([1,2,3])
# l.extend([1,2])
# l.append(1)
# l.extend({1,2,3,4,2,2,1,3})
# print(len(l))#op: 15

#n=int(input())
# x=0
# for i in range(1,n+1):
#     x^=i
# print(x)#big(N)

# def XoR(n):
#     if n%4==1:
#         return 1
#     if n%4==2:
#         return n+1
#     if n%4==3:
#         return 0
#     if n%4==0:
#         return n#big (1)
# l=int(input())
# r=int(input())
# a=XoR(r)
# b=XoR(l-1)
# print(a^b)

#printing 1 to n to 1 using recursion

# def p(n, c=1):
#     if c == n:
#         return str(n)
#     return str(c) + p(n, c+1)+str(c)
# n= int(input())
# result = p(n)
# print(result)

#54321 tail recursion
# def fun(n):
#     if n==0:
#         return
#     print(n,end=" ")
#     fun(n-1)
# n=5
# fun(n)

#12345 head recursion
# def fun(n):
#     if n==0:
#         return
#     fun(n-1)
#     print(n,end=" ")
# n=5
# fun(n)

#5 4 3 2 1 200

# def fun(n):
#     if n!=0:
#         print(n,end=" ")
#         fun(n-1)
#         return 200
# n=5
# print(fun(n))
# 
# def fun(n):
#     if n==0:
#         return 200
#     print(n,end=" ")
#     t=fun(n-1)
#     return t
# n=5
# print(fun(n))

#5 4 3 2 1 1 2 3 4 5

# def fun(n):
#     if n==0:
#         return 
#     print(n,end=" ")
#     fun(n-1)
#     print(n,end=" ")
# n=5
# fun(n)

#5 4 3 2 1 2 3 4 5 

# def fun(n):
#     if n==0:
#         return 
#     print(n,end=" ")
#     fun(n-1)
#     if n!=1:
#         print(n,end=" ")
# n=5
# fun(n)

#print all natural numbers till n

# def fun(n):
#     if n==0:
#         return
#     fun(n-1)
#     print(n,end=" ")
# n=int(input())
# fun(n)

#all odd numbers from 1 to 100

# def print_odd(n=1):
#     if n > 100:
#         return
#     if n % 2 == 1:
#         print(n)
#     print_odd(n + 1)
# print_odd()
# 
# all even numbers

# def print_even(n=1):
#     if n > 100:
#         return
#     if n % 2 == 0:
#         print(n)
#     print_even(n + 1)
# print_even()

#factorial of a number

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
# n=int(input())
# print(factorial(n))

# given number is prime or not

# def is_prime(n, i=2):
#     if n <= 1:
#         return False
#     if i * i > n:
#         return True
#     if n % i == 0:
#         return False
#     return is_prime(n, i + 1)
# n=int(input())
# print(is_prime(n))

#fibonacci series

# def fib(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# n=int(input())
# print(fib(n))

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# n=int(input())
# print(fibonacci(n))

#minimun path to go to 1 

# def fun(n):
#     if n==1:
#         return 0
#     elif n%2==0:
#         return 1+fun(n//2)
#     else:
#         return 1+min(fun(n-1), fun(n+1))
# n=15
# print(fun(n))

# sum of elements in a list

# def fun(l,i=0):
#     if i==len(l):
#         return 0
#     return l[i]+fun(l,i+1)
# l=[1,4,2,3,5]
# print(fun(l))






