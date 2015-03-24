import siena_cms_tools as cms
import matplotlib.pylab as plt

import sys

import time

start = time.time()
collisions = cms.get_collisions(sys.argv[1])
print "Time to read in %d collisions: %f seconds" % (len(collisions),time.time()-start)

print len(collisions)

#fig = plt.figure(figsize=(7,5),dpi=100)
#ax = fig.add_subplot(1,1,1)
#ax = fig.gca(projection='3d')
#plt.subplots_adjust(top=0.98,bottom=0.02,right=0.98,left=0.02)

fig = plt.figure()
#ax = fig.add_subplot(1,1,1)
ax = fig.gca(projection='3d')
for i in xrange(100):
    lines,fig,ax = cms.display_collision3D(collisions[i],fig=fig,ax=ax)
    plt.pause(0.001)

#plt.show(block=False)

