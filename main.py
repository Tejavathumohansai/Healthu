"""
A simple Blockchain using in  Python to protect the data
"""

import hashlib

class GeekCoinBlock:
    
    def __init__(self, previous_block_hash, transaction_list):

        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{transaction_list} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
 
def generateblockchain(blockc,f1):
    block1 = GeekCoinBlock(blockc,f1)
    datas=block1.block_data
    haskey=block1.block_hash
    print(f"Block 1 data: {block1.block_data}")
    print(f"Block 1 hash: {block1.block_hash}")
    return datas,haskey

    


    