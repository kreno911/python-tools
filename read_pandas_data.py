import pandas as pd

print("Pandas version: %s" % pd.__version__)

# Add to notes for exceptions
def except_raise1(level):
    ''' if level is negative, throw/raise exception '''
    if level < 1:
        raise Exception(level, "Hello")
    return level

try:
    level = except_raise1(-22) # change to 33 to test else (-22)
    print("Level was %d" % level)
except Exception as e:
    #print("Bad value: %s" % e.args[0])  # Will print: Bad value: -22
    print("All values: ", e.args)  # Will print: All values:  (-22, 'Hello')
else:
    print("Enter good value...see this message...")  # When: 33
finally:
    print("Finally always executed...")  # Always prints


