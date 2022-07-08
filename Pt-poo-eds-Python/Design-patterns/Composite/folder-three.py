"""
System like a folder structure, functions available like add, 
move, copy, delete.
"""

from ast import Delete
from platform import node

"""
For each folder (composite) object, we maintain a dictionary of children. Often, a 
list is sufficient, but in this case, a dictionary will be useful for looking up children 
by name. Our paths will be specified as node names separated by the / character, 
similar to paths in a Unix shell.
"""

class Component:
    def __init__(self, name ) -> None:
        self.name = name

    def move( self, new_path ):
        new_folder = get_path(new_path)
        del self.parent.children( self.name )
        new_folder.children[self.name ] = self
        self.parent = new_folder
        
    def delete( self ):
        del self.parent.children[self.name ]
        
class Folder( Component ):
    def __init__(self, name) -> None:
        super().__init__(self, name)
        self.children = {}
        
    def add_child( self, child ):
        pass
    
    def copy(self, new_path):
        pass
    
class File( Component ):
    def __init__(self, name, contents ) -> None:
        super().__init__(name)
        self.contents = contents
        
    def copy( self, new_path ):
        pass
    
root = Folder('')
def get_path(path):
    names = path.split('')[1:]
    node = root
    for name in names:
        node = node.children[name]
    return node

def add_child( self, child ):
    child.parent = self
    self.children[child.name] = child

"""
$ python3 -i 1261_09_18_add_child.py
>>> folder1 = Folder('folder1')
>>> folder2 = Folder('folder2')
>>> root.add_child(folder1)
>>> root.add_child(folder2)
>>> folder11 = Folder('folder11')
>>> folder1.add_child(folder11)
>>> file111 = File('file111', 'contents')
>>> folder11.add_child(file111)
>>> file21 = File('file21', 'other contents')
>>> folder2.add_child(file21)
>>> folder2.children
{'file21': <__main__.File object at 0xb7220a4c>}
>>> folder2.move('/folder1/folder11')
>>> folder11.children
{'folder2': <__main__.Folder object at 0xb722080c>, 'file111': <__main__.
File object at 0xb72209ec>}
"""

""" 
----- With no base classes
class Folder:
    def __init__(self, name) -> None:
        pass
    
    def add_child( self, child ):
        pass
    
    def move( self, new_path ):
        pass
    
    def copy( self, new_path ):
        pass
    
    def delete( self ):
        pass
    
    
class File:
    def __init__(self, name, contents ) -> None:
        self.name = name
        self.contents = contents

    def move( self, new_path ):
        pass
    
    def copy( self, new_path ):
        pass
    
    def delete( self ):
        pass
 
  """