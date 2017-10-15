import configparser

Config = configparser.ConfigParser()

Config.read("config.ini")

print(Config.sections())

def ConfigSectionMap(section):
	dict1 = {}
	options = Config.options(section)
	for option in options:
		try:
			dict1[option] = Config.get(section, option)
			if dict1[option] == -1:
				DebugPrint("skip: %s" % option)
		except:
			print("exception on %s!" % option)
			dict1[option] = None
	return dict1

Name = ConfigSectionMap("SectionOne")['name']
Age = ConfigSectionMap("SectionOne")['age']
print ("Hello %s. You are %s years old." % (Name, Age))

port = Config.get("Settings", "Port")
print (port)