# MD4224_Light
## 02_Mini_Simulation_Scan: Mini simulation scan (sc grid 64 x 64 x 32, 5E4 particles) using Tomo longitudinal distribution

- Each simulation in the scan has an identical setup, and uses the folder name to set certain switches.
- Start by editing the simulation in 00_Master.
- Once the simulation is complete (remove all old simulation folders) use create_new_scan.sh to copy the master simulation into the correct folder names.
- On HPC-Batch, one may simply pull the repository, and run Submit_All.py to submit all simulations to run on HPC-Batch.

## 00_Master:
- simulation_parameters.py: majority of simulation setup is done here
- pyOrbit.py: main simulation file
- Flat_file.madx: MAD-X script used to create a PTC flat file, read by PyORBIT to create the accelerator lattice
- Make_SLURM_submission_script.py: used to automatically generate the HPC-Batch simulation submission script
- clean_all.sh: resets simulation folder completely - WARNING: removes all simulation output
- clean_run.sh: removes simulation output files
- clean_junk.sh: removes junk ifles from simulation run
- setup_environment.sh: calls PyORBIT custom enviroment - required for a simulation on AFS/LXPlus/HPC-Batch
- START_local.sh: script to run simulaiton locally in an AFS accessible directory (LXPlus, HPC-Batch, etc)
- PTC/ PTC scripts
- PS_Lattice/: fixed version of the PS lattice pulled from acc-models
- lib/: PyORBIT libraries used for things such as generation of initial distribution, generating and handling output etc

## Output_playground_SC_NoSC.ipynb:
- Once simulations are complete, one may use this notebook to compare all output/output.mat files in which we record turn-by-turn bunch data

## create_new_scan.sh
- copies 00_Master to create full scan

## Submit_All.py
- python script used to go into each simulation folder, run Make_SLURM_submission_script to create SLURM_submission_script.sh for each simulation, then calls the script to launch on HPC-Batch


