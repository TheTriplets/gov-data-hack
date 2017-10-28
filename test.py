import requests
import json
my_key = '579b464db66ec23bdd0000012b367a2e4b1a4eea709b1fe67a4f1d10'
api = 'https://api.data.gov.in/resource/027a444f-3392-4c63-997e-39c8aaf2f6e3'
param = {"format" : "json", "api-key" : my_key}

res = requests.get(api, params = param)
print(res.status_code)
my_dict = json.loads(res.text)

for k, v in my_dict.items():
	if (k == 'records'):
		my_list = v

state_list = []
year_list = [2009, 2010, 2011, 2012, 2013, 2014, 2015] #x-axix

data_2009 = []
data_2010 = []
data_2011 = []
data_2012 = []
data_2013 = []
data_2014 = []
data_2015 = []

data_list = [data_2009, data_2010, data_2011, data_2012, data_2013, data_2014, data_2015]

for data in my_list:
	for (k, v) in data.items():
		if (k == 'states_uts'):
			state_list.append(v)
		
fun =()
for year in year_list:
	for record in my_list:
		for(k, v) in record.items():
			if (k == '_'+str(year)):
				if(year == 2009):
					data_2009.append(v)
				elif (year == 2010):
					data_2010.append(v)
				elif(year == 2011):
					data_2011.append(v)
				elif(year == 2012):
					data_2012.append(v)
				elif (year == 2013):
					data_2013.append(v)
				elif(year == 2014):
					data_2014.append(v)
				else:
					data_2015.append(v)