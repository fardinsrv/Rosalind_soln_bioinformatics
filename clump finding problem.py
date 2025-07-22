# Given integers L and t, a string Pattern forms an (L, t)-clump inside a (larger) string Genome if there is an interval of Genome of length L in which Pattern appears at least t times. For example, TGCA
#  forms a (25,3)-clump in the following Genome: gatcagcataagggtcccTGCAATGCATGACAAGCCTGCAgttgttttac
# .

# Clump Finding Problem
# Find patterns forming clumps in a string.

# Given: A string Genome, and integers k, L, and t.

# Return: All distinct k-mers forming (L, t)-clumps in Genome.
#ba1e
def clump_finding_problem(genome,k_mer_length,interval,existing_num):
    string = ''
    already_appearing_kmer = set()
    for i in range(0,len(genome)-interval+1):
        gen = genome[i:i + interval]
        dict = {}
        
        for j in range(0,interval- k_mer_length+1):
            
            key = gen[j: j+ k_mer_length]
            
            if key not in dict :
                dict[key] = 1
            elif key in dict and key not in already_appearing_kmer:
                dict[key] += 1
                if dict[key] >= existing_num:
                    string += key + ' '
                    already_appearing_kmer.add(key)
    return string                


with open(r"rosalind_datset\rosalind_ba1e.txt","r") as file:
    lines = file.readlines()
genome = lines[0].strip()

line_parts = lines[1].strip().split()

k_mer_length = int(line_parts[0])
interval = int(line_parts[1])
existing_num = int(line_parts[2])

print(clump_finding_problem(genome,k_mer_length,interval,existing_num))
