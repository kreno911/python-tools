'''
Use this file to do all python 3 class functionality.
Dont build anything real, this should be a knowledge base to use for
all other projects.
'''

'''
Three ways to define singleton:
    -module level - modules are singleton be default
    -create standard singleton class 
    -Borg singleton - use if you need to share state 
        https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/
'''
# Define a Singleton class like we do in Java
# https://www.geeksforgeeks.org/what-is-the-difference-between-__init__-and-__call__/
class Singleton:
    __instance = None

# Define a Settings class which is equal to a properties class
class Settings():
    pass