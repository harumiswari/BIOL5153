#! /usr/bin/env python3

# This script generates a PBS file for the AHPCC Razor Cluster

# This section prints the header/required info for the PBS script

# define some variables
job_name = 'harumi_py'
queue = 'onenode16core'
out = 'harumi_py'
node = 1
pro = 10
wall = 3 # this is in hours


print('#PBS -N', job_name) # job name
print('#PBS -q', queue) # which queue to use
print('#PBS -j oe') # join the STDOUT and STDERR into a single file
print('#PBS -o' + out + '.$PBS_JOBID') # set the name of the job output file
print('#PBS -l nodes=' + str(node) + ':ppn=' + str(pro)) # how many resource to ask for (nodes = num nudes, ppn = num processors)
print('#PBS -l walltime=' + str(wall) + ':00:00') # set the walltime (default to 1 hr)
print()

# cd into working directory
print('cd $PBS_O_WORKDIR')
print()

# load the necessary modules
print('# load modules')
print('module purge')
print('module load gcc/7.2.1')
print()

# commands for this job
print('# insert commands here')