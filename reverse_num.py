def reverse_number(num):
    n=num
    digit=0
    rev=0
    while n>0:
        digit=n%10 # store last digit
        rev=rev*10+digit # add that digits to rev
        n//=10
    return rev
num=123
print(reverse_number(num))
