# Caeser Cipher
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text= input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def encrypt (original_txt, shift_amount):
    cipher_txt = ""
    for letter in original_txt:
       shifted_pos =  alphabets.index(letter) + shift_amount

       if shifted_pos > 25:
           shifted_pos = shifted_pos - 26
       elif shifted_pos < 0:
           shifted_pos = shifted_pos + 26
           
       cipher_txt += alphabets[shifted_pos]

    print ("Here is the encoded result : ", cipher_txt)

def decrypt (original_txt, shift_amount):
    cipher_txt = ""
    for letter in original_txt:
       shifted_pos =  alphabets.index(letter) - shift_amount

       if shifted_pos > 25:
           shifted_pos = shifted_pos - 26
       elif shifted_pos < 0:
           shifted_pos = shifted_pos + 26
       cipher_txt += alphabets[shifted_pos]

    print ("Here is the decoded result : ", cipher_txt)

if direction == "encode":
    encrypt (text, shift)
elif direction == "decode":
    decrypt (text, shift)   
else:
    print("Please enter a valid input")
