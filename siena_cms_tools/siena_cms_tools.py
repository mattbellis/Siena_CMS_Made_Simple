################################################################################
# CMS Made Simple
################################################################################

import numpy as np

################################################################################
### I REALLY, REALLY HOPE THIS WORKS!!!!!!!!!!!!!!!
### 
### Yup! I think it works.
### Let's try this again....
###
### Third verse, same as the first....
###
################################################################################
def cms_tools_help(verbose=0):

    if verbose<1:
        print "Usage:\n"
        print "\tcollisions = get_collisions(f)"
        print "\nWhere f is a file (or zip file)"
        print "\n"
        print "\tjets,topjets,muons,electrons,met = collision"
        print "\tmass,px,py,pz,csv = jet"
        print "\t#### EXPLANATION? AT LEAST OF CSV######"
        print "\tmass,px,py,pz,nsub,minmass = topjet"
        print "\tmass,px,py,pz = muon"
        print "\tmass,px,py,pz = electron"
        print "\tpt,phi = met"
        print "\n"


    if verbose>=1:

        print "Usage:\n"
        print "\tcollisions = get_collisions(f)"
        print "\nWhere f is a file (or zip file)"
        print "\n"
        print "\tjets,topjets,muons,electrons,met = collision"
        print "\n"
        print "jets: Decay products of the quarks. Sprays of particles. (AK5Jets)"
        print "topjets: Jet from the top quark (CA8Jets)"
        print "muons & electrons- if a top decays leptonicly (the W decays to a lepton (muon or electron) and neutrino.\n"
        print "\tIt can also decay to a tau, but the tau cannot be detected because it decays too quickly)"
        print "met: Missing energy in the transverse plane. This is often used to identify if there was a neutrinos in the\n"
        print "\tevent, as they are not detected by CMS."
        print "\n"
        print "\tmass,px,py,pz,csv = jet"
        print "\tmass,px,py,pz,nsub,minmass = topjet"
        print "\tmass,px,py,pz = muon"
        print "\tmass,px,py,pz = electron"
        print "\tpt,phi = met"
        print "\n"
        print "jet:\n"
        print "\tmass-mass of the particle/jet"
        print "\tpx-momentum in the x direction"
        print "\tpy-momentum in the y direction"
        print "\tpz-momentum in the z direction"
        print "\tcsv: Combined Secondary Vertex. This variable ranges from 0-1 (CHECK THIS!) and attempts to distinguish"
        print "\t\tbetween b-quarks which live longer and fly further before decaying, and lighter quarks which decay very"
        print "\t\tquickly. The closer this value is to 1, the greater confidence we have that the jet came from a b-quark."
        print "topjet:\n"
        print "\tmass-mass of the particle/jet"
        print "\tpx-momentum in the x direction"
        print "\tpy-momentum in the y direction"
        print "\tpz-momentum in the z direction"
        print "\tnsub: Number of sub-jet structure. Depending on how boosted the top is, the algorithm can still look for"
        print "\t\tsubstructure which would correspond to the jets from the decay of the b-quark or W boson."
        print "\tminmass-"
        print "pt-momentum in the transverse plane.  Momentum that is orthongonal to the beam."
        print "phi-called the azimuthal angle.  It is the angle between the pt and x-axis if the beams are on the z. "
        print "\n"

################################################################################
################################################################################
def pretty_print(collision):

    jets,topjets,muons,electrons,met = collision

    print "------- jets"
    for p in jets:
        mass,px,py,pz,csv = p
        print "mass:%8.5f px:%12.5f py:%12.5f pz:%12.5f csv:%12.5f" % (mass,px,py,pz,csv)
    print "------- top jets"
    for p in topjets:
        mass,px,py,pz,nsub,minmass = p
        print "mass:%8.5f px:%12.5f py:%12.5f pz:%12.5f nsub:%12.5f min mass:%12.5f" % (mass,px,py,pz,nsub,minmass)
    print "------- muons"
    for p in muons:
        mass,px,py,pz = p
        print "mass:%8.5f px:%12.5f py:%12.5f pz:%12.5f" % (mass,px,py,pz)
    print "------- electrons"
    for p in electrons:
        mass,px,py,pz = p
        print "mass:%8.5f px:%12.5f py:%12.5f pz:%12.5f" % (mass,px,py,pz)
    print "------- met"
    for p in met:
        pt,phi = p
        print "pt:%8.5f phi:%8.5f" % (pt,phi)


