#right-angle triangle
x= 1
n= 5
while ( x<= n):
    print("*" * x)
    x= x+1



#isosceles triangle
j=9
for i in range(1,10,2):
    print(" "*j+i*"*")
    j=j-1



#diamond
n = 4
for i in range(n-1):
    print((n-i) * " " + (2*i+1) *"*")
for j in range(n-1, -1, -1):
    print((n-j) * " " + (2*j+1) *"*")


#reverse right-angle triangle
num = 5
for z in range(1,num+1):
    print("*"* num)
    num = num-1




