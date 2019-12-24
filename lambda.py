
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
result = map(lambda x:x**2,[1,2,4,99])
print (list(result))
# prints: [1, 4, 16, 9801]

# split a sentence and get lenght for each word
string = "I am a string named string with 3 strings"
print "string= %s" % string
print map(lambda w: len(w), string.split())

