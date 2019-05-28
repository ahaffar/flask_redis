from flask import Flask, render_template
import redis
import time

app = Flask(__name__)

redis_server = redis.Redis(host='redis', port='6379')

def page_load_counter():
 retries = 2
 while True:
  try:
   return redis_server.incr('hits')
  except redis.exceptions.ConnectionError as exec:
   if retries == 0:
    raise exc
   retries -=1
   time.sleep(0.5)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/count")
def counter():
  page_load_hits =  page_load_counter()
  return render_template("page_load.html", variable=page_load_hits)

if __name__=="__main__":
  app.run(debug=True,host='0.0.0.0')
