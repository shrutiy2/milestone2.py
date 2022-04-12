from math import log10
def random_genome(dna,gc_content):
    dna = dna.upper()
    logproblist = [] #initialize list to accumulate log_10 of the probability that the input dna is randomly generated given a specific frequency of G or C bases
    product = 1 #initialize a variable to store the current probability at any given time in the following for loop
    for i in range(len(gc_content)): #for each GC frequency the dna strand is read one letter at a time, with each letter having a probability of being randomly chosen given the GC frequency
        for c in range(len(dna)): # these probabilities are all multiplied together in the variable product to give the overall probability that the whole strand is generated
            if dna[c]=='G' or dna[c]=='C':
                product *= (gc_content[i]/2)
            elif dna[c]=='A' or dna[c]=='T':
                product *= ((1-gc_content[i])/2)
        logproblist.append(log10(product)) #the log of the probabilities is taken for comparison and they are added to the list
        product = 1 #product is reset to 1 after each pass through the loop
    return logproblist
