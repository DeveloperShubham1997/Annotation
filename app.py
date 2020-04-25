
#app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

import os
#import magic
import urllib.request
from app import app
from flask import Flask, flash, request, redirect, render_template
from jsonmerge import merge
import json
from werkzeug.utils import secure_filename




app = Flask(__name__)
app.secret_key = "secret key"


	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
		print("**************")
		print(os.getcwd())
        # check if the post request has the files part
		if 'files[]' not in request.files:
			flash('No file part')
			return redirect(request.url)
		files = request.files.getlist('files[]')
		os.chdir("json2")
		for file in files:
			file.save(secure_filename(file.filename))
			# print(file)
			# if(file and allowed_file(file.filename)):
			# 	filename = secure_filename(file.filename)
			# 	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		jsons=os.listdir()

		final_json={}
		for i in jsons:
			with open(i) as f:
				base = json.load(f)
			final_json=merge(final_json,base)
			with open("final.json","w") as outfile:
				json.dump(final_json,outfile)
		
		for i in jsons:
			if (i!="final.json"):
				os.remove(i)
		os.chdir("/home/shubham/FlaskIntroduction/")
		print("#############")
		print(os.getcwd())

		flash('File(s) successfully uploaded')
		return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
