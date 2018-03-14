import datetime as dte
from Block.py import Block

# Class for interacting with the blockchain
class Blockchain:
    def __init__(self):
        self.blockchain = []
        self.blockchain.append(Block(0, dte.datetime.now(), "Genesis Block", "Admin", "0"))
        
    def nextBlock(self, content, actor):
        index = len(self.blockchain)
        block = Block(index, dte.datetime.now(), content, actor, self.blockchain[index - 1].hash)
        self.blockchain.append(block)
