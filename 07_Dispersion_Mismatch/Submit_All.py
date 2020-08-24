import os

Horizontal_Scan_NoSC = True
Horizontal_Scan = True
Vertical_Scan_NoSC = True
Vertical_Scan = True

master_dir = os.getcwd()

H_locations = []
H_locations.append('/1_H_07')
H_locations.append('/1_H_08')
H_locations.append('/1_H_09')
H_locations.append('/1_H_10')
H_locations.append('/1_H_11')
H_locations.append('/1_H_12')
H_locations.append('/1_H_13')
H_locations.append('/1_H_14')
H_locations.append('/1_H_15')
H_locations.append('/1_H_16')
H_locations.append('/1_H_17')
H_locations.append('/1_H_18')
H_locations.append('/1_H_19')
H_locations.append('/1_H_20')
H_locations.append('/1_H_21')

V_locations = []
V_locations.append('/1_V_10')
V_locations.append('/1_V_11')
V_locations.append('/1_V_12')
V_locations.append('/1_V_13')
V_locations.append('/1_V_14')
V_locations.append('/1_V_15')
V_locations.append('/1_V_16')
V_locations.append('/1_V_17')
V_locations.append('/1_V_18')
V_locations.append('/1_V_19')
V_locations.append('/1_V_20')
V_locations.append('/1_V_21')
V_locations.append('/1_V_22')
V_locations.append('/1_V_23')
V_locations.append('/1_V_24')

H_locations_NoSC = []
#H_locations_NoSC.append('/0_H_07')
H_locations_NoSC.append('/0_H_08')
H_locations_NoSC.append('/0_H_09')
H_locations_NoSC.append('/0_H_10')
H_locations_NoSC.append('/0_H_11')
H_locations_NoSC.append('/0_H_12')
H_locations_NoSC.append('/0_H_13')
H_locations_NoSC.append('/0_H_14')
H_locations_NoSC.append('/0_H_15')
H_locations_NoSC.append('/0_H_16')
H_locations_NoSC.append('/0_H_17')
H_locations_NoSC.append('/0_H_18')
H_locations_NoSC.append('/0_H_19')
H_locations_NoSC.append('/0_H_20')
H_locations_NoSC.append('/0_H_21')

V_locations_NoSC = []
V_locations_NoSC.append('/0_V_10')
V_locations_NoSC.append('/0_V_11')
V_locations_NoSC.append('/0_V_12')
V_locations_NoSC.append('/0_V_13')
V_locations_NoSC.append('/0_V_14')
V_locations_NoSC.append('/0_V_15')
V_locations_NoSC.append('/0_V_16')
V_locations_NoSC.append('/0_V_17')
V_locations_NoSC.append('/0_V_18')
V_locations_NoSC.append('/0_V_19')
V_locations_NoSC.append('/0_V_20')
V_locations_NoSC.append('/0_V_21')
V_locations_NoSC.append('/0_V_22')
V_locations_NoSC.append('/0_V_23')
V_locations_NoSC.append('/0_V_24')

if Horizontal_Scan_NoSC:
	for loc in H_locations_NoSC:
		print '--------------------------------------------------------------------------------------------'
		print '\t Submitting HPC-Batch simulation: ', loc
		print '--------------------------------------------------------------------------------------------'
		dir_ = master_dir + loc
		make_command = 'python Make_SLURM_submission_script.py'
		submit_command = 'sbatch SLURM_submission_script.sh'
		os.chdir(dir_)
		os.system(make_command)
		os.system(submit_command)

if Vertical_Scan_NoSC:
	for loc in V_locations_NoSC:
		print '--------------------------------------------------------------------------------------------'
		print '\t Submitting HPC-Batch simulation: ', loc
		print '--------------------------------------------------------------------------------------------'
		dir_ = master_dir + loc
		make_command = 'python Make_SLURM_submission_script.py'
		submit_command = 'sbatch SLURM_submission_script.sh'
		os.chdir(dir_)
		os.system(make_command)
		os.system(submit_command)

if Horizontal_Scan:
	for loc in H_locations:
		print '--------------------------------------------------------------------------------------------'
		print '\t Submitting HPC-Batch simulation: ', loc
		print '--------------------------------------------------------------------------------------------'
		dir_ = master_dir + loc
		make_command = 'python Make_SLURM_submission_script.py'
		submit_command = 'sbatch SLURM_submission_script.sh'
		os.chdir(dir_)
		os.system(make_command)
		os.system(submit_command)

if Vertical_Scan:
	for loc in V_locations:
		print '--------------------------------------------------------------------------------------------'
		print '\t Submitting HPC-Batch simulation: ', loc
		print '--------------------------------------------------------------------------------------------'
		dir_ = master_dir + loc
		make_command = 'python Make_SLURM_submission_script.py'
		submit_command = 'sbatch SLURM_submission_script.sh'
		os.chdir(dir_)
		os.system(make_command)
		os.system(submit_command)
