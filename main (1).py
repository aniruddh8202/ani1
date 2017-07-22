a=int(input("Enter the number"))
factorial=1
if a<0:
    print'factorial of a negative number does not exist'
elif a==0:
    print'Answer is 0'
else:
    for i in range(1,a + 1):
       factorial = factorial*i
    print'The factorial of',a,'is',factorial
    
    