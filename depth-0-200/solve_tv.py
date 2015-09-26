"""
Example script for doing the inversion of synthetic FTG data
"""

import logging
logging.basicConfig()

import pylab
import numpy
from enthought.mayavi import mlab

from fatiando.data.gravity import TensorComponent
from fatiando.inversion.pgrav import PGrav3D, DepthWeightsCalculator
from fatiando.visualization import plot_prism

import make_data


# Read the tensor component data from the data files
zzdata = TensorComponent(component='zz')
zzdata.load("gzz_data.txt")

xxdata = TensorComponent(component='xx')
xxdata.load("gxx_data.txt")

yydata = TensorComponent(component='yy')
yydata.load("gyy_data.txt")

xydata = TensorComponent(component='xy')
xydata.load("gxy_data.txt")

xzdata = TensorComponent(component='xz')
xzdata.load("gxz_data.txt")

yzdata = TensorComponent(component='yz')
yzdata.load("gyz_data.txt")


# Make a solver class and define the model space discretization    
solver = PGrav3D(x1=-400, x2=400, y1=-400, y2=400, z1=0, z2=800, \
                 nx=8, ny=8, nz=8, \
                 gzz=zzdata,\
                 gxy=xydata, gxz=xzdata, \
                 gxx=xxdata, gyy=yydata, gyz=yzdata)
# Compute the depth weight coefficients
dwsolver = DepthWeightsCalculator(pgrav_solver=solver, height=150)

dwsolver.solve_lm(initial=[10, 3], contam_times=0, \
                  lm_start=1, lm_step=10, it_p_step=20, max_it=100)

dwsolver.plot_adjustment(title="Depth Weights Adjustment")

z0, power = dwsolver.mean

Wp = solver.depth_weights(z0, power, normalize=True)

# Solve the linear inverse problem using Tikhonov regularization
#solver.solve_linear(damping=10**(-10), \
                    #smoothness=10**(-5), \
                    #curvature=0, \
                    #prior_weights=Wp, \
                    #data_variance=make_data.stddev**2, \
                    #contam_times=2)
                    
# Solve the non-linear problem
solver.solve_lm(damping=10**(-10), \
               smoothness=0, \
               curvature=0, \
               sharpness=10**(-4), beta=10**(-4), \
               initial=None, \
               prior_weights=Wp, \
               data_variance=make_data.stddev**2, \
               contam_times=1, \
               lm_start=10, lm_step=10, it_p_step=10, max_it=100)
solver.dump("res-tv.txt")

solver.plot_residuals()
#solver.plot_adjustment((14,14))
pylab.show()

solver.plot_stddev()
solver.plot_mean()

for prism in make_data.prisms:
    
    plot_prism(prism)
    
mlab.show_pipeline()
mlab.show()

