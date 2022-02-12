# Complete code for bitcoin mining
from hashlib import sha256
MAX_NONCE = 100000000000
# print (sha256("ABC".encode("ascii")).hexdigest())
def SHA256(text): #2 This utility function supply the input test
    return sha256(text.encode("ascii")).hexdigest() #1 .hexdigest() get the actual hash out of it
# This is 64 bit for hexadecimel
def mine(block_number,transactions,previous_hash,prefix_zeros): #4 passing all parameters
    # Mine function will take transaction
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE): # for loop exhort computational budget
        text = str(block_number) + transactions + previous_hash + str(nonce)
        # string as generated , str block number + transactions num + previous hash + string nonce string
        new_hash = SHA256(text) #6 generated new hash
        if new_hash.startswith(prefix_str):
            print(f"Yes, BC mining has successfully with nonce value:{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")


if __name__=='__main__':
    transactions = '''  
    Dhaval->Bhavin->20,
    Mando->Cara->45
    '''
    difficulty = 4 #5 difficulty level in front of hash
    import time
    start = time.time()
    print("Start mining")
    new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
    #4 fist is block number, then mining function giving transactions, previous hash, passing difficulty level
    total_time = str((time.time() - start))
    print(f"End mining, Mining took:{total_time} seconds")
    print(new_hash)




