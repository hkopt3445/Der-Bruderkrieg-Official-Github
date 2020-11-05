import os
 
directory = '/Users/imaitra13777/Documents/Paradox Interactive/Hearts of Iron IV/mod/austriamod/gfx/interface/aaa_usa_election_stuff/'

for filename in os.listdir(directory):
   filenamestorage = filename[:-4]
   if filename.endswith(".dds"):
    print("spriteType = {")
    print("name = GFX_USA_election_" + filenamestorage) 
    print("texturefile = " + "gfx/interface/aaa_usa_election_stuff/" + filename )
    print("}")
    print("")
   else:
       continue
