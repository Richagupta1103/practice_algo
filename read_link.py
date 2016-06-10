import json, urllib, datetime
data = urllib.urlopen("https://api.github.com/search/issues?q=repo:Shippable/support+state:open&per_page=100").read()
output = json.loads(data)
print "Total number of open issues", output['total_count']
utc_datetime = datetime.datetime.utcnow()
last_24hr = utc_datetime-datetime.timedelta(days=1)
last_24hr = last_24hr.strftime("%Y-%m-%dT%H:%M:%S")
data = urllib.urlopen("https://api.github.com/search/issues?q=repo:Shippable/support+created:>"+last_24hr+"+state:open&per_page=100").read()
output = json.loads(data)
print "Number of open issues that were opened in the last 24 hours", output['total_count']
last_7days = utc_datetime-datetime.timedelta(days=7)
last_7days = last_7days.strftime("%Y-%m-%dT%H:%M:%S")
data = urllib.urlopen("https://api.github.com/search/issues?q=repo:Shippable/support+created:"+last_7days+".."+last_24hr+"+state:open&per_page=100").read()
output = json.loads(data)
print "Number of open issues that were opened more than 24 hours ago but less than 7 days ago", output['total_count']
data = urllib.urlopen("https://api.github.com/search/issues?q=repo:Shippable/support+created:<"+last_7days+"+state:open&per_page=100").read()
output = json.loads(data)
print "Number of open issues that were opened more than 7 days ago", output['total_count']
