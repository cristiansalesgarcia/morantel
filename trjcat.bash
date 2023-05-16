#!/bin/csh -f

set cnt    = #FIRST TRAJECTORY YOU ARE CONCATENATING, SHOWN AT THE STEPx_[HERE]
set cntmax = #THE TOTAL NUMBER OF COMPLETE RUNS YOU WANT TO CONCATENATE

echo "1" > instructions.dat
echo "0" >> instructions.dat


while ( ${cnt} <= ${cntmax} )
    set istep = step7_${cnt}
    set pstep = step7_noPBC_${cnt}
      gmx trjconv -s ${istep}.tpr -f ${istep}.trr -o ${pstep}.xtc -pbc mol -center<instructions.dat

    @ cnt += 1
end

rm instructions.dat

gmx trjcat -f<file_input.txt -settime<time_input.txt

rm file_input.txt time_input.txt
