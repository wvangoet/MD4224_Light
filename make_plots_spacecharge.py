#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:03:59 2020

@author: wvangoet
"""

from make_spacecharge_plots_lib import *

setup_plt()

SC_flag = 1

dd1 = dict()
dd2 = dict()
dd3 = dict()
dd4 = dict()
dd5 = dict()
dd6 = dict()

#SPACECHARGE
add_input_folder(dd1, '12_mini_simulation_old/', 1, SC_flag)
add_input_folder(dd2, '12_mini_simulation_old/', 0, SC_flag)
add_input_folder(dd3, '09_Test_simulation_Lattice1/', 1, SC_flag)
add_input_folder(dd4, '09_Test_simulation_Lattice1/', 0, SC_flag)
add_input_folder(dd5, '10_Test_simulation_Lattice2/', 1, SC_flag)
add_input_folder(dd6, '10_Test_simulation_Lattice2/', 0, SC_flag)

dd1.pop('6.20')

make_directory('Plots')

dd_list = [dd1,dd3,dd5,dd2,dd4,dd6]

#%%
from make_spacecharge_plots_lib import *

#sigma_x
plot_parameter(dd_list,'sig_x', r'$\sigma_{x}$ [mm]', 1E3, SC_flag)
#sigma_xp
plot_parameter(dd_list,'sig_xp', r'$\sigma_{xp}$ [-]', 1E3, SC_flag)
#sigma_y
plot_parameter(dd_list,'sig_y', r'$\sigma_{y}$ [mm]', 1E3, SC_flag)
#sigma_yp
plot_parameter(dd_list,'sig_yp', r'$\sigma_{yp}$ [-]', 1E3, SC_flag)

#beta_x
plot_parameter(dd_list,'beta_x', r'$\beta_x$ [m]', 1,SC_flag)
#beta_y
plot_parameter(dd_list,'beta_y', r'$\beta_y$ [m]', 1,SC_flag)
#D_x
plot_parameter(dd_list,'D_x', r'$D_x$ [m]', 1,SC_flag)
#D_y
plot_parameter(dd_list,'D_y', r'$D_y$ [m]', 1,SC_flag)

#dpp_rms
plot_parameter(dd_list,'dpp_rms', r'$\frac{\delta p}{p}_{RMS}$ [1E-3]', 1E3, SC_flag)
#bunchlength
plot_parameter(dd_list,'bunchlength', r'B$_l$ [ns]', 1E9, SC_flag)
#sig_z
plot_parameter(dd_list,'sig_z', r'$\sigma_z$ [m]', 1, SC_flag)
#sig_dE
plot_parameter(dd_list,'sig_dE', r'$\sigma_{dE}$ [MeV]', 1E3, SC_flag)
#eps_z
plot_parameter(dd_list,'eps_z', r'$\epsilon_z$ [eV s]', 1, SC_flag)
#espn_x
plot_parameter(dd_list,'epsn_x', r'$\epsilon_x$ [mm mrad]', 1E6, SC_flag)
#espn_y
plot_parameter(dd_list,'epsn_y', r'$\epsilon_y$ [mm mrad]', 1E6, SC_flag)
#light average emittance
plot_parameter_av_em(dd_list, 1E6, SC_flag)

#%%
from make_spacecharge_plots_lib import *
#emmitance end point
plot_parameter_em(dd_list, 1E6, 1)

#%%

fig, ax = plt.subplots()
plot_dict_em(dd_list[0],dd_list[2],dd_list[4],ax,'epsn_x', 1E6)

