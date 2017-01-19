from myfunctions import *

# Definitions
Modes=[1,2,3,4]                         # Modes of interest
istate=1                                # Electronic state of interest
Nstate=2				# Total number of states
xyzfile='inputs/equilibrium.xyz'
AtomList,R0 = read_xyz(xyzfile)         # Read atom list and equilibrium geometry
Time,v = read_gwpcentres(Nstate,istate) # Read list of time-steps (atomic units) and displacement factors
D=R0                    # Starting geometry
j=1                     # Arbitrarily selected value for example, v[i][j] really means the displacement factor of mode i and row index j repeats every Ng rows for Gaussian k and t=t+1

# Displace coordinates according to displacement factors for N modes
for i in range(len(Modes)):     # loop over modes
   Factor = v[i][j]
   imode=Modes[i]
   D = displace_coords(D,imode,Factor)

# Create output file
fname='displaced.xyz'
write_xyz(AtomList,D,fname)     # Write final displaced geometry to file

