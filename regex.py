# Define a function clean(s) where s is a string and
# the function returns s with all characters removed
# which are not A, C, G, or T.

import re


def clean(s):
    return re.sub("[^ACGT]", "",s)
