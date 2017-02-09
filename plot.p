
set terminal png size 1200,900 enhanced font "Helvetica,20"
set output 'output.png'
set title "Pyrazine XAS"
set xlabel "E (eV)"
set ylabel "Intensity (arb. units)"

plot "outputs/cvs-adc-gs.dat" using 1:2 title 'GS' with lines, \
     "outputs/cvs-adc-mom.dat" using 1:2 title 'ES (S1)' with lines, \
     "outputs/cvs-adc-mom-s2.dat" using 1:2 title 'ES (S2)' with lines

#"outputs/cvs-adc-triplet.dat" using 1:2 title 'ES (SCF triplet)' with lines, \
