import sys
import re
from importlib import metadata as importlib_metadata

def get_Modules(mods):
    modVersion =[]
    dists = importlib_metadata.distributions()
    for dist in dists:
        name = dist.metadata["Name"]
        version = dist.version
        if name in mods: 
            modVersion.append(name +"==" + version)
    return modVersion

def main(path):
    mod_set = set()
    try:
        with open (path, 'r') as rf:
            for m in rf:
                if (m.startswith("import") or m.startswith("from")): 
                    temp = m.split(' ')[1].replace("\n", "")
                    temp = temp.split(".",1)[0]
                    mod_set.add(temp)
    except IOError:
        print("Error: File does not appear to exist.")
        return
    print("-"*50)
    print("Libraries called: " + str(mod_set))
    mod_list = get_Modules(list(mod_set))
    
    if len(mod_list) > 0:
        f = open("requirements.txt", "w")
        for mod in mod_list:
            f.write(mod)
        f.close()
        print("File generated: requirement.txt")
    else:
        print("File: " + path + " does not need a requirement.txt file")
        print("This can also mean you might have custom modules not native to Python known libraries")
    print("-"*50)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("This python script takes only 1 argument of the script path")
        x = input("Please give a python script directory address: ")
        main(x)
