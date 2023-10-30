import os
import shutil

# Define the source folder containing numpy files
source_folder = ''

# Define the destination folders
validation_folder = ''
train_folder = ''

# Create the destination folders if they don't exist
if not os.path.exists(validation_folder):
    os.makedirs(validation_folder)
if not os.path.exists(train_folder):
    os.makedirs(train_folder)

# Define the list of patient numbers for the validation set
validation_patients = [
    '001', '004', '006', '010', '016', '023', '026', '031', '034', '040', '043', '046', '047', '056', '057', '058',
    '064', '073', '074', '077', '078', '079', '083', '091', '094', '095', '102', '109', '110', '115', '120', '125',
    '127', '133', '138', '146', '153', '154', '156', '177', '181', '194', '195', '196', '209', '219', '220', '221',
    '226', '230', '232', '234', '238', '240', '250', '251', '256', '279', '287', '289', '293', '298', '306', '311',
    '312', '315', '327', '328', '335', '343', '350', '352', '359', '368'
]

# List all files in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith('.npy'):
        file_path = os.path.join(source_folder, filename)

        # Extract the patient number from the filename
        patient_number = filename.split('_')[2]

        # Choose the destination folder based on patient number presence in the list
        if patient_number in validation_patients:
            destination = validation_folder
        else:
            destination = train_folder

        # Move the file to the appropriate destination
        shutil.move(file_path, os.path.join(destination, filename))

print("File movement complete.")
