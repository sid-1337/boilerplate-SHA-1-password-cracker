import hashlib

def crack_sha1_hash(hash, use_salts = False):
    if not use_salts :
        with open("top-10000-passwords.txt",'r') as f:
            line = f.readline()
            while line != '':
                if hashlib.sha1(line.encode()).hexdigest() == hash:
                    f.close()
                    return line
            return "PASSWORD NOT IN DATABASE"
    else:
        with open("known-salts.txt",'r') as salts:
            salt = salts.readline()
            while salt != '':
                with open("top-10000-passwords.txt",'r') as f:
                    line = f.readline()
                    while line != '':
                        if hashlib.sha1(line.encode(),salt=salt.encode()).hexdigest() == hash:
                            f.close()
                            salts.close()
                            return line
                    f.close()
            return "PASSWORD NOT IN DATABASE"
                

                
    return True