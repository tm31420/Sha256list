import hashlib
from bitcoin import *

def convert(aa):
    string = aa
    aa = hashlib.sha256(string).hexdigest()    
    return aa
out = open("addr2.txt")
win = out.read()
with open("addr.txt") as file: 
    for line in file:
        ss = str.strip(line)
        nn = convert(ss)
        nn = int(nn,16)
        myhex = "%064x" % nn
        myhex = myhex[:64]
        priv = myhex
        pub = privtopub(priv)
        pubkey1 = encode_pubkey(privtopub(priv), "bin_compressed")
        addr = pubtoaddr(pubkey1)
        n = addr
        #print(n)
        if n.strip() in win:
            print ("found!!!",addr,myhex)
            break
