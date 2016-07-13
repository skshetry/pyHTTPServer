#!/usr/bin/env python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json,logging,os,sys

address="127.0.0.3"
PORT = 7777
class serverhandler(BaseHTTPRequestHandler):
	#This handles any requests that the server receives
	
	#GET req handler
	def do_GET(self):
		logging.warning("**GETting started**") 
		logging.warning(self.headers)
		self.send_response(200)
		#200 is OK
		#Response for successful HTTP requests
		#link:https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
		self.send_header("Content-type","application/json")
		self.end_headers()
		self.wfile.write("<html><body>GET Done</body></html>")
	def do_POST(self):
		logging.warning("**POSTing**")
		self.send_response(200)
		self.request.sendall(json.dumps({'path':self.path}))
		self.send_header("Content-type","application/json")
		self.end_headers()
		
		self.wfile.write("<html><body>POST Done</body></html>")
		
def runserver():
	try:
		print('http server is starting...')
		server_address = (address,PORT)
		httpd = HTTPServer(server_address,"S")
		logging.warning("**HTTP server starting**")
		print('http server is running...listening on port 127.0.0.3:7777' )
		httpd.serve_forever()
	except KeyboardInterrupt:
		httpd.server_close()

runserver()

    
