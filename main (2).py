a=int(input('Enter the number'))
r=0
while(a>0):
    re=a%10
    r=(r*10)+re
    a=a/10
print'Reverse of entered number is',r
    