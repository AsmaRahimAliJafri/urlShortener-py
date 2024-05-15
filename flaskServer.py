from flask import Flask, redirect
from dbClient import urlMappingCollection
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
app = Flask(__name__)

# rate limiter to constraint the number of requests
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["100 per day", "10 per hour"]
)

@app.route('/')
def index():
    return 'base route for shortly server'


# add case for gracefully handling key error exceptions
@app.route('/<short_url>')
@limiter.limit("50/minute")
def redirect_to_expanded(short_url):
    try:
        found = urlMappingCollection.find_one({'shortId': short_url})
        expanded_url = found.get("originalUrl")
        if expanded_url:
            return redirect(expanded_url)
        else:
            return "route not found in dict"
    except:
        print("Error when redirecting to expanded url")


if __name__ == '__main__':
    app.run(debug=True)
