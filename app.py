import os
import subprocess
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Define the script folder path
SCRIPT_FOLDER = 'script'

# Function to get all folder paths inside the script folder
def get_folder_paths():
    folders = []
    for foldername in os.listdir(SCRIPT_FOLDER):
        folder_path = os.path.join(SCRIPT_FOLDER, foldername)
        if os.path.isdir(folder_path):
            folders.append(foldername)
    return folders

# Function to get all Python files in a selected folder
def get_files_in_folder(folder):
    folder_path = os.path.join(SCRIPT_FOLDER, folder)
    files = []
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith('.py'):
                files.append(filename)
    return files

# Route to render the index.html template
@app.route('/')
def index():
    folders = get_folder_paths()
    default_folder = 'msm'  # Set default folder to 'msm'
    files = get_files_in_folder(default_folder)  # Get files in the default folder
    return render_template('index.html', folders=folders, files=files, default_folder=default_folder)

# API endpoint to get Python files in a selected folder
@app.route('/files/<folder>')
def get_files(folder):
    files = get_files_in_folder(folder)
    return jsonify(files)

# API endpoint to run the selected script
@app.route('/run/<filename>', methods=['POST'])
def run_script(filename):
    folder = request.json.get('folder')
    file_path = os.path.join(SCRIPT_FOLDER, folder, filename)

    try:
        # Use subprocess to run the Python script and capture the output
        result = subprocess.run(['python', file_path], capture_output=True, text=True)

        # Check if the script ran successfully
        if result.returncode == 0:
            return jsonify({"status": "Pass", "result": result.stdout})
        else:
            return jsonify({"status": "Fail", "result": result.stderr})
    except Exception as e:
        return jsonify({"status": "Fail", "result": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
