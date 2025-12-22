# set are always unique
essentail_spices = {'cardamom','ginger','cinnamom'}
optional_spices = {'cloves','ginger','black papper'}

all_spices = essentail_spices | optional_spices
print(f'All spices: {all_spices}')

common_spices = essentail_spices & optional_spices
print(f'Common spices: {common_spices}')

only_in_essential = essentail_spices - optional_spices
print(f'Only in essential: {only_in_essential}')

print(f"is 'cloves' in essentiel spices? {'cloves' in essentail_spices}" )
print(f"is 'cloves' in optinal spices? {'cloves' in optional_spices}" )
