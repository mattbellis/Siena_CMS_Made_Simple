import siena_cms_tools as cms
import matplotlib.pylab as plt

import sys

import time

#import seaborn as sn

start = time.time()
collisions = cms.get_collisions(sys.argv[1])
print "Time to read in %d collisions: %f seconds" % (len(collisions),time.time()-start)

print len(collisions)

fig = plt.figure(figsize=(7,5),dpi=100)
ax = fig.add_subplot(1,1,1)
ax = fig.gca(projection='3d')

lines,fig,ax = cms.display_collision3D(collisions[1],fig=fig,ax=ax)

ax.set_xlabel(r'$p_x$ (GeV/c$^2$)',fontsize=16)
ax.set_ylabel(r'$p_y$ (GeV/c$^2$)',fontsize=16)
ax.set_zlabel(r'$p_z$ (GeV/c$^2$)',fontsize=16)

plt.tight_layout()

plt.show()

