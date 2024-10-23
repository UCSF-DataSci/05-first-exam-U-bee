'''
File name: `dna_operations.py`

Create a Python script that performs various operations on DNA sequences. Your script should:

1. Accept a DNA sequence as a command-line argument.
2. Implement the following functions:
   - `complement(sequence)`: Returns the complement of a DNA sequence (A -> T, C -> G, G -> C, T -> A).
   - `reverse(sequence)`: Returns the reverse of a sequence (e.g. "CCTCAGC" -> "CAGCCTC").
   - `reverse_complement(sequence)`: Returns the reverse complement of a DNA sequence (e.g. "CCTCAGC" -> "GAGCTTG"); i.e. the reverse of the complement (apply `complement` then `reverse`, or vice versa).
3. For the input sequence, print:
   - The original sequence
   - Its complement
   - Its reverse
   - Its reverse complement

Tips:
- Create a dictionary mapping each base to its complement for easy lookup; e.g., `complement['A'] = 'T'`.
- String slicing with a step of -1 can be used to reverse a string efficiently.
- Remember to handle both uppercase and lowercase input.
- Use `sys.argv` or `argparse` to access command-line arguments in your script.
- (optional, advanced) Use `str.maketrans()` and `str.translate()` for efficient base substitution.

### Task

Run the script on the sequence "CCTCAGC"

### Example usage
`````
python dna_operations.py GAATTC
`````

Expected output:
`````
Original sequence: GAATTC
Complement: CTTAAG
Reverse: CTTAAG
Reverse complement: GAATTC
'''
import argparse

def reverse(sequence):
    return sequence[::-1]

def complement(sequence):
    map = str.maketrans("ATGC", "TACG")
    return sequence.translate(map)

def reverse_complement(sequence):
    return complement(reverse(sequence))

def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument("dna_sequence", type=str, help="dna sequence to modify")
        
    args = parser.parse_args()
    sequence = args.dna_sequence.upper()

    allowed = {'A','T','G','C'}
    if not set(sequence) <= allowed:
        print("Your input has dissallowed values in it, this only accepts DNA sequence characters (AGTC)")
        return
    print(f"Original sequence: {sequence}")
    print(f"Complement: {complement(sequence)}")
    print(f"Reverse: {reverse(sequence)}")
    print(f"Reverse complement: {reverse_complement(sequence)}")

if __name__ == "__main__":
    main()