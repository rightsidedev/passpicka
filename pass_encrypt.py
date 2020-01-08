'''
Written by Mandy Kopelke for CSB2019 Assignment 1

Function to encrypt a password
INPUT: 
    1
OUTPUT:
    1
'''
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto import Random

def encrypt_pass(password):
    key = get_random_bytes(16)
    iv = Random.new().read(AES.block_size)
    data = 'b"'
    data += password
    data += '"'
    print(f'key is: {key} ||| data is: {data}')
    cipher = AES.new(key, AES.MODE_CFB, iv)
    
    ct_bytes = cipher.encrypt(data)
    iv = b64encode(iv).decode('utf-8')
    ct_bytes = b64encode(ct_bytes).decode('utf-8')
    result = json.dumps({'iv':iv, 'ciphertext':ct_bytes})
    # print(f'cipher is: {cipher}')
    # msg = iv + cipher.encrypt(b'Attack at dawn')
    return(result)

def decrypt_pass("dU/CvzIEuwxISS+ylkTJ+A==","):
    key = get_random_bytes(16)
    iv = Random.new().read(AES.block_size)
    data = 'b"'
    data += password
    data += '"'
    print(f'key is: {key} ||| data is: {data}')
    cipher = AES.new(key, AES.MODE_CFB, iv)
    
    ct_bytes = cipher.encrypt(data)
    iv = b64encode(iv).decode('utf-8')
    ct_bytes = b64encode(ct_bytes).decode('utf-8')
    result = json.dumps({'iv':iv, 'ciphertext':ct_bytes})
    # print(f'cipher is: {cipher}')
    # msg = iv + cipher.encrypt(b'Attack at dawn')
    return(result)









outpass = encrypt_pass("testpassword")
print(f'key and encryted text: {outpass}')

"""
data = b"secret"
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CFB)
ct_bytes = cipher.encrypt(data)
iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')
result = json.dumps({'iv':iv, 'ciphertext':ct})
print(result)
"""