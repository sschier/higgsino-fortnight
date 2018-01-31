"""
A tree_trimmer.py skim function 
"""

def skim(ch):
    if ch.n_basemu >= 1.:
        for trigger in ["HLT_mu4", "HLT_mu10", "HLT_mu14", "HLT_mu18"]:
            if hasattr(ch, trigger) and getattr(ch, trigger):
                return True
    return False

# EOF
