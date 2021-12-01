import RPi.GPIO as g
from mcrcon import MCRcon as r
import sevenseq.sevenseq as sevenseq
import time

with r('192.168.1.15', 'lmao') as mcr:
    while True:
        time.sleep(0.01)
        result = mcr.command("data get entity xanderalex Pos")
        if "xanderalex has the following entity data: " in result:
            raw = result.replace("xanderalex has the following entity data: ", "").replace(",", "").replace("[", "").replace("]", "").replace("d", "").split(" ")
            if "-" in raw[1]:
                rawneg = -abs(int(float(raw[1].replace("-", " "))))
                rawneg = -abs(int(float(raw[1].replace("-", " "))))
                sevenseq.setnum(rawneg)
            else:
                sevenseq.setnum(int(float(raw[1])))