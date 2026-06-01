import gc

import sys

# Create object - reference count = 1
name = [4,5,2,3,5,3]
print(sys.getrefcount(name))  # shows count

# Add another reference - count = 2
name2 = name
print(sys.getrefcount(name))  # increases

# Delete one reference - count back to 1
del name2
print(sys.getrefcount(name))  # decreases

# Delete last reference - count = 0 → memory freed immediately
del name
# "Ashish" string is now freed from memory