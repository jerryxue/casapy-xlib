#!/bin/csh -f 
#   due to some issue with casapy,
#   one has to switch to csh and source this script
#   to keep all processes in the parent shell.

#set sdir=`pwd -L`  #   get the script path. 
                    #   This may be safer than <set currentdir="${cwd}">
#set pdir="$sdir:h" #   get the working directory path

set pdir="/Volumes/data3/ruixue1/reduc/21cm/"
set sdir="~/Dropbox/Worklib/casapy/scripts/sting-hi"
foreach source (    n0337 \ 
                    # n0772 
                    # n1156 n1569 n1637 \
                    # n2782 n2976 n3147 n3198 n3486 n3593 \
                    # n4151 n4254 n4273 n4536 n4605 \
                    # n4654 n5371 n5713 n6503 n6951 \
               )
    cd "${pdir}/${source}/"
    pwd
    `casapy --log2term -c ${sdir}/${source}hi.py`
end
