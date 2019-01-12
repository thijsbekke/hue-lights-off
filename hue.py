import logging
import json

try:
	import requests
except:
	import urequests as requests


class Bridge:
	def __init__(self, ip, username):
		self.username = username
		self.ip = ip

	def uri(self, path):
		return 'http://{}/api/{}/{}'.format(self.ip, self.username, path)

	def get(self, path):
		uri = self.uri(path)
		logging.debug("GET " + uri)
		response = requests.get(uri).json()
		logging.debug("Response: ".response)

		return response

	def put(self, path, data):
		uri = self.uri(path)
		logging.debug("PUT " + uri)
		data = json.dumps(data)
		logging.debug("Data " + data)
		response = requests.put(uri, data=data).json()
		logging.debug("Response " + str(response))

		return response
