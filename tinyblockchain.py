import datetime as date
import hashlib as hasher


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) +
                    str(self.timestamp) +
                    str(self.data) +
                    str(self.previous_hash)).encode())
        return sha.hexdigest()


def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "This is block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


blockchain = [create_genesis_block()]
previous_block = blockchain[0]
num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
    next_block_to_add = next_block(previous_block)
    blockchain.append(next_block_to_add)
    previous_block = next_block_to_add
    print("Block #{} has been added to the blockchain at {}!".format(next_block_to_add.index, next_block_to_add.timestamp))
    print("Hash: {}\n".format(next_block_to_add.hash))
