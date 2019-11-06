import json
import yaml
import http.client as httplib
import urllib
import hashlib
from datetime import datetime, timedelta, date


config = yaml.load(open('../config.yaml'))

host = config['whmcs_host']
url = config['whmcs_api_url']
command = config['whmcs_api_command']
username = config['whmcs_api_username']
password = config['whmcs_api_password']

startdate = datetime.today() - timedelta(days=1)

today = date.today()
first_selling_date = date(2018, 8, 9)
delta = today - first_selling_date

values = {
  'username' : username,
  'password' : hashlib.md5(password.encode('utf-8')).hexdigest(),
  'action' : command,
  'responsetype' : 'json',
  'startdate' : startdate,
}

headers = {
  'User-Agent': 'python',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Access-Control-Allow-Credentials': 'true',
  'Access-Control-Max-Age': '86400',
}

values = urllib.parse.urlencode(values)

conn = httplib.HTTPSConnection(host)
conn.request("POST", url, values, headers)
response = conn.getresponse()
data = response.read()
json_data = json.loads(data)

days = (delta.days)
total_today = (json_data['total'][0][1])

with open(config['absolute_path']+config['csv_path'],'a') as f:
  f.write("\n")
  f.write(str(days)+","+str(total_today))