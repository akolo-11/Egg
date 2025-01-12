import math
import datetime
from my_module import ident# Или import my_module
#from package import addition
from package import subtraction
from package.addition import add
from package.multiplication import mult as mult1ply
import package
#from package.subtraction import sub

def task_1_2():
    print(math.sqrt(9))
    print(datetime.datetime.now())
    ident()

def task_3():
    print(add(5, 4))
    print(subtraction.sub(5, 4))
    print(package.addition.add(1, 2))
    print(mult1ply(2, 3))

task_1_2()
print("-------------------------------------")
task_3()