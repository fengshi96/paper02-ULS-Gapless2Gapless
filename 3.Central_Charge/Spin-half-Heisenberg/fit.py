import sys, re, math, random		## for passing an argument and list of variables ## regexes, math functions, random numbers
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import scipy.interpolate
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.ticker as tkr
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from subprocess import call
from collections import Counter
import subprocess
pi = 3.14159265


N = 0 # global #site
##### ----------------------
def main(total, cmdargs):
	if total != 2:
			print (" ".join(str(x) for x in cmdargs))
			raise ValueError('missing arguments')
	global N
	N += int(cmdargs[1])

	### -------- EE -------------------

	filename="EntHeisenberg.dat"	


	file = open(filename,'r')
	lines = file.readlines()
	file.close()

	ll = np.zeros(len(lines)-1)  # -1 for the empty line at the end
	ES = np.zeros(len(lines)-1)
	
	for i in range(len(lines)-1):
		line = lines[i].strip("\n").split()
		ll[i] = int(line[0])
		ES[i] = float(line[1])	
	print(ll)
	print(ES)
	
	#cut = 5
	start = 10; end = 190
	#a, b = fitting(ll, ES, start, end)
	popt, pcov = curve_fit(func, ll[start:end], ES[start:end])
	x = np.linspace(1.0,N,num=400)
	print(x)
	print(popt*6)
        #print fittings
	fit = np.array(( [x[int(start/N*400):int(end/N*400)], func(x[int(start/N*400):int(end/N*400)], popt[0], popt[1], popt[2]) ])).T
	printfArray(fit, "fit.dat")	

	#===========================
	fig = plt.figure(figsize=(5, 4))
	gs = gridspec.GridSpec(2, 1)
	gs.update(left=0.12, right=0.75, top=0.97, bottom=0.08, wspace=0.0, hspace=0.35)
	ax = plt.subplot(111)

	# ax.scatter(KzRange[i], ES_all[i][j,0]-ES_all[i][0,0], marker='_', color='red')
	ax.scatter(ll, ES, marker='o', s=6, color='red')
	ax.plot(x[int(start/N*400):int(end/N*400)], func(x[int(start/N*400):int(end/N*400)], popt[0], popt[1], popt[2]), '-', color='teal')


	plt.grid(which='major',linestyle='--',alpha=0.35)
	#plt.xscale('log')
	#plt.yscale('log')
	#plt.ylim(ymin=1.0, ymax=1.8)
	plt.xticks(fontsize=16)
	plt.yticks(fontsize=16)
	plt.xlabel(r"$n$", fontsize=18)
	plt.ylabel(r"$S(n)$", fontsize=18)	
	plt.savefig('EE.pdf', bbox_inches='tight', dpi=300)
	












#### ========================================================================================
#### ========================= Functions ====================================================
#### ========================================================================================
#### ========================================================================================
#### ========================= Functions ====================================================
#### ========================================================================================
def func(x, a, b, c):
    return a * np.log(2 * N * np.sin(pi * x / N) / pi ) + b * (np.cos(2 * pi * x / 2))/ (np.abs( N  * np.sin(pi * x / N)) ** (2.0/3.0)) + c
    
def fitting(x, y, start, end):
	lin_y = y[start:end]
	lin_x = np.log(2 * N * np.sin(pi * x[start:end] / N) / pi )
	
	X = np.array(( [[lin_x[i], 1] for i in range(len(lin_x)) ] ))
	Y = np.array( lin_y )
	#Y = np.array( lin_y ) - 0.20 * (np.cos(2 * pi * x[start:end] / N))/np.abs(N * np.sin(pi * x[start:end] / N)) ** 0.5
	a,b = np.linalg.lstsq(X,Y,rcond=None)[0]
	return a, b
	
def read_density(NumberOfSites,str,matchstring):
	file = open(str,'r')
	lines = file.readlines()
	file.close()
	for i in range(0,len(lines)):
			line = lines[i]
			if re.search(matchstring, line, re.I):
				matchindex=i+1
				break
	try:
		matchindex
	except NameError:
		print ("***match string", matchstring)
		print ('***MYERROR:matchindex in read_density function is not defined - no match found')
	rows = NumberOfSites
	cols = 2
	m = [[0.0 for x in range(cols)] for y in range(rows)] ## allocate m list
	for i in range(0,rows):
		line = lines[matchindex+1+i];
		temp = line.split(" ")
		val = ConvertImag(temp[1])
		m[i][0] = val.real;
		m[i][1] = val.imag;  	### defined 2D Matrix
	return np.asarray(m);
	
