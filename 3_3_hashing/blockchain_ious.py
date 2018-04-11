"""
Blockchain IOUs
Simple program demonstrating how a Blockchain can be used to keep track of IOUs.

Activity adapted from Javascript example by Simply Explained - Savjee:
    https://www.youtube.com/watch?v=zVqczFZr124
"""
__author__ = "Charlie Friend"

import hashlib


class Block:
    def __init__(self, ower, owes, amount):
        self.ower = ower
        self.owes = owes
        self.amount = amount

        # Leave the last block hash empty until you add to the blockchain
        self.lastblock_hash = ''

    def calculate_hash(self):
        message = ""
        message += self.ower
        message += self.owes
        message += str(self.amount)
        message += self.lastblock_hash

        return hashlib.sha256(message.encode()).hexdigest()

    def to_string(self):
        message = self.ower + " owes " + self.owes + " $" + str(self.amount)
        return message


def add_block(block, blockchain):
    """Adds a block to the blockchain list. Updates lastblock_hash."""
    last_block = blockchain[-1]
    block.lastblock_hash = last_block.calculate_hash()
    blockchain.append(block)


def print_blockchain(blockchain):
    """Prints all the IOUs in the blockchain."""
    for i in range(1, len(blockchain)):
        print(blockchain[i].to_string())


def check_blockchain(blockchain):
    """Checks that all entries in the blockchain haven't been tampered with!"""
    for i in range(1, len(blockchain)):
        block = blockchain[i]
        last_block = blockchain[i - 1]

        # Check that the last block's hash is the same as we recorded in this
        # block. If not, then the blockchain has been tampered with!
        if block.lastblock_hash != last_block.calculate_hash():
            return False

    return True


def main():
    # Create blockchain and add genesis block
    genesis = Block("", "", 0)
    blockchain = [genesis]

    # Add blocks to the blockchain
    add_block(Block("Charlie", "Katie", 25), blockchain)
    add_block(Block("Jim", "Charlie", 30),   blockchain)
    add_block(Block("Charlie", "Simon", 10), blockchain)

    print_blockchain(blockchain)
    print()

    # Check that the blockchain is valid
    is_chain_valid = check_blockchain(blockchain)
    print("Is this blockchain valid? " + str(is_chain_valid))
    print()

    # Try and mess with one of the blocks
    tampered_block = blockchain[2]
    tampered_block.amount = 1000000  # 1 million dollars!

    # Now re-print the blockchain and check it's valid
    print_blockchain(blockchain)
    print()
    is_chain_valid = check_blockchain(blockchain)
    print("Is this blockchain valid? " + str(is_chain_valid))


if __name__ == "__main__":
    main()
