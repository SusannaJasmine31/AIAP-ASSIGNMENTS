from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('TASK1.HTML')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')
    
    if username and password:
        print(f"Successful login - Username: {username}")
        return jsonify({'success': True, 'message': f'Welcome, {username}!'})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 400

if __name__ == '__main__':
    app.run(debug=True)
