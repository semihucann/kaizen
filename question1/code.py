import hashlib as hasher

number_of_code = 100 	

### Auxiliary functions ################################################
def get_code_as_allowed_characters(hashed):
	allowed_characters = "ACDEFGHKLMNPRTXYZ234579"
	result = []
	k = 0
	hashed = hashed.upper() 
	for i in hashed:
		if k<8:
			exist = 0
			for j in allowed_characters:
				if i is j:
					exist = 1
					result.append(i)
					k += 1
					break
		else:
			break
	str1 = ''.join(result)
	return str1

def get_one_code(i, salt):
	kaizen_hasher = hasher.sha256()
	salted_data = str(i) + salt
	kaizen_hasher.update(salted_data.encode("utf-8"))
	hashed = kaizen_hasher.hexdigest()
	return hashed
				
### GenerateCodes function #############################################

def GenerateCodes():

	kaizen_salt = "kaizen_2021_example_secret_salt_text"

	print("Num\t", "Code")
	for i in range(0,number_of_code):
		hashed =  get_one_code(i, kaizen_salt)
		print(str(i)+".\t ",get_code_as_allowed_characters(hashed))


### CheckCode function #################################################	
	
def CheckCode (code):
	kaizen_salt = "kaizen_2021_example_secret_salt_text"

	exist = False
	
	for i in range(0,number_of_code):
		hashed = get_one_code(i, kaizen_salt)
		generated_code = get_code_as_allowed_characters(hashed)
		if generated_code == code:
			exist = True
			break
	return exist	

### Main Part  #########################################################
	
import argparse
parser = argparse.ArgumentParser(description='Code generator and checker')

parser.add_argument("-c", "--check"   , required=False,help="Check Code")

args = vars(parser.parse_args())

if args["check"] is None:
	GenerateCodes()
elif args["check"] is not None:
	code = args["check"]
	print(CheckCode(code))
