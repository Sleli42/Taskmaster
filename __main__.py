#!/usr/bin/env Python

import cmd
import sys
import logging
import inits
import displays
from tools import exit_msg, open_config_file

class	line_edit(cmd.Cmd):

	prompt = '[py]$: ';

	data = open_config_file(sys.argv[1:]);
	tmp = data.get("programs");
	process = {}

	init = inits.taskInit()
	display = displays.displaysFct()
	process["name"] = init.createArrayProcessName(tmp)
	process["status"] = init.createArrayProcessStatus(tmp)
	display.displayData(process)
	def emptyline(self):
		pass
	def do_infos(self, line):
		self.display.displayInfos(line, self.tmp)
	def	do_EOF(self, line):
		exit_msg();
		return (True);
	def	do_exit(self, line):
		exit_msg();
		return (True);
	def	do_quit(self, line):
		exit_msg();
		return (True);


if __name__ == '__main__':
	# fileConfig = "config.yaml"
	if len(sys.argv) < 2:
		print "Please add: 'config.yaml' file"
	else:	
		if sys.argv[1] and sys.argv[1].endswith(".yaml") == True:
			line_edit().cmdloop()
		else:
			logging.warning('ERROR\nCheck if ur config file is avalaible')