def find_pattern(pattern, dna):
    pat_len = len(pattern)
    dna_len = len(dna)
    pat_result = []
    
    for i in range(dna_len - pat_len + 1):
        j = 0
        while(j < pat_len):
            if (dna[i + j] != pattern[j]):
                break
            j += 1
        
        if (j == pat_len):
            pat_result.append(i)
        
    print("Pattern found at index = ", pat_result)


dna = "ATGAACACGAATAAAGA"
pattern = "GAA"

find_pattern(pattern=pattern, dna=dna)