import hashlib as hsh
import datetime as dte

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

# Class for interacting with the blockchain
class Blockchain:
    def __init__(self):
        self.blockchain = []
        self.blockchain.append(Block(0, dte.datetime.now(), "Genesis Block", "Admin", "0"))
        
    def nextBlock(self, content, actor):
        index = len(self.blockchain)
        block = Block(index, dte.datetime.now(), content, actor, self.blockchain[index - 1].hash)
        self.blockchain.append(block)

# Driver
def Main():
    blockchain = Blockchain()
    actor = "Brody"
    for i in range(100):
        blockchain.nextBlock("This is block #" + str(i+1), actor)
    for i in range(100):
        print(blockchain.blockchain[i].contents)
        
Main()