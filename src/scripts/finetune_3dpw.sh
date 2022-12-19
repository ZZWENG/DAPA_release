for exp_id in 3dpw_005; do
options=''
case "$exp_id" in
3dpw_005) 
	checkpoint=/scratch/users/zzweng/DAPA/2021_10_23-02_02_06.pt
	noise_scale=0.005
    ds=3dpw_train
;;
3dpw_005_test) 
	checkpoint=/scratch/users/zzweng/DAPA/2021_10_23-02_02_06.pt
	noise_scale=0.05
    ds=3dpw
;;
esac

cmd="train.py --name ours \
--checkpoint ${checkpoint} \
--resume \
--checkpoint_steps 500 \
--log_dir logs \
--ft_dataset ${ds} \
--wandb_project DAPA_clean \
--test_steps 1200 \
--rot_factor 0 \
--ignore_3d \
--add_background \
--openpose_train_weight 1. \
--gt_train_weight 0. \
--use_texture \
--g_input_noise_scale ${noise_scale} \
--g_input_noise_type mul \
--vposer
"


if [ $1 == 0 ] 
then
echo python $cmd
python $cmd
break 100
else
sbatch <<< \
"#!/bin/bash
#SBATCH --job-name=July12
#SBATCH --output=slurm_logs/July12-%j-out.txt
#SBATCH --error=slurm_logs/July12-%j-err.txt
#SBATCH --mem=48gb
#SBATCH --gres=gpu:1
#SBATCH -p syyeung
#SBATCH --time=48:00:00


rm -rf /scratch/groups/syyeung/zzweng/logs/July12_${exp_id}
echo $cmd
python $cmd
"
fi

done

