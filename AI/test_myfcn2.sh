#!/bin/sh
#SBATCH -p v
#SBATCH --gres=gpu:1
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

python3 test_eq_myfcn2.py -d data/Earthquake_Data/data_reshaped_honshu6464_mag50 -g 0 -m result_myfcn2/model_13 -b 10