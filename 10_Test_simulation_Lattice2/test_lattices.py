#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:20:57 2020

@author: wvangoet
"""
import os
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from math import log10, floor
from BB_lib import *

def LorentzBeta(gamma):
    return np.sqrt( 1. - (1./gamma**2) )

def round_sig(x, sig=3):
    return round(x, sig-int(floor(log10(abs(x))))-1)

def print_some_lines(line_list, min_, max_):
    j = 0
    for i in line_list:
        if (j <= max_) and (j >= min_):
            print(i)
        j = j + 1
    return

print_all_lines = lambda x: sys.stdout.write("\n".join(x) + "\n")


def Read_PTC_Twiss_Return_Dict(filename, verbose=True):
    # Dictionary for output
    d = dict()
    d['HEADER_FILENAME'] = filename
    keywords = ''
    
    # First we open and count header lines
    fin0=open(filename,'r').readlines()
    headerlines = 0
    for l in fin0:
        # Store each header line
        headerlines = headerlines + 1
        # Stop if we find the line starting '* NAME'
        if '* NAME' in l:
            keywords = l
            break
        # Store the headers as d['HEADER_<name>'] = <value>
        else:
            #try:
            #    d[str('HEADER_'+l.split()[1])]=[float(l.split()[-1])]     
            #except ValueError:
            #    d[str('HEADER_'+l.split()[1])]=[str(l.split()[-1])]   
            if '"' in l:
                d[str('HEADER_'+l.split()[1])]=[str(l.split('"')[1])]
            else:
                d[str('HEADER_'+l.split()[1])]=[float(l.split()[-1])]                 
    headerlines = headerlines + 1    
    
    if verbose: print('\nRead_PTC_Twiss_Return_Dict found Keywords: \n',keywords)
    
    # Make a list of column keywords to return (as an aid to iterating)
    dict_keys = []
    for key in keywords.split():
        dict_keys.append(key)
    dict_keys.remove('*')
    
    if verbose: print('\nRead_PTC_Twiss_Return_Dict Dict Keys: \n',dict_keys)
    
    # Initialise empty dictionary entries for column keywords 
    for key in dict_keys:
        d[key]=[]
        
    if verbose: print('\nRead_PTC_Twiss_Return_Dict header only dictionary \n', d)
    
    # Strip header
    fin1=open(filename,'r').readlines()[headerlines:]   
    
    # Populate the dictionary line by line
    for l in fin1:
        i = -1        
        for value in l.split():
            i = i+1
            if 'NAME' in dict_keys[i]:
                d[dict_keys[i]].append(str(value))
            else:
                d[dict_keys[i]].append(float(value))    
                
    # Return list of column keywords 'dict_keys', and dictionary 'd'
    return dict_keys, d

d_keys, d1 = Read_PTC_Twiss_Return_Dict('0_H_07/optimised_flat_file.tfs', verbose=True)
d_keys, d2 = Read_PTC_Twiss_Return_Dict('0_V_10/optimised_flat_file.tfs', verbose=True)
d_keys, d3 = Read_PTC_Twiss_Return_Dict('1_H_07/optimised_flat_file.tfs', verbose=True)
d_keys, d4 = Read_PTC_Twiss_Return_Dict('1_V_10/optimised_flat_file.tfs', verbose=True)

#%%

# + 13,14,25,26,63
# - 55 72 95 99 00

d_keys, d1 = Read_PTC_Twiss_Return_Dict('optimised_flat_file.tfs', verbose=True)

ssz = get_positions_of_quads() 
#s_operational = np.asarray([5,6,9,10,13,14,17,18,21,22,25,26,27,28,31,32,35,36,39,40,45,46,49,50,56,59,60,63,67,68,71,77,78,81,82,85,86,89,90,96])-1
s_operational = np.asarray([5,6,9,10,17,18,21,22,27,28,31,32,35,36,39,40,45,46,49,50,55,56,59,60,67,68,71,72,77,78,81,82,85,86,89,90,95,96,99,100])-1
int_steps = 13

madx,posz = place_quads_wmarkers(int_steps,s_operational,range(100),ssz)

madx.call(file='locations.str')
madx.input('''
seqedit,sequence = PS;
	select, flag=seqedit, pattern= PR.QFN55;
	select, flag=seqedit, pattern= PR.QDN72;
	select, flag=seqedit, pattern= PR.QFN95;
	select, flag=seqedit, pattern= PR.QFN99;
	select, flag=seqedit, pattern= PR.QDN00;
	remove, element=SELECTED;
endedit;


seqedit,sequence = PS;
	PR.QFN13: MULTIPOLE, KNL:={0,kf};
	PR.QDN14: MULTIPOLE, KNL:={0,kd};
	PR.QFN25: MULTIPOLE, KNL:={0,kf};
	PR.QDN26: MULTIPOLE, KNL:={0,kd};
	PR.QFN63: MULTIPOLE, KNL:={0,kf};

	install, element=PR.QFN13,  at=Pos_LeQ13;
	install, element=PR.QDN14,  at=Pos_LeQ14;
	install, element=PR.QFN25,  at=Pos_LeQ25;
	install, element=PR.QDN26,  at=Pos_LeQ26;
	install, element=PR.QFN63,  at=Pos_LeQ63;
endedit;
''')

madx.input('''
seqedit, sequence=PS;
	flatten;
	cycle , start=PR.BWSH65;
	flatten;
endedit;

use, sequence=PS;
''')
madx.input('twiss;')
quick_match(madx,'21','24')
print(madx.table.summ.q1,madx.table.summ.q2)
plt.plot(madx.table.twiss.s,madx.table.twiss.dx,'r', d1['S'],d1['DISP1'],'b')
plt.legend(['self-made','flat file'])
plt.show()