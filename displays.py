import inits, displays

class	displaysFct:

	def		displayStatus(self, status):
		if status == True:
			return "\033[36mRUNNING\033[39m"
		elif status == False:
			return "WAITING"
		else:
			return "\033[31mSTOPPED\033[39m"

	def		displayData(self, cmd, allProcess):
		process = {}
		init = inits.taskInit()
		process["name"] = init.createArrayProcessName(allProcess)
		process["status"] = init.createArrayProcessStatus(allProcess)
		if cmd:
			ct = 0
			while (ct < len(process["name"])):
				if process["name"][ct] == cmd:
					print ("  " + str(process["name"][ct]) + "\t\t\t" \
								+ self.displayStatus(process["status"][ct]))
				ct += 1;
		else:
			ct = 0
			while (ct < len(process["name"])):
				print ("  " + str(process["name"][ct]) + "\t\t\t" \
							+ self.displayStatus(process["status"][ct]))
				ct += 1;

	def		displayValueData(self, value, value2display):
		tmp = value.get(value2display)
		if (tmp):
			if (value2display == "umask" or value2display == "cmd"
				 or value2display == "env"):
				print ("  " + value2display + '\t\t\t' + str(tmp))
			else:
				print ("  " + value2display + '\t\t' + str(tmp))

	def		displayAllDatas(self, cmd, value):
		array = []

		for name, other in value.items():
			array.append(str(name))

		print ("\t\t" + cmd + " datas:")
		print ("  \033[32m-------------------------------------------\033[39m")
		ct = 0
		while ct < len(array):
			self.displayValueData(value, array[ct])
			ct += 1
		print ("  \033[32m-------------------------------------------\033[39m")

	def		displayInfos(self, cmd, config):
		if (cmd):
			for key, value in config.items():
				stop = True;
				if key == str(cmd):
					self.displayAllDatas(cmd, value)
					break ;
				else:
					stop = False
			if stop == False:
				print "Bad process name: [ " + str(cmd) + " ]"
		else:
			print "\033[31mUsage\033[39m: infos [name]\n\t-> infos need process name"