# Use flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
# Import math for mathematical operations
import math
#Import sympy to check for primes
from sympy import *

# Create the flask app
app = Flask(__name__)
# Create the API object
api = Api(app)

# Offer help if no method requested
class Hello(Resource):

	def get(self):

		return jsonify({'message': 'Use one of the following methods: square, factorial, prime, or charcount'})

# Calculate the square of a number

class Square(Resource):

	def get(self, num):

		return jsonify({'square': num**2})

# Calculate the factorial of a number

class Factorial(Resource):

	def get(self, num):

		return jsonify({'factorial': math.factorial(num)})

# Return true if a number is prime, otherwise false

class Prime(Resource):

	def get(self, num):

		return jsonify({'isprime': isprime(num)})

# Return the count of characters in a string

class Count(Resource):

    def get(self, input):

        return jsonify({'charcount': len(input)})

# Add endpoints
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')
api.add_resource(Count, '/count/<string:input>')
api.add_resource(Factorial, '/factorial/<int:num>')
api.add_resource(Prime, '/prime/<int:num>')

# Run on TCP/80
if __name__ == '__main__':

	app.run(host='0.0.0.0', port=80, debug = True)