################################################################################
################################################################################
def get_collisions(infile,verbose=False):

    collisions = []

    not_at_end = True
    collision_count = 0
    new_collision = True
    while ( not_at_end ):

        ############################################################################
        # Read in one collision
        ############################################################################
        line = infile.readline()

        if collision_count%1000==0 and verbose:
            print "collision count: ",collision_count

        if line=="":
            not_at_end = False

        if line.find("Event")>=0:
            new_collision = True

        if new_collision==True:

            # Read in the jet info for this collision.
            jets = []
            line = infile.readline()
            njets = int(line)
            for i in xrange(njets):
                line = infile.readline()
                vals = line.split()
                e = float(vals[0])
                px = float(vals[1])
                py = float(vals[2])
                pz = float(vals[3])
                bquark_jet_tag = float(vals[4])
                jets.append([e,px,py,pz,bquark_jet_tag])

            # Read in the top jet info for this collision.
            topjets = []
            line = infile.readline()
            ntopjets = int(line)
            for i in xrange(ntopjets):
                line = infile.readline()
                vals = line.split()
                e = float(vals[0])
                px = float(vals[1])
                py = float(vals[2])
                pz = float(vals[3])
                nsub = float(vals[4])
                minmass = float(vals[5])
                topjets.append([e,px,py,pz,nsub,minmass])

            # Read in the muon info for this collision.
            muons = []
            line = infile.readline()
            nmuons = int(line)
            num_mu=0
            for i in xrange(nmuons):
                line = infile.readline()
                vals = line.split()
                e = float(vals[0])
                px = float(vals[1])
                py = float(vals[2])
                pz = float(vals[3])
                #charge = int(vals[4])
                #muons.append([e,px,py,pz,charge])
                muons.append([e,px,py,pz])
                num_mu+=1
                

            # Read in the electron info for this collision.
            electrons = []
            line = infile.readline()
            nelectrons = int(line)
            for i in xrange(nelectrons):
                line = infile.readline()
                vals = line.split()
                e = float(vals[0])
                px = float(vals[1])
                py = float(vals[2])
                pz = float(vals[3])
                #charge = int(vals[4])
                #electrons.append([e,px,py,pz,charge])
                electrons.append([e,px,py,pz])

            # Read in the photon info for this collision.
            #'''
            photons = []
            line = infile.readline()
            nphotons = int(line)
            for i in xrange(nphotons):
                line = infile.readline()
                vals = line.split()
                e = float(vals[0])
                px = float(vals[1])
                py = float(vals[2])
                pz = float(vals[3])
                photons.append([e,px,py,pz])
            #'''


            # Read in the information about the missing transverse energy (MET) in the collision.
            # This is really the x and y direction for the missing momentum.
            met = []
            line = infile.readline()
            nmet = int(line)
            for i in xrange(nmet):
                line = infile.readline()
                vals = line.split()
                #met_px = float(vals[0])
                #met_py = float(vals[1])
                met_pt = float(vals[0])
                met_phi = float(vals[1])
                met.append([met_pt,met_phi])

            new_collision = False
            collision_count += 1

            collisions.append([jets,topjets,muons,electrons,photons,met])

    return collisions

###############################################################################
'''
def get_collisions_from_zipped_file(infile,verbose=False):
    return get_collisions(infile)
'''

###############################################################################

def get_array_collisions(infile):
    collisions = np.load(infile)
    infile.close()
    return collisions


###############################################################################

def get_compressed_collisions(infile):
    b = np.load(infile)
    collisions = b['arr_0']
    infile.close()
    return collisions


###############################################################################

def get_pickle_collisions(infile):
    collisions = pickle.load(infile)
    infile.close()
    return collisions


