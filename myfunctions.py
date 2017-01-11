def read_equilibrium_xyz():
   ##################################################
   f = open('equilibrium.xyz','r') # open file
   au2ang = 0.529177249
   ##################################################
   # Read equilibrium coordinates
   # as column vector in AU, with the format X1,Y1,Z1,X2,Y2,Z2,...
   lines=f.readlines()
   R0=[]
   AtomList=[]
   c=0
   for x in lines:
       c=c+1
       if c>2:
          AtomList.append(x.split()[0]) 	# List of atomic labels
          for i in range(1,4):
             R0.append(float(x.split()[i])/au2ang)
   f.close()
   ##################################################
   return AtomList,R0


def read_normalmodes(Nat,imode):
   ##################################################
   # Definitions
   N = 3*Nat  # Number of coordinates
   ##################################################
   # Error checks
   if Nat==2:
      Nmode=2
   elif Nat>2:
      Nmode=N-6
   else:
      print "ERROR: Something wrong with number of atoms"
      print "Are there <2 atoms?"
      return
   
   if imode>=1 and imode<=Nmode:
      print "Reading displacements for mode " + str(imode)
   else:
      print 'ERROR: imode out of range (1,Nmode).'
      return
   ##################################################   
   # Read normal mode displacements (from 'normalmodes.txt' file)
   f = open('normalmodes.txt','r')
   lines=f.readlines()
   ##################################################
   # Known pattern of g09 frequencies output file...
   row = int((imode-1)/5)
   a = (row+1)*7 + row*N
   b = (row+1)*(7 + N)
   d = row*5
   ##################################################
   # Append displacements to column vector 'displacements'
   c=0
   Displacements=[]
   for x in lines:
       c=c+1
       if c>a and c<=b:
             Displacements.append(float(x.split()[imode+2-d]))
   f.close()
   ##################################################
   return Displacements


def displace_coords(imode,Factor):
   ##################################################
   # Displace equilibrium coords (R0) along mode 'imode' (0<int<=Nmode) by 'factor' (float)
   au2ang = 0.529177249
   AtomList,R0=read_equilibrium_xyz()	# Read AtomList (vector of length Nat) and R0 (vector of length 3*Nat)
   Nat=len(AtomList)			# Number of atoms 
   Displc=read_normalmodes(Nat,imode)	# Read normal mode displacement (vector of length 3*Nat)
   
   f=open('displaced_coords.xyz','w')
   f.write(str(Nat)+'\n')
   f.write('Displaced Coordinates\n')

   for i in range(0,3*Nat):
      if i%3==0:
         Atom=AtomList[i/3]
         x=(R0[i] + Factor*Displc[i])*au2ang 	# Coordinates displaced along normal mode by 'factor'
      elif (i-1)%3==0:
         y=(R0[i] + Factor*Displc[i])*au2ang
      elif (i-2)%3==0:
         z=(R0[i] + Factor*Displc[i])*au2ang	
         f.write( Atom + '  ' + str(x) + '  ' + str(y) + '  ' + str(z) + '\n')

   f.close()
   ################################################## 
   return


def read_gwpcentres(Nstate,istate):
   ##################################################
   # Read displacement factors from file 'gwpcentres'3
   # At the moment hard-coded 4-modes, so can only be used when there are exactly 4 modes..
   f=open('gwpcentres','r')
   lines=f.readlines()
   Time=[]; v1=[]; v2=[]; v3=[]; v4=[];
   c=0
   for x in lines:
       c=c+1
       if c>1:
          if (c-2)%(2*Nstate+1)==0:
             Time.append(float(x.split()[1]))         # List of time in AU
          elif (c+3-2*istate)%(2*Nstate+1)==0:	       # This obtains state 1 values, can generalise for state 'istate'
             v1.append(float(x.split()[0]))
             v2.append(float(x.split()[1]))
             v3.append(float(x.split()[2]))
             v4.append(float(x.split()[3]))
   f.close()
   return Time,v1,v2,v3,v4 


