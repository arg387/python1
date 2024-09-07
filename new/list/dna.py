dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']
item_found =False
item_to_find = "ACT"

for item in dna_sequence:
  if item == item_to_find:
    item_found = True
  else:
    item_found = False
if item_found == True:
  print("Item Found!")
else:
  print("Item not found")