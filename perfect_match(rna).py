from math import factorial
def perfect_match(rna):
    rna = rna.upper()
    c_count = rna.count('C')
    a_count = rna.count('A')
    matches = factorial(c_count)*factorial(a_count)
    if len(rna)%2 != 0:
        matches = 0
    return matches