# CODE_displace_coords

## Description

Calculate X-ray absorption spectra from a quantum dynamics trajectory.  

## Example Usage

Extract from gwpcentres file:

```
 #            4          10
 time:   0.0000000000000000
 state:           1
   0.000000000       0.000000000       0.000000000       0.000000000
  0.9352661232       0.000000000       0.000000000       0.000000000
   0.000000000      0.9352661232       0.000000000       0.000000000
   0.000000000       0.000000000      0.9352661232       0.000000000
   0.000000000       0.000000000       0.000000000      0.9352661232
 -0.9352661232       0.000000000       0.000000000       0.000000000
   0.000000000     -0.9352661232       0.000000000       0.000000000
   0.000000000       0.000000000     -0.9352661232       0.000000000
   0.000000000       0.000000000       0.000000000     -0.9352661232
  0.9352661232      0.9352661232       0.000000000       0.000000000
 state:           2
   0.000000000       0.000000000       0.000000000       0.000000000
  0.9352661232       0.000000000       0.000000000       0.000000000
   0.000000000      0.9352661232       0.000000000       0.000000000
   0.000000000       0.000000000      0.9352661232       0.000000000
   0.000000000       0.000000000       0.000000000      0.9352661232
 -0.9352661232       0.000000000       0.000000000       0.000000000
   0.000000000     -0.9352661232       0.000000000       0.000000000
   0.000000000       0.000000000     -0.9352661232       0.000000000
   0.000000000       0.000000000       0.000000000     -0.9352661232
  0.9352661232      0.9352661232       0.000000000       0.000000000
 time:   41.341373336559997
 state:           1
 -0.6883521395E-02  0.8224127040E-02 -0.2870900380E-01   0.000000000
  0.9109454151      0.8224127040E-02 -0.2870900380E-01   0.000000000
 -0.6883521395E-02  0.9375857968     -0.2870900380E-01   0.000000000
 -0.6883521395E-02  0.8224127040E-02  0.8801445246       0.000000000
 -0.4705419099E-01 -0.3958130750E-01  0.2568199602E-02  0.2386044828
 -0.9247124579      0.8224127040E-02 -0.2870900380E-01   0.000000000
 -0.6883521395E-02 -0.9211375427     -0.2870900380E-01   0.000000000
 -0.6883521395E-02  0.8224127040E-02 -0.9375625322       0.000000000
 -0.4705419099E-01 -0.3958130750E-01  0.2568199602E-02 -0.2386044828
  0.9109454151      0.9375857968     -0.2870900380E-01   0.000000000
 state:           2
 -0.3541889254E-01 -0.1917443803E-01 -0.4932732269E-02 -0.1062194758E-11
  0.8883616066     -0.1018631503E-01 -0.8717163010E-02   0.000000000
 -0.2946732988E-01  0.9191753547     -0.8717163010E-02   0.000000000
 -0.2946732988E-01 -0.1018631503E-01  0.9001363654       0.000000000
 -0.4749912624E-01 -0.3986490517E-01  0.2098486366E-02  0.6305138940
 -0.9472962664     -0.1018631503E-01 -0.8717163010E-02   0.000000000
 -0.2946732988E-01 -0.9395479848     -0.8717163010E-02   0.000000000
 -0.2946732988E-01 -0.1018631503E-01 -0.9175706914       0.000000000
 -0.4749912624E-01 -0.3986490518E-01  0.2098486370E-02 -0.6305138940
  0.8883616066      0.9191753547     -0.8717163010E-02   0.000000000

```

Extract from output file:

