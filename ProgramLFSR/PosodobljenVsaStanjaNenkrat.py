# Janez Bučar izjavljam, da je program moje delo. 35160122, 22.12.2021
# Samo zagnati treba program pa sam instalira PyLFSR...
# pip install pylfsr

import sys
import subprocess
import itertools
from pylfsr import LFSR

# Spodnja skripta instalira potrebno knjiznico ce je se nimate:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pylfsr'])



state = [list(i) for i in itertools.product([0, 1], repeat=4)]

# V FPOLY VNESEMO POTENCE PO VRST NPR  fpoly = [4, 1] JE X^4 + X + 1

fpoly = [4, 2]  # polinom x^4 +x^2 + 1

L = LFSR(initstate=[0, 0, 0, 0], fpoly=fpoly, counter_start_zero=False)
L.info()
L2 = LFSR(initstate=[0, 1, 0, 0], fpoly=fpoly, counter_start_zero=False) # V INITSTATE VNESEMO ZACETNO STANJE ZA LFSR GRAFICNI PRIKAZ 



for i in state:

    L = LFSR(initstate=i, fpoly=fpoly, counter_start_zero=False)
    for _ in range(5):  #PERIODA = range + 1 KER ZACNE Z 0 v tem primeru je perioda 6s
        L.next()

    print('Izhodno zaporedje za začetno stanje: ', i, ':   ', L.seq)
    perioda = len(L.seq)

print ('PERIODA: ', perioda)
print('JANEZ BUČAR, 35160122, 22.12.2021')


#  PRIKAZ GRAFIČNI LFSR je v programu LFSR
L2.Viz(show=True, show_labels=False, title='LSFR za trenutno začetno stanje:')