def printfArray(A, filename, transpose = False):
    file = open(filename, "w")
    try:
        col = A.shape[1]
    except IndexError:
        A = A.reshape(-1, 1) 
    
    row = A.shape[0]
    col = A.shape[1]

    if transpose == False:
        for i in range(row):
            for j in range(col - 1):
                file.write(str(A[i, j]) + " ")
            file.write(str(A[i, col - 1]))  # to avoid whitespace at the end of line
            file.write("\n")
    elif transpose == True:
        for i in range(col):
            for j in range(row - 1):
                file.write(str(A[j, i]) + " ")
            file.write(str(A[row - 1, i]))
            file.write("\n")
    else:
        raise ValueError("3rd input must be Bool")
    file.close()
##### ----------------------
def split(mat):
	orb=2
	nrows = mat.shape[0];
	ncols = mat.shape[1]; ##if mat else 0
	mat = np.asarray(mat)
	assert(nrows==ncols)
	fatrows=int(nrows/orb);
	fatcols=int(ncols/orb);

	AA = np.zeros((fatrows,fatcols));
	BB = np.zeros((fatrows,fatcols));
	AB = np.zeros((fatrows,fatcols));

	for i in range(0,fatrows):
		ia = i*orb+0
		ib = i*orb+1
		for j in range(0,fatcols):
			ja = j*orb+0
			jb = j*orb+1
	
			AA[i,j] = mat[ia,ja]
			BB[i,j] = mat[ib,jb]
			AB[i,j] = mat[ia,jb]

	return AA, BB, AB

##### ----------------------
def ConvertImag(s):
	repart = float(s.split(",")[0].split("(")[1])
	impart = float(s.split(",")[1].split(")")[0])
	return complex(repart,impart)

##### ----------------------
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

##### ----------------------
def readMatrix(str):
	file = open(str,'r')
	lines = file.readlines()
	file.close()

	Type = lines[0].split(" ")[2]
	Type = ConvertImag(Type);
	rows = int(Type.real)
	cols = int(Type.imag)

	counter = 0
	m = np.zeros((rows,cols)) ### [[0.0 for x in range(rows)] for y in range (cols)]
	for i in range(1,rows+1):
		line = lines[i];
		temp = line.split(" ")
		for j in range(0,cols):
			#m[j+i*cols] = float(temp[j])  ### defined 1D aray
			val = ConvertImag(temp[j]);
			m[i-1,j] = val.real	   ### defined 2D Matrix
		counter = counter + 1
	file.close()

	for i in range(0,rows):
		for j in range(i,cols):
			m[j,i] = m[i,j]	   ### defined 2D Matrix
			if(i==j): 
				m[i,j] = 2.0;
	return m; 
##### ----------------------

	
def PrintMatrix(m):
	string="""
DegreesOfFreedom=1
GeometryKind=LongRange
GeometryOptions=none
Connectors"""
	
	num_rows = len(m);
	num_cols = m.shape[1] #len(m[0]) if m else 0
	string += " "+str(num_rows)+" "+str(num_cols)
	print (string )
	for i in range(0,num_rows):
		print (" ".join(str(x) for x in m[i]))


def grepfilenum(keyword, filedir):
		List = []
		ls = subprocess.Popen(["ls", filedir], stdout=subprocess.PIPE)
		grep = subprocess.Popen(["grep", keyword],stdin=ls.stdout, stdout=subprocess.PIPE)
		endOfPipe = grep.stdout
		for line in endOfPipe:
	    		List.append(str(line).strip("b'n\$"))
		List.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))
		res = [float(sub.split('_')[1]) for sub in List] 
		return res
##### ----------------------


if __name__ == '__main__':
	sys.argv ## get the input argument
	total = len(sys.argv)
	cmdargs = sys.argv	
	main(total, cmdargs)
































