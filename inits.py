class	taskInit:

	def		createArrayProcessName(self, dict):
		array = []
		ct = 1

		try:
			for nameProcess, info in dict.items():
				array.append(nameProcess)
				tmp = info.get("numprocs")
				if (tmp > 0):
					ct = 1
					while (ct < tmp):
						array.append(nameProcess + ":" + str(ct))
						ct += 1
		except:
			return
		return array

	def		createArrayProcessStatus(self, dict):
		array = []

		try:
			for nameProcess, info in dict.items():
				tmp = info.get("autostart")
				array.append(tmp)
				tmp2 = info.get("numprocs")
				if (tmp2 > 0):
					ct = 1
					while (ct < tmp2):
						array.append(tmp)
						ct += 1
		except:
			return
		return array