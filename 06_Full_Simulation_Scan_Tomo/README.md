# MD4224_Light
## 06_Full_Simulation_Scan: Full simulation scan (sc grid 128 x 128 x 64, 5E5 particles) using Tomo longitudinal distribution

- Each simulation in the scan has an identical setup, and uses the folder name to set certain switches.
- Start by editing the simulation in 00_Master.
- Once the simulation is complete (remove all old simulation folders) use create_new_scan.sh to copy the master simulation into the correct folder names.
- On HPC-Batch, one may simply pull the repository, and run Submit_All.py to submit all simulations to run on HPC-Batch.

## 00_Master:
- **simulation_parameters.py**: majority of simulation setup is done here
- **pyOrbit.py**: main simulation file
- **Flat_file.madx**: MAD-X script used to create a PTC flat file, read by PyORBIT to create the accelerator lattice
- **Make_SLURM_submission_script.py**: used to automatically generate the HPC-Batch simulation submission script
- **Make_SLURM_plotting_script.py**: used to automatically generate the HPC-Batch plotting submission script
- **Plot_Tune_and_Distn_Footprints.py**: used to plot tune footprint and bunch distributions for dumped turns (select in simulation parameters)
- **clean_all.sh**: resets simulation folder completely - **WARNING: removes all simulation output**
- **clean_run.sh**: removes simulation output files
- **clean_junk.sh**: removes junk files from simulation run
- **setup_environment.sh**: calls PyORBIT custom enviroment - required for a simulation on AFS/LXPlus/HPC-Batch (note python 2.7)
- **START_local.sh**: script to run simulation locally in an AFS accessible directory (LXPlus, HPC-Batch, etc)
- **PTC/**: PTC scripts
- **PS_Lattice/**: fixed version of the PS lattice pulled from acc-models
- **lib/**: PyORBIT libraries used for things such as generation of initial distribution, generating and handling output etc

## Output_playground_SC_NoSC.ipynb:
- Once simulations are complete, one may use this notebook to compare all output/output.mat files in which we record turn-by-turn bunch data
- Output plots are saved in Plots/

## create_new_scan.sh
- copies 00_Master to create full simulation scan folder structure for both H and V scans with and without space charge (or as selected in create_new_scan.sh)

## Submit_All.py
- python script used to go into each simulation folder, run Make_SLURM_submission_script to create SLURM_submission_script.sh for each simulation, then calls the script to launch on HPC-Batch
- use like: python Submit_All.py

## Submit_Plots.py
- python script used to go into each simulation folder, run Make_SLURM_plotting_script to create SLURM_plotting_script.sh for each simulation, then calls the script to launch on HPC-Batch
- use like: python Submit_All.py

## distribute_master.py
- python script to copy individual files from 00_master to selected simulation scan folders

## Git_Commands.sh
- example Git commands used to save data etc
