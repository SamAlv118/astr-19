class Animal:
	def describe(self):
		print(f"Description of {self.name}")
		print(f"*Arm Length: {self.arm_len} cm")
		print(f"*Leg Length: {self.leg_len} cm")
		print(f"*Number of Eyes: {self.num_eyes}")
		print(f"*Has a Tail?: {self.has_tail}")
		print(f"*Has Fur?: {self.has_fur}")




	def __init__(self, name = "default_name", arm_len = 0.0, leg_len = 0.0, num_eyes = 0, has_tail = False, has_fur = False):
		self.name = name
		self.arm_len = arm_len
		self.leg_len = leg_len
		self.num_eyes = num_eyes
		self.has_tail = has_tail
		self.has_fur = has_fur

def main():
	myAnimal = Animal("Raccoon", 30.0, 12.0, 2, True, True)
	myAnimal.describe()

if __name__ == '__main__':
	main()