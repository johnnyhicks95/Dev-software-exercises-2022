# example, go trough a list

import sys

x = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# (les efficent ) it has to storage the list on memory
print(sys.getsizeof(x))

# (mroe efficient) Does nto starage a list in memory
print(sys.getsizeof(range(1, 11)))  

for element in x:
        print(element)

for i in range( 1, 11 ):
    print(i)

# -------------------------------
# Example 2
# mapear una lista que regrese un iterador de los elementos encontrados

y= map( lambda i: i**2, x )

print (y) # reutrn a memory object location
print( list(y) ) # returns :[ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]

#in a iteration
for i in y:
    print(i)

# (les efficent ) it has to storage the list on memory
print(sys.getsizeof(list(y) ))  # 152
# (mroe efficent ) it has to storage the list on memory
print( sys.getsizeof(y) )  #48

# next()
print( next(y) )  # 1
print( next(y) )  # 4
print( next(y) )  # 9
print( next(y) )  # 16

print("For loop starts")
# -- another way to iterate using for
for i in y:
    print(i)
# 25  36  49  64  81 100


# -- another way to iterate using while
while True:  # becouse we do not know ho wmany items
    try:
        value = next(y)
        print(value)
    except StopIteration:
        print('Done')
        break


# iter

x = range(1, 11)

next( iter(x) )
#for i in iter(x)

#----------------------
# Creating legacy iterators
class Iter:
    def __init_(self, n):
        self.n = n

    def __iter__(self):
        self.current = -1
        return self 

    def __next__(self):
        self.current += 1

        if self.current >= self.n:
            raise StopIteration

        return self.current


X = Iter(5)
for i in x:
    print(i)  # 0 1 2 3 4

itr = iter(x)
print( next(itr) )  # 0
print( next(itr) )  # 1
print( next(itr) )  # 2


#----------------------
# Creating  iterators
def gen(n):
    for i in range(n):
        yield i

for i in gen(5):
    print(i)

 