###############################################################################
def get_onebyonesixty_collisions(infile):
    toReturn = []
    collisions = get_compressed_collisions(infile)
    for collision in collisions:
        toAdd = []
        tempJets = collision[0:40]
        tempMuons = collision[40:80]
        tempElectrons = collision[80:120]
        tempPhotons = collision[120:160]
        met = collision[160:162].tolist()
        #tempJets = tempJets[tempJets!=0]
        #tempMuons = tempMuons[tempMuons!=0]
        #tempElectrons = tempElectrons[tempElectrons!=0]
        #tempPhotons = tempPhotons[tempPhotons!=0]
        i = 0
        jets = []
        while i+5 <= len(tempJets) and tempJets[i] != 0:
            jets.append(tempJets[i:i+5].tolist())
            i += 5
        muons = []
        i = 0
        while i+5 <=len(tempMuons) and tempMuons[i] != 0:
            muons.append(tempMuons[i:i+5].tolist())
            i += 5
        electrons = []
        i = 0
        while i+5 <= len(tempElectrons) and tempElectrons[i] != 0:
            electrons.append(tempElectrons[i:i+5].tolist())
            i += 5
        photons = []
        i = 0
        while i+5 <= len(tempPhotons) and tempPhotons[i] != 0:
            photons.append(tempPhotons[i:i+4].tolist())
            i += 5
        #jets = np.array(jets)
        #muons = np.array(muons)
        #electrons = np.array(electrons)
        #photons = np.array(photons)
        #met = np.array(met)
        toAdd.append(jets)
        toAdd.append(muons)
        toAdd.append(electrons)
        toAdd.append(photons)
        toAdd.append(met)
        #toAdd = np.array(toAdd)
        toReturn.append(toAdd)
    #toReturn = np.array(toReturn)
    return toReturn

###############################################################################

def get_fourbyforty_collisions(infile):
    toReturn = []
    collisions = get_compressed_collisions(infile)
    for collision in collisions:
        toAdd = []
        tempJets = collision[0][0:40]
        tempMuons = collision[1][0:40]
        tempElectrons = collisions[2][0:40]
        tempPhotons = collision[3][0:40]
        met = collision[3][40:42]
        i = 0
        jets = []
        while i+5 <= len(tempJets) and tempJets[i] != 0:
            jets.append(tempJets[i:i+5].tolist())
            i += 5
        muons = []
        i = 0
        while i+5 <=len(tempMuons) and tempMuons[i] != 0:
            muons.append(tempMuons[i:i+5].tolist())
            i += 5
        electrons = []
        i = 0
        while i+5 <= len(tempElectrons) and tempElectrons[i] != 0:
            electrons.append(tempElectrons[i:i+5].tolist())
            i += 5
        photons = []
        i = 0
        while i+5 <= len(tempPhotons) and tempPhotons[i] != 0:
            photons.append(tempPhotons[i:i+4].tolist())
            i += 5
        toAdd.append(jets)
        toAdd.append(muons)
        toAdd.append(electrons)
        toAdd.append(photons)
        toAdd.append(met)
        #toAdd = np.array(toAdd)
        toReturn.append(toAdd)
    #toReturn = np.array(toReturn)
    return toReturn




###############################################################################

def get_thirtytwobyfive_collisions(infile):
    toReturn = []
    collisions = get_compressed_collisions(infile)
    for collision in collisions:
        toAdd = []
        tempJets = collision[0:8].tolist()
        tempMuons = collision[8:16].tolist()
        tempElectrons = collision[16:24].tolist()
        tempPhotons = collision[24:32].tolist()        
        met = collision[32][0:1].tolist()
        jets = []
        muons = []
        electrons = []
        photons = []
        for jet in tempJets:
            if jet[0] != 0:
                jets.append(jet)
        for muon in tempMuons:
            if muon[0] != 0:
                muons.append(muon)
        for electron in tempElectrons:
            if electron[0] != 0:
                electrons.append(electron)
        for photon in tempPhotons:
            if photon[0] != 0:
                photons.append(photon[0:4])
        
        toAdd.append(jets)
        toAdd.append(muons)
        toAdd.append(electrons)
        toAdd.append(photons)
        toAdd.append(met)
       # toAdd = np.array(toAdd)
        toReturn.append(toAdd)
    #toReturn = np.array(toReturn)
    return toReturn










