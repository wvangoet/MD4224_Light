import os

Horizontal_Scan_NoSC = True
Horizontal_Scan = True
Vertical_Scan_NoSC = True
Vertical_Scan = True

master_dir = os.getcwd()

H_locations = []
H_locations.append('1_H_21p2')
H_locations.append('1_H_21p0')
H_locations.append('1_H_20p8')
H_locations.append('1_H_20p6')
H_locations.append('1_H_20p4')
H_locations.append('1_H_20p2')
H_locations.append('1_H_20p0')
H_locations.append('1_H_19p8')
H_locations.append('1_H_19p6')
H_locations.append('1_H_19p4')
H_locations.append('1_H_19p2')
H_locations.append('1_H_19p0')
H_locations.append('1_H_18p8')
H_locations.append('1_H_18p6')
H_locations.append('1_H_18p4')
H_locations.append('1_H_18p2')
H_locations.append('1_H_18p0')

V_locations = []
V_locations.append('1_V_21p2')
V_locations.append('1_v_21p0')
V_locations.append('1_V_20p8')
V_locations.append('1_V_20p6')
V_locations.append('1_V_20p4')
V_locations.append('1_V_20p2')
V_locations.append('1_V_20p0')
V_locations.append('1_V_19p8')
V_locations.append('1_V_19p6')
V_locations.append('1_V_19p4')
V_locations.append('1_V_19p2')
V_locations.append('1_V_19p0')
V_locations.append('1_V_18p8')
V_locations.append('1_V_18p6')
V_locations.append('1_V_18p4')
V_locations.append('1_V_18p2')
V_locations.append('1_V_18p0')

H_locations_NoSC = []
H_locations_NoSC.append('0_H_21p2')

V_locations_NoSC = []
V_locations_NoSC.append('0_V_21p2')

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
