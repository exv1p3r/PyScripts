#!/usr/bin/env python2
import crypt

def testPass(cryptPass):
	salt = cryptPass[0:2]
	dictFile = open("diccionario.txt", "r")
	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word, salt)
		if (cryptWord == cryptPass):
			print "[*] Password found: " + word + "\n"
			return
		else:
			print "[-] Password not found.\n"
			return
def main():
	passFile = open("passwords.txt", 'r')
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(":")[0]
			cryptPass = line.split(":")[1].strip(' ')
			print "[*] Cracking password for: " + user
			testPass(cryptPass)
if __name__ == '__main__':
	main()
