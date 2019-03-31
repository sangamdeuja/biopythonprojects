
# Write a function ngram2i(ngram) where ngram is a short
# string with the alphabet ACGT and the function returns
# its position among all strings of the same length when alphabetically
# sorted
#
# for example ngram2i("AAAA") should return 0
# ngram2i("AAAC") should return 1
# ngram2i("AAAT") should return 3
# ngram2i("AACA") should return 4
# ...
# ngram2i("TTTT") should return 255


def ngram2i(ngram):
    myDict={'A':0,'C':1,'G':2,'T':3}
    n=len(ngram)
    N=0
    for item in ngram:
        N=N*4+myDict[item]
    return N

print ngram2i('TT')
