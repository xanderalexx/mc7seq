import RPi.GPIO as g
from mcrcon import MCRcon as r
import sevenseq.sevenseq as sevenseq
import time
import config.config as config
import sys
import math
if __name__ == '__main__':
    import config.config as config

print(len(sys.argv), str(sys.argv))
arg = sys.argv[1]
try:
    arg2 = sys.argv[2]
except:
    print("")
#/data get entity @e[type=minecraft:villager, name=A1, limit=1] Offers.Recipes[5].uses
with r(config.ip, config.password) as mcr:
    if arg == "y":
        while True:
            time.sleep(0.01)
            result = mcr.command("data get entity " + config.ign + " Pos")
            if (config.ign + " has the following entity data: ") in result:
                raw = result.replace(config.ign + " has the following entity data: ", "").replace(",", "").replace("[", "").replace("]", "").replace("d", "").split(" ")
                if "-" in raw[1]:
                    rawneg = -abs(int(float(raw[1].replace("-", ""))))
                    sevenseq.setnum(rawneg)
                else:
                    sevenseq.setnum(int(float(raw[1])))
    elif arg == "health":
        while True:
            result = mcr.command("data get entity " + config.ign + " Health")
            if (config.ign + " has the following entity data: ") in result:
                raw = result.replace(config.ign + " has the following entity data: ", "").replace("f", "")
                sevenseq.setnum(int(math.ceil(float(raw))))
    elif arg == "villager":
        if("," in arg2):
            villagerarray = arg2.split(",")
        else:
            villagerarray = [arg2]
        while True:
            time.sleep(0.01)
            total = 0
            for v in villagerarray:
                time.sleep(0.01)
                result = mcr.command("data get entity @e[type=minecraft:villager, name=" + v + ", limit=1] Offers.Recipes[5].uses")
                if(v + " has the following entity data: " in result):
                    raw = result.replace(v + " has the following entity data: ", "")
                    total = total + int(raw)
            sevenseq.setnum(total)