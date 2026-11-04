import os
from cloudlink import cloudlink

# Render passes PORT as a string; it must be converted to an int
port = int(os.environ.get("PORT", 3000))

if __name__ == "__main__":
    # 1. Instantiate the parent cloudlink object (lowercase class name)
    cl = cloudlink() 
    
    # 2. Initialize the server module
    server = cl.server(logs=True) 
    
    print(f"Booting CloudLink on 0.0.0.0:{port}...")
    
    # 3. Use 'ip' instead of 'host' to match CloudLink 0.2.x requirements
    server.run(ip="0.0.0.0", port=port)
