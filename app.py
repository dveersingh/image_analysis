import os
import os
import uuid

from PIL import Image

from flask import Flask, request,render_template,flash, redirect

UPLOAD_FOLDER = './static/upload'

app = Flask(__name__,static_folder='static')
app.secret_key = "36567576vhvf667rgcgccc"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['.png', '.jpg', '.jpeg'])




@app.route('/')
def home():
	return render_template('home.html')

@app.route('/upload_image')
def upload_form():
	return render_template('index.html')
	
@app.route('/analyse_image')
def analyze():
	return render_template('analysis.html')




@app.route('/upload_image', methods=['GET', 'POST'])
def upload_img():

	if request.method == 'POST':
		if 'file1' not in request.files:
			#return 'there is no file1 in form!'
			flash('400 Bad Request looks like an other option.')
			return redirect(request.url)
		file1 = request.files['file1']
		
		if file1.filename == '':
			flash('415  No image selected for uploading')
			return redirect(request.url)
			
		filename, file_extension = os.path.splitext(file1.filename)
		#getting file extension
		if file_extension in ALLOWED_EXTENSIONS:
			unique_id = str(uuid.uuid4()) # genrating id
			path = os.path.join(app.config['UPLOAD_FOLDER'], unique_id+file_extension)
			file1.save(path) # saving file
			flash('Image successfully uploaded and id is :  ' + unique_id)
			#return unique_id
			return redirect(request.url)
		else:
			#return "error \n  only Image file allowed (.jpg, .png, .jpeg)"
			flash('Allowed image types are -> png, jpg, jpeg')
			return redirect(request.url)
	return render_template('index.html')
	
	
	
	
@app.route('/analyse_image', methods=['GET', 'POST'])
def analysis_file():
	if request.method == 'POST':
		id_ = request.form.get('unique_id')
		#getting the image id
		for i in ALLOWED_EXTENSIONS:
			if os.path.isfile(app.config['UPLOAD_FOLDER']+"/"+id_+i):
			
				#checking file is present or not
				im = Image.open(app.config['UPLOAD_FOLDER']+"/"+id_+i)	
				width, height = im.size
				#getting image height aand width using pillow
				#return {'width' : width, 'height' : height}
				flash("width : " + str(width) + " ,  "+ "height : " +"  "+ str(height))
				return redirect(request.url)
		
		flash("404 File does not exixt")
		return redirect(request.url)

	return render_template('analysis.html')
	
	
	
@app.route('/list_images', methods=['GET'])
def list_file():
	hists = os.listdir(app.config['UPLOAD_FOLDER'])
	#list all the files in directory
	return render_template('list.html', hists=hists)

if __name__ == '__main__':
    app.run(debug = True, port = 5000)