```
 Time  =       0.00 fs,       CPU =       0.05 s,    Norm    = 1.00000000
 E-tot =   0.687531 ev,    E-corr =   0.000000 ev,   Delta-E =     0.0000 mev

 state = 1  pop.: 0.00000000   E-corr:  -0.000000 ev,   E-tot =  -0.000000 ev
 state = 2  pop.: 1.00000000   E-corr:   0.000000 ev,   E-tot =   0.687531 ev

 Diagonal Densities *1000,  state = 1
v1        C  4:   0.0000   0.0000   0.0000   0.0000   0.0000   0.0000   0.0000
     8 - 10>    0.0000   0.0000   0.0000

 Gross Gaussian Populations *10 (weighted),  state = 1
v1      ReC 4:   0.0000   0.0000   0.0000   0.0000   0.0000   0.0000   0.0000
     8 - 10>    0.0000   0.0000   0.0000

 Mode expectation values and variances,  state = 1
v1          : <q>=   0.0000  <dq>=   0.0000  <p>=   0.0000  <dp>=   0.0000
v6a         : <q>=   0.0000  <dq>=   0.0000  <p>=   0.0000  <dp>=   0.0000
v9a         : <q>=   0.0000  <dq>=   0.0000  <p>=   0.0000  <dp>=   0.0000
v10a        : <q>=   0.0000  <dq>=   0.0000  <p>=   0.0000  <dp>=   0.0000

 Diagonal Densities *1000,  state = 2
v1        C  4:1000.0000   0.0000   0.0000   0.0000   0.0000   0.0000   0.0000
     8 - 10>    0.0000   0.0000   0.0000

 Gross Gaussian Populations *10 (weighted),  state = 2
v1      ReC 4:  10.0000   0.0000   0.0000   0.0000   0.0000   0.0000   0.0000
     8 - 10>    0.0000   0.0000   0.0000

 Mode expectation values and variances,  state = 2
v1          : <q>=   0.0000  <dq>=   0.7000  <p>=   0.0000  <dp>=   0.7143
v6a         : <q>=   0.0000  <dq>=   0.7000  <p>=   0.0000  <dp>=   0.7143
v9a         : <q>=   0.0000  <dq>=   0.7000  <p>=   0.0000  <dp>=   0.7143
v10a        : <q>=   0.0000  <dq>=   0.7000  <p>=   0.0000  <dp>=   0.7143
------------------------------------------------------------------------------

 Time  =       1.00 fs,       CPU =       0.18 s,    Norm    = 1.00000000
 E-tot =   0.687536 ev,    E-corr =   0.025228 ev,   Delta-E =     0.0047 mev

 state = 1  pop.: 0.03120778   E-corr:   0.012614 ev,   E-tot =   0.008375 ev
 state = 2  pop.: 0.96879222   E-corr:   0.012614 ev,   E-tot =   0.679160 ev

 Diagonal Densities *1000,  state = 1
v1        C  4:   0.0000   0.0000   0.0000   0.0000 212.7451   0.0000   0.0000
     8 - 10>    0.0000 212.7451   0.0000

 Gross Gaussian Populations *10 (weighted),  state = 1
v1      ReC 4:   0.0000   0.0000   0.0000   0.0000   0.1560   0.0000   0.0000
     8 - 10>    0.0000   0.1560   0.0000

 Mode expectation values and variances,  state = 1
v1          : <q>=  -0.0471  <dq>=   0.7000  <p>=  -0.1824  <dp>=   0.7143
v6a         : <q>=  -0.0396  <dq>=   0.7000  <p>=  -0.0122  <dp>=   0.7143
v9a         : <q>=   0.0026  <dq>=   0.7000  <p>=  -0.1605  <dp>=   0.7143
v10a        : <q>=  -0.0000  <dq>=   1.2207  <p>=  -0.0000  <dp>=   1.2291

 Diagonal Densities *1000,  state = 2
v1        C  4:1310.1461   0.0316   0.0090   0.0413   9.0726   0.0246   0.0055
     8 - 10>    0.0399   9.0726   0.0010

 Gross Gaussian Populations *10 (weighted),  state = 2
v1      ReC 4:   9.4220   0.0011   0.0003   0.0014   0.1304   0.0009   0.0002
     8 - 10>    0.0014   0.1304  -0.0000

 Mode expectation values and variances,  state = 2
v1          : <q>=  -0.0288  <dq>=   0.7006  <p>=  -0.3050  <dp>=   0.7137
v6a         : <q>=  -0.0091  <dq>=   0.7002  <p>=  -0.1827  <dp>=   0.7140
v9a         : <q>=  -0.0092  <dq>=   0.7008  <p>=  -0.0720  <dp>=   0.7135
v10a        : <q>=   0.0000  <dq>=   0.6765  <p>=  -0.0000  <dp>=   0.7393
```

Example code:

```python
# Contents of test.py
from myfunctions import *

# Definitions
Modes=[11,3,14,8]                       # Modes of interest, known from comparison to pyrazine 4-mode model paper
istate=1                                # Electronic state of interest
Nstate=2                                # Total number of states
xyzfile='inputs/equilibrium.xyz'        # xyz file
AtomList,R0 = read_xyz(xyzfile)         # Read atom list and equilibrium geometry from xyz file
Nmode,Ng,Time,v = read_gwpcentres(Nstate,istate) # Read list of time-steps (atomic units) and displacement factors
D=R0                                    # Starting geometry
j=1                                     # Arbitrarily selected example value; v[i][j] signifies the displacement factor of mode i and row index j, which repeats every Ng (total number of Gaussians) rows for Gaussian k with t=t+1 (+1 time-step)

# Displace coordinates according to displacement factors for N modes
for i in range(len(Modes)):             # loop over modes
   Factor = v[i][j]                     # Displacement factor in atomic units of length
   imode=Modes[i]                       # Mode number
   D = displace_coords(D,imode,Factor)  # Displace coordinates by iteration

# Create output file
fname='displaced.xyz'                   # output xyz file
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

## Dependencies 

Python 2.7.6 



