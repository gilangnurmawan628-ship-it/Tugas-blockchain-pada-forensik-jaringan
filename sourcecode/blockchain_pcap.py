import hashlib
import os

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()

pcap_files = [
    "evidence/PCAP01_NIM.pcap",
    "evidence/PCAP02_NIM.pcap",
    "evidence/PCAP03_NIM.pcap",
    "evidence/PCAP04_NIM.pcap",
    "evidence/PCAP05_NIM.pcap"
]

for file in pcap_files:
    if os.path.exists(file):
        print("Nama File :", file)
        print("Ukuran File :", os.path.getsize(file), "bytes")
        print("SHA-256 :", calculate_sha256(file))
        print("-" * 50)
