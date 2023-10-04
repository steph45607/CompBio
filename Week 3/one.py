def validate_dna(dna):
    seqm = dna.upper()
    valid = seqm.count("A") + seqm.count("C") + seqm.count("G") + seqm.count("T")
    if valid == len(seqm):
        return True
    else:
        return False

def freq(amino):
    dict = {}
    for i in amino.upper():
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
    n = len(dna)
    for i in dict:
        percent = (dict[i]/n)*100
        print(i + " = " + str(percent) + "%")

def complement(dna):
    pairs = {
    'A':'T', 'T':'A', 'G':'C', 'C':'G'
    }
    dna = dna.upper()
    reverse = []

    for i in range(len(dna)):
        if dna[i] in pairs:
            reverse.append(pairs[dna[i]])

    string = ""

    print("Complement =  " + string.join(reverse))

def transcription(dna):
    translate_rna = {
        'A':'U', 'T':'A', 'G':'C', 'C':'G'
    }
    dna = dna.upper()
    rna = []

    for i in range(len(dna)):
        if dna[i] in translate_rna:
            rna.append(translate_rna[dna[i]])

    string = ""

    print("mRNA = " + string.join(rna))
    return string.join(rna)

def translate_codon(cod):
    tc = {
        "UUU" : "Phe (F)", "UUC" : "Phe (F)", "UUA" : "Leu (L)", "UUG" : "Leu (L)",
        "UCU" : "Ser (S)", "UCC" : "Ser (S)", "UCA" : "Ser (S)", "UCG" : "Ser (S)",
        "UAU" : "Tyr (Y)", "UAC" : "Tyr (Y)", "UAA" : "_", "UAG" : "_", 
        "UGU" : "Cys (C)", "UGC" : "Cys (C)", "UGA" : "_", "UGG" : "Trp (W)", 

        "CUU" : "Leu (L)", "CUC" : "Leu (L)", "CUA" : "Leu (L)", "CUG" : "Leu (L)", 
        "CCU" : "Pro (P)", "CCC" : "Pro (P)", "CCA" : "Pro (P)", "CCG" : "Pro (P)", 
        "CAU" : "His (H)", "CAC" : "His (H)", "CAA" : "Gln (Q)", "CAG" : "Gln (Q)",
        "CGU" : "Arg (R)", "CGC" : "Arg (R)", "CGA" : "Arg (R)", "CGG" : "Arg (R)", 

        "AUU" : "Ile (I)", "AUC" : "Ile (I)", "AUA" : "Ile (I)", "AUG" : "Met (M)", 
        "ACU" : "Thr (T)", "ACC" : "Thr (T)", "ACA" : "Thr (T)", "ACG" : "Thr (T)",
        "AAU" : "Asn (N)", "AAC" : "Asn (N)", "AAA" : "Lys (K)", "AAG" : "Lys (K)",
        "AGU" : "Ser (S)", "AGC" : "Ser (S)", "AGA" : "Arg (R)", "AGG" : "Arg (R)", 

        "GUU" : "Val (V)", "GUC" : "Val (V)", "GUA" : "Val (V)", "GUG" : "Val (V)", 
        "GCU" : "Ala (A)", "GCC" : "Ala (A)", "GCA" : "Ala (A)", "GCG" : "Ala (A)", 
        "GAU" : "Asp (D)", "GAC" : "Asp (D)", "GAA" : "Glu (E)", "GAG" : "Glu (E)", 
        "GGU" : "Gly (G)", "GGC" : "Gly (G)", "GGA" : "Gly (G)", "GGG" : "Gly (G)", 

    }

    if cod in tc:
        return tc[cod]
    
    else:
        None

def translate(rna):
    amino = []
    if len(rna)%3 == 0:
        for i in range(0, len(rna),3):
            codon = rna[i:i + 3]
            amino.append(translate_codon(codon))
    else:
        print("Not enough nucleotide")
    
    print("Aminoacid = ", ' - '.join(amino))

dna = input("Input DNA = ")

if validate_dna(dna):
    # freq(dna)
    complement(dna)
    # transcription(dna)
    translate(transcription(dna))
else:
    print("Invalid DNA sequence")