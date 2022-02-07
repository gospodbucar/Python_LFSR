# JANEZ BUČAR, 35160122 IZJAVLJAM DA JE PROGRAM MOJE DELO 22.12.2021
# TREBA JE DODATI INTERPRETER galois v PyCharm

import sys
import subprocess

# DODA PIP ČE ŠE NI INSTALIRAN 'pip install galois':
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'galois'])

import galois

poly1 = galois.Poly.Degrees([4, 1, 0])
poly2 = galois.Poly.Degrees([4, 2, 0])
poly3 = galois.Poly.Degrees([4, 3, 2, 1, 0])

print('\n')
print("polinom: ", poly1, "\n", " nerazcepen: ", galois.is_irreducible(poly1), "  primitiven: ", galois.is_primitive(poly1))
print("polinom: ", poly2, "\n", " nerazcepen: ", galois.is_irreducible(poly2), "  primitiven: ", galois.is_primitive(poly2))
print("polinom: ", poly3, "\n", " nerazcepen: ", galois.is_irreducible(poly3), "  primitiven: ", galois.is_primitive(poly3))
print('JANEZ BUCAR, 35160122')

