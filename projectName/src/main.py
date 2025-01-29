import datetime
f = open("/workspace/version-control/projectName/output/version.md", "w")
f.write(str(datetime.datetime.today()))
f.close()