from myfunctions import *

Nstate=2 # Number of states: 2 state model
Modes=[11,3,14,8] # Known from comparison to pyrazine 4-mode model paper 
xyzfile='equilibrium.xyz'






# TEST for 1 time-step, state=1, and Ng=1
####################################################
istate=1
AtomList,R0 = read_xyz(xyzfile)
Time,v = read_gwpcentres(Nstate,istate)

D=R0
for i in range(len(Modes)):
   # v[column][row] = v[mode index][Gaussian index]
   Factor = v[i][20]
   imode=Modes[i]   
   D = displace_coords(D,imode,Factor)

fname='TEST.xyz'
write_xyz(AtomList,D,fname)
####################################################





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
