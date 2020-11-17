#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:02:53 2020

@author: wvangoet
"""

import os
import glob
import imageio
import pickle
import pandas as pd
import numpy as np
import PyNAFF as pnf
import scipy.io as sio 
import matplotlib.cm as cm
from math import log10, floor
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from scipy.optimize import curve_fit


sc = 'SbS'
legend_label1 = r'$Q_x$'  
legend_label2 = r'$Q_y$'   
main_label = 'MD4224_Light'
main_label2 = main_label + '_zoom'
scaled_label = main_label + '_scaled'
turn_tot = 2200
zoom_turns = 30
turns = [0, 1, 10, 50, 100, 874, 2185, 2199]
#betagamma = 2.492104532 * 0.9159915293879255
save_folder = 'Plots'
title_3 = 'Lattice 2'
title_2 = 'Lattice 1'
title_1 = 'Lattice og'
case_label_2 = r'Horizontal Scan ($Q_y$ = 6.24)'
case_label_1 = r'Vertical Scan ($Q_x$ = 6.21)'

def setup_plt():
    plt.rcParams['figure.figsize'] = [9.0, 8.0]
    plt.rcParams['figure.dpi'] = 300
    plt.rcParams['savefig.dpi'] = 300
    
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 14
    
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    
    plt.rcParams['font.size'] = 10
    plt.rcParams['legend.fontsize'] = 8
    
    plt.rcParams['lines.linewidth'] = 1
    plt.rcParams['lines.markersize'] = 5
    
def round_sig(x, sig=3):
        return round(x, sig-int(floor(log10(abs(x))))-1)

def replace_point_with_p(input_str):
        return input_str.replace(".", "p")
    
def is_non_zero_file(fpath):  
        print('\n\t\t\tis_non_zero_file:: Checking file ', fpath)
        print('\n\t\t\tis_non_zero_file:: File exists = ', os.path.isfile(fpath))
        print('\n\t\t\tis_non_zero_file:: Size > 3 bytes = ', os.path.getsize(fpath))
        return os.path.isfile(fpath) and os.path.getsize(fpath) > 3
    
    
    
def add_input_file(dd, filename, label):
	f = filename
	p = dict()
	sio.loadmat(f, mdict=p)
	dd[label] = p	
	print('\tAdded output data from ', filename, '\t dictionary key: ', label)
	return dd

def make_directory(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path) 
        
def add_input_folder(dd, lattice_str, horizontal_flag, spacecharge_flag):
    
    spacecharge_str = str(int(spacecharge_flag))
    if horizontal_flag:
        plane = 'H'
        q_range_min = 7
        q_range_max = 21
        
    else:
        plane = 'V'
        q_range_min = 10
        q_range_max = 24
    
    for i in range(q_range_min,q_range_max+1):
        if i < 10:
           dd = add_input_file(dd, lattice_str+spacecharge_str+'_'+plane+'_0'+str(i)+'/output/output.mat', '6.0'+str(i)) 
        else:
           dd = add_input_file(dd, lattice_str+spacecharge_str+'_'+plane+'_'+str(i)+'/output/output.mat', '6.'+str(i)) 
    
    return dd

def plot_dict(dd,ax,parameter, multi):
    colors = cm.rainbow(np.linspace(0, 1, len(dd.keys())))
    c_it = int(0)
    for key, value in sorted(dd.items()):
        lab_ = key
        ax.plot(dd[key]['turn'][0], dd[key][parameter][0]*multi, label=lab_, color=colors[c_it]);
        c_it = c_it + 1; 

def plot_parameter(dd_list, parameter, ylabels, multi1, SC_flag):
    if bool(SC_flag):
        SC_str = 'SC'
    else:
        SC_str = 'noSC'

    plt.rcParams['figure.figsize'] = [12.0, 8.0]
    hspace = 0.1
    vspace = 0.1
   
    fig, axs = plt.subplots(2, 3, sharex='col', sharey='row', gridspec_kw={'hspace':hspace, 'wspace':vspace})
    (ax1, ax2, ax3), (ax4, ax5, ax6) = axs
    ax_list = [ax1,ax2,ax3,ax4,ax5,ax6]
    
    for i in range(len(dd_list)):
        plot_dict(dd_list[i],ax_list[i],parameter, multi1)
    
    tit = main_label + ' ' + parameter + ' ' + SC_str
    fig.suptitle(tit)
    
    ax1.set_ylabel(ylabels);
    ax4.set_ylabel(ylabels);
    ax4.set_xlabel('Turn [-]');
    ax5.set_xlabel('Turn [-]');
    ax6.set_xlabel('Turn [-]');
    
    ax1.set_title(title_1);
    ax2.set_title(title_2);
    ax3.set_title(title_3);
    
    ax1.legend(loc=2, title=legend_label1);
#    ax2.legend(loc=2, title=legend_label1);
#    ax3.legend(loc=2, title=legend_label1);
    ax4.legend(loc=2, title=legend_label2);
#    ax5.legend(loc=2, title=legend_label2);
#    ax6.legend(loc=2, title=legend_label2);
    
    ax1.grid(lw=0.5, ls=':');     
    ax2.grid(lw=0.5, ls=':');
    ax3.grid(lw=0.5, ls=':');
    ax4.grid(lw=0.5, ls=':');
    ax5.grid(lw=0.5, ls=':');
    ax6.grid(lw=0.5, ls=':');

    ax7 = ax3.twinx()
    ax8 = ax6.twinx()
    
    ax7.set_yticklabels([]);
    ax8.set_yticklabels([]);
    
    ax7.set_yticks([]);
    ax8.set_yticks([]);
    
    ax7.set_ylabel(case_label_2);
    ax8.set_ylabel(case_label_1);
    
    for ax in axs.flat:
        ax.label_outer()  
    
    savename = save_folder +'/' + main_label + '_' + parameter + '_' +SC_str+'.png'
    plt.savefig(savename);

 
    
def plot_parameter_av_em(dd_list, multi1, SC_flag):
    if bool(SC_flag):
        SC_str = 'SC'
    else:
        SC_str = 'noSC'

    plt.rcParams['figure.figsize'] = [12.0, 8.0]
    hspace = 0.1
    vspace = 0.1
   
    fig, axs = plt.subplots(2, 3, sharex='col', sharey='row', gridspec_kw={'hspace':hspace, 'wspace':vspace})
    (ax1, ax2, ax3), (ax4, ax5, ax6) = axs
    ax_list = [ax1,ax2,ax3,ax4,ax5,ax6]
    
    for i in range(len(dd_list)):
        plot_dict_av_em(dd_list[i],ax_list[i], multi1)
    
    tit = main_label + ' average emittance ' + SC_str
    fig.suptitle(tit)
    
    ax1.set_ylabel(r'$\frac{\epsilon_x + \epsilon_y}{2}$ [mm mrad]');
    ax4.set_ylabel(r'$\frac{\epsilon_x + \epsilon_y}{2}$ [mm mrad]');
    ax4.set_xlabel('Turn [-]');
    ax5.set_xlabel('Turn [-]');
    ax6.set_xlabel('Turn [-]');
    
    ax1.set_title(title_1);
    ax2.set_title(title_2);
    ax3.set_title(title_3);
    
    ax1.legend(loc=2, title=legend_label1);
#    ax2.legend(loc=2, title=legend_label1);
#    ax3.legend(loc=2, title=legend_label1);
    ax4.legend(loc=2, title=legend_label2);
#    ax5.legend(loc=2, title=legend_label2);
#    ax6.legend(loc=2, title=legend_label2);
    
    ax1.grid(lw=0.5, ls=':');     
    ax2.grid(lw=0.5, ls=':');
    ax3.grid(lw=0.5, ls=':');
    ax4.grid(lw=0.5, ls=':');
    ax5.grid(lw=0.5, ls=':');
    ax6.grid(lw=0.5, ls=':');

    ax7 = ax3.twinx()
    ax8 = ax6.twinx()
    
    ax7.set_yticklabels([]);
    ax8.set_yticklabels([]);
    
    ax7.set_yticks([]);
    ax8.set_yticks([]);
    
    ax7.set_ylabel(case_label_2);
    ax8.set_ylabel(case_label_1);
    
    for ax in axs.flat:
        ax.label_outer()  
    
    savename = save_folder +'/' + main_label + '_average_emittance_' +SC_str+'.png'
    plt.savefig(savename);
    
def plot_dict_av_em(dd,ax,multi):
    colors = cm.rainbow(np.linspace(0, 1, len(dd.keys())))
    c_it = int(0)
    for key, value in sorted(dd.items()):
        x = np.array(dd[key]['turn'][0])
        y = np.array((dd[key]['epsn_x'][0]*multi + dd[key]['epsn_y'][0]*multi)/2)
        lab_ = key
        ax.plot(x,y, label=lab_, color=colors[c_it]);
        c_it = c_it + 1;    
    
def plot_parameter_em(dd_list, multi1, SC_flag):
    if bool(SC_flag):
        SC_str = 'SC'
    else:
        SC_str = 'noSC'

    plt.rcParams['figure.figsize'] = [12.0, 8.0]
    hspace = 0.1
    vspace = 0.1
   
    fig, axs = plt.subplots(2, 1, gridspec_kw={'hspace':hspace, 'wspace':vspace})
    (ax1), (ax2) = axs
    
    plot_dict_em(dd_list[0],dd_list[1],dd_list[2],ax1,'epsn_x', multi1)
    plot_dict_em(dd_list[3],dd_list[4],dd_list[5],ax2,'epsn_y', multi1)
    
    tit = main_label + ' endpoint emittance ' + SC_str
    fig.suptitle(tit)
    
    ax1.set_ylabel('Horizontal Emittance [mm mrad]');
    ax2.set_ylabel('Vertical Emittance [mm mrad]');
    ax1.set_xlabel('Qx');
    ax2.set_xlabel('Qy');
     
    ax1.legend();
    ax2.legend();

    ax1.grid(lw=0.5, ls=':');     
    ax2.grid(lw=0.5, ls=':');

    ax3 = ax1.twinx()
    ax4 = ax2.twinx()
    
    ax3.set_yticklabels([]);
    ax4.set_yticklabels([]);
    
    ax3.set_yticks([]);
    ax4.set_yticks([]);
    
    ax3.set_ylabel(case_label_2);
    ax4.set_ylabel(case_label_1);
    
#    for ax in axs.flat:
#        ax.label_outer()  
    
    savename = save_folder +'/' + main_label + '_endpoint_em_' +SC_str+'.png'
    plt.savefig(savename);
    
def plot_dict_em(dd1,dd2,dd3,ax,parameter, multi):
    colors = cm.rainbow(np.linspace(0, 1, 3))
    c_it = int(0)
    ax.scatter([key for key in dd2], [dd2[key][parameter][0][-1]*multi for key in dd2], label='Lattice 1', color=colors[c_it]);
    c_it = c_it + 1;
    ax.scatter([key for key in dd3], [dd3[key][parameter][0][-1]*multi for key in dd3], label='Lattice 2', color=colors[c_it]);
    c_it = c_it + 1;  
    ax.scatter([key for key in dd1], [dd1[key][parameter][0][-1]*multi for key in dd1], label='Lattice og', color=colors[c_it]);
       
    
    