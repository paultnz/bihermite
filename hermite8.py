#!/usr/bin/env python3
#
# Paul Teal - pault@nmr.nz
# Thursday 7 November, 2024
# Monday 2 December, 2024


from itertools import product
from math import comb
from fractions import Fraction as fr
import sympy as sy
import re 

def split_string(str,maxlen=100):
  # This is just for limiting the maximum length of latex display lines
  sections = re.split(r'(?=[+-])',str)
  result = []
  current = ''
  for ss in sections:
    current += ss
    if len(current) >= maxlen:
      result.append(current)
      current = ''
  if current:
    result.append(current)
  return result  


def mup(Elist):
  # recursive function for evaluating moments
  if Elist == []:
    return 1
  if Elist == [1,1]:
    return mu20
  if Elist == [2,2]:
    return mu02
  if Elist == [1,2]:
    return mu11
  if Elist == [2,1]:
    return mu11
  Rout = 0
  for ii in range(len(Elist)-1):
    left = mup([ Elist[ii], Elist[-1] ])
    right = mup(Elist[:ii] + Elist[ii+1:-1])
    Rout += left * right
  return Rout

def sub2(sb1,sb2):
  return mup([1] * sb1 + [2] * sb2)


def biHermite(n, m, y1=0, y2=0, mu=0):
  # Generate terms for (y1 + j*Y1)^n
  terms1 = []
  for k in range(n + 1):
    terms1.append((comb(n, k) * (1j ** k), n-k, k))

  # Generate terms for (y2 + j*Y2)^m
  terms2 = []
  for k in range(m + 1):
    terms2.append((comb(m, k) * (1j ** k), m-k, k))
  # Combine terms from both expansions
  terms = 0
  for (coef1, a_pow, b_pow), (coef2, c_pow, d_pow) in product(terms1, terms2):
    coef_all = coef1 * coef2
    if coef_all.imag == 0: # ignore imaginary
      coef_all = int(coef_all.real)
      combined = coef_all * y1**a_pow * y2**c_pow * sub2(b_pow,d_pow)
      terms += combined
  return terms

if __name__ == "__main__":
  # Example usage: the first iteration is purely symbolic, then the
  # second and third use some specific values
  for loop in range(3):
    if loop==0:
      mu20, mu02, mu11, y1, y2= sy.symbols('mu20  mu02  mu11  y1  y2')
    elif loop==1:
      #override symbols with specific values
      mu20 = fr(2,3); mu02 = fr(2,3); mu11 = -fr(1,3); y1 = fr(1,3); y2 = fr(1,3)
    elif loop==2:
      y1 = fr(2,3); y2 = fr(2,3)

    if loop<2:  
      # Print values of mu
      print('\\begin{align*}')
      for mn in range(4,9+1,2):
        for m in range( (mn+2)//2):
          n = mn-m
          l2 = sub2(m,n)
          print(f'\\mu_{{{m}{n}}} =& ' + sy.latex(sy.simplify(l2)) + '\\\\')
      print('\\end{align*}')
      print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

    print('\\begin{align*}')
    for nm in range(1,10): 
      for m in range(0,(nm+2)//2):
        n = nm - m
        result = sy.expand(biHermite(n, m, y1, y2),mul=True)
        la = sy.latex(result)
        print(f'H_{{{n}{m}}} =&',sep='',end='')
        if not result.free_symbols:
          print(f'{la} \\approx {result.evalf():.4f}\\\\')
        else:
          lines = split_string(la,150)
          for line in lines[:-1]:
            print(line,'\\\\& ')
          print(lines[-1],'\\\\')
    print('\\end{align*}')
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

