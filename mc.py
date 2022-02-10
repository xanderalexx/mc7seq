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
    elif arg == "melontrades":
        villagerarray = config.villagers_with_melons
        while True:
            time.sleep(0.01)
            total = 0
            for v in villagerarray:
                time.sleep(0.01)
                result = mcr.command("data get entity @e[type=minecraft:villager, name=" + v + ", limit=1] Offers.Recipes[5].uses")
                if(v + " has the following entity data: " in result):
                    raw = result.replace(v + " has the following entity data: ", "")
                    if int(raw) != 12:
                        total = total + 1
            sevenseq.setnum(total)
    elif arg == "booktrades":
        villagerarray = config.villagers_with_books
        arraytracker = []
        for v in villagerarray:
            arraytracker.append(0)
        while True:
            time.sleep(0.01)
            total = 0
            rotation = 0
            for v in villagerarray:
                time.sleep(0.01)
                result = mcr.command("data get entity @e[type=minecraft:villager, name=" + v + ", limit=1] Offers.Recipes[2].uses")
                if(v + " has the following entity data: " in result):
                    raw = int(result.replace(v + " has the following entity data: ", ""))
                    if arraytracker[rotation] != raw and raw != 12:
                        print(v + " is ready to trade")
                        arraytracker[rotation] = raw
                    if raw != 12:
                        total = total + 1
                    rotation += 1
            sevenseq.setnum(total)
    elif arg == "tool":
        while True:
            maxDamage = None
            time.sleep(0.01)
            item = str(mcr.command("data get entity " + config.ign + " SelectedItem.id")).replace(config.ign + " has the following entity data: ", "").replace('"', "")
            try:
                damage = int(str(mcr.command("data get entity " + config.ign + " SelectedItem.tag.Damage")).replace(config.ign + " has the following entity data: ", ""))
            except:
                try:
                    itemCount = int(str(mcr.command("data get entity " + config.ign + " SelectedItem.Count")).replace(config.ign + " has the following entity data: ", "").replace("b", ""))
                    sevenseq.setnum(itemCount)
                    #print ("\033[A                             \033[A")
                    print("id: " + item + ", count: " + str(itemCount))
                except:
                    sevenseq.setnum(0)
                    #print ("\033[A                             \033[A")
                    print("idk")
            else:
                if "diamond" in item:
                    maxDamage = 1561
                elif "iron" in item:
                    maxDamage = 250
                elif "stone" in item:
                    maxDamage = 131
                elif "gold" in item:
                    maxDamage = 32
                elif "wood" in item:
                    maxDamage = 59
                elif "netherite" in item:
                    maxDamage = 2031
                elif "bow" in item:
                    maxDamage = 384
                elif "fishing" in item:
                    maxDamage = 64
                elif "flint" in item:
                    maxDamage = 64
                elif "carrot" in item:
                    maxDamage = 25
                elif "shear" in item:
                    maxDamage = 238
                elif "shield" in item:
                    maxDamage = 336
                elif "trident" in item:
                    maxDamage = 250
                elif "elytra" in item:
                    maxDamage = 432
                elif "crossbow" in item:
                    maxDamage = 465
                elif "warped" in item:
                    maxDamage = 100
                try:
                    newDamage = (maxDamage - damage)
                    final = round((newDamage / maxDamage) * 100)
                    if final == 100:
                        final = 99
                    #print ("\033[A                             \033[A")
                    print("id: " + item + ", (" + str(newDamage) + " / " + str(maxDamage) + ") * 100 = " + str(final))
                    sevenseq.setnum(final)
                except:
                    #print ("\033[A                             \033[A")
                    print("idk")
                    sevenseq.setnum(0)