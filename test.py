# Contents of test.py
from myfunctions import *

# Definitions
Modes=[11,3,14,8] 			# Modes of interest, known from comparison to pyrazine 4-mode model paper
istate=1                                # Electronic state of interest
Nstate=2				# Total number of states
xyzfile='inputs/equilibrium.xyz'	# xyz file
AtomList,R0 = read_xyz(xyzfile)         # Read atom list and equilibrium geometry from xyz file
Time,v = read_gwpcentres(Nstate,istate) # Read list of time-steps (atomic units) and displacement factors
D=R0                    		# Starting geometry
j=1                     		# Arbitrarily selected example value; v[i][j] signifies the displacement factor of mode i and row index j, which repeats every Ng (total number of Gaussians) rows for Gaussian k with t=t+1 (+1 time-step)

# Displace coordinates according to displacement factors for N modes
for i in range(len(Modes)):     	# loop over modes
   Factor = v[i][j]			# Displacement factor in atomic units of length
   imode=Modes[i]			# Mode number
   D = displace_coords(D,imode,Factor)	# Displace coordinates by iteration

# Create output file
fname='displaced.xyz'			# output xyz file
write_xyz(AtomList,D,fname)     	# Write final displaced geometry to file

