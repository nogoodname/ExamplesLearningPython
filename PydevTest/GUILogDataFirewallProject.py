#!/usr/bin/env python3
'''
Created on Mar 7, 2013

@author: school
'''
import tkinter as tk

pfs = tk.Frame ()

pfs.pack()

def loginpress():
    if (entrybox.get() == "pwtest"):
        if (entrybox2.get() == "Dictator" ):
            pfbutlast = tk.Button (pfs, text = "Close", command = pfs.quit).pack(side=tk.BOTTOM)
            pfbutsup = tk.Button (pfs, text = "Suppressed activty", command = SupActi).pack(side=tk.TOP)
            pfbutelite = tk.Button (pfs, text = "Elite activty", command = EliteActi).pack(side=tk.TOP)
            pfbutdate =tk.Button (pfs, text = "Traffic 18th of March", command = Traf18M).pack (side=tk.TOP)
            pfbutip1 = tk.Button (pfs, text = "Traffic 192.168.20.2", command = IPtraf1).pack (side=tk.TOP)
    
def SupActi():
    pfdata = open ("pfsensetrafficlogs")
    for sup in pfdata:
        if 'SUPPRESSED' in sup:
            print (sup)
            
def EliteActi():
    pfdata = open ("pfsensetrafficlogs")
    for elite in pfdata:
        if "ELITE" in elite:
            print (elite)
            
def Traf18M():
    pfdata = open ("pfsensetrafficlogs")
    for t18m in pfdata:
        if "Mar 18" in t18m:
            print (t18m)

def IPtraf1():
    pfdata = open ("pfsensetrafficlogs")
    for IP1 in pfdata:
        if "192.168.20.2" in IP1:
            print (IP1)
    
    
logintitle = tk.Label (pfs, text = "pfSense logdata login").pack(side=tk.TOP)
    
entrybox = tk.StringVar()
entrybox.set("Password")
entrybox2=tk.StringVar()
entrybox2.set("Username")
entry2 =tk.Entry (pfs, textvariable=entrybox2).pack(side=tk.TOP)
entry = tk.Entry (pfs, textvariable=entrybox, show = "*").pack(side=tk.TOP)
   
pfbut1 = tk.Button (pfs, text = "login", command = loginpress ). pack(side=tk.RIGHT)
#pfbutlast = tk.Button (pfs, text = "Close", command = pfs.quit).pack(side=tk.BOTTOM)
    
pfs.pack()

pfs.mainloop()