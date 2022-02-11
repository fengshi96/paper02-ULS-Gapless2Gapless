#!/bin/bash -x
zero=0.0; pi=3.14159265
JJ=1.0;


for Hz in 1.00 1.10

do
mkdir Hz_$Hz
cd Hz_$Hz
	cp ../Midinput.inp .
        sed -e 's/LLLLLL/'$Hz'/g' \
            -e 's/JJJJJJ/'$JJ'/g' \
                <Midinput.inp  > input.inp
        rm Midinput.inp
mydir=$(pwd)
rawjob="$(cat <<EOF
#!/bin/sh
#PBS -N L-AKLT-Hz-$Hz
#PBS -l nodes=1:ppn=8 
#PBS -l walltime=64:00:00 
#PBS -l vmem=96gb			
#PBS -l mem=96gb
#PBS -m a				
#PBS -M feng.934@osu.edu	
#PBS -j oe			
#PBS -q batch
hostname
#PBS -r n
module load intel
module load mkl
cd \$PBS_O_WORKDIR
time
../dmrg2 input.inp &> runForinput.cout
time
EOF
)"

	echo "$rawjob" &> job.pbs
    
	qsub job.pbs


        echo -n "Hz = $Hz,    "

cd ..
done


