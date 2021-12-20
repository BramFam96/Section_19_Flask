from postbasics import *
# Dynamic Routing continued:
    # Routes can contain multiple variables:
@app.route('/products/<category>/<int:product_id>')
def product_details(category, product_id):
    return None;