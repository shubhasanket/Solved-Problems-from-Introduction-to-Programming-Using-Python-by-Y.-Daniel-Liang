'''(Encrypt files) Encode the file by adding 5 to every byte in the file. Write a program
that prompts the user to enter an input filename and an output filename and
saves the encrypted version of the input file to the output file.
(Decrypt files) Suppose a file is encrypted using the scheme in Exercise 13.8.
Write a program to decode an encrypted file. Your program should prompt the
user to enter an input filename and an output filename and should save the unencrypted
version of the input file to the output file.
'''

import os.path

while True:
    fn = input("Enter file name: ")
    if os.path.isfile(fn):
        break
ofn = "Done.txt"   # output file name 
inf = open(fn, "r") # performing a read binary on the file
data = inf.read()
inf.close()

##print(data)
##print(data.decode())

b_arr = bytearray(data.encode()) # Returns a bytearray object

for i in range (len(b_arr)): # adding 5 to every byte
    b_arr[i] += 5
    
out_f = open(ofn, "w")
out_f.write(b_arr.decode())
out_f.close()
##print(b_arr.decode())

input("Please open the output file to check the encryption. Press enter to continue")

inf = open(ofn, "r") #reading from the encrypted file
b_arr = bytearray(inf.read().encode())
inf.close()

for i in range (len(b_arr)):
    b_arr[i] -= 5

out_f = open(ofn, "w")
out_f.write(b_arr.decode())
out_f.close()
    
##print(repr(b_arr.decode()))
