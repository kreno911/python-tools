
## Test out lambda functions

# RULES
# lambdas are anonymous functions (not bound to a name)
# lambdas can only be on 1 line
# python >= 2.2
# made for inline application

# Add some #s
add = lambda num1,num2: num1 + num2
print (add(3,3))
# prints: 6

# Use the map function
result = map(lambda x:x**2,[1,2,4,10,99])
# Assign the list as it changes results if you call list(results) within the print 
list_of_results = list(result)
print ("Map results: ", list_of_results)
# prints: [1, 4, 16, 100, 9801]

# split a sentence and get lenght for each word
string = "I am a string named string with 3 strings"
print("string= %s" % string)
# Need to convert the map to a string to see what it looks like
print(list(map(lambda w: len(w), string.split())))

# Filter function
# Print out all data for values >= 100
# This works in python 2 and 3 but output is slightly diff 
alist = list(filter(lambda n: n >= 100, list_of_results))
print("Filtered list V2.7: ", alist)
