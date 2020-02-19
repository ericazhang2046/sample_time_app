from flask import Flask
app = Flask(__name__)


@app.route('/time')
import datetime
 
currentDT = datetime.datetime.now()
 
print (currentDT.strftime("%Y-%m-%d %H:%M:%S"))
print (currentDT.strftime("%Y/%m/%d"))
print (currentDT.strftime("%H:%M:%S"))
print (currentDT.strftime("%I:%M:%S %p"))
print (currentDT.strftime("%a, %b %d, %Y"))


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
