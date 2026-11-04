import os
from cloudlink import CloudLink

# Render passes PORT as a string; convert it to an int
port = int(os.environ.get("PORT", 3000))

if __name__ == "__main__":
    print(f"Booting legacy CloudLink on 0.0.0.0:{port}...")
    
    # Capitalized CloudLink class initialization for version 0.1.x
    cl = CloudLink(host="0.0.0.0", port=port)
