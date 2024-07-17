# Install pycryptodome from the terminal 
# pip install pycryptodome

# Next step is to import DES3 for Encryption and md5 for key
from Crypto.Cipher import DES3
from hashlib import md5

# For selecting operation from given choice(Encryption or Decryption)
while True:
    print('Choose the operation you want to perform:\n\t Select 1- forEncryption\n\t Select 2- forDecryption')
    operation = input('Your Choice: ')
    if operation not in ['1', '2']:
        break
        
    # Image / File Path to perform the operation
    file_path = input('File path: ')
    
    # Key for performing Triple DES algorithm
    key = input('TDES key: ')

    # This encodes any given key to 16 byte ascii key with the md5 operation
    key_hash = md5(key.encode('ascii')).digest()

    # Adjust key parity of generated Hash Key for Final Triple DES Key
    tdes_key = DES3.adjust_key_parity(key_hash)
    
    #  Cipher with integration of Triple DES key, MODE_EAX for Confidentiality & Authentication
    #  and nonce for generating random / pseudo random number which is used for authentication protocol
    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')

    # Open & read file from given path
    with open(file_path, 'rb') as input_file:
        file_bytes = input_file.read()
        
        if operation == '1':
            # Perform Encryption operation
            new_file_bytes = cipher.encrypt(file_bytes)
        else:
            # Perform Decryption operation
            new_file_bytes = cipher.decrypt(file_bytes)
    
    # Write updated values in file from given path
    with open(file_path, 'wb') as output_file:
        output_file.write(new_file_bytes)
        print('Operation Done!')
        break
        
# Code Complete!