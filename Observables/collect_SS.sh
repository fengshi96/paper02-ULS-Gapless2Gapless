#!/bin/bash -x
zero=0.0; pi=3.14159265


cd ..
for Hz in 1.00 1.10 #$(seq 0.00 0.05 4.10) #0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40 0.45 0.50 0.55 0.60 0.65 0.70 0.75 0.80 0.85 0.90 0.95 1.00 1.05 1.10 1.15 1.20 1.25 1.30 1.35 1.40 1.45 1.50
do
	cd Hz_$Hz	
	mkdir -p Observables
	cd Observables
	mydir=$(pwd)

rawjob="$(cat <<EOF
#!/bin/sh
#PBS -N L-$Hz
#PBS -l nodes=1:ppn=8
#PBS -l walltime=48:00:00
#PBS -l vmem=64gb
#PBS -l mem=64gb
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
../../Observables/SpinCurr_xx ../input.inp 
time
EOF
)"
echo "$rawjob" &> obs_xx.pbs



rawjob="$(cat <<EOF
#!/bin/sh
#PBS -N L-$Hz
#PBS -l nodes=1:ppn=8
#PBS -l walltime=48:00:00
#PBS -l vmem=64gb
#PBS -l mem=64gb
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
../../Observables/SpinCurr_yy ../input.inp
time
EOF
)"
echo "$rawjob" &> obs_yy.pbs



rawjob="$(cat <<EOF
#!/bin/sh
#PBS -N L-$Hz
#PBS -l nodes=1:ppn=8
#PBS -l walltime=48:00:00
#PBS -l vmem=64gb
#PBS -l mem=64gb
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
../../Observables/SpinCurr_zz ../input.inp
time
EOF
)"
echo "$rawjob" &> obs_zz.pbs


        qsub obs_xx.pbs
	qsub obs_yy.pbs
	qsub obs_zz.pbs
	
	echo "    ===== done with $Hz" 
	cd ../../
done




