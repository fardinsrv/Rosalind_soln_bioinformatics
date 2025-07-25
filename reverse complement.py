# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'. Given a nucleotide p, we denote its complementary nucleotide as p. The reverse complement of a DNA string Pattern = p1…pn is the string Pattern = pn … p1 formed by taking the complement of each nucleotide in Pattern, then reversing the resulting string.

# For example, the reverse complement of Pattern = "GTCA" is Pattern = "TGAC".

# Reverse Complement Problem
# Find the reverse complement of a DNA string.

# Given: A DNA string Pattern.

# Return: Pattern, the reverse complement of Pattern.

#ba1c
def reverse_complement(string):
    com = {"A": "T", "T": "A", "C": "G", "G": "C"}
    complement = ''
    for i in string:
        complement += com[i]
    return complement[::-1]
