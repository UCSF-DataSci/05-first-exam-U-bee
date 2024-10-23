import random
import textwrap

sequence_length = 1000000
nucleotides = ['A', 'C', 'G', 'T']
random_sequence = ''.join(random.choices(nucleotides, k=sequence_length))
formatted_sequence = textwrap.fill(random_sequence, width=80)


with open("..\\data\\random_sequence.fasta", 'w') as f:
    f.write(formatted_sequence)

print("Random DNA sequence generated and saved to random_sequence.fasta")