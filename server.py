import os
import cloudlink

# Render passes PORT as a string; convert it to an int
port = int(os.environ.get("PORT", 3000))

if __name__ == "__main__":
    print(f"Booting legacy CloudLink on 0.0.0.0:{port}...")
    
    # In v0.1.x, call cloudlink directly from the import using lowercase
    cl = cloudlink.cloudlink(host="0.0.0.0", port=port)
