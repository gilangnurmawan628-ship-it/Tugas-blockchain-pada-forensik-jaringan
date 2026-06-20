import hashlib
import json
from datetime import datetime

class Block:
    def __init__(self, index, timestamp, evidence_file,
                 packet_count, evidence_hash, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.evidence_file = evidence_file
        self.packet_count = packet_count
        self.evidence_hash = evidence_hash
        self.previous_hash = previous_hash
        self.block_hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "evidence_file": self.evidence_file,
            "packet_count": self.packet_count,
            "evidence_hash": self.evidence_hash,
            "previous_hash": self.previous_hash
        }

        return hashlib.sha256(
            json.dumps(block_data, sort_keys=True).encode()
        ).hexdigest()

# Genesis Block
blockchain = []

genesis = Block(
    0,
    str(datetime.now()),
    "Genesis",
    0,
    "0",
    "0"
)

blockchain.append(genesis)

# Contoh Evidence Block
for i in range(1, 6):
    previous_hash = blockchain[-1].block_hash

    block = Block(
        i,
        str(datetime.now()),
        f"PCAP0{i}.pcap",
        i * 20,
        hashlib.sha256(f"PCAP0{i}".encode()).hexdigest(),
        previous_hash
    )

    blockchain.append(block)



    return True

# Validasi blockchain
if validate_blockchain(blockchain):
    print("Blockchain Validation : VALID")
else:
    print("Blockchain Validation : INVALID")
