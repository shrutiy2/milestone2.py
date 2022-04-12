def get_edges(dna_dict):
    edge_adj_list = [] #initialize list to accumulate ROSALIND indentifier tuples
    suff_dict = {} #initialize two dictionaries to modify input for easier processing
    pref_dict = {}
    for key in dna_dict:
        pref_dict[key] = (dna_dict[key])[0:3] #pairs ROSALIND identifiers with first 3 associated bases 
        suff_dict[key] = (dna_dict[key])[len(dna_dict[key])-3:len(dna_dict[key])] #pairs ROSALIND identifiers with last 3 associated bases 
    for key in suff_dict:
        for key2 in pref_dict:
            if suff_dict[key] == pref_dict[key2] and key != key2: #finds matching beginning and ending sequences of DNA, if these sequences are not from the same ROSALIND identifier then they share an edge
                edge_adj_list.append((key,key2)) #ROSALIND identifier pair is added to the edge adjacency list
    return edge_adj_list
