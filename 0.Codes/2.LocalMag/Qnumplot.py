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
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.patches import Arc
from subprocess import call
pi = 3.14159265



##### ----------------------
def main():
	#read y-axis--------------------
	filename="Sz.dat"
	file = open(filename,'r')
	linesS = file.readlines()
	file.close()
	

	#filename="Sz.dat"
	#file = open(filename,'r')
	#linesSz = file.readlines()
	#file.close()



	#read x-axis---------------------
	Lam = np.round(np.arange(0.0, 6.05, 0.05),2) 
	Nl = len(Lam)

	#process y-axis----------------------
	St = np.zeros(Nl); Sz = np.zeros(Nl)

	#for S_t, L_t, J_t------
	for i in range(0,Nl):
		tempS = linesS[0].split(" ")
		outS = float(tempS[i])
		St[i] = outS

	#for S_z, L_z, J_z------
	#for i in range(0,Nl):
	#	tempSz = linesSz[0].split(" ")
	#	outSz = float(tempSz[i])

	#	Sz[i] = outSz


	
	print(Lam); print(Sz) 
	#print(Lam); print(St); print(Lt); print(Jt)

	
	#----------------------------plot--------------------------


	plt.rc('font', family='serif')	
	fig = plt.figure(figsize=(9,5))  
	ax=fig.add_subplot(111)

	markersize=5
	plt.xlabel('$H_z$',fontsize=20)
	plt.xticks(fontsize=20)
	#plt.xticks([0.0,0.4,0.8,1.2])#,['0.0','0.4','0.8','1.2'])
	plt.yticks(fontsize=20)
	#plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0])
	#plt.ylim(ymin = 0,ymax = 1.0)
	plt.xlim(xmin = 0,xmax = 6)
	#titlelabel = " Spin_Total "
	#plt.title(titlelabel,fontsize=16, color='black')

	#plt.plot(Lam, Sz, 'o-', color='black', label=r'$M_S$',markersize=markersize)
	plt.plot(Lam, St, 'o-', color='magenta', label=r'$S_z$',markersize=markersize)

	#plt.axvline(x=0.34,color='black', linestyle='--')
	#plt.axvline(x=1.20,color='black', linestyle='--')

	"""plt.tick_params(
	    axis=u'y',          # changes apply to the y-axis
	    which='both',      # both major and minor ticks are affected
	    bottom='on',      # ticks along the bottom edge are off
	    top='on',         # ticks along the top edge are off
	    labelbottom='on', right='off', left='on', labelleft='on') # labels along the bottom edge are off

	plt.tick_params(
	    axis=u'x',          # changes apply to the x-axis
	    which='both',      # both major and minor ticks are affected
	    bottom='on',      # ticks along the bottom edge are off
	    top='off',         # ticks along the top edge are off
	    labelbottom='on', right='off', left='on', labelleft='on') # labels along the bottom edge are off"""

	plt.grid(which='major',linestyle='--',alpha=0.25)
	plt.tick_params(which=u'major',axis=u'both',length=6,color="black",direction='in')
	plt.tick_params(which=u'minor',axis=u'x',length=3,color="black",direction='in')
	plt.tick_params(which=u'minor',axis=u'y',length=3,color="black",direction='in')
	#plt.locator_params(nbins=4)
	minor_locator = tkr.AutoMinorLocator(4)
	ax.xaxis.set_minor_locator(minor_locator)
	minor_locator = tkr.AutoMinorLocator(2)
	ax.yaxis.set_minor_locator(minor_locator)
	plt.legend(loc='best',ncol=2, fontsize=20, frameon=False,columnspacing=1,handlelength=1.0,handletextpad=0.4)
	plt.savefig('Sz.pdf',bbox_inches='tight',dpi=300)
	plt.close()



#### ========================================================================================
#### ========================= Functions ====================================================
#### ========================================================================================
#### ========================================================================================
#### ========================= Functions ====================================================
#### ========================================================================================
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
##### ----------------------


if __name__ == '__main__':
	sys.argv ## get the input argument
	total = len(sys.argv)
	cmdargs = sys.argv	
	main()
































