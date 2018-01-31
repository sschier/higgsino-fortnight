"""
A tree_trimmer.py skim function 
"""

def skim(ch):
    if ch.n_baseel >= 1.:
        for trigger in ["HLT_e5_lhvloose", "HLT_e10_lhvloose_L1EM7", "HLT_e15_lhvloose_L1EM13VH", "HLT_e20_lhvloose"]:
            if hasattr(ch, trigger) and getattr(ch, trigger):
                return True
    #else: return False
    return False

# EOF
