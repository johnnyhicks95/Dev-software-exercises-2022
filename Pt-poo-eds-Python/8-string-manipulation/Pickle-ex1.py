import pickle
# Serialize and deserializing objects
# Too manage classes and objects
# Works only wuth another oython programs

example_dict = { 1:"6", 2:"2", 3:"f" }

# wb: writing bites
pickle_out = open("dict.pickle", "wb")
pickle.dump( example_dict, pickle_out )
pickle_out.close()

# ----- reading pickle file ----
pickle_in = open( "dict.picle", "rb" )
example_dict = pickle.load( pickle_in )

print( example_dict )
print( example_dict[2] )


""" Using classes """
# import pickle
# Use when manipulating machine learning data
class Person:
    def __init__(self, name, age, weight) :
        self.name = name
        self.age = age
        self.weight =weight
        
    def print_info(self):
        print(self.name)
        print(self.age)
        print(self.weight)

    def get_older(self, years):
        self.age+= years
        
p1 = Person( "Mike", 25, 89 )
p1.print_info()
p1.get_older(6)
p1.print_info()

# Create/ write as bites
with open( "mike.pickle", 'wb' ) as f:
    pickle.dump( p1, f )
    
# open a pickle filw
with open( 'micke.pickle','rb' ) as f:
    p1 = pickle.load( f )

p1.print_info()
