from flask import Flask, jsonify, request

app = Flask(__name__)
stores = [
    {
        'name': 'beautiful store',
        'items': [
            {
                'name': 'flowers',
                'price': 100
            }
        ]
    },
    {
        'name': 'beautiful store 2',
        'items': [
            {
                'name': 'books',
                'price': 100
            }
        ]
    }
]


@app.route('/')
def home():
    return "Hello to Store App"


# to add new store details
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': request_data['items']
    }
    stores.append(new_store)
    return jsonify(new_store)


# to get store details store name will be passed as an argument
@app.route('/store/<string:name>')
def get_store_name(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# to get list of all stores
@app.route('/store')
def get_all_store_name():
    return jsonify({'stores': stores})


# to add items to existing store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})


# to get items of existing store
@app.route('/store/<string:name>/item')
def get_store_item(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'store not found'})


if __name__ == '__main__':
    app.run(debug=True)
