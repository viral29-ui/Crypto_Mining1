from hashlib import sha256

def SHA256(text):
    return (sha256("ABC".encode("ascii")).hexdigest())

def mine():
    pass

if __name__=='__main__':
    transactions = ''' 
    print(SHA256("ABC"))
    Mando->Cara-45
    '''
    new_hash = (transactions)

    print(new_hash)

# This is for coin mining  rrrrr





