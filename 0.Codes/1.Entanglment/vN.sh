#!/bin/bash -x
rm vN.dat
for Hz in $(seq 0.00 0.05 6.00)

do
  	python vN_Ent.py 64 $Hz 
	echo "Hz_$Hz submitted"
done
wait
python vN_plot.py


