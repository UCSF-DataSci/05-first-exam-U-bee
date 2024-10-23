import argparse


def find_cut_sites(sequence, cut_site):
    cut_site = cut_site.replace("|", "") 
    cut_sites = []
    index = sequence.find(cut_site)
    while index != -1:
        cut_sites.append(index)
        index = sequence.find(cut_site, index + 1) 
    return cut_sites

def find_cut_site_pairs(cut_sites, min_distance=80000, max_distance=120000):
    pairs = []
    for i in range(len(cut_sites)):
        for j in range(i + 1, len(cut_sites)):
            distance = cut_sites[j] - cut_sites[i]
            if min_distance <= distance <= max_distance:
                pairs.append((cut_sites[i], cut_sites[j]))
    return pairs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('fasta_file', type=str, help="Path")
    parser.add_argument('cut_site', type=str, help="G|GATCC")
    
    args = parser.parse_args()

    fasta_file = args.fasta_file
    cut_site = args.cut_site

    with open(fasta_file, 'r') as file:
        lines = file.readlines()
        dna_sequence = ''.join([line.strip() for line in lines if not line.startswith(">")])
    
    print(f"Analyzing cut site: {cut_site.replace('|', '')}")

    cut_sites = find_cut_sites(dna_sequence, cut_site)
    print(f"Total cut sites found: {len(cut_sites)}")

    cut_site_pairs = find_cut_site_pairs(cut_sites)
    print(f"Cut site pairs 80-120 kbp apart: {len(cut_site_pairs)}")

    print("First 5 pairs:")
    for idx, (start, end) in enumerate(cut_site_pairs[:5]):
        print(f"{idx + 1}. {start} - {end}")

    results_file = '../results/cutsite_summary.txt'
    with open(results_file, 'w') as file:
        file.write(f"Total cut site pairs 80-120 kbp apart: {len(cut_site_pairs)}\n")
        file.write("First 5 pairs:\n")
        for idx, (start, end) in enumerate(cut_site_pairs[:5]):
            file.write(f"{idx + 1}. {start} - {end}\n")

    print(f"Results saved to {results_file}")

if __name__ == "__main__":
    main()
