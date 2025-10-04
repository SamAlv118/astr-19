import random

def SumRandFloat():
	a = random.random()
	b = random.random()
	print(a+b)
	print(type(a+b))

def SumRandInt():
	a = random.randint(1,10)
	b = random.randint(1,10)
	print(a+b)
	print(type(a+b))

def SumRandBoth():
	a = random.random()
	b = random.randint(1,10)
	print(a+b)
	print(type(a+b))

def main():
	SumRandFloat()
	SumRandInt()
	SumRandBoth()

if __name__ == "__main__":
	main()
