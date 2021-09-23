#Author Graham Harper
#identikey grha4536
#CYBR HW 1
#ran with Python 3.7.5
# partial idea for waiting animation came from https://stackoverflow.com/questions/7039114/waiting-animation-in-command-prompt-python
#layout of timing code from https://stackoverflow.com/questions/3620943/measuring-elapsed-time-with-the-time-module/46544199

# imports and hardcoded ascii lists
import hashlib
import time
allChars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[]^_`{|}~'
alpha = 'abcdefghijklmnopqrstuvwxyz'

def Brute(md5_hash):
	inp = input("Would you like to use a simplified alphabet or a all characters possible? \nWARNING All chars takes substantially longer \nEven simple can take several minutes to complete \nEnter 1 for simple or 2 for all chars ")
	if inp == '2':             
		lib = allChars
	else:
		lib = alpha
	hashedCorrect2 = md5_hash
	i = 0
	count = 0
	#waiting animation
	#wait = [".", "..", "...", "....", ".....", "......", ".......", "........"]
	#for i in range(6):
	#	print("Currently Cracking", wait[i % len(wait)], end="\r")
	#	i+=1
	#	time.sleep(0.2)
	#start timer
	t0 = time.time()
	#iterate through alphabet 1 char password
	for c in lib:
		guess=c
		#calculate the hash of guess
		test = hashlib.md5(guess.encode())
		test2 = test.hexdigest()
		count+=1	#increment the counter because we are checking a guess
		if test2 == hashedCorrect2:		#if the guess is correct print correct
			print("The cracked password is : ", guess)
			elapsed = int(time.time()-t0)
			print("it took ", '{:02d}:{:02d}:{:02d}'.format(elapsed // 3600, (elapsed % 3600 // 60), elapsed % 60), " to crack")
			print("in ", count, "tries")
			cracked = True
			exit()
		#if the guess is not correct after going through all 1 char passwords, go to 2 chars
		# the following code is the same, just adding one digit at a time up to max 6 chars
		else:
			guess2 = guess
			for c in lib:
				guess2 = guess + c 
				#print(guess2)
				test = hashlib.md5(guess2.encode())
				test2 = test.hexdigest()
				count+=1
				if test2 == hashedCorrect2:
					print("The cracked password is : ", guess2)
					elapsed = int(time.time()-t0)
					print("it took ", '{:02d}:{:02d}:{:02d}'.format(elapsed // 3600, (elapsed % 3600 // 60), elapsed % 60), " to crack")
					print("in ", count, "tries")
					cracked = True
					exit()
				else:
					guess3 = guess2
					for c in lib:
						guess3 = guess2 + c 
						#print(guess3)
						test = hashlib.md5(guess3.encode())
						test2 = test.hexdigest()
						count+=1
						if test2 == hashedCorrect2:
							print("The cracked password is : ", guess3)
							elapsed = int(time.time()-t0)
							print("it took ", '{:02d}:{:02d}:{:02d}'.format(elapsed // 3600, (elapsed % 3600 // 60), elapsed % 60), " to crack")
							print("in ", count, "tries")
							cracked = True
							exit()
						else:
							guess4 = guess3
							for c in lib:
								guess4 = guess3 + c 
								#print(guess4)
								test = hashlib.md5(guess4.encode())
								test2 = test.hexdigest()
								count+=1
								if test2 == hashedCorrect2:
									print("The cracked password is : ", guess4)
									elapsed = int(time.time()-t0)
									print("it took ", '{:02d}:{:02d}:{:02d}'.format(elapsed // 3600, (elapsed % 3600 // 60), elapsed % 60), " to crack")
									print("in ", count, "tries")
									cracked = True
									exit()
								else:
									guess5 = guess4
									for c in lib:
										guess5 = guess4 + c 
										#print(guess5)
										test = hashlib.md5(guess5.encode())
										test2 = test.hexdigest()
										count+=1
										if test2 == hashedCorrect2:
											print("The cracked password is : ", guess5)
											elapsed = int(time.time()-t0)
											print("it took ", '{:02d}:{:02d}:{:02d}'.format(elapsed // 3600, (elapsed % 3600 // 60), elapsed % 60), " to crack")
											print("in ", count, "tries")
											cracked = True
											exit()
										else:
											guess6 = guess5
											for c in lib:
												guess6 = guess5 + c 
												#print(guess6)
												test = hashlib.md5(guess6.encode())
												test2 = test.hexdigest()
												count+=1
												if test2 == hashedCorrect2:
													print("The cracked password is : ", guess6)
													elapsed = int(time.time()-t0)
													print("it took ", '{:02d}:{:02d}:{:02d}'.format(elapsed // 3600, (elapsed % 3600 // 60), elapsed % 60), " to crack")
													print("in ", count, "tries")
													cracked = True
													exit()
	#if we go through all 6 chars and dont find the password, exit
	print("Failed to crack password")
	exit()
def Dict(md5_hash2, dictn):
	hashedCorrect = md5_hash2
	#attempt to open the dictionary file
	try:
	    dictn = open(dictn,"r", encoding='utf-8-sig')
	except:
	    print("File not found")
	    quit()

	count = 0
	print("Currently Cracking")
	t0 = time.time()
	dictn2 = dictn
	guess =""
	#iterate through each entry in the file
	for c in dictn2:
		guess=c
		print(guess)
		#hash each entry
		test = hashlib.md5(c.strip().encode())
		test2 = test.hexdigest()
		print(guess.strip(), test2)
		count+=1
		#compare our hash to the hash that was given
		if test2 == hashedCorrect:
			print("The cracked password is : ", guess)
			elapsed = int(time.time()-t0)
			print("it took ", '{:02d}:{:02d}:{:02d}'.format(elapsed // 3600, (elapsed % 3600 // 60), elapsed % 60), " to crack")
			print("in ", count, "tries")
			exit()
	else:
		print("Password not found in file")

print("Welcome to Graham's password cracker")
print("Please select a password cracking method")
print("Select 1 for brute force")
print("Select 2 for dictionary")
print("Select 3 to exit")
valid = False
val = ""
while valid != True:
	inp = input("What do you want to do: ")
	if inp == "1":
		val = "brute force"
		valid = True
	elif inp == "2":
		val = "dictionary"
		valid = True
	elif inp == "3":
		val = "exit"
		valid = True
		exit()
	else: 
		print("You entered an incorrect key, please try again")
		valid = False
	print("You selected", val)
	if val == "brute force":
		print("You selected brute force")
		inp2 = input("Please enter the MD5 hash of the password you want to crack: ")
		Brute(inp2)
	if val == "dictionary":
		print("You selected dictionary")
		inp3 = input("Please enter the MD5 hash of the password you want to crack: ")
		inp4 = input("Please enter the path to your dictionary: ")
		Dict(inp3, inp4)

