import py_read_output as r 
import matplotlib.pyplot as pl

s = r.read_spectrum("yso_a")

pl.plot(s["Lambda"], s["A85P0.50"])
pl.show()