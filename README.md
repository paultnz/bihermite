



Python code to calculate bivariate Hermite polynomials.

Paul Teal - pault@nmr.nz

Thursday 7 November, 2024

Monday 2 December, 2024

Tuesday 7 January 2025

The input to the functions here are $V^{11},V^{12},V^{22}$ and $y_1,y_2$ - not $V_{11},V_{12},V_{22}$ and $x_1,x_2$.

Function sub2(sb1,sb2) takes as argument the two subscripts of
moment mu_ab, and returns the value. If global variables mu20, mu02,
mu11 are symbolic variables (defined using sympy) then it returns
the answer it terms of those, but if they are numeric then it
returns a numeric answer.

Function biHermite(n, m, y1, y2) takes the 2 subscripts of H.  If y1
and y2 are symbolic, then it returns a symbolic answer, but if they
are numeric it returns a numeric answer.

Note that if you are using symbolic y1 and y2, then you probably
want to set the optional argument recurse=False, because doing so
will give answers in terms of higher order moments, which will be
more concise.

The example code gives some symbolic evaluation and then numerical examples
for the cases $V_{11}=2,V_{12}=1,V_{22}=2$
and $x_1=x_2=1$ or $x_1=x_2=2$.
