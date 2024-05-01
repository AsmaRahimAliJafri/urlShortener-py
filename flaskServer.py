from flask import Flask, redirect
from dbClient import urlMappingCollection

app = Flask(__name__)


@app.route('/')
def index():
    return 'base route for shortly server'


# add case for gracefully handling key error exceptions
@app.route('/<short_url>')
def redirect_to_expanded(short_url):
    found = urlMappingCollection.find_one({'shortId': short_url})
    expanded_url = found.get("originalUrl")
    if expanded_url:
        return redirect(expanded_url)
    else:
        return "route not found in dict"


if __name__ == '__main__':
    app.run(debug=True)
