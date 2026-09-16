## Code Used

### 1. CDS Length Calculation

```python
length1 = 189 - 76 + 1
print(length1)

length2 = 966 - 607 + 1
print(length2)

total = length1 + length2
print(total)
print(total % 3)
```

### 2. Define DNA Nucleotides and Reverse Complement

```python
DNA_Nucleotides = ['A', 'C', 'G', 'T']

DNA_ReverseComplement = {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
}
```

### 3. Codon Table

```python
codon_table = {
    "TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
    "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
    "TAT":"Y", "TAC":"Y", "TAA":"Stop", "TAG":"Stop",
    "TGT":"C", "TGC":"C", "TGA":"Stop", "TGG":"W",

    "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
    "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",

    "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
    "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",

    "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
    "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"
}
```

### 4. DNA to mRNA Conversion

```python
mRNA = dna.replace("T", "U")
```

### 5. Manual Protein Translation

```python
protein = ""

for i in range(0, len(cds), 3):
    codon = cds[i:i+3]
    amino_acid = codon_table[codon]

    if amino_acid == "Stop":
        break

    protein += amino_acid

print("Translated protein:", protein)
print("Protein length:", len(protein))
```

### 6. Extracting the First 30 Residues

```python
first_30 = protein[:30]

print(first_30)
print(len(first_30))
```

### 7. Comparing with Deposited Protein

```python
if protein == deposited:
    print("The two sequences are identical.")
else:
    print("The two sequences are NOT identical.")
```

### 8. Biopython Translation

```python
from Bio.Seq import Seq

bio_translation = str(Seq(cds).translate(table=1, to_stop=True))

print("Manual protein length:", len(protein))
print("Biopython protein length:", len(bio_translation))
```

### 9. Finding the First Difference
python
for i, (a, b) in enumerate(zip(protein, bio_translation), start=1):
    if a != b:
        print("First difference at position:", i)
        print("Manual translation:", a)
        print("Biopython translation:", b)
        break
else:
    if len(protein) == len(bio_translation):
        print("The two translations are identical.")
    else:
        print("Sequences match up to the shorter sequence, but lengths differ.")
        
        
        

Ran an unrefined search for GPX1[gene] AND human[orgn].Refined the search by fetching the accession NM_000581.4 in FASTA format to obtain the exact human GPX1 RefSeq mRNA record.
Downloaded the same record again in GenBank format and checked the accession, organism, sequence length, CDS coordinates and protein_id from the feature table.
Used the protein_id from the GenBank record to fetch the deposited GPX1 protein as FASTA from the protein database.Checked the downloaded files using head and grep.Extracted the first header line from each downloaded file into headers.txt.Took the GPX1 mRNA sequence and extracted only the CDS region identified from the GenBank record.Checked that the extracted CDS length is divisible by 3, so that it can be divided into complete codons.
Created my own codon table containing all 64 possible codons and their corresponding amino acids.Read the CDS sequence three nucleotides at a time and looked up each codon in my codon table.Built the translated protein one amino acid at a time.Printed the first 30 amino acids of my translated protein.Compared my translated protein with the deposited GPX1 protein sequence from Question 1(c).Removed the FASTA header and line breaks from the deposited protein sequence before comparison.Also cross-checked my translation using Biopython's Seq.translate() function.Compared the length of my translated GPX1 protein with the deposited GPX1 protein.The canonical deposited GPX1 protein NP_000572.2 is 203 amino acids long. �NCBI +1 The translated sequence was checked against the deposited protein sequence.Compared the two sequences position by position to identify whether they were identical.If a difference was present, recorded the first position where the two sequences differed and reported the amino acid present in each sequence.Also considered the terminal * produced by translation as a stop codon, not as an amino acid.
