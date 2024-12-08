def create_codon_dict(file_path):
  file = open (file_path, "r")
  rows = file.readlines()
  file.close()
  new_dict = {}
  for row in rows: 
    row = row.strip().split('\t')
    codon = row[0]
    amino_acid = row[2]
    new_dict[codon] = amino_acid 
  return new_dict


