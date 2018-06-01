
# Name: urllooper.py
# Description: Code snippet that makes HTTP/HTTPS url requests in a loop and
# allows you to process the data received and change URL parameters before
# the next url request.
# Author: Michael Miranda, 2018/05/31

import urllib.request
url='http://www.spartix.com'

for i in range(0,3):
	res = urllib.request.urlopen(url)
	data = res.read() # can also limit by bytes using res.read(10) to read first 10 bytes
	# insert code to process the data received

	# if a certain condition is met, you can also change the url for the next request	
	#if i == 1:
	#	url='https://www.google.com'	
	print(data)
	# or do something else with the data
