import siena_cms_tools as cms
import matplotlib.pylab as plt

import sys

infile = open(sys.argv[1])

#collisions = cms.get_collisions(infile)
collisions = cms.get_collisions_from_file_name(sys.argv[1])

print len(collisions)

#fig = plt.figure(figsize=(7,5),dpi=100)
#ax = fig.add_subplot(1,1,1)
#ax = fig.gca(projection='3d')
#plt.subplots_adjust(top=0.98,bottom=0.02,right=0.98,left=0.02)

lines,fig,ax = cms.display_collision3D(collisions[1])

#plt.show(block=False)

