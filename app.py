from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
  return render_template('index.html')

@app.route('/pokemon/<int:idInput>')
def printName(idInput):
  id,name = pokeRequest(idInput)
  outputString = 'The Pokemon with id %d is ' % idInput + name
  return createHTML(outputString)

@app.route('/pokemon/<nameInput>')
def printID(nameInput):
  id,name = pokeRequest(nameInput)
  outputString = '%s has id ' % nameInput.capitalize() + id
  return createHTML(outputString)

def pokeRequest(query):
  r = requests.get('http://pokeapi.co/api/v2/pokemon/' + str(query))
  responseDict = r.json()['forms'][0]
  url=responseDict['url']
  base = 'https://pokeapi.co/api/v2/pokemon-form/'
  id = str(url.split(start)[1][0:-1])
  name = responseDict['name']
  return id,name

def createHTML(outputString):
    page = """<html>
    <head>
    <title>Poke index</title>
    </head>
    <body><h1>{outputString}</h1></body>
    </html>""".format(outputString = outputString)
    return page

if __name__ == '__main__':
  app.run()

