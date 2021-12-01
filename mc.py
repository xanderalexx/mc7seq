import RPi.GPIO as g
from mcrcon import MCRcon as r

pin1 = 4
pin2 = 21
pin3 = 20
pin4 = 16

pressed1 = False
pressed2 = False
pressed3 = False
pressed4 = False

g.setmode(g.BCM)
g.setup(pin1, g.IN)
g.setup(pin2, g.IN)
g.setup(pin3, g.IN)
g.setup(pin4, g.IN)

with r('192.168.1.4', 'lmao') as mcr:
	while True:
		if g.input(pin1) == 1 and not pressed1:
			pressed1 = True
			print(mcr.command("execute at @a[name=xanderalex] run summon minecraft:pig ~ ~ ~"))
		elif g.input(pin1) == 1 and pressed1:
			continue
		else:
			pressed1 = False
		if g.input(pin2) == 1 and not pressed2:
			pressed2 = True
			print(mcr.command("kill @e[type=!minecraft:player]"))
		elif g.input(pin2) == 1 and pressed2:
			continue
		else:
			pressed2 = False
		if g.input(pin3) == 1 and not pressed3:
			pressed3 = True
			print(mcr.command("time set day"))
		elif g.input(pin3) == 1 and pressed3:
			continue
		else:
			pressed3 = False
		if g.input(pin4) == 1 and not pressed4:
			pressed4 = True
			print(mcr.command("time set night"))
		elif g.input(pin4) == 1 and pressed4:
			continue
		else:
			pressed4 = False
