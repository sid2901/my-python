# fibonacci_series
#it is a series of numbers in which each number is a sum of the preceeding number
n=int(input("enter a number"))
sum=0
a=0
b=1
count =1
while(count<=n):
    count+=1
    print (sum)
    a=b
    b=sum
    sum=a+b