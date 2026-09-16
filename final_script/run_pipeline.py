import csv
from pathlib import Path
from Bio import Entrez, SeqIO

Entrez.email = "your_email@example.com"

SCRIPT_DIR = Path(__file__).resolve().parent
RESULTS_DIR = SCRIPT_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)

genes = [
    {"name": "MB",   "category": "Nuclear control", "accession": "NM_001362846", "feature_gene": None,   "table": 1},
    {"name": "COX1", "category": "Mitochondrial",    "accession": "NC_012920.1",  "feature_gene": "COX1", "table": 2},
    {"name": "GPX1", "category": "Selenoprotein",    "accession": "NM_000581.4",  "feature_gene": None,   "table": 1},
]

results = []

for gene in genes:
    print("Processing", gene["name"])

    handle = Entrez.efetch(db="nucleotide", id=gene["accession"], rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()

    cds_feature = None
    for feature in record.features:
        if feature.type == "CDS":
            if gene["feature_gene"] is None:
                cds_feature = feature
                break
            elif gene["feature_gene"] in feature.qualifiers.get("gene", []):
                cds_feature = feature
                break

    cds_seq = cds_feature.location.extract(record.seq)
    cds_length = len(cds_seq)

    deposited_protein = cds_feature.qualifiers["translation"][0]
    deposited_length = len(deposited_protein)

    translated_protein = str(cds_seq.translate(table=gene["table"], to_stop=True))
    translated_length = len(translated_protein)

    if translated_protein == deposited_protein:
        identical = "Y"
        first_mismatch = "NA"
    else:
        identical = "N"
        first_mismatch = None
        shortest = min(translated_length, deposited_length)
        for i in range(shortest):
            if translated_protein[i] != deposited_protein[i]:
                first_mismatch = i + 1
                break
        if first_mismatch is None:
            first_mismatch = shortest + 1

    results.append([
        gene["name"],
        gene["accession"],
        gene["category"],
        cds_length,
        translated_length,
        deposited_length,
        identical,
        first_mismatch,
    ])

output_file = RESULTS_DIR / "summary_table.tsv"
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(["Gene","Accession", "Category", "CDS_length", "Translated_length",
                      "Deposited_length", "Identical", "First_mismatch_position"])
    writer.writerows(results)

print("Summary table saved to:", output_file)
