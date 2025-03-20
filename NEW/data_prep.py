import pandas as pd

# Load the input files
output_props = pd.read_csv('output_properties-v2.csv')
input_e_props = pd.read_csv('input_properties-e-v2.csv')
input_f_props = pd.read_csv('input_properties-f-v2.csv')

# Merge the properties for ematerial
output_props = output_props.merge(
    input_e_props,
    left_on='ematerial',
    right_on='material_code',
    suffixes=('', '_ematerial')
).drop(columns=['ematerial', 'material_code'])

# Merge the properties for fmaterial
output_props = output_props.merge(
    input_f_props,
    left_on='fmaterial',
    right_on='material_code',
    suffixes=('', '_fmaterial')
).drop(columns=['fmaterial', 'material_code'])

# Save the new CSV file
output_props.to_csv('merged_properties.csv', index=False)

print("New CSV file 'merged_properties.csv' has been created.")