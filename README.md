# CODE_displace_coords

## Description

Calculate X-ray absorption spectra from a quantum dynamics trajectory for pyrazine (4-mode 2-state model).  

## Example Usage

#### Extract from 'gwpcentres' file 
The beginning of the file gives two numbers (4 and 3) which are the number of modes and number of Gaussians respectively. As you can see there are four columns (modes) and three rows (Gaussians per mode). Each section starts with the time (atomic units), then state (1,2 in this case), and then the displacements (atomic units) along each normal mode. Note: Using only three Gaussians is not recommended but used here for an easier explanation. 

```
  #            4           3
 time:   0.0000000000000000
 state:           1
   0.000000000       0.000000000       0.000000000       0.000000000
  0.9352661232       0.000000000       0.000000000       0.000000000
   0.000000000      0.9352661232       0.000000000       0.000000000
 state:           2
   0.000000000       0.000000000       0.000000000       0.000000000
  0.9352661232       0.000000000       0.000000000       0.000000000
   0.000000000      0.9352661232       0.000000000       0.000000000
 time:   41.341373336559997
 state:           1
 -0.6883521397E-02  0.8224127040E-02 -0.2870900383E-01   0.000000000
  0.9109454151      0.8224127040E-02 -0.2870900383E-01   0.000000000
 -0.6883521397E-02  0.9375857968     -0.2870900383E-01   0.000000000
 state:           2
 -0.2946498382E-01 -0.1017365944E-01 -0.8717163015E-02   0.000000000
  0.8883616066     -0.1008518108E-01 -0.8717163018E-02   0.000000000
 -0.2946732990E-01  0.9191753547     -0.8717163018E-02   0.000000000

```

Using the 'read_gwpcentres' function,

```python

istate=1                                # Electronic state of interest
Nstate=2                                # Total number of states
# Read list of time-steps (atomic units) and displacement factors
Nmode,Ng,Time,v = read_gwpcentres(Nstate,istate) 

for j in range(6):
   string = str(v[0][j]) + ' ' + str(v[1][j]) + ' ' + str(v[2][j]) + ' ' + str(v[3][j])
   print string.split()
```
gives the first 6 displacements for state 1 and the four modes (columns), in this case corresponding to exactly two time-steps,

```
['0.0', '0.0', '0.0', '0.0']
['0.9352661232', '0.0', '0.0', '0.0']
['0.0', '0.9352661232', '0.0', '0.0']
['-0.006883521397', '0.00822412704', '-0.02870900383', '0.0']
['0.9109454151', '0.00822412704', '-0.02870900383', '0.0']
['-0.006883521397', '0.9375857968', '-0.02870900383', '0.0']

```

#### Extract from 'output' file
The important lines for this are the Time (fs) and the Gross Gaussian Populations for each state. The spectrum for a specific time-step is the weighted sum of spectra for each Gaussian. The Gaussian displacements are in the gwpcentres file (above) and the weightings are in this file. 

```
 Time  =       0.00 fs,       CPU =       0.04 s,    Norm    = 1.00000000
 E-tot =   0.687531 ev,    E-corr =   0.000000 ev,   Delta-E =     0.0000 mev

 state = 1  pop.: 0.00000000   E-corr:  -0.000000 ev,   E-tot =  -0.000000 ev
 state = 2  pop.: 1.00000000   E-corr:   0.000000 ev,   E-tot =   0.687531 ev

...

 Gross Gaussian Populations *10 (weighted),  state = 1
v1      ReC 4:   0.0000   0.0000   0.0000

...

 Gross Gaussian Populations *10 (weighted),  state = 2
v1      ReC 4:  10.0000   0.0000   0.0000

...

------------------------------------------------------------------------------

 Time  =       1.00 fs,       CPU =       0.06 s,    Norm    = 1.00000000
 E-tot =   0.687532 ev,    E-corr =   0.000000 ev,   Delta-E =     0.0004 mev

 state = 1  pop.: 0.00000000   E-corr:  -0.000000 ev,   E-tot =  -0.000000 ev
 state = 2  pop.: 1.00000000   E-corr:   0.000000 ev,   E-tot =   0.687532 ev

...

 Gross Gaussian Populations *10 (weighted),  state = 1
v1      ReC 4:   0.0000   0.0000   0.0000

...

 Gross Gaussian Populations *10 (weighted),  state = 2
v1      ReC 4:   9.9982   0.0014   0.0005

...

```

