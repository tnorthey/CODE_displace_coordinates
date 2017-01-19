# spectrum.py: prints the spectrum energies (x-axis) and intensities (y-axis)
# Usage: python spectrum.py <option=ADC,SRC> <file name>

from myfunctions import *
import sys

option=sys.argv[1]
filename=sys.argv[2]

if option=='ADC':
   XAS = read_adc(filename)
elif option=='SRC':
   XAS = read_src(filename)
else: 
   print "Pick option='ADC' or 'SRC'"

x,spect = generate_spectrum(XAS)

print x
print spect
