import request


@app.route('/product', methods=['POST'])
def get_method():
    name = request.json['name']

    new_product = Product(name)  # query = 'insert into tablename'

    db.session.add(new_product)  # db.execute(query)
    db.session.commit()  # db.commit()

    return product_schema.jsonify(new_product)  # return josnify(data)


# Get all products
@app.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()  # query = select *from tablename

    result = products_schema.dump(all_products)  # data = query.fetchall()
    return jsonify(result.data)  # return json.dumps(data)