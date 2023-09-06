import hashlib

# Define four strings
data = ["A", "B", "C", "D"]

# Function to calculate the hash of a string using SHA-256
def calculate_hash(string):
    sha256 = hashlib.sha256()
    sha256.update(string.encode("utf-8"))
    return sha256.hexdigest()

# Calculate hashes for the data
hashes = [calculate_hash(string) for string in data]

# Function to build a Merkle tree from a list of hashes
def build_merkle_tree(hashes):
    if len(hashes) == 1:
        return hashes[0]

    # Ensure the number of hashes is even
    if len(hashes) % 2 != 0:
        hashes.append(hashes[-1])

    # Create a list to store intermediate Merkle tree levels
    level = []

    # Pair and hash adjacent hashes
    for i in range(0, len(hashes), 2):
        combined = hashes[i] + hashes[i + 1]
        level.append(calculate_hash(combined))

    # Recursively build the next level of the tree
    return build_merkle_tree(level)

# Build the Merkle tree
merkle_root = build_merkle_tree(hashes)

# Print the hashes and Merkle root
print("Hashes:")
for i, string in enumerate(data):
    print(f"{string}: {hashes[i]}")

print("\nMerkle Root:")
print(merkle_root)