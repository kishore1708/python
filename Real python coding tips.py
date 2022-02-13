
#Using Range function
def fizz_buzz(numbers):
    for i in range(len(numbers)):
        num=numbers[i]
        if num%3==0:
            numbers[i]="fizz"
        if num % 5 == 0:
            numbers[i] = "buzz"
        if num%3==0 and num%5==0:
            numbers[i]="fizz_buzz"
    return numbers

a=[2,3,4,5,6,8,9,10]
print(fizz_buzz(a))


#Using Enumaerate function
def fizz_buzz_en(numbers):
    for i,num in enumerate(numbers):
        if num%3==0:
            numbers[i]="fizz"
        if num % 5 == 0:
            numbers[i] = "buzz"
        if num%3==0 and num%5==0:
            numbers[i]="fizz_buzz"
    return numbers

b=[2,4,6,9,10,15]
print(fizz_buzz_en(b))


#map function

lst=[1,3,8,-9]

print(list(map(lambda x:x*x,lst)))

#without using map
def square(x):
    return x*x
num=[]

for i in lst:#Normal for loop
    num.append(square(i))
print(num)

#List comprehension
print([square(i) for i in lst])

#filter
print(list(filter(lambda x:x%2 == 1,lst)))

def _odd(x):#Normal for loop
    return x%2 == 1

num=[]
for i in lst:
    if _odd(i):
     num.append(i)
print(num)

#List comprehension
print([i for i in lst  if _odd(i)])