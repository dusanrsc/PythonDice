import os
import random

from random import randint

dice = random.randint(1, 6)

os.system("color 0a")
os.system("mode 27,14")

input("\n        Press ENTER")

if dice == 1:
    print("""
        ___________
       |           |
       |           |
       |           |
       |     *     |
       |           |
       |           |
       |           |
        -----------
         """)
    
if dice == 2:
    print("""
        ___________
       |           |
       |  *        |
       |           |
       |           |
       |           |
       |        *  |
       |           |
        -----------
          """)
    
if dice == 3:
    print("""
        ___________
       |           |
       |  *        |
       |           |
       |     *     |
       |           |
       |        *  |
       |           |
        -----------
          """)
    
if dice == 4:
    print("""
        ___________
       |           |
       |  *     *  |
       |           |
       |           |
       |           |
       |  *     *  |
       |           |
        -----------
          """)
    
if dice == 5:
    print("""
        ___________
       |           |
       |  *     *  |
       |           |
       |     *     |
       |           |
       |  *     *  |
       |           |
        -----------
          """)
    
if dice == 6:
    print("""
        ___________
       |           |
       |  *     *  |
       |           |
       |  *     *  |
       |           |
       |  *     *  |
       |           |
        -----------
          """)
input()
