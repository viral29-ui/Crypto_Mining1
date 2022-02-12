from hashlib import sha256
# print (sha256("ABC".encode("ascii")).hexdigest())
def SHA256(text): #2 This utility function supply the input test
    return (sha256("ABC".encode("ascii")).hexdigest()) #1 .hexdigest() get the actual hash out of it
# This is 64 bit for hexadecimel
def mine(block_number,transactions,previous_hash,prefix_zeros): #4 passing all parameters
    # Mine function will take transaction
    nonce = 2
    text = str(block_number) + transactions + previous_hash + str(nonce)
    # string as generated , str block number + transactions num + previous hash + string nonce string
    new_hash = SHA256(text) # generated new hash
    return new_hash

if __name__=='__main__':
    transactions = '''  #3 Demi transaction
    print(SHA256("ABC"))
    Dhaval->Bhavin->20,
    Mando->Cara-45
    '''
    difficulty = 4 #5 difficulty level in front of hash
    new_hash = mine(5,transactions,'b5d4045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78', difficulty)
    #4 fist is block number, then mining function giving transactions, previous hash, passing difficulty level
    print(new_hash)




