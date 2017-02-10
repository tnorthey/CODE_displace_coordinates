# CODE_displace_coords

## Description

Calculate X-ray absorption spectra from a quantum dynamics trajectory for pyrazine (4-mode 2-state model).  

## Example Usage

#### Extract from 'gwpcentres' file 
The beginning of the file gives two numbers (4 and 10) which are the number of modes and number of Gaussians respectively. As you can see there are four columns (modes) and ten rows (Gaussians per mode). Each section starts with the time (atomic units), then state (1,2 in this case), and then the displacements (atomic units) along each normal mode.

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

Using the 'read_gwpcentres' function,

```python

istate=1                                # Electronic state of interest
Nstate=2                                # Total number of states
# Read list of time-steps (atomic units) and displacement factors
Nmode,Ng,Time,v = read_gwpcentres(Nstate,istate) 

for j in range(20):
   string = str(v[0][j]) + ' ' + str(v[1][j]) + ' ' + str(v[2][j]) + ' ' + str(v[3][j])
   print string.split()
```
gives the first 20 displacements for state 1 and the four modes (columns), in this case corresponding to exactly two time-steps,

```
['0.0', '0.0', '0.0', '0.0']
['0.9352661232', '0.0', '0.0', '0.0']
['0.0', '0.9352661232', '0.0', '0.0']
['0.0', '0.0', '0.9352661232', '0.0']
['0.0', '0.0', '0.0', '0.9352661232']
['-0.9352661232', '0.0', '0.0', '0.0']
['0.0', '-0.9352661232', '0.0', '0.0']
['0.0', '0.0', '-0.9352661232', '0.0']
['0.0', '0.0', '0.0', '-0.9352661232']
['0.9352661232', '0.9352661232', '0.0', '0.0']
['-0.006883521395', '0.00822412704', '-0.0287090038', '0.0']
['0.9109454151', '0.00822412704', '-0.0287090038', '0.0']
['-0.006883521395', '0.9375857968', '-0.0287090038', '0.0']
['-0.006883521395', '0.00822412704', '0.8801445246', '0.0']
['-0.04705419099', '-0.0395813075', '0.002568199602', '0.2386044828']
['-0.9247124579', '0.00822412704', '-0.0287090038', '0.0']
['-0.006883521395', '-0.9211375427', '-0.0287090038', '0.0']
['-0.006883521395', '0.00822412704', '-0.9375625322', '0.0']
['-0.04705419099', '-0.0395813075', '0.002568199602', '-0.2386044828']
['0.9109454151', '0.9375857968', '-0.0287090038', '0.0']

```

#### Extract from 'output' file
The important lines for this are the Time (fs) and the Gross Gaussian Populations for each state. The spectrum for a specific time-step is the weighted sum of spectra for each Gaussian. The Gaussian displacements are in the gwpcentres file (above) and the weightings are in this file. 

```
 Time  =       0.00 fs,       CPU =       0.05 s,    Norm    = 1.00000000
 E-tot =   0.687531 ev,    E-corr =   0.000000 ev,   Delta-E =     0.0000 mev

 state = 1  pop.: 0.00000000   E-corr:  -0.000000 ev,   E-tot =  -0.000000 ev
 state = 2  pop.: 1.00000000   E-corr:   0.000000 ev,   E-tot =   0.687531 ev

...

 Gross Gaussian Populations *10 (weighted),  state = 1
v1      ReC 4:   0.0000   0.0000   0.0000   0.0000   0.0000   0.0000   0.0000
     8 - 10>    0.0000   0.0000   0.0000

...

 Gross Gaussian Populations *10 (weighted),  state = 2
v1      ReC 4:  10.0000   0.0000   0.0000   0.0000   0.0000   0.0000   0.0000
     8 - 10>    0.0000   0.0000   0.0000

...

 Time  =       1.00 fs,       CPU =       0.18 s,    Norm    = 1.00000000
 E-tot =   0.687536 ev,    E-corr =   0.025228 ev,   Delta-E =     0.0047 mev

 state = 1  pop.: 0.03120778   E-corr:   0.012614 ev,   E-tot =   0.008375 ev
 state = 2  pop.: 0.96879222   E-corr:   0.012614 ev,   E-tot =   0.679160 ev

...
 
 Gross Gaussian Populations *10 (weighted),  state = 1
v1      ReC 4:   0.0000   0.0000   0.0000   0.0000   0.1560   0.0000   0.0000
     8 - 10>    0.0000   0.1560   0.0000

...

 Gross Gaussian Populations *10 (weighted),  state = 2
v1      ReC 4:   9.4220   0.0011   0.0003   0.0014   0.1304   0.0009   0.0002
     8 - 10>    0.0014   0.1304  -0.0000

...

```

Using the 'read_output' function,

```python
Nstate=2                                # Total number of states
Ng=10					# Total number of Gaussians
Time,gWeights = read_output(Nstate,Ng)   # Read time-steps (fs), and Gaussian weights

for j in range(4):
   string = str(gWeights[0][j]) + ' ' + str(gWeights[1][j]) + ' ' + str(gWeights[2][j])
   print string.split()

```

gives only the first three columns (Gaussians), and each row is in the order "state 1, state 2" for time-step 1, then "state 1, state 2" for time-step 2, and so on, 

```
['0.0', '0.0', '0.0']
['10.0', '0.0', '0.0']
['0.0', '0.0', '0.0']
['9.422', '0.0011', '0.0003']
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


```math
a+b=c
\pi
\sum_i
```
