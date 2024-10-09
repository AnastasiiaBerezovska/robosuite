import os

# Directory containing the demo files
directory = "/home/anastasiia/my_project/FinalDemonstrations"

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a demo file
    if filename.endswith(".hdf5"):
        # Construct the command to run the script
        command = f"/home/anastasiia/fri/bin/python /home/anastasiia/robomimic/robomimic/scripts/conversion/convert_robosuite.py --dataset {os.path.join(directory, filename)}"
        print(command)
        # Run the command
        os.system(command)