# CODE_displace_coords

## Description

Python function toolset for displacing coordinates along a normal mode.

## Functions

### read_xyz  

#####Description:
Reads xyz file 'fname'

#####Usage:
```python
read_xyz(fname)
```

#####Inputs:    
- fname, the file name of the xyz file to read

#####Outputs:   
- AtomList (string list), list of atomic labels;
 
- Coords (float list), coordinates as column vector with the format X1,Y1,Z1,X2,Y2,Z2,...

### write_xyz: Write xyz file 'fname' using atom list 'AtomList' and Cartesian coordinates 'Coords'
#####Usage:
```python
write_xyz(AtomList,Coords,fname)
```

#####Inputs:    
- AtomList (string list), list of atomic labels

- Coords (float list), coordinates as column vector with the format X1,Y1,Z1,X2,Y2,Z2,... 

- fname (str), output xyz file name
  
#####Outputs:   
- 'fname' (file), xyz file


### read_displacements: Reads displacement coordinates for mode 'imode' from 'normalmodes.txt'
#####Usage:
```python
read_displacements(Nat,imode)
```

#####Inputs:    
- Nat (int), total number of atoms

- imode (int), the displacements are taken from mode number 'imode'

#####Outputs:   
- D (float list), single column of displacement coordinates (length 3 x Nat)

### read_gwpcentres: Read displacement factors from file 'gwpcentres' for state 'istate'.
#####Usage:
```python
read_gwpcentres(Nstate,istate)
```

#####Inputs:    
- Nstate (int), the total number of states

- istate (int), the state to read

#####Outputs:   
- Time (float list), list of time in atomic units 

- v (float array), displacement factors array with columns 0,1,...,Nmode-1 pertaining to modes 1,2,...,Nmode, rows correspond to Ng Gaussians

### read_output: Read Gaussian weights (and state weights) from file 'output' for state 'istate'.
#####Usage:
```python
read_output(Nstate,Ng)
```

#####Inputs:    
- Nstate (int), total number of states

- Ng (int), total number of Gaussians

#####Outputs:   
- Time (float list), list of time in fs 

- Pop (float array), state populations with columns 0,1,...,Nstate-1 pertaining to states 1,2,...,Nstate

- gWeights (float array), Gaussian populations with columns 0,1,...,Ng-1 pertaining to Gaussians 1,2,...,Ng


### read_adc: Reads excitation energies and oscillator strengths from qchem XAS ADC calculation output.
#####Usage:
```python
read_adc(ADCoutput)
```

#####Inputs:    
- ADCoutput (str), ADC output file name

#####Outputs:   
- XAS (float array), XAS[0] = energies, XAS[1] = oscillator strengths


### read_src: Reads excitation energies and oscillator strengths from qchem XAS SRC calculation output.
#####Usage:
```python
read_adc(SRCoutput)
```

#####Inputs:    
- SRCoutput (str), SRC output file name

#####Outputs:   
- XAS (float array), XAS[0] = energies, XAS[1] = oscillator strengths


### displace_coords: Displace coords from xyz file 'xyzfile' along mode 'imode' (0<int<=Nmode) by 'Factor' (float)
#####Usage:
```python
displace_coords(Coords,imode,Factor)
```

#####Inputs:    
- Coords (float list), coordinates as column vector with the format X1,Y1,Z1,X2,Y2,Z2,...

- imode (int), the coordinates are displaced along mode number 'imode'

- Factor (float), the coordinates are displaced along mode number 'imode' by 'Factor' atomic units  

#####Outputs:   
- D (float list), displaced coordinates with same formatting as 'Coords'


### generate_spectrum: Generates spectrum with Lorentzian broadened lines (with FWHM=0.5 eV)
#####Usage:
```python
generate_spectrum(XAS)
```

#####Inputs:    
- XAS (float array), XAS[0] = energies, XAS[1] = oscillator strengths

#####Outputs:   
- x (float list), x-axis energies (eV)

- spect (float list), spectrum (arb. units) with Lorentzian broadened lines with FWHM=0.5 eV 


## Files:




