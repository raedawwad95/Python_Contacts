from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

 #This class will handle any incoming request from
 #the browser 

class myHandler(BaseHTTPRequestHandler):
	#This will handle GET requests
	def do_GET(self):
		# Add the outgoing status here
		
		# You will need to change this if you are sending something
  		# other than plain text, like JSON or HTML.
		self.send_header('Content-type','text/html')
		self.end_headers()

		# Send the "Hello World" message here 
		
		return
