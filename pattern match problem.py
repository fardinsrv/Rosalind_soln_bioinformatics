# In this problem, we ask a simple question: how many times can one string occur as a substring of another? Recall from “Find the Most Frequent Words in a String” that different occurrences of a substring can overlap with each other. For example, ATA
#  occurs three times in CGATATATCCATAG
# .

# Pattern Matching Problem
# Find all occurrences of a pattern in a string.

# Given: Strings Pattern and Genome.

# Return: All starting positions in Genome where Pattern appears as a substring. Use 0-based indexing.
#ba1d
def pattern_matching_prob(pattern,genome):
    position = ''
    for i in range(0,len(genome)-len(pattern)+1):
        if genome[i:i+len(pattern)] == pattern:
            position += str(i) + " " 
    return position

with open(r"rosalind_datset\rosalind_ba1d.txt", "r") as file:
    line = file.read().splitlines()
pattern =line[0].strip()
genome = line[1].strip()
print(pattern_matching_prob(pattern,genome))
