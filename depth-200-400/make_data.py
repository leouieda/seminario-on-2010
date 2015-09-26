"""
Make some synthetic FTG data
"""

import logging
logging.basicConfig()

import numpy
import pylab

from fatiando.data.gravity import TensorComponent
from fatiando.utils.geometry import Prism


# Create a synthetic body
prisms = []
prism = Prism(dens=1000, x1=-100, x2=100, y1=-100, y2=100, z1=200, z2=400)
prisms.append(prism)

stddev = 0.1
    
def main():
    
    # Make a computation grid
    step = 75
    low = -600
    high = 600
    x = numpy.arange(low, high + step, step, 'f')
    y = numpy.arange(low, high + step, step, 'f')
    X, Y = pylab.meshgrid(x, y)
        
    # Create the data classes and generate synthetic data (at 150 m altitude)
    zzdata = TensorComponent(component='zz')
    zzdata.synthetic_prism(prisms=prisms, X=X, Y=Y, z=-150, stddev=stddev, \
                           percent=False)
    zzdata.dump("gzz_data.txt")
    
    xxdata = TensorComponent(component='xx')
    xxdata.synthetic_prism(prisms=prisms, X=X, Y=Y, z=-150, stddev=stddev, \
                           percent=False)
    xxdata.dump("gxx_data.txt")
    
    yydata = TensorComponent(component='yy')
    yydata.synthetic_prism(prisms=prisms, X=X, Y=Y, z=-150, stddev=stddev, \
                           percent=False)
    yydata.dump("gyy_data.txt")
    
    xydata = TensorComponent(component='xy')
    xydata.synthetic_prism(prisms=prisms, X=X, Y=Y, z=-150, stddev=stddev, \
                           percent=False)
    xydata.dump("gxy_data.txt")
    
    xzdata = TensorComponent(component='xz')
    xzdata.synthetic_prism(prisms=prisms, X=X, Y=Y, z=-150, stddev=stddev, \
                           percent=False)
    xzdata.dump("gxz_data.txt")
    
    yzdata = TensorComponent(component='yz')
    yzdata.synthetic_prism(prisms=prisms, X=X, Y=Y, z=-150, stddev=stddev, \
                           percent=False)
    yzdata.dump("gyz_data.txt")
    
    # Make nice plots
    pylab.figure(figsize=(4,3))
    pylab.title("$g_{zz}$")
    pylab.contourf(X, Y, zzdata.togrid(*X.shape), 30)
    pylab.colorbar()
    pylab.xlim(low, high)
    pylab.ylim(low, high)
    pylab.savefig("gzz.png")
    
    pylab.figure(figsize=(4,3))
    pylab.title("$g_{xx}$")
    pylab.contourf(Y, X, xxdata.togrid(*X.shape), 30)
    pylab.colorbar()
    pylab.xlim(low, high)
    pylab.ylim(low, high)
    pylab.savefig("gxx.png")
    
    pylab.figure(figsize=(4,3))
    pylab.title("$g_{xy}$")
    pylab.contourf(Y, X, xydata.togrid(*X.shape), 30)
    pylab.colorbar()
    pylab.xlim(low, high)
    pylab.ylim(low, high)
    pylab.savefig("gxy.png")
    
    pylab.figure(figsize=(4,3))
    pylab.title("$g_{xz}$")
    pylab.contourf(Y, X, xzdata.togrid(*X.shape), 30)
    pylab.colorbar()
    pylab.xlim(low, high)
    pylab.ylim(low, high)
    pylab.savefig("gxz.png")
    
    pylab.figure(figsize=(4,3))
    pylab.title("$g_{yy}$")
    pylab.contourf(Y, X, yydata.togrid(*X.shape), 30)
    pylab.colorbar()
    pylab.xlim(low, high)
    pylab.ylim(low, high)
    pylab.savefig("gyy.png")
    
    pylab.figure(figsize=(4,3))
    pylab.title("$g_{yz}$")
    pylab.contourf(Y, X, yzdata.togrid(*X.shape), 30)
    pylab.colorbar()
    pylab.xlim(low, high)
    pylab.ylim(low, high)
    pylab.savefig("gyz.png")
    
    pylab.show()
    
    
if __name__ == '__main__':
    
    main()