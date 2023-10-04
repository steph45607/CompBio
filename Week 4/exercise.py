import re
import tracemalloc

def validate_dna(dna):
    dna_len = len(dna)
    result = re.search("[TGACtagc]*", dna)
    # miss used "^[CAGTcagt]+$"
    re_len = len(result.group())
    if dna_len == re_len:
        print("True")
        return True
    else:
        print("False")
        return False

def improved_validation(dna):
    


tracemalloc.start()
validate_dna("gsdkajfdsa")
print(tracemalloc.get_traced_memory())
tracemalloc.stop()

tracemalloc.start()
validate_dna("AAGTCCCTGACT")
print(tracemalloc.get_traced_memory())
tracemalloc.stop()