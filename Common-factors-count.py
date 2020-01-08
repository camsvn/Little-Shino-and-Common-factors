import time
#from functools import reduce

def gcd(a, b):    
    while b:
        a, b = b, a%b
    return a
'''
#APPROACH 1:
def factors(n):
    c=0
    factors=list()
    for i in range(1,n):        
        if i*i<=n:
            if n%i==0:
                factors.append(i)
                if i*i == n:
                    c+=1
                else:
                    c+=2
                    factors.append(int(n/i))
    if c==0:
        c=1
        factors.append(1)
    print("Factors",factors)
    return c
'''

'''
#APPROACH 2: [With importing functools]
def factors(n):    
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))) 
'''

#APPROACH 3 [Without importing]
def factors(n):    
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result



#Starts Execution from here
try:
    a=int(input("Input your first number: "))
    b=int(input("Input your second number: "))
except:
    print("Expecting Interger Values")

ts=time.time() #timer start
gf=gcd(a,b)
#if using APPROACH 1
'''print(factors(gf))'''
#if using APPROACH 2 & 3
print(len(factors(gf)))
print("Executed in: ",time.time()-ts) #Print time to execute the function