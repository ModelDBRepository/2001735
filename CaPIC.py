"""
This script aims to measure the Ca PIC, and do the IV test
# some of the functions here depend on defining the dendrites list as "basal" list
"""


from neuron import h

#####-----------------End of Function------------------------------------------------

def setDendriticdistance(cellObj):
    """This function calculate path distance of each segments to the soma"""
    
    new_nseg    =13
    for sec in cellObj.basal:
        if(sec.nseg < new_nseg):
            sec.nseg = new_nseg

    for sec in cellObj.basal:
        for seg in sec:
            seg.DendDist_info       = h.distance(cellObj.soma(0.5),seg)
    ###---------------end of for loop---------------------------------------------

    for sec in cellObj.basal:
        for seg in sec:
            if(seg.DendDist_info < -0.0001):
                print "ERROR: Negative dendritic path distance in segment %s (%f)\n" %(h.secname(sec=sec), seg.x)
                print "Revise where the dendrite is connected to the soma \n"
    ###---------------end of for loop---------------------------------------------
    print "Distance calculated"

#####-----------------End of Function------------------------------------------------

def placePunctaCaPIC(cellObj,cond,proximalLimit, distalLimit, theta = -43, clusterFreq = 100, clusterwidth = 25):
    """This function place the CaPIC channels

    INPUTS:
    clusterFreq : distance to repeat the Ca cluster , default = 100 um
    clusterwidth:  cluster width , default = 25 um
    theta       : Activation voltage, default = -43 mV

    the cluster width is 25 um 
    """

    ### place CaPIC on the dendrites
    for sec in cellObj.basal:
        sec.insert('Llva')
        sec.gcaLlvabar_Llva     = 0
        sec.theta_m_Llva        = theta       #(mV)
        # sec.tau_m_Llva          = 60        #(ms)
        # sec.kappa_m_Llva        = -6
    ##---------------------------------------

    d = proximalLimit
    while (d<distalLimit):
        for sec in cellObj.basal:
            for seg in sec:
                if( (seg.DendDist_info >= d) and (seg.DendDist_info < d+clusterwidth) ):
                    seg.gcaLlvabar_Llva     = cond
        d += clusterFreq
    ##------end of while loop-------------
    print "CaPIC channels has beem added from %d to %d" %(proximalLimit,distalLimit)

#####-----------------End of Function------------------------------------------------



