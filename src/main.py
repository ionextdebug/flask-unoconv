from flask import Flask
from flask import render_template
from flask import request
import os
import uuid

app = Flask(__name__,
            static_url_path='/static', 
            static_folder='static',
            template_folder='templates')

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/upload', methods = ['POST'])   
def upload():   
    if request.method == 'POST':   
        f = request.files['file']
        uuid_filename = f"{uuid.uuid1()}_{f.filename}"
        f.save(uuid_filename)
        os.system(f"unoconv -f pdf {uuid_filename}")
        return "Success!"
  
if __name__ == '__main__':   
    app.run(debug=True)
