from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

# Route to render the Blockly interface
@app.route('/')
def index():
    return render_template('index.html')

# Route to execute the generated Python code
@app.route('/run_code', methods=['POST'])
def run_code():
    code = request.json.get('code')
    try:
        # Use subprocess to safely execute the code
        result = subprocess.run(
            ['python3', '-c', code], capture_output=True, text=True, check=True
        )
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = e.stderr

    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True)
