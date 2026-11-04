import os
from cloudlink import CloudLink

# Render provides a dynamic PORT environment variable
port = int(os.environ.get("PORT", 3000))

cl = CloudLink()

if __name__ == "__main__":
    # Start the Cloudlink server on 0.0.0.0 and the assigned port
    cl.run(host="0.0.0.0", port=port)
