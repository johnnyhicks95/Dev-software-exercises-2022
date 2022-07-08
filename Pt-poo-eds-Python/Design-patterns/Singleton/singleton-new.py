"""
Python doesn't have private constructors, but for this purpose, it has something 
even better. We can use the __new__ class method to ensure that only one instance 
is ever created:
"""
class OneOnly:
    _singleton = None
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(
                OneOnly, cls 
            ).__new__(cls, *args, **kwargs )
        return cls._singleton

"""
>>> o1 = OneOnly()
>>> o2 = OneOnly()
>>> o1 == o2
True
>>> o1
<__main__.OneOnly object at 0xb71c008c>
>>> o2
<__main__.OneOnly object at 0xb71c008c>

"""