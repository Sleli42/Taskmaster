#!/usr/bin/env Python

import cmd
import sys
import logging, inits, displays, start_proc
from tools import exit_msg, open_config_file

class	line_edit(cmd.Cmd):

	prompt = '[py]$: ';

	data = open_config_file(sys.argv[1:]);
	tmp = data.get("programs");
	# process = {}

	# init = inits.taskInit()
	display = displays.displaysFct()
	start = start_proc.start()
	# process["name"] = init.createArrayProcessName(tmp)
	# process["status"] = init.createArrayProcessStatus(tmp)
	display.displayData("", tmp)
	def emptyline(self):
		pass
	def	do_start(self, line):
		self.start.startFct(line, self.tmp)
	def	do_status(self, line):
		self.display.displayData(line, self.tmp)
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