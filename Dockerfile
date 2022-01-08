FROM python:3.9-slim-bullseye
RUN  pip install flask
RUN pip install pillow
ADD . app
WORKDIR /app
#RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]