Using the 'read_output' function,

```python
Nstate=2                                # Total number of states
Ng=3					# Total number of Gaussians
Time,gWeights = read_output(Nstate,Ng)   # Read time-steps (fs), and Gaussian weights

for j in range(4):
   string = str(gWeights[0][j]) + ' ' + str(gWeights[1][j]) + ' ' + str(gWeights[2][j])
   print string.split()

```

gives the three columns (Gaussians), and each row is in the order "state 1, state 2" for time-step 1, then "state 1, state 2" for time-step 2, and so on, 

```
['0.0', '0.0', '0.0']
['10.0', '0.0', '0.0']
['0.0', '0.0', '0.0']
['9.9982', '0.0014', '0.0005']

```

## Functions

### read_xyz  

#####Description
Reads xyz file 'fname'

#####Usage
```python
AtomList,Coords = read_xyz(fname)
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
Displc = read_displacements(Nat,imode)
```

#####Inputs    
- Nat (int), total number of atoms

- imode (int), the displacements are taken from mode number 'imode'

#####Outputs   
- Displc (float list), single column of displacement coordinates (length 3 x Nat)

### read_gwpcentres 

#####Description
Read displacement factors from file 'gwpcentres' for state 'istate'.

#####Usage
```python
Nmode,Ng,Time,v = read_gwpcentres(Nstate,istate)
```

#####Inputs    
- Nstate (int), the total number of states

- istate (int), the state to read

#####Outputs   
- Nmode (int), number of modes

- Ng (int), number of Gaussians

- Time (float list), list of time in atomic units 

- v (float array), displacement factors array with columns 0,1,...,Nmode-1 pertaining to modes 1,2,...,Nmode, rows correspond to Ng Gaussians
 
### read_output 

#####Description
Read Gaussian weights (and state weights) from file 'output' for state 'istate'.

#####Usage
```python
Time,gWeights = read_output(Nstate,Ng)
```

#####Inputs    
- Nstate (int), total number of states

- Ng (int), total number of Gaussians

#####Outputs   
- Time (float list), list of time in fs 

- gWeights (float array), Gaussian populations with columns 0,1,...,Ng-1 pertaining to Gaussians 1,2,...,Ng


### read_adc

#####Description
Reads excitation energies and oscillator strengths from qchem XAS ADC calculation output.

#####Usage
```python
XAS = read_adc(ADCoutput)
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
XAS = read_adc(SRCoutput)
```

#####Inputs    
- SRCoutput (str), SRC output file name

#####Outputs   
- XAS (float array), XAS[0] = energies, XAS[1] = oscillator strengths


### generate_spectrum 

#####Description
Generates spectrum with Lorentzian broadened lines (with FWHM=0.5 eV)

#####Usage
```python
x,spect = generate_spectrum(XAS)
```

#####Inputs    
- XAS (float array), XAS[0] = energies, XAS[1] = oscillator strengths

#####Outputs   
- x (float list), x-axis energies (eV)

- spect (float list), spectrum (arb. units) with Lorentzian broadened lines with FWHM=0.5 eV 


### displace_coords 

#####Description
Displace coords from xyz file 'xyzfile' along mode 'imode' `(0<int<=Nmode)` by 'Factor' (float)

#####Usage
```python
D = displace_coords(Coords,imode,Factor)
```

#####Inputs    
- Coords (float list), coordinates as column vector with the format X1,Y1,Z1,X2,Y2,Z2,...

- imode (int), the coordinates are displaced along mode number 'imode'

- Factor (float), the coordinates are displaced along mode number 'imode' by 'Factor' atomic units  

#####Outputs   
- D (float list), displaced coordinates with same formatting as 'Coords'


## Files

## Dependencies 

Python 2.7 

