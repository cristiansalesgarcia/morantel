!/bin/csh -f

set cnt = 1
set cntmax = #NUMBER OF RUNS

echo "1" > instructions.dat
echo "0" >> instructions.dat

while ( ${cnt} <= ${cntmax} )
	set istep = step7_${cnt}
	set pstep = step7_noPBC_${cnt}
		gmx trjconv -s ${istep}.tpr -f ${istep}.trr -o ${pstep}.xtc -pbc mol -center<instructions.dat
	@ cnt += 1
end

rm instructions.dat	