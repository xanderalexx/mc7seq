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