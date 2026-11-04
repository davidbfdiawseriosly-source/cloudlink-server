import os
import cloudlink

# Render passes PORT as a string; convert it to an int
port = int(os.environ.get("PORT", 3000))

if __name__ == "__main__":
    print(f"Booting legacy CloudLink on 0.0.0.0:{port}...")
    
    # Explicitly call the cloudlink class INSIDE the cloudlink module
    cl = cloudlink.cloudlink(host="0.0.0.0", port=port)
