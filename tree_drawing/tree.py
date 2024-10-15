# tree.py

from turtle import *
# 💻 IMPORT MODULES BELOW  💻 #
from tree_parts import tree_top, tree_trunk



# 💻 WRITE THE tree_full() FUNCTION BELOW  💻 #
def tree_full(size):
    tree_trunk(size)
    penup()
    back(25)
    pendown()
    tree_top(size)
    


# 💻 DON'T FORGET TO CALL THE FUNCTION BELOW  💻 #
tree_full(100)
input()
