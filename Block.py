import hashlib as hsh

# Class representing an actual block
class Block:
    def __init__(self, index, dateTimeStamp, contents, actor, previousHash):
        self.index = index
        self.dateTimeStamp = dateTimeStamp
        self.contents = contents
        self.actor = actor
        self.previousHash = previousHash
        self.hash = self.generate_hash()
        
    def generate_hash(self):
        sha = hsh.sha256()
        hashedData = str(self.index) + str(self.dateTimeStamp) + str(self.contents) + str(self.actor) + str(self.previousHash)
        sha.update(hashedData.encode())
        return sha.hexdigest