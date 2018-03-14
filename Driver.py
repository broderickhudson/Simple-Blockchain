from Blockchain.py import Blockchain

# Driver
def Main():
    blockchain = Blockchain()
    actor = "Brody"
    for i in range(100):
        blockchain.nextBlock("This is block #" + str(i+1), actor)
    for i in range(100):
        print(blockchain.blockchain[i].contents)
        
Main()