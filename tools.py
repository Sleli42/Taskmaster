import sys
import yaml
from colors import red, green, purple, light_purple

def open_config_file(argv):
	config = open(sys.argv[1], 'r')
	data = yaml.load(config)
	config.close()
	return data


def	exit_msg():
	red("Program closing..")
	light_purple("\t\t..See u soon")
	return True