# Use these commands to move data from HPC-Batch to the Git repository
# commands are given as run from the directory MD4224_Light/02_Mini_Simulation_Scan/

# Once simulations are run, save all turn-by-turn output data:
git pull                                                                # Make sure your repository is up to date
git add */output/output.mat                                             # Add all output.mat files from this simulation scan to the repository
git commit -m '02: Outputs added on HPC-Batch'                          # Commit the changes to the repository and comment accordingly
git push                                                                # Push the changes to the respository which now includes the output files

# After the simulations are run you may execute Plot_SLURM.sh to plot the dumped bunch tune footprints and phase space
# Note that this is only done for the space charge simulations as without space charge it is not possible to plot the tune footprint
# The plotting script may be run like:
sbatch Plot_SLURM.sh

# Once complete we want to add the plot .png files to the respository
# This is preferable to adding the bunch output files as they are large and GitHub will not accept individual files > 100 MB
# and a warning will be given for files > 50 MB
# Note that for a mini simulation scan each bunch output file is around 5 MB, for the current setup the bunch is dumped 68 times equating to around
# 340 MB. Conversely a single folder of .png files will be around 85 MB

# For mini simulation scans we can add the plots a few simulations at a time
# Adding more may cause the git push to fail on HPC-Batch due to connection time-out etc
git pull
git add 1_H_07/bunch_output/*.png
git add 1_H_08/bunch_output/*.png
git add 1_H_09/bunch_output/*.png
git commit -m '02: 1_H_ 07,08,09: bunch oputput plots added on HPC-Batch'

git pull
git add 1_H_10/bunch_output/*.png
git add 1_H_11/bunch_output/*.png
git add 1_H_12/bunch_output/*.png
git commit -m '02: 1_H_ 10,11,12: bunch oputput plots added on HPC-Batch'

# To check what you have committed alread use the command:
git status -uno

# Also note that I have used the full commands for git pull/push/add/commit etc
# You may speed up this process by editing your .bashrc (on your HPC-Batch account) and adding:
alias gp='git pull'
alias gpp='git push'
alias gs='git status'                                                   # status of whole respository
alias gsu='git status -uno'                                             # status of repository ignoring untracked files
alias ga='git add'
alias gc='git commit -m'                                                # -m is to add a message in format 'like this'

# After sourcing the edited .bashrc by logging in again or using:
source ~/.bashrc

# You may then change the top set of commands to:
gp                                                                      # Make sure your repository is up to date
ga */output/output.mat                                                  # Add all output.mat files from this simulation scan to the repository
gc '02: Outputs added on HPC-Batch'                                     # Commit the changes to the repository and comment accordingly
gpp                                                                     # Push the changes to the respository which now includes the output files

