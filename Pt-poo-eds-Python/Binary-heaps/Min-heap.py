# Min-heap: init method
# Nodes has int data types, methods compare natural numbers

from cgitb import small
from crypt import methods
from heapq import heapify
from sys import implementation
from turtle import up


class MinHeap:
    def __init__(self, capacity):
        self.storage = [0]*capacity
        self.capacity = capacity
        self.size = 0
	
# Min-heap: helper methods (parent and child indexes)

def getParentIndex( self, index):
    return (index-1)//2

def getLeftChildIndex( self, index ):
    return 2*index+1

def getRightChildIndex( self, index ):
    return 2*index+2

# If the node has or no a parent: boolean
def hasParent( self, index ):
    return self.getParentIndex(index)  >= 0

# Whether or not, if the index es greater, this can not have a child
def hasLeftChild( self, index ):
    return self.getLeftChildIndex( index ) < self.size

def hasRightChild( self, index ):
    return self.getRightChild( index ) < self.size

# ---- Min-heap helper methods
def parent( self, index ):
    return self.storage[ self.getParentIndex(index) ]

def leftChild( self, index ):
    return self.storage[ self.getLeftChildIndex(index) ]

def rightChild( self, index ):
    return self.storage[ self.getRightChildIndex(index) ]


def isFull( self ):
    return self.size== self.capacity

def swap( self, index1, index2 ):
    temp  = self.storage[index1]
    self.storage[ index1 ] = self.storage[ index2 ]
    self.storage[ index2 ] = temp

# ---- Inserting within the heap
def insert( self, data):
    if( self.isFull() ):
        raise("Heap is full")
    
    self.storage[ self.size ] = data
    self.size += 1
    self.heapifyUp()
    
# --- min-heap: heapify up
def heapifyUp( self ):
    index = self.size-1
    while( self.hasParent(index) and self.parent(index) > self.storage[ index ] ):
        self.swap( self.getParentIndex(index), index )
        index = self.getParentIndex(index)


# ------ Recursive implementation  methods
def insert( self, data):
    if( self.isFull() ):
        raise("Heap is full")
    
    self.storage[ self.size ] = data
    self.size += 1
    self.heapifyUp( self.size-1 )
    
# --- min-heap: heapify up
def heapifyUp( self, index ):
    # index = self.size-1
    # while -> if
    if( self.hasParent(index) and self.parent(index) > self.storage[ index ] ):
        self.swap( self.getParentIndex(index), index )
        self.heapifyUp( self.getParentIndex(index) )

# --Min-heap: remove min
def removeMin(self):
    if( self.size ==0 ):
        raise( "Empty heap" )
    data= self.storage[0]
    self.storage[0] = self.storage[self.size-1]
    self.size-=1
    self.heapifyDown()
    return data

def heapifyDown( self ):
    index=0
    while( self.hasLeftChild(index) ):
        smallerChildIndex = self.getLeftChildIndex(index)
        if( self.hasRightChild(index) and self.rightChild(index)<self.leftChild(index) ):
            smallerChildIndex = self.getRightChilIndex(index)
        if(self.storage[index] < self.storage[smallerChildIndex] ):
            break
        else:
            self.swap( index, smallerChildIndex )
        index = smallerChildIndex
    
    
# -- Recursive implementation
def removeMin(self):
    if( self.size ==0 ):
        raise( "Empty heap" )
    data= self.storage[0]
    self.storage[0] = self.storage[self.size-1]
    self.size-=1
    self.heapifyDown(0)
    return data
    
def heapifyDown(self, index):
    smallest = index
    
    if(self.hasLeftChild(index) and self.storage[smallest] > self.leftChild(index) ):
        smallest = self.getLeftChildIndex(index)
    if( self.hasRightChild(index) and self.storage[smallest] > self.rightChild(index) ):
        smallest = self.getRightChildIndex(index)
    if( smallest != index ):
        self.swap( index, smallest )
        self.heapifyDown(smallest)
        
    
    


