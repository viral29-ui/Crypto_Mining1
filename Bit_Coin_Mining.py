# Complete code for bitcoin mining
from hashlib import sha256 #using sha256 function generate hexadecimal
MAX_NONCE = 200000000000 # max nonce number depends on computation power
def SHA256(text): #2 This utility function supply the input test
    return sha256(text.encode("ascii")).hexdigest() #1 .hexdigest() get the actual hash out of it
# This is 64 bit for hexadecimal
def mine(block_number,transactions,previous_hash,prefix_zeros): #4 passing all parameters
    # Mine function will take transaction
    prefix_str = '0'*prefix_zeros # Generate first 4 digits numbers as it should be for hash function
    for nonce in range(MAX_NONCE): # for loop exhort computational budget that's why use here
        text = str(block_number) + transactions + previous_hash + str(nonce)
        # string as generated with str block number + transactions num + previous hash + string nonce string
        new_hash = SHA256(text) #6 generated new hash
        if new_hash.startswith(prefix_str): # if condition given for new hash when prefix
            print(f"Yes, BC mining has successfully with nonce value:{nonce}") # Final step after generate
            return new_hash # when if condition done then return new hash

    raise BaseException(f"Unable to do mining due to expense for {MAX_NONCE} times")
        # The raise is exception function when computation budget has over

if __name__=='__main__': # main python entry point with given if condition
    transactions = ''' Robi-> Rony->20 & Ryad-> Ripon->45 ''' # In oder to mining create transaction among ppl
    difficulty = 5 #5 difficulty level in front of hash that take long time
    import time # Importing library
    start = time.time() # use time.time() function provide current time
    print("Start mining")
    new_hash = mine(6,transactions,'0000000xa126944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
    #4 fist is block number, then mining function giving transactions, previous hash, passing difficulty level
    total_time = str((time.time() - start)) # (current time - start time) that generate execution as result
    print(f"End mining, Mining took:{total_time} seconds") # result of total execution times..
    print(new_hash)

"""
Take Note: BC mining like play an online game as you get certain reward. Mining coin can earn but difficulty level
if high then it took one year to mine bit coin. It require special hardware for mining. Those machine guessing faster
if some machine powerful to guess as faster and lucky then he can win. Even after 2 minutes if someone trying to guess.
Whoever have chance first in guessing such game he can win that bit coin. Since difficulty level is increasing that's 
why mining bit coin is challenging & time consuming even for high value machine.
"""
