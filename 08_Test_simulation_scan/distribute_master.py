import shutil

pyorbit = False
simulation_parameters = False
lib_bunch_gather = False
bunch_plotting = True
plotting_script = True

Horizontal_Scan_NoSC = True
Horizontal_Scan = True
Vertical_Scan_NoSC = True
Vertical_Scan = True

master_directory = './00_Master'
pyorbit_file = master_directory + '/pyOrbit.py'
sim_params_file = master_directory + '/simulation_parameters.py'
flat_file = master_directory + '/lib/pyOrbit_Bunch_Gather.py'
bunch_plotting_file = master_directory + '/Plot_Tune_and_Distn_Footprints.py'
plotting_script_file = master_directory + '/Make_SLURM_plotting_script.py'

H_locations = []
#H_locations.append('./1_H_07')
#H_locations.append('./1_H_08')
#H_locations.append('./1_H_09')
#H_locations.append('./1_H_10')
#H_locations.append('./1_H_11')
#H_locations.append('./1_H_12')
#H_locations.append('./1_H_13')
#H_locations.append('./1_H_14')
#H_locations.append('./1_H_15')
#H_locations.append('./1_H_16')
#H_locations.append('./1_H_17')
#H_locations.append('./1_H_18')
#H_locations.append('./1_H_19')
#H_locations.append('./1_H_20')
H_locations.append('./1_H_21')

V_locations = []
#V_locations.append('./1_V_10')
#V_locations.append('./1_V_11')
#V_locations.append('./1_V_12')
#V_locations.append('./1_V_13')
#V_locations.append('./1_V_14')
#V_locations.append('./1_V_15')
#V_locations.append('./1_V_16')
#V_locations.append('./1_V_17')
#V_locations.append('./1_V_18')
#V_locations.append('./1_V_19')
#V_locations.append('./1_V_20')
#V_locations.append('./1_V_21')
#V_locations.append('./1_V_22')
#V_locations.append('./1_V_23')
V_locations.append('./1_V_24')

H_locations_NoSC = []
#H_locations_NoSC.append('./0_H_07')
#H_locations_NoSC.append('./0_H_08')
#H_locations_NoSC.append('./0_H_09')
#H_locations_NoSC.append('./0_H_10')
#H_locations_NoSC.append('./0_H_11')
#H_locations_NoSC.append('./0_H_12')
#H_locations_NoSC.append('./0_H_13')
#H_locations_NoSC.append('./0_H_14')
#H_locations_NoSC.append('./0_H_15')
#H_locations_NoSC.append('./0_H_16')
#H_locations_NoSC.append('./0_H_17')
#H_locations_NoSC.append('./0_H_18')
#H_locations_NoSC.append('./0_H_19')
#H_locations_NoSC.append('./0_H_20')
H_locations_NoSC.append('./0_H_21')

V_locations_NoSC = []
#V_locations_NoSC.append('./0_V_10')
#V_locations_NoSC.append('./0_V_11')
#V_locations_NoSC.append('./0_V_12')
#V_locations_NoSC.append('./0_V_13')
#V_locations_NoSC.append('./0_V_14')
#V_locations_NoSC.append('./0_V_15')
#V_locations_NoSC.append('./0_V_16')
#V_locations_NoSC.append('./0_V_17')
#V_locations_NoSC.append('./0_V_18')
#V_locations_NoSC.append('./0_V_19')
#V_locations_NoSC.append('./0_V_20')
#V_locations_NoSC.append('./0_V_21')
#V_locations_NoSC.append('./0_V_22')
#V_locations_NoSC.append('./0_V_23')
V_locations_NoSC.append('./0_V_24')


if pyorbit:
	if Vertical_Scan:
		for loc in V_locations:
			newPath = shutil.copy(pyorbit_file, loc)
			print sim_params_file, ' copied to ', loc
	if Horizontal_Scan:
		for loc in H_locations:
			newPath = shutil.copy(pyorbit_file, loc)
			print sim_params_file, ' copied to ', loc
	if Vertical_Scan_NoSC:
		for loc in V_locations_NoSC:
			newPath = shutil.copy(pyorbit_file, loc)
			print sim_params_file, ' copied to ', loc
	if Horizontal_Scan_NoSC:
		for loc in H_locations_NoSC:
			newPath = shutil.copy(pyorbit_file, loc)
			print sim_params_file, ' copied to ', loc

if simulation_parameters:
	if Vertical_Scan:
		for loc in V_locations:
			newPath = shutil.copy(sim_params_file, loc)
			print sim_params_file, ' copied to ', loc
	if Horizontal_Scan:
		for loc in H_locations:
			newPath = shutil.copy(sim_params_file, loc)
			print sim_params_file, ' copied to ', loc
	if Vertical_Scan_NoSC:
		for loc in V_locations_NoSC:
			newPath = shutil.copy(sim_params_file, loc)
			print sim_params_file, ' copied to ', loc
	if Horizontal_Scan_NoSC:
		for loc in H_locations_NoSC:
			newPath = shutil.copy(sim_params_file, loc)
			print sim_params_file, ' copied to ', loc

if lib_bunch_gather:
	if Vertical_Scan:
		for loc in V_locations:
			loc_2 = loc + '/lib'
			newPath = shutil.copy(flat_file, loc_2)
			print sim_params_file, ' copied to ', loc_2
	if Horizontal_Scan:
		for loc in H_locations:
			loc_2 = loc + '/lib'
			newPath = shutil.copy(flat_file, loc_2)
			print sim_params_file, ' copied to ', loc_2
	if Vertical_Scan_NoSC:
		for loc in V_locations_NoSC:
			loc_2 = loc + '/lib'
			newPath = shutil.copy(flat_file, loc_2)
			print sim_params_file, ' copied to ', loc_2
	if Horizontal_Scan_NoSC:
		for loc in H_locations_NoSC:
			loc_2 = loc + '/lib'
			newPath = shutil.copy(flat_file, loc_2)
			print sim_params_file, ' copied to ', loc_2
                        
if bunch_plotting_file:
	if Vertical_Scan:
		for loc in V_locations:
			newPath = shutil.copy(bunch_plotting_file, loc)
			print bunch_plotting_file, ' copied to ', loc
	if Horizontal_Scan:
		for loc in H_locations:
			newPath = shutil.copy(bunch_plotting_file, loc)
			print bunch_plotting_file, ' copied to ', loc
	if Vertical_Scan_NoSC:
		for loc in V_locations_NoSC:
			newPath = shutil.copy(bunch_plotting_file, loc)
			print bunch_plotting_file, ' copied to ', loc
	if Horizontal_Scan_NoSC:
		for loc in H_locations_NoSC:
			newPath = shutil.copy(bunch_plotting_file, loc)
			print bunch_plotting_file, ' copied to ', loc
                        
if plotting_script:
	if Vertical_Scan:
		for loc in V_locations:
			newPath = shutil.copy(plotting_script_file, loc)
			print plotting_script_file, ' copied to ', loc
	if Horizontal_Scan:
		for loc in H_locations:
			newPath = shutil.copy(plotting_script_file, loc)
			print plotting_script_file, ' copied to ', loc
	if Vertical_Scan_NoSC:
		for loc in V_locations_NoSC:
			newPath = shutil.copy(plotting_script_file, loc)
			print plotting_script_file, ' copied to ', loc
	if Horizontal_Scan_NoSC:
		for loc in H_locations_NoSC:
			newPath = shutil.copy(plotting_script_file, loc)
			print plotting_script_file, ' copied to ', loc
