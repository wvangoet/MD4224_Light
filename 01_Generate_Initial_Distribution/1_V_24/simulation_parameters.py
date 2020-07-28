import os
import numpy as np

# Folder naming convention:
# Space charge flag - horizontal/vertical scan - scan point
# e.g. 0_H_07

space_charge_flag = int(os.getcwd().split('/')[-1][0])
print 'simulation_parameters: space charge = ', space_charge_flag
transverse_plane = os.getcwd().split('/')[-1][2]
print 'simulation_parameters: transverse_plane = ', transverse_plane
scan_tune = os.getcwd().split('/')[-1][-2:]

parameters = {}

# Nominal working point for BCMS PS beam
parameters['tunex']			= '6.21'
parameters['tuney']			= '6.24'

if transverse_plane == 'H':
        parameters['lattice_start'] 	= 'PR.BWSH65'
        parameters['tunex']             = '6.' + str(scan_tune)
elif transverse_plane == 'V':
        parameters['lattice_start'] 	= 'PR.BWSV64'
        parameters['tuney']             = '6.' + str(scan_tune)
else:
        print 'simulation_parameters: transverse plane selection not recognised, please use either H or V in the folder name'
        print 'For example: 0_H_07 will launch a no space charge simulation for the horizontal tune of 6.07'
        exit(0)
        
        
parameters['n_macroparticles']			= int(5E5)

# Make sure to fix the initial distribution at the nominal working point (6.21, 6.24)
parameters['tomo_file'] = '../../00_Longitudinal_Distribution/PyORBIT_Tomo_file_MD4224_HB.mat'
parameters['input_distn']=''

parameters['gamma']			= 2.49253731343
parameters['intensity']			= 72.5E+10
parameters['bunch_length']		= 140e-9
parameters['blength']			= 140e-9
parameters['epsn_x']			= 1E-6
parameters['epsn_y']			= 1E-6
parameters['dpp_rms']			= 8.7e-04
parameters['LongitudinalJohoParameter'] = 1.2
parameters['LongitudinalCut'] 	        = 2.4
parameters['TransverseCut']		= 5
parameters['rf_voltage']		= 0.0212
parameters['circumference']		= 2*np.pi*100
parameters['phi_s']			= 0
parameters['macrosize']			= parameters['intensity']/float(parameters['n_macroparticles'])

# PS Injection 1.4 GeV
parameters['gamma'] 	= 2.49253731343
parameters['beta'] 	= np.sqrt(parameters['gamma']**2-1)/parameters['gamma']
c 			= 299792458
parameters['sig_z'] 	= (parameters['beta'] * c * parameters['blength'])/4.

parameters['turns_max'] = int(2200)

# Define how often we dump bunch output files
#-----------------------------------------------------------------------
tu1 = range(-1, parameters['turns_max'], 200) # every 200 turns
tu2 = range(50, 100, 10)        # every 10 turns between 50-100
tu3 = range(1, 50)              # every turn for the first 50 turns
tu = tu2 + tu1 + tu3 
tu.append(874) # Wire Scanner at ctime = 172 s
tu.append(2185)# Wire Scanner at ctime = 175 s
# ~ tu.append(6556)# Wire Scanner at ctime = 185 s
parameters['turns_print'] = sorted(tu)
parameters['turns_update'] = sorted(tu)

# Simulation switches
#-----------------------------------------------------------------------
switches = {
        'CreateDistn': True,
	'Update_Twiss':	False,  # Perform PTC twiss and dump each turn - needed to output tune changes
	'GridSizeX': 128,
	'GridSizeY': 128,
	'GridSizeZ': 64
}

if space_charge_flag:
        switches['Space_Charge'] = True        
        parameters['BLonD_File'] = '../../00_Longitudinal_Distribution/BLonD_Longitudinal_Distributions/BLonD_Longitudinal_Distn_Run2_MD4224_SC.npz'
else:
        switches['Space_Charge'] = False
        parameters['BLonD_File'] = '../../00_Longitudinal_Distribution/BLonD_Longitudinal_Distributions/BLonD_Longitudinal_Distn_Run2_MD4224.npz'
        

# PTC RF Table Parameters
#-----------------------------------------------------------------------
harmonic_factors = [1] # this times the base harmonic defines the RF harmonics (for SPS = 4620, PS 10MHz 7, 8, or 9)
time = np.array([0,1,2])
ones = np.ones_like(time)
Ekin_GeV = 1.4*ones
RF_voltage_MV = np.array([parameters['rf_voltage']*ones]).T # in MV
RF_phase = np.array([np.pi*ones]).T

RFparameters = {
	'harmonic_factors': harmonic_factors,
	'time': time,
	'Ekin_GeV': Ekin_GeV,
	'voltage_MV': RF_voltage_MV,
	'phase': RF_phase
}

# Write tunes.str file for MAD-X input
#-----------------------------------------------------------------------
script_name = 'tunes.str'
if os.path.exists(script_name):  
	print 'tune file ' + script_name + ' already exists. Deleting'
	os.remove(script_name)

f= open(script_name,"w")

f.write('/**********************************************************************************\n')
f.write('*                             Tunes for PTC-PyORBIT simulation\n')
f.write('***********************************************************************************/\n')
f.write('tune_x = 0.' + str(parameters['tunex'][-2:]) + ';\n')
f.write('tune_y = 0.' + str(parameters['tuney'][-2:]) + ';\n')
f.write('lattice_start = ' + transverse_plane + ';')
