#!/bin/csh -f 
#   due to some issue with casapy,
#   one has to switch to csh and source this script
#   to keep all processes in the parent shell.

#set sdir=`pwd -L`  #   get the script path. 
                    #   This may be safer than <set currentdir="${cwd}">
#set pdir="$sdir:h" #   get the working directory path



set pdir="/Volumes/Scratch/reduc/co10/msc"
set sdir="/Users/Rui/Dropbox/Worklib/casapy/scripts/sting-co"
foreach source (    n0337 n0772 n1156 n1569 n1637 \
                    n2782 n2976 n3147 n3198 n3486 n3593 \
                    n4151 n4254 n4536 n4605 \
                    n4654 n5371 n5713 n6951 )
    cd "${pdir}/msc/${source}/comb/"
    pwd
    `casapy --log2term -c ${sdir}/${source}_comb.py`
end
