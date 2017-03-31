import py_read_output as r 
import matplotlib.pyplot as pl

#put name of model here
MODEL_NAME = "fu_ori_alpha4"
s = r.read_spectrum(MODEL_NAME)

pl.plot(s["Lambda"], s["A85P0.50"])
pl.savefig("{}_spectrum.png".format(MODEL_NAME))