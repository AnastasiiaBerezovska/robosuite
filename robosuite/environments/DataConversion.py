import argparse
import json
import os
import h5py
from glob import glob
from collections import Counter
import numpy as np
import datetime
import cv2

def convert_to_robomimic(hdf5_name, out_dir):
    out_path = os.path.join(out_dir, "new_final_robomimic_data.hdf5")
    f_out = h5py.File(out_path, mode='w')
    f_out_data_grp = f_out.create_group("data")
         

    h5fr = h5py.File(hdf5_name,'r')
    for demo_name in h5fr.keys():
        current_demo = h5fr [demo_name]
        actions = current_demo["actions"]
        states = current_demo["states"]
        observations = current_demo["observations"]
        #timestamps

        print(demo_name)
        print(len(states))
  
        new_num_samples = actions.shape[0]
        # import ipdb; ipdb.set_trace()
        new_states = np.concatenate((states["position"], states["orientation"]), axis=1)
        new_actions = np.concatenate((actions["position"], actions["orientation"]), axis=1)
        new_observations = np.zeros((new_num_samples, 64, 64, 3)) # initializations
        # import ipdb; ipdb.set_trace()
        for i in range (new_num_samples):
            current_image = observations[i]
            crop_image = current_image [:, 280:280+720] # cropped image
            resize_image = cv2.resize(crop_image, (64, 64))
            new_observations[i] = resize_image
        f_out_data_grp[demo_name+ "/"+ "num_samples"] = new_num_samples
        f_out_data_grp[demo_name+ "/"+ "actions"] = new_actions
        # f_out_data_grp[demo_name+ "/"+ "states"] = new_states
        f_out_data_grp[demo_name+ "/"+ "obs/image"] = new_observations
        f_out_data_grp[demo_name+ "/"+ "obs/state"] = new_states
        print(new_observations.shape)
        print(new_actions.shape)
        print(new_states.shape)

    f_out.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--hdf5", type=str, required = True)
    parser.add_argument("-d", "--save-directory", type=str, required=True)
    args = parser.parse_args()
    if not os.path.exists(args.save_directory):
        os.makedirs(args.save_directory)

    convert_to_robomimic(args.hdf5, args.save_directory)
 # write file