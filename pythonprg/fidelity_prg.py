data = 100
def fact(n):
    fact = 1
    for i in range (1, n*i):
        fact = fact*i
    return fact

    
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10  
        reversed_num = reversed_num * 10 + digit 
        n //= 10  
    return reversed_num

