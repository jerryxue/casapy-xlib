#!/bin/csh -f 
#   due to some issue with casapy,
#   one has to switch to csh and source this script
#   to keep all processes in the parent shell.

#set sdir=`pwd -L`  #   get the script path. 
                    #   This may be safer than <set currentdir="${cwd}">
#set pdir="$sdir:h" #   get the working directory path

#foreach source (    n0337 n0772 n1156 n1569 n1637 n2681 \
#                    n2782 n2976 n3147 n3198 n3486 n3593 \
#                    n3949 n4151 n4254 n4273 n4536 n4605 \
#                    n4654 n5371 n5713 n6503 n6951 )

set pdir="/Volumes/Scratch/reduc/sting-co"
set sdir="/Users/Rui/Dropbox/Worklib/casapy/scripts/sting-13co"
# foreach source (    n0337 n0772 n1569 \
#                     n1637 n2782 n3147 n3198 n3486 n3593 \
#                     n3949 n4254 n4273 n4536 n4654 \
#                     n5371 n5713 n6951 )
#     rm -rf "${pdir}/msc13/${source}"
#     mkdir "${pdir}/msc13/${source}"
#     cd "${pdir}/msc13/${source}"
#     pwd
#     `casapy --log2term -c ${sdir}/${source}co13.inp`
# end


foreach source ( n0772 n3593 n3949 n5713 n1156 n2976 n2681 n4151 )
    rm -rf "${pdir}/msc13/${source}"
    mkdir "${pdir}/msc13/${source}"
    cd "${pdir}/msc13/${source}"
    pwd
    `casapy --log2term -c ${sdir}/${source}co13.inp`
end
