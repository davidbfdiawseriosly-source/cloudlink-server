import os
from cloudlink import cloudlink

# Render passes PORT as a string; convert it to an int
port = int(os.environ.get("PORT", 3000))

if __name__ == "__main__":
    print(f"Booting legacy CloudLink on 0.0.0.0:{port}...")
    
    # In 0.1.x, you pass host and port directly to the main class instantiation
    cl = cloudlink(host="0.0.0.0", port=port)
