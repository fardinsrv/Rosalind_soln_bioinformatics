# Given a k-mer Pattern and a longer string Text, we use d(Pattern, Text) to denote the minimum Hamming distance between Pattern and any k-mer in Text,

# d(Pattern,Text)=minall k-mers Pattern' in TextHammingDistance(Pattern,Pattern′).

# Given a k-mer Pattern and a set of strings Dna = {Dna1, … , Dnat}, we define d(Pattern, Dna) as the sum of distances between Pattern and all strings in Dna,

# d(Pattern,Dna)=∑i=1td(Pattern,Dnai).

# Our goal is to find a k-mer Pattern that minimizes d(Pattern, Dna) over all k-mers Pattern, the same task that the Equivalent Motif Finding Problem is trying to achieve. We call such a k-mer a median string for Dna.

#ba2b
#medianstring
def hamming_dist(string_1, string_2):
        hamming_distance = 0
        for i in range(len(string_1)):
            if string_1[i] != string_2[i]:
                hamming_distance += 1
        return hamming_distance
def generate_all_kmers(k):
    bases = ['A', 'C', 'G', 'T']

    kmers = ['']  # start with empty string

    for i in range(k):
        new_kmers = []
        for prefix in kmers:
            for base in bases:
                new_kmers.append(prefix + base)
        kmers = new_kmers

    return kmers

def kmers_from_string(text,k):
    k_mer_list = []
    for i in range(0,len(text)-k+1):
        k_mer_list.append(text[i:i+k])
    return k_mer_list    
         
def medianstring(dna_strings,k):
    #dna_strings = list of st
    median_string = ''
    all_kmers = generate_all_kmers(k)  #all_kmers of length k  
    min_distance = float('inf')  # Initialize to a large number
    for k_mer in all_kmers:
        total_distance = 0

        # Step 2: For each DNA string, find the min distance of this k_mer
        for dna in dna_strings:
            min_dist_in_string = float('inf')

            for substring in kmers_from_string(dna, k):
                dist = hamming_dist(k_mer, substring)
                if dist < min_dist_in_string:
                    min_dist_in_string = dist
            total_distance += min_dist_in_string

        # Step 3: If this total distance is better, update median_string
        if total_distance < min_distance:
            min_distance = total_distance
            median_string = k_mer

    return median_string



with open('rosalind_ba2b.txt', 'r') as file:
        lines = file.read().splitlines()
        k = int(lines[0])        # first line: integer k
        dna_strings = lines[1:]
print(medianstring(dna_strings, k))
