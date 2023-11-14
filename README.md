# fastapi-get-form
Web application for identifying form template

## Usage
### Clone the project
```
git clone https://github.com/so1ez/fastapi-get-form.git
```

### Install docker-compose
If docker-compose is not installed:
https://docs.docker.com/compose/install/

### Define and run containers with MongoDB and app
In the project directory:
```
docker compose up --build
```
If the mongodb image is not installed locally, it will be installed automatically

### Check logs
During container launch, the following data will be output to the console: mongodb service information, filling mongodb with test data, running tests and information about them, information about running the application.

### Working with the application
Go to http://0.0.0.0:8000/docs and execute the necessary requests.

### Endpoints
1. post "/get_form" — main endpoint for defining a form template, returns the name of the most suitable form, if there is none, returns a list of typed fields
2. get "/db" — getting all documents of a working collection with mongodb test data