from myfunctions import *

Nstate=2 # Number of states: 2 state model
# Modes=[11,3,14,8] # Known from comparison to pyrazine 4-mode model paper 
Modes=[11,3,14]     # TEST line! Can delete later
xyzfile='equilibrium.xyz'

# TEST
imode=11
Factor=2.0
istate=2
imode=1
Time,v = read_gwpcentres(Nstate,istate)
displace_coords(xyzfile,imode,Factor)

# v[column][row]
print v[0][0]
print v[2][11]

#for istate in range(1,Nstate):		# Loop over states
"""
istate=1
Time,v1,v2,v3,v4 = read_gwpcentres(Nstate,istate)
for t in range(1,len(Time)): 	# Loop over timesteps
   c=0
   for imode in Modes:		# Loop over modes
      c=c+1
      if c==1:
         displace_coords(xyzfile,imode,v1[t])
      elif c==2:
         displace_coords(xyzfile,imode,v2[t])
      elif c==3:
         displace_coords(xyzfile,imode,v3[t])
      elif c==4:
         displace_coords(xyzfile,imode,v4[t])
"""
