for exp_id in gym; do
options=''
case "$exp_id" in
gym) 
	checkpoint=/scratch/users/zzweng/DAPA/2021_10_23-02_02_06.pt
	noise_scale=0.5
    ds=gymnastics
    options=""
;;
gymnastics_darkpose) 
	checkpoint=/scratch/users/zzweng/DAPA/2021_10_23-02_02_06.pt
	noise_scale=0.5
    ds=gymnastics_darkpose
    options=""
;;
gym_baseline) 
	checkpoint=/scratch/users/zzweng/DAPA/2021_10_23-02_02_06.pt
	noise_scale=0.5
    ds=gymnastics
    options="--adapt_baseline --run_smplify"
;;
smart) 
	checkpoint=/scratch/users/zzweng/DAPA/2021_10_23-02_02_06.pt
	noise_scale=1
    ds=smart
    options=""
;;
smart_baseline) 
	checkpoint=/scratch/users/zzweng/DAPA/2021_10_23-02_02_06.pt
	noise_scale=0.5
    ds=smart
    options="--adapt_baseline --run_smplify"
;;
esac

cmd="train.py --name ${exp_id} \
--checkpoint ${checkpoint} \
--resume \
--checkpoint_steps 500 \
--log_dir logs \
--ft_dataset ${ds} \
--wandb_project DAPA_clean \
--test_steps 1200 \
--summary_steps 10  \
--rot_factor 0 \
--ignore_3d \
--num_epochs 200 \
--add_background \
--openpose_train_weight 1. \
--gt_train_weight 0. \
--use_texture \
--g_input_noise_scale ${noise_scale} \
--g_input_noise_type mul \
--vposer  \
${options}
"


if [ $1 == 0 ] 
then
echo python $cmd
python $cmd
break 100
else
sbatch <<< \
"#!/bin/bash
#SBATCH --job-name=aug10
#SBATCH --output=slurm_logs/aug10-%j-out.txt
#SBATCH --error=slurm_logs/aug10-%j-err.txt
#SBATCH --mem=48gb
#SBATCH --gres=gpu:1
#SBATCH -p syyeung
#SBATCH --time=48:00:00


rm -rf /scratch/groups/syyeung/zzweng/logs/aug10_${exp_id}
echo $cmd
python $cmd
"
fi

done

