import hue
import yaml
import logging

class App:
	def __init__(self):
		with open("settings.yml", 'r') as ymlfile:
			settings = yaml.load(ymlfile)

			logging.debug(settings)

			self.bridge = hue.Bridge(settings['hue']['ip'], settings['hue']['username'])
			self.group = settings['hue']['light']

	def run(self):
		self.bridge.put('groups/{}/'.format(str(self.group)), {"stream": {"active": False}})
		self.bridge.put('groups/{}/action'.format(str(self.group)), {"on": False})

logging.basicConfig(level=logging.DEBUG)

light = App()
light.run()
