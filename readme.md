# Python Flask Code-along demo API

## (Optional for testing on Windows) Create and activate virtual environment

mkdir venv
python -m venv venv
.\venv\Scripts\activate.ps1

## Install requirements

pip3 install -r requirements.txt

## Run app

python app.py

## Usage

### Find factorial of an integer
c
curl http://127.0.0.1:5000/factorial/10

### Square an integer

curl http://127.0.0.1:5000/square/8

### Count the number of characters in a string

curl http://127.0.0.1:5000/count/12345678

### Check whether a number is prime (true/false)

curl http://127.0.0.1:5000/prime/2027