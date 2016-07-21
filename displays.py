class	displaysFct:

	def		displayStatus(self, status):
		if status == True:
			return "\033[36mRUNNING\033[39m"
		elif status == False:
			return "WAITING"
		else:
			return "\033[31mSTOPPED\033[39m"

	def		displayData(self, process):
		print "processName\t\tprocessStatus\n"
		ct = 0
		while (ct < len(process["name"])):
			print str(process["name"][ct]) + "\t\t\t" \
						+ self.displayStatus(process["status"][ct])
			ct += 1;

	def		displayAllDatas(self, cmd, value):
		print ("\t\t" + cmd + " datas:")
		print ("  \033[32m-------------------------------------------\033[39m")
		print (  "  Cmd:\t\t\t" + value.get("cmd"))
		tmp = value.get("numprocs")
		if (tmp):
			print (  "  nbProcess:\t\t" + str(tmp))
		tmp = value.get("unmask")
		if (tmp):
			print (  "  Unmask:\t\t" + str(tmp))
		tmp = value.get("workingdir")
		if (tmp):
			print (  "  Working directory:\t" + str(tmp))
		tmp = value.get("autostart")
		if (tmp):
			print (  "  AutoStart:\t\t" + str(tmp))
		tmp = value.get("autorestart")
		if (tmp):
			print (  "  AutoRestart:\t\t" + str(tmp))
		tmp = value.get("exitcodes")
		if (tmp):
			print (  "  ExitCodes:\t\t" + str(tmp))
		tmp = value.get("startretries")
		if (tmp):
			print (  "  StartRetries:\t\t" + str(tmp))
		tmp = value.get("starttime")
		if (tmp):
			print (  "  StartTime:\t\t" + str(tmp))
		tmp = value.get("stopsignal")
		if (tmp):
			print (  "  StopSignal:\t\t" + str(tmp))
		tmp = value.get("stoptime")
		if (tmp):
			print (  "  StopTime:\t\t" + str(tmp))
		tmp = value.get("stdout")
		if (tmp):
			print (  "  Stdout:\t\t" + str(tmp))
		tmp = value.get("stderr")
		if (tmp):
			print (  "  Stderr:\t\t" + str(tmp))
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