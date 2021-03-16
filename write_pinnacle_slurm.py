#!/usr/bin/env python3

# This script generates a slurm file for the AHPCC Pinnacle Cluster
# define variables

job_name = 'harumi_pin'
queue = 'ocomp06'
out = 'harumi_pin'
node = 1
pro = 32
wall = 6 # this is in hours

print('#SBATCH -J', job_name) # job name
print('#SBATCH --partition', queue) # which queue to use
print('#SBATCH -o' + out +'_%j.txt') # STDOUT output file
print('#SBATCH -e' + out +'_%j.err') # STDERR output file
print('#SBATCH --nodes=' + str(node)) # number of nodes
print('#SBATCH --ntasks-per-node=' + str(pro)) # number of processor
print('#SBATCH --time=' + str(wall)+ ':00:00') # set the walltime

print (
'''
export OMP_NUM_THREADS=32
 
# load required modules
module load samtools
module load jellyfish
module load bowtie2
module load salmon/0.8.2
module load java
 
# cd into the directory where you're submitting this script from
cd $SLURM_SUBMIT_DIR

# copy files from storage to scratch
rsync -av RNA-R*.fastq.gz /scratch/$SLURM_JOB_ID

# cd onto the scratch disk to run the job
cd /scratch/$SLURM_JOB_ID/

# run the Trinity assembly
/share/apps/bioinformatics/trinity/trinityrnaseq-v2.11.0/Trinity --seqType fq --left RNA-R1.fastq.gz --right RNA-R2.fastq.gz --CPU 48 --max_memory 250G --trimmomatic --no_normalize_reads --full_cleanup --output trinity_Run2
 
# copy output files back to storage
rsync -av trinity_Run2 $SLURM_SUBMIT_DIR
'''
)