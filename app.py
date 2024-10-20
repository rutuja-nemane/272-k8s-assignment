from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Base URL of the Item Service
ITEM_SERVICE_URL = 'http://item-service:5001/items'

@app.route('/')
def home():
    # Fetch items from the Item Service
    response = requests.get(ITEM_SERVICE_URL)
    items = response.json()
    return render_template('index.html', items=items)

# Add a new item via form submission
@app.route('/add_item', methods=['POST'])
def add_item():
    data = request.json  # Fetch JSON data from the request body
    name = data.get('name')
    description = data.get('description')
    new_item = {"name": name, "description": description}
    # Send new item to the Item Service
    requests.post(ITEM_SERVICE_URL, json=new_item)
    return redirect(url_for('home'))

# Delete an item
@app.route('/delete_item/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    # Send delete request to the Item Service
    requests.delete(f"{ITEM_SERVICE_URL}/{item_id}")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
