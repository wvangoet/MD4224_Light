#!/bin/bash

# Pickle and output files
rm -r output
rm -r bunch_output
rm -r lost
rm -r input

rm PS.seq
rm ptc_twiss
rm *.tfs
rm PTC-PyORBIT_flat_file.flt
rm tunespread.dat
rm madx.ps
rm PS_Lattice/tunes.str

. clean_junk.sh
