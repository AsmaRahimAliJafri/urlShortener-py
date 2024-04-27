from flask import Flask, redirect
from mydictonary import get_expanded_url, add_url, dataStruct_dict
from lock_module import lock
from dbClient import urlMappingCollection
app = Flask(__name__)

@app.route('/')
def index():
    return 'base route for shortly server'

# add case for gracefully handling key error exceptions
@app.route('/<short_url>')
def redirect_to_expanded(short_url):
    lock.acquire()
    try:
        # print("dataStruct_dict ======================================= ", dataStruct_dict.items())
        # expanded_url = dataStruct_dict[short_url]
        # print("flaskServer.py ----------------------------- expanded_url = ", expanded_url)
        found=urlMappingCollection.find_one({'shortId':short_url})
        expanded_url = found.get("originalUrl")
        print("=====================================================================================================================", expanded_url)
        if expanded_url:
            return redirect(expanded_url)
        else:
            return "route not found in dict"
    finally:
        lock.release()
if __name__=='__main__':
    app.run(debug=True)