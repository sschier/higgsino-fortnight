"""
A tree_trimmer.py skim function to accept things firing electron triggers.
"""

def skim(ch):
    #for i_ev in xrange(ch.met_Et):
    if ch.jetPt.size() > 0.:
        if ch.met_Et > 200. and ch.jetPt[0] > 150.:
            return True
    else: 
        if ch.met_Et > 200.:
            return True

    return False

# EOF
