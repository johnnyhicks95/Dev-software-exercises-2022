""" 
List: [1, 2, "a", 3]

List comprehenssion:
    [expression for val in collections]
    [ expr for val in collection if <test> ]
    [ expr for val in collection if <test> and <test 2> ]
    [ expr for val in collection1 and val2 in collection2 ]
"""

# ------ List of squares ------
squares = [ ]

for i in range (1, 10):
    squares.append(i**2)
print(squares) 

# --> using comprehension
squares2 = [i**2 for i in range(1,10) ]
print(squares2)

# ------ List oof squares divided by 5 ------
remainders5 = [ x**2 % 5 for x in range(1,10) ]



# ------ List of movies ------
movies = ["Star wars", "Gandhi", "Casablanca"]
gmovies = []

for title in movies:
    if title.startswith("G"):
        gmovies.append(title)

print(gmovies)
# Using list comprehension
gmovies = [ title for title in movies if title.startswith("G") ]
print(gmovies)
# ["Gandhi"]



# ------ List of movies in tuples ------
movies = [ 
          ("Cirizen Kane", 1941), 
          ("Spirited Away",2001),
          ("Gattaca", 1997) 
]

# Find movies released before 2000
pre2k = [ title for (title, year) in movies if year < 2000 ]
print( pre2k )
# --> output
# [ 'Citizen Kane', 'Gattaca'  ]



# ------ Escalar multiplication ------
v= [2, -3, 1]
# DO Not try! =  4*v
w = [ 4*x for x in v ]
print(w)
# --> output
# [8, -12, 4]



# ------ Cartesian Product ------
# If A and B are sets, the the cartesian product is set of pairs
# (a,b) where 'a' is in A and 'b' is in B

""" Example:
    A= {1, 3}
    B= {x,y}
    AxB= { (1,x), (1,y), (3,x), (3,y) } 
"""

A = [ 1, 3, 5, 7]
B = [ 2, 4, 6, 8 ]
cartesian_product = [ (a, b) for a in A for b in B ]
print( cartesian_product )

""" [(1, 2), (1, 4), (1, 6), (1, 8), (3, 2), (3, 4), 
(3, 6), (3, 8), (5, 2), (5, 4), (5, 6), (5, 8), 
(7, 2), (7, 4), (7, 6), (7, 8)]
 """