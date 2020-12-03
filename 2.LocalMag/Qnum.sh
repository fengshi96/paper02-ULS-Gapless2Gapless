#!/bin/bash -x
rm Sz.dat
cd ..
for Hz in $(seq 0.00 0.05 6.00)
do
	cd Hz_$Hz
	cd Observables
	cp ../../2.LocalMag/QuantNumbZ.py .
	python QuantNumbZ.py 64 $Hz
	echo "$Hz done"
cd ../..
done
