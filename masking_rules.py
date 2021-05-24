# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:49:08 2021

@author: Anshuman Sahu
"""

def masking_rule(s:str):
    
    """Masking rule"""
    
    l = len(s)
    return s[0] + '*'*(l-len(s[-int(l*.5):])-1) + s[-int(l*.5):]