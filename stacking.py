import os
import numpy as np

# Define the paths to your data and the output folder
data_folder = 'preprocessed data'
output_folder = 'training'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize a dictionary to store stacked arrays
stacked_arrays = {}

# List of subfolder names
subfolders = ['t1', 't2', 't1ce', 'flair']

for subfolder in subfolders:
    # Define the path to the current subfolder
    subfolder_path = os.path.join(data_folder, subfolder)

    # Loop through the numpy files in the current subfolder
    for filename in os.listdir(subfolder_path):
        if filename.endswith('.npy'):
            file_path = os.path.join(subfolder_path, filename)
            file_name = os.path.splitext(filename)[0]

            # Load the numpy array
            data = np.load(file_path)

            # Check if the array name already exists in the dictionary
            if file_name in stacked_arrays:
                print(f"Stacking '{file_name}' from '{subfolder}' into the dictionary.")
                stacked_arrays[file_name] = np.stack([stacked_arrays[file_name], data], axis=-1)
            else:
                print(f"Creating '{file_name}' entry for '{subfolder}' in the dictionary.")
                stacked_arrays[file_name] = data

# Save the stacked arrays to the output folder
for name, stacked_array in stacked_arrays.items():
    output_path = os.path.join(output_folder, f'{name}.npy')
    np.save(output_path, stacked_array)

print("Data stacking and saving complete.")
