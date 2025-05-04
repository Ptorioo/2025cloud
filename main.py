from flask import Flask, request, jsonify

app = Flask(__name__)

# Root route
@app.route('/')
def home():
    return "Welcome to the Flask server!"

# Example GET route
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify({'message': f'Hello, {name}!'})

# Example POST route
@app.route('/api/data', methods=['POST'])
def handle_data():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No JSON payload received'}), 400
    # Process data here
    return jsonify({'received': data})

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
