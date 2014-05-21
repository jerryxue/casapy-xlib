#!/bin/csh -f 
#   due to some issue with casapy,
#   one has to switch to csh and source this script
#   to keep all processes in the parent shell.

#set sdir=`pwd -L`  #   get the script path. 
                    #   This may be safer than <set currentdir="${cwd}">
#set pdir="$sdir:h" #   get the working directory path

set pdir="/Volumes/Scratch/reduc/co10"
set sdir="/Users/Rui/Dropbox/Worklib/casapy/scripts/sting-co"
foreach source (    0337 0772 1156 1569 1637 \
                    2681 2782 2976 3147 3198 \
                    3486 3593 3949 4151 4254 \
                    4273 4536 4605 4654 5371 \
                    5713 6503 6951 )
    cd "${pdir}/msc/n${source}/"
    pwd
    rm -rf *
    `casapy --log2term -c ${sdir}/n${source}co.py`
end
