#!/bin/bash

cat template-adc-s2.inp1 > qchem.inp
tail -n +3 displaced.xyz >> qchem.inp
cat template-adc-s2.inp2 >> qchem.inp

