import json
##
##
##
"""
def write_file(passfile,passdata):
    print(f'in update file module')
    with open(passfile,'w') as inpassfile:
        print('file is open for write')
        json.dump(passdata, inpassfile)
    # note: need to check for errors
"""
"""
Function to update a password in the password file
IN:     passfile: name of the password file (in same dir as code)
        inpassname: id(name) of the password being searched for
        newpass: new password to allocate to the password id(name)
OUT:    
"""
def update_passfile(passfile, inpassname, newpass):
    with open(passfile,'r') as passfilein:
        passdata = json.load(passfilein)
        passdata[inpassname] = newpass

    with open(passfile,'w') as inpassfile:
        print('file is open for write')
        json.dump(passdata, inpassfile)
    # write_file(passfile, passdata)
#   return()

update_passfile('./data/passfile.txt','password1','thisisgettingold')