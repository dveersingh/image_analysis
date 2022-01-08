## With Docker

        docker build --tag flask_app .

        docker run --name flask-app -p 5000:5000 flask-app


## Without Docker
    
#### There are 2 requirements to run this flask app : flask and pillow

        pip install flask , pillow
        
        
#### To run the app without docker : 


          python app.py

### uploaded images will store in static/upload.

App will run on port 5000.
 ### Links 
http://localhost:5000/

http://localhost:5000/upload_image

http://localhost:5000//analyse_image'

http://localhost:5000/list_images
