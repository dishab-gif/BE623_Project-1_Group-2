Team Members
Member	Category	Gene	Accession
Madhurima Datta (C)	Nuclear (control)	MB (Myoglobin)	NM_001362846
Disha Biswas (B)	Mitochondrial	MT COX1	NC_012920.1
Utsa Das (A) 	Selenoprotein	GPX1	NM_000581.4

For Question 1 the steps that I performed:
•	Ran an unrefined esearch for MB[gene] AND human[orgn] .
•	Refined by fetching directly with the accession NM_001362846 and rettype=fasta to get the exact human RefSeq mRNA record.
•	Downloaded the same accession again with rettype=gb and read the accession, organism, sequence length, CDS coordinates and protein_id from the feature table.
•	Used the protein_id from the GenBank record to fetch the deposited protein as FASTA from the protein database then checked its length with head and grep/wc.
•	Pulled the first header line from every downloaded file into headers.txt.
The commands I used:
 1a) unrefined search https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nucleotide&term=MB[gene]+AND+human[orgn] 
1a) refined fetch (FASTA) 
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=NM_001362846&rettype=fasta&retmode=text # saved as myproj1.fasta 
1b) same record but GenBank format https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=NM_001362846&rettype=gb&retmode=text # saved as sequence.gb 
1c) deposited protein FASTA https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=NP_001349775.1&rettype=fasta&retmode=text # saved as proteinofmb.fasta 
head -1 proteinofmb.fasta grep -v ">" proteinofmb.fasta | tr -d '\n' | wc -c 
1d) headers head -n 1 myproj1.fasta proteinofmb.fasta sequence.gb > headers.txt cat headers.txt
Tools I used –
head, grep, tr, wc, cat.

For Question 2 the steps that I performed –
•	Took the mRNA sequence and cut out just the coding part using the CDS position from question 1(b) (positions 60 to 525). Checked that this piece has 465 letters, which divides evenly by 3 (so it's a whole number of codons). 
•	Made my own codon table (a dictionary listing all 64 possible codons and the amino acid each one stands for). Then went through the coding sequence three letters at a time, looked each codon up in my table and built the protein one amino acid at a time. Printed the first 30 amino acids and the total length.
•	Checked my translated protein against the official one from question 1(c). Removed the * symbol at the end of mine (it just marks "stop," it's not a real amino acid) and cleaned up the official sequence (removed the header line and line breaks). Then compared the two side by side and they matched.
•	Double-checked my work using Biopython's built-in Seq.translate() function on the same coding sequence and it gave the exact same result as my own translation.
The commands I used –
2a) mycds = mrna_sequ[60:525] 
len(mycds), len(mycds) % 3
2b) codon_table = {...} 
for i in range(0, len(mycds), 3): 
myprotein += codon_table[mycds[i:i+3]]
2c) myprotein.rstrip('*') == onlyprotein
2d) from Bio.Seq import Seq 
Seq(mycds).translate()
Tools I used –
Python (manual string slicing, a self-built codon dictionary and a loop) for 2a,b,c and cross-checked with Biopython's Seq.translate() for 2d.

For Question 3 the steps that I performed – 
•	Compared translated length (155, including the * stop symbol) to the deposited protein length (154). 
•	Explained the difference of 1: * marks the translation stop not an amino acid, so once it's stripped the two sequences match exactly (154 residues each).



