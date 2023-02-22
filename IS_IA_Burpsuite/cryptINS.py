from cryptography.fernet import Fernet

key = b'MCpRKg7UzZQIFdvcEahMuiRcORF-FOwsHlHnSx4TAE0='
f = Fernet(key)

def encryption(s):
    return f.encrypt(s.encode()).decode()

def decryption(s):
    return f.decrypt(s)        