Helper Functions
##-----------------------------------------------------------
##Helper Functions
def stripquotes(S):
    """strips quotes and prefix"""
    q= S[-1]
    return S[S.find(q):].strip(q)
def strcmp(S1, S2):
    """compares strings of strings"""
    if not isinstance(S1, basestring) or not isinstance(S2, basestring):
        return False
    return stripquotes(S1)==stripquotes(S2)