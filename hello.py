import ConfigParser

from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
  return "Hello Napier from the configuration testing app"

@app.route('/config/')
def config():
  str = []
  str.append('This is the data of the config file: <br />')
  str.append('Debug:'+app.config['DEBUG'])
  str.append('Port:'+app.config['port'])
  str.append('URL:'+app.config['url'])
  str.append('IP Address:'+app.config['ip_address'])
  return '<br />'.join(str)

def init(app):
  config = ConfigParser.ConfigParser()
  try:
      config_location = "etc/defaults.cfg"
      config.read(config_location)

      app.config['DEBUG'] = config.get("config", "debug")
      app.config['ip_address'] = config.get("config", "ip_address")
      app.config['port'] = config.get("config", "port")
      app.config['url'] = config.get("config", "url")

  except:
      print "Could not read configs from: ", config_location

if __name__ == '__main__':
  init(app)
  app.run(
          host = app.config['ip_address'],
          port = int(app.config['port'])
          )



