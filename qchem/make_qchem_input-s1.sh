#!/bin/bash

cat template-adc-s1.inp1 > qchem.inp
tail -n +3 displaced.xyz >> qchem.inp
cat template-adc-s1.inp2 >> qchem.inp

