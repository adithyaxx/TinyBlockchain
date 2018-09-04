from blockchain import Blockchain

def main():
    b = Blockchain()

    for i in range(0, 15):
        print("Block #%s added to the blockchain: %s" % (str(i), b.blocks[i].hash))
        b.mine(parent_block=b.get_current_block())

main()
