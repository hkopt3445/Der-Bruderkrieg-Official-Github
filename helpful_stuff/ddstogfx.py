import os
 
directory = r"Documents\Paradox Interactive\Hearts of Iron IV\mod\DBK_backup_stuff\gfx\interface\aaa_westfalen_gui"

for filename in os.listdir(directory):
   filenamestorage = filename[:-4]
   if filename.endswith(".dds"):
    print("spriteType = {")
    print("name = GFX_bavarian_management" + filenamestorage) 
    print("texturefile = " + "gfx/interface/aaa_westfalen_gui/" + filename )
    print("}")
    print("")
   else:
       continue
