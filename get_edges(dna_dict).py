def get_edges(dna_dict):
    edge_adj_list = []
    suff_dict = {}
    pref_dict = {}
    for key in dna_dict:
        pref_dict[key] = (dna_dict[key])[0:3]
        suff_dict[key] = (dna_dict[key])[len(dna_dict[key])-3:len(dna_dict[key])]
    for key in suff_dict:
        for key2 in pref_dict:
            if suff_dict[key] == pref_dict[key2] and key != key2:
                edge_adj_list.append((key,key2))
    return edge_adj_list