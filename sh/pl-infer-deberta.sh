#!/bin/bash
#SBATCH --job-name=pl-infer-deberta
#SBATCH --nodes=1                   
#SBATCH --ntasks=1                  
#SBATCH --cpus-per-task=8           
#SBATCH --mem=32GB
#SBATCH --time=167:00:00
#SBATCH --mail-type=END             
#SBATCH --mail-user=yw3642@nyu.edu  
#SBATCH --output=log/%x-%A.out
#SBATCH --error=log/%x-%A.err
#SBATCH --gres=gpu:1                
#SBATCH -p aquila                   
#SBATCH --nodelist=agpu7            

module purge                        
module load anaconda3 cuda/11.1.1              

nvidia-smi
nvcc --version
cd /gpfsnyu/scratch/yw3642/nbme/src     

echo "START"               
source deactivate
source /gpfsnyu/packages/anaconda3/5.2.0/bin/activate kaggle          
python -u pl_infer.py \
--pretrained_checkpoint /gpfsnyu/scratch/yw3642/hf-models/microsoft_deberta-large \
--model_dir /gpfsnyu/scratch/yw3642/nbme/ckpt/2022-04-28-23:23:06-cf4f
echo "FINISH"                       