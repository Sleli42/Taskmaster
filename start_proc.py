import time, shlex, subprocess
import displays

class	start:

	def		startProcess(self, processName, processData):
		# print processData["cmd"]
		splitProcess = shlex.split(processData["cmd"])
		tmpEnv = processData.get("env")
		if tmpEnv is not None:
			goodEnv = tmpEnv
		else:
			goodEnv = None
		sub = subprocess.Popen(			# exec ls -Rl /
			splitProcess,
			cwd = processData["workingdir"],
			stdin = subprocess.PIPE,
			stdout = None,
			stderr = None,
			env = goodEnv)
		sub.kill()						# kill ls -Rl /
		tmp = processData.get("autostart")
		if tmp is not None:
			processData["autostart"] = True

	def		startFct(self, processName, process):
		display = displays.displaysFct()
		if processName:
			for key, value in process.items():
				if key == processName:
					# print "key == " + key
					self.startProcess(processName, value)
					display.displayData(processName, process)
					# print "go to start " + processName
		else:
			print "\033[31mUsage\033[39m: start [name]\n\t-> start need process name"




			# cmd_split = shlex.split(self.path)
			# 	proc = subprocess.Popen(
			# 		cmd_split,
			# 		cwd = self.workingdir,
			# 		stdin = subprocess.PIPE,
			# 		stdout = self.fdout,
			# 		stderr = self.fderr,
			# 		env = self.env
			# 	)
			# 	self.status = "STARTING"
			# 	self.stop_timer = -1
			# 	self.start_timer = 0
			# 	self.process = proc
			# 	self.time = time.time()