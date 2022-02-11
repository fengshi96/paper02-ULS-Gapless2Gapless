#!/bin/bash -x
zero=0.0; pi=3.14159265


cd ..
for Hz in $(seq 0 0.05 0.00) #0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40 0.45 0.50 0.55 0.60 0.65 0.70 0.75 0.80 0.85 0.90 0.95 1.00 1.05 1.10 1.15 1.20 1.25 1.30 1.35 1.40 1.45 1.50
do
	cd Hz_$Hz	
	mkdir -p Observables
	cd Observables
	mydir=$(pwd)

rawjob="$(cat <<EOF
#!/bin/sh
#PBS -N Lyzzy-$Hz
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
../../Observables/SpinCurr_yzzy ../input.inp 
time
EOF
)"
echo "$rawjob" &> obs_yzzy.pbs

rawjob="$(cat <<EOF
#!/bin/sh
#PBS -N Lzyyz-$Hz
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
../../Observables/SpinCurr_zyyz ../input.inp 
time
EOF
)"
echo "$rawjob" &> obs_zyyz.pbs

rawjob="$(cat <<EOF
#!/bin/sh
#PBS -N Lzzyy-$Hz
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
../../Observables/SpinCurr_zzyy ../input.inp 
time
EOF
)"
echo "$rawjob" &> obs_zzyy.pbs

rawjob="$(cat <<EOF
#!/bin/sh
#PBS -N Lyyzz-$Hz
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
../../Observables/SpinCurr_yyzz ../input.inp 
time
EOF
)"
echo "$rawjob" &> obs_yyzz.pbs

rawjob="$(cat <<EOF
#!/bin/sh
#PBS -N Lxxxx-$Hz
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
../../Observables/SpinCurr_xxxx ../input.inp 
time
EOF
)"
echo "$rawjob" &> obs_xxxx.pbs

rawjob="$(cat <<EOF
#!/bin/sh
#PBS -N Lyyyy-$Hz
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
../../Observables/SpinCurr_yyyy ../input.inp 
time
EOF
)"
echo "$rawjob" &> obs_yyyy.pbs

rawjob="$(cat <<EOF
#!/bin/sh
#PBS -N Lzzzz-$Hz
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
../../Observables/SpinCurr_zzzz ../input.inp 
time
EOF
)"
echo "$rawjob" &> obs_zzzz.pbs

rawjob="$(cat <<EOF
#!/bin/sh
#PBS -N Lxyxy-$Hz
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
../../Observables/SpinCurr_xyxy ../input.inp 
time
EOF
)"
echo "$rawjob" &> obs_xyxy.pbs

rawjob="$(cat <<EOF
#!/bin/sh
#PBS -N Lxzxz-$Hz
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
../../Observables/SpinCurr_xzxz ../input.inp 
time
EOF
)"
echo "$rawjob" &> obs_xzxz.pbs

rawjob="$(cat <<EOF
#!/bin/sh
#PBS -N Lyxyx-$Hz
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
../../Observables/SpinCurr_yxyx ../input.inp 
time
EOF
)"
echo "$rawjob" &> obs_yxyx.pbs

rawjob="$(cat <<EOF
#!/bin/sh
#PBS -N Lyzyz-$Hz
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
../../Observables/SpinCurr_yzyz ../input.inp 
time
EOF
)"
echo "$rawjob" &> obs_yzyz.pbs

rawjob="$(cat <<EOF
#!/bin/sh
#PBS -N Lzxzx-$Hz
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
../../Observables/SpinCurr_zxzx ../input.inp 
time
EOF
)"
echo "$rawjob" &> obs_zxzx.pbs

rawjob="$(cat <<EOF
#!/bin/sh
#PBS -N Lzyzy-$Hz
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
../../Observables/SpinCurr_zyzy ../input.inp 
time
EOF
)"
echo "$rawjob" &> obs_zyzy.pbs

	# 2nd row
        qsub obs_yzzy.pbs
        qsub obs_zyyz.pbs
        qsub obs_zzyy.pbs
        qsub obs_yyzz.pbs
        
        #1st row
        qsub obs_xxxx.pbs
        qsub obs_yyyy.pbs
        qsub obs_zzzz.pbs
        
        qsub obs_xyxy.pbs
        qsub obs_xzxz.pbs
        
        qsub obs_yxyx.pbs
        qsub obs_yzyz.pbs
        
        qsub obs_zxzx.pbs
        qsub obs_zyzy.pbs
        
	
	echo "    ===== done with $Hz" 
	cd ../../
done




