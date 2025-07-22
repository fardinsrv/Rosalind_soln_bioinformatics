# We say that position i in k-mers p1 … pk and q1 … qk is a mismatch if pi ≠ qi. For example, CGAAT and CGGAC have two mismatches. The number of mismatches between strings p and q is called the Hamming distance between these strings and is denoted HammingDistance(p, q).

# Hamming Distance Problem
# Compute the Hamming distance between two DNA strings.

# Given: Two DNA strings.

# Return: An integer value representing the Hamming distance.
#ba1g
def hamming_dist(string_1, string_2):
    hamming_distance = 0
    for i in range(len(string_1)):
        if string_1[i]!= string_2[i]:
            hamming_distance += 1
    return hamming_distance      

with open(r"rosalind_datset\rosalind_ba1g.txt", "r") as file:
    lines = file.readlines()
    string_1 = lines[0].strip()
    string_2 = lines[1].strip()
print(hamming_dist(string_1,string_2))
