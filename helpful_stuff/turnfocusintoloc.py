myFile = open(r"C:\Users\17138\Documents\Paradox Interactive\Hearts of Iron IV\mod\dbkgithub\common\national_focus\SOV_pavel_milyukov_path.txt")

substring = "id ="
substring2 = "relative"
substring3 = "SOV_"

for line in myFile:
    if(substring in line):
        values = line.split("id = ")
        if(substring2 not in values[0]):
            if(substring3 in values[1]):
                nohyphines = values[1].split("_")
                print(nohyphines[0])