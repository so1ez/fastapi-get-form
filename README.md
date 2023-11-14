# fastapi-get-form
Web application for identifying form template

## In branch "v1.2/boytsov/release" there is a version of the application running 2 containers mongodb and app using docker-compose and dockerfile

## Usage
### Clone the project
```
git clone https://github.com/so1ez/fastapi-get-form.git
```
### Start a mongo Docker container
```
docker run -d -p 27017:27017 --name mongo_container mongo
```
If the mongodb image is not installed locally, it will be installed automatically
### Configure an app
in the project directory:
Create a virtual environment
```
python3 -m venv venv
```
Activate the virtual enviroment (Linux)
```
source venv/bin/activate
```
Install dependencies
```
python3 -m pip install -r requirements.txt
```
### Filling the mongodb database with test data
```
python3 src/database.py
```

We can see test data in the console
### Running the script with test requests
```
python3 -m pytest
```
In the console we can see the results of test requests
### Run the web application
Execute the command
```
uvicorn src.main:app --reload
```
Go to http://127.0.0.1:8000/docs and execute the necessary requests.
### Endpoints
1. post "/get_form" — main endpoint for defining a form template, returns the name of the most suitable form, if there is none, returns a list of typed fields
2. get "/db" — getting all documents of a working collection with mongodb test data