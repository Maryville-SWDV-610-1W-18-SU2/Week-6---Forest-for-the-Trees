'''
Week 6 - Forest for the Trees
Generate a random list of integers.  
Show the binary heap tree resulting from inserting the integers on the list one at a time.
Using the list from the previous question, show the binary heap tree resulting from the list as a parameter to the buildHeap method.  
Show both the tree and list form.'''

from random import *
from pythonds.binaryHeap import *

#function to display number tree"""
def displayTree(items):
    print()
    print("{0:>20}".format(items[1]))
    print()
    print("{0:>18}{1:>4}".format("/", " \\" ))
    print()
    print("{0:16}{1:>9}".format(items[2 * 1], items[2 * 1 + 1]))
    print()
    print("{0:>14}{1:>4}{2:>5}{3:>4}".format("/", " \\", "/", " \\" ))
    print()
    print("{0:>12}{1:7}{2:>3}{3:>7}".format(items[2 * 2], items[2 * 2 + 1],items[2 * 3], items[2 * 3 + 1]))
    
#function to test inserting integers one at a time
def oneAtATime(randomNumbers):
    binHeap = BinaryHeap()
    print("Random Numbers = ", randomNumbers)
    print()
    print("------------List one at a time----------------")
    #insert values one number at a time
    for i in range(7):
        binHeap.insert(randomNumbers[i])
    displayTree(binHeap.getResults())


def main():
    
    #generate randomly a list of numbers between 1 and 250 of length 7
    randomNumbers = sample(range(1,250), 7)
    oneAtATime(randomNumbers)

    
main()