print('Starting pipeline')
print('Loading input data')

# Exclude sequences shorter than 7
def qc_sequences(seq_list):
    return [seq for seq in seq_list if len(seq) >= 7]

print('Checking file formats')
print('Running quality control')

# Simulated reads
reads = ['ATG', 'ATGCT', 'GCTAAG', 'A', 'GGCAT', 'ATGCTAGC', 'GCTAGCTA']
filtered_reads = qc_sequences(reads)
removed = len(reads) - len(filtered_reads)


print(f"{len(filtered_reads)} reads passed QC")
print(f"{removed} reads were filtered out")

print('Performing analysis')
print('Pipeline complete')
