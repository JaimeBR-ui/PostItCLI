# Jaime Bohorquez
# Filename: post.py

import sys
from menu import print_preview

# Let's get how many command line args we have.
length = len(sys.argv)

# The length of the arguments is at least 1 since the fist argument is
# the name of the script that is being interpreted.

if length == 1:
    print_preview()

elif length > 1 and sys.argv[1] == "it":
    # Let's save the rest of the arguments
    pass
elif length > 1 and sys.argv[1] == "show":
    # Show the contents
    pass
