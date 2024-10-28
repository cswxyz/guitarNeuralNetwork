import os
from view.api import app

if __name__ == '__main__':
    # Set the port to Render's specified PORT environment variable or default to 8080
    port = int(os.environ.get("PORT", 8080))
    # Ensure the app binds to 0.0.0.0 for Render
    app.run(host="0.0.0.0", port=port, debug=True)
