from math import log10
def random_genome(dna,gc_content):
    dna = dna.upper()
    logproblist = []
    product = 1
    for i in range(len(gc_content)):
        for c in range(len(dna)):
            if dna[c]=='G' or dna[c]=='C':
                product *= (gc_content[i]/2)
            elif dna[c]=='A' or dna[c]=='T':
                product *= ((1-gc_content[i])/2)
        logproblist.append(log10(product))
        product = 1
    return logproblist