# Tuples => () this is Tuples that cannot be change
masala_spices = ("cardamom","cloves","cinnamom")

(spice1, spice2, spice3) = masala_spices
print(f'Main Masala spices: {spice1}, {spice2}, {spice3}')

ginger_ratio, cadramom_ratio = 2, 1
print(f'ratio is G {ginger_ratio} and C {cadramom_ratio}')
ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio
print(f'ratio is G {ginger_ratio} and C {cadramom_ratio}')

# membership testing

print(f'Is gigner in masala_spices? {'ginger' in masala_spices}')
print(f'Is gigner in masala_spices? {'cinnamom' in masala_spices}')
print(f'Is gigner in masala_spices? {'Cinnamom' in masala_spices}')