import itertools
import sys

""" generators
Are Functions that act like iterators
"Generates" the elements in a loop
"On demand" iteration object
 """

def g():
    yield 1
    yield 2
    yield 3
    
# print( g() )
# <generator object g at 0x0000001c1f848BAS0>
# Object let us iterate over
""" for x in g():
    print(x) """
""" 1
2
3 
"""


# ----- Prime numbers ----
def prime_numbers():
    #Handle the first prime
    yield 2
    prime_cache = [2] # Cache of primes
    
    # loop over positive, odd integers
    for n in itertools.count(3, 2):
        is_prime = True 
        
        # Chech to see if any prime number divides n
        for p in prime_cache:
            if n % p == 0:
                is_prime = False
                break
        
        # Is it prime?
        if is_prime:
            prime_cache.append(n)
            yield n 
            
for p in prime_numbers():
    print(p)
    if p > 30:
        break
    

# ---- Generator expression: ( expression ) ------

squares = ( x**2 for x in itertools.count(1) )
print("")
print("Generator expression")
for x in squares:
    print(x)
    
    if x > 10:
        squares.close()
        
print( "Bites size: " )
print(sys.getsizeof(squares))
