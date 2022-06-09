from pystyle import *
from hashlib import sha256

banner = r"""
  ad8888888888ba
 dP'         `"8b,
 8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
 8  8' `8           "88baadP''''YbaaadP'''YbdP''Yb
 8  8   8              '''        '''      ''    8b
 8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
 8  `''''       ,d8""
 Yb,         ,ad8"    
  "Y8888888888P" """

ascii_art = r"""
  _____                        __                      
 |_   _|                      [  |  _                  
   | |       .--.   _   _   __ | | / ] .---.   _   __  
   | |   _ / .'`\ \[ \ [ \ [  ]| '' < / /__\\ [ \ [  ] 
  _| |__/ || \__. | \ \/\ \/ / | |`\ \| \__.,  \ '/ /  
 |________| '.__.'   \__/\__/ [__|  \_]'.__.'[\_:  /   
											  																																		\__.'"""[1:]

def init():
	System.Clear()
	System.Size(160, 50)
	System.Title("Lowkey")
	Anime.Fade(text=Center.Center(banner), color=Colors.green_to_white, mode=Colorate.Vertical, enter=True)

def main():
	System.Clear()
	print('\n' * 2)
	print(Colorate.Diagonal(color=Colors.green_to_white, text=Center.XCenter(ascii_art)))
	print('\n' * 3)
	name = Write.Input(text="Name of the file to (de)crypt > ", color=Colors.green_to_white, interval=0.005)
	final = Write.Input(text="Name of the final file > ", color=Colors.green_to_white, interval=0.005)
	key = Write.Input(text="Enter your key > ", color=Colors.green_to_white, interval=0.005)
	keys = sha256(key.encode("utf-8")).digest()
	with open(name,"rb") as f_name:
		with open(final,"wb") as f_final:
			i = 0
			while f_name.peek():
				c = ord(f_name.read(1))
				j = i % len(keys)
				b = bytes([c^keys[j]])
				f_final.write(b)
				i = i + 1
	Write.Input(text="'" + name + "' was succesfully (de)crypted into the '" + final + "' file!", color=Colors.green_to_white, interval=0.005)


if __name__ == '__main__':
	init()
	while True:
		main()