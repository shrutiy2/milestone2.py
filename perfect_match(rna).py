from math import factorial
def perfect_match(rna):
    rna = rna.upper() #formatting input for consistency
    c_count = rna.count('C') #counts for each base in the rna strand
    g_count = rna.count('G')
    a_count = rna.count('A')
    u_count = rna.count('U')
    matches = factorial(c_count)*factorial(a_count) #there are n! ways to pair n C's with G's. The same is true for A and U. Multiplying these together gives the number of ways to arrange these arrangements.
    if c_count != g_count or a_count != u_count: #if there is not a G for every C or A for every U a perfect match is impossible
        matches = 0
    return matches
