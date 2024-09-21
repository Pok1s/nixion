import pytest
from blockchain.blockchain import Blockchain

@pytest.fixture
def blockchain():
    """Fixture to create a new Blockchain instance for each test."""
    return Blockchain()

def test_create_block(blockchain):
    """Test the creation of a new block."""
    blockchain.new_block(proof=12345)
    
    assert len(blockchain.chain) == 2, "Blockchain should have 2 blocks after adding a new block"
    
    new_block = blockchain.chain[-1]
    assert new_block['proof'] == 12345, "The proof of the new block should be 12345"

def test_create_transaction(blockchain):
    """Test the creation of a new transaction."""
    blockchain.new_transaction(sender='A', recipient='B', amount=10)
    
    assert len(blockchain.current_transactions) == 1, "There should be 1 transaction in the list"
    
    transaction = blockchain.current_transactions[0]
    
    assert transaction['sender'] == 'A', "Sender should be 'A'"
    assert transaction['recipient'] == 'B', "Recipient should be 'B'"
    assert transaction['amount'] == 10, "Amount should be 10"

def test_blockchain_initialization(blockchain):
    """Test the initial state of the blockchain."""
    
    genesis_block = blockchain.chain[0]
    
    assert len(blockchain.chain) == 1, "Blockchain should start with 1 block"
    assert genesis_block['index'] == 1, "The genesis block index should be 1"
    assert genesis_block['previous_hash'] == '1', "The previous hash of the genesis block should be '1'"
    assert genesis_block['proof'] == 100, "The proof of the genesis block should be 100"

def test_transaction_not_added_to_chain(blockchain):
    """Test that transactions are not added to the blockchain but to the transaction list."""
    blockchain.new_transaction(sender='A', recipient='B', amount=10)
    blockchain.new_block(proof=12345)
    
    assert len(blockchain.current_transactions) == 0, "Transactions should be cleared after adding a new block"

def test_blockchain_hashing(blockchain):
    """Test the hashing of the blocks."""
    blockchain.new_block(proof=12345)
    previous_block = blockchain.chain[-2]
    current_block = blockchain.chain[-1]
    
    assert current_block['previous_hash'] == blockchain.hash(previous_block), "The previous hash of the current block should match the hash of the previous block"

def test_blockchain_integrity(blockchain):
    """Test the integrity of the blockchain."""
    blockchain.new_block(proof=12345)
    blockchain.new_transaction(sender='A', recipient='B', amount=10)
    blockchain.new_block(proof=67890)
    
    for i in range(1, len(blockchain.chain)):
        previous_block = blockchain.chain[i - 1]
        current_block = blockchain.chain[i]
        
        assert current_block['previous_hash'] == blockchain.hash(previous_block), "Block chain integrity compromised"

def test_duplicate_transactions(blockchain):
    """Test that duplicate transactions are handled correctly."""
    blockchain.new_transaction(sender='A', recipient='B', amount=10)
    blockchain.new_transaction(sender='A', recipient='B', amount=10)
    
    assert len(blockchain.current_transactions) == 2, "Duplicate transactions should be allowed for now (if logic supports it)"

if __name__ == '__main__':
    pytest.main()
