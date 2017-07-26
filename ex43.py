from sys import exit
from random import randint

class Sence(object):

	def enter(self):
		print "This sence is not yet configured. Subclass it and implement enter()."
		exit(1)
        
        
class Engine(object):

	def __init__(self, sence_map):
		self.sence_map = sence_map
        
	def play(self):
		current_sence = self.sence_map.opening_sence()
        
		while True:
			print " \n-----------"
			next_sence_name = current_sence.enter()
			current_sence = self.sence_map.next_sence(next_sence_name)

class Death(Sence):

	quips = [
         "you died. you kinda suck at this.",
         "your mom would be proud...if she were smarter.",
         "such a luser.",
         "I have a small puppy that's better at this."
	]
    
	def enter(self):    
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)
        
class CentralCorridor(Sence):

	def enter(self):
		print "beijing"
		print "balalalala"
		print "\n"
		print "."*10
        
	action = raw_input(">")
    
	if action == "shoot!":
		print "you are dead."	
		return 'death'
        
	elif action == "dodge!":
		print "you are dead too."
		return 'death'
		
	elif action == "tell a joke":
		print "you are smart."
		return 'laser_weapon_armpry'
        
	else:
		print " Dose not compute."
		return 'central_corridor'
        
class LaserWeaponArmory(Sence):
	def enter(self):
		print "bejing, balalla..."
		print "guess passing number. the code is 3 digits."
		code = "d%d%d%" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]>")
		guesses = 0
        
		while guess != code and guesses < 10:
			print "Bzzzeddd!"
			guesses += 1
			guess = raw_input("[keypad]>")
            
		if guess == code:
			print "yeah~~"
			return 'the_bridge'
		else:
			print "you are wrong."
			print "you die."
			return 'death'
            
class TheBridge(Sence):
	def enter(self):
		print "welcome!"
		print "you must make a fire in the hole."
        
		action = raw_input(">")
        
		if action == "throw the bomb":
			print "it gose off"
			return 'death'
            
		elif action == "slowly place the bomb":
			print "it has been worked."
			return 'escape_pod'
            
		else:
			print "dose not compute."
			return 'the_bridge'
        
class EscapePod(Sence):
	def enter(self):
		print "ballaala..."
		print "guess which one is the right escapepod?"
        
		good_pod = randint(1, 5)
		guess = raw_input("you choose the pod is?\n>")
        
		if guess != good_pod:
			print "wrong"
			return 'death'
            
		else:
			print "right"
			print " you win"
            
			return 'finished'
            
        
class Map(object):

	sences ={
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponAromry(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
	}
        
	def __init__(self, start_sence):
		self.start_sence = start_sence
        
	def next_sence(self, sence_name):
		return Map.sences.get(sence_name)
        
	def opening_sence(self):
		return self.next_sence(self.start_sence)
        
             
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
        
         
        
        
    
        
    