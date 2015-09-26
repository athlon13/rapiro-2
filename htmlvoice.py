from bottle import route, run, template
import threading
import urllib 

counter = 0
rlock = threading.Lock()




@route('/reset/')
def reset():
    global rlock
    global r
    with rlock:
        r.reset()
    return template('{{counter}}', counter=counter)

@route('/cmd/<command>')
def cmd(command):
	global rlock
	with rlock:
		query = urllib.unquote(command).decode('utf8').replace('+', ' ')
		print "query=%s" % (query)
	return template('{ "command" : {{command}},  "status": "ok" }', command=command)

@route('/')
def index():
	return template('voice.tpl') 


@route('/<q>')
def index(q):
	print "query=%s" % (q)
        return template('voice.tpl')

run(host='0.0.0.0', port=8080)
