# CODE_displace_coords

## Description

Python function toolset for displacing coordinates along a normal mode.

## Example Usage

```python
# Contents of test.py
from myfunctions import *

# Definitions
Modes=[1,2,3,4]                         # Modes of interest
istate=1                                # Electronic state of interest
Nstate=2                                # Total number of states
xyzfile='inputs/equilibrium.xyz'
AtomList,R0 = read_xyz(xyzfile)         # Read atom list and equilibrium geometry
Time,v = read_gwpcentres(Nstate,istate) # Read list of time-steps (atomic units) and displacement factors
D=R0                                    # Starting geometry
j=1                                     # Arbitrarily selected example value; v[i][j] signifies the displacement factor of mode i and row index j, which repeats every Ng (total number of Gaussians) rows for Gaussian k with t=t+1 (+1 time-step)

# Displace coordinates according to displacement factors for N modes
for i in range(len(Modes)):             # loop over modes
   Factor = v[i][j]
   imode=Modes[i]
   D = displace_coords(D,imode,Factor)  # Displace coordinates by iteration

# Create output file
fname='displaced.xyz'
write_xyz(AtomList,D,fname)             # Write final displaced geometry to file

```

## Functions

### read_xyz  

#####Description
Reads xyz file 'fname'

#####Usage
```python
read_xyz(fname)
```

#####Inputs    
- fname, the file name of the xyz file to read

#####Outputs   
- AtomList (string list), list of atomic labels;
 
- Coords (float list), coordinates as column vector with the format X1,Y1,Z1,X2,Y2,Z2,...

### write_xyz 

#####Description
Write xyz file 'fname' using atom list 'AtomList' and Cartesian coordinates 'Coords'

#####Usage
```python
write_xyz(AtomList,Coords,fname)
```

#####Inputs    
- AtomList (string list), list of atomic labels

- Coords (float list), coordinates as column vector with the format X1,Y1,Z1,X2,Y2,Z2,... 

- fname (str), output xyz file name
  
#####Outputs   
- 'fname' (file), xyz file


### read_displacements 

#####Description
Reads displacement coordinates for mode 'imode' from 'normalmodes.txt'

#####Usage
```python
read_displacements(Nat,imode)
```

#####Inputs    
- Nat (int), total number of atoms

- imode (int), the displacements are taken from mode number 'imode'

#####Outputs   
- D (float list), single column of displacement coordinates (length 3 x Nat)

### read_gwpcentres 

#####Description
Read displacement factors from file 'gwpcentres' for state 'istate'.

#####Usage
```python
read_gwpcentres(Nstate,istate)
```

#####Inputs    
- Nstate (int), the total number of states

- istate (int), the state to read

#####Outputs   
- Time (float list), list of time in atomic units 

- v (float array), displacement factors array with columns 0,1,...,Nmode-1 pertaining to modes 1,2,...,Nmode, rows correspond to Ng Gaussians

### read_output 

#####Description
Read Gaussian weights (and state weights) from file 'output' for state 'istate'.

#####Usage
```python
read_output(Nstate,Ng)
```

#####Inputs    
- Nstate (int), total number of states

- Ng (int), total number of Gaussians

#####Outputs   
- Time (float list), list of time in fs 

- Pop (float array), state populations with columns 0,1,...,Nstate-1 pertaining to states 1,2,...,Nstate

- gWeights (float array), Gaussian populations with columns 0,1,...,Ng-1 pertaining to Gaussians 1,2,...,Ng


### read_adc

#####Description
Reads excitation energies and oscillator strengths from qchem XAS ADC calculation output.

#####Usage
```python
read_adc(ADCoutput)
```

#####Inputs    
- ADCoutput (str), ADC output file name

#####Outputs   
- XAS (float array), XAS[0] = energies, XAS[1] = oscillator strengths


### read_src 

#####Description
Reads excitation energies and oscillator strengths from qchem XAS SRC calculation output.

#####Usage
```python
read_adc(SRCoutput)
```

#####Inputs    
- SRCoutput (str), SRC output file name

#####Outputs   
- XAS (float array), XAS[0] = energies, XAS[1] = oscillator strengths


### displace_coords 

#####Description
Displace coords from xyz file 'xyzfile' along mode 'imode' `(0<int<=Nmode)` by 'Factor' (float)

#####Usage
```python
displace_coords(Coords,imode,Factor)
```

#####Inputs    
- Coords (float list), coordinates as column vector with the format X1,Y1,Z1,X2,Y2,Z2,...

- imode (int), the coordinates are displaced along mode number 'imode'

- Factor (float), the coordinates are displaced along mode number 'imode' by 'Factor' atomic units  

#####Outputs   
- D (float list), displaced coordinates with same formatting as 'Coords'


### generate_spectrum 

#####Description
Generates spectrum with Lorentzian broadened lines (with FWHM=0.5 eV)

#####Usage
```python
generate_spectrum(XAS)
```

#####Inputs    
- XAS (float array), XAS[0] = energies, XAS[1] = oscillator strengths

#####Outputs   
- x (float list), x-axis energies (eV)

- spect (float list), spectrum (arb. units) with Lorentzian broadened lines with FWHM=0.5 eV 


## Files




