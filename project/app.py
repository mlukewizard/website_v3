from flask import Flask, render_template
from project.database.database_interface import Product, get_all_entry_type, delete_and_create_database, add_item

delete_and_create_database()
add_item(Product(productID="1", brand="Fix-My-Road-Rash", details="Bandage", img1Path=r"static\img\product-img\1\bandage1.jpg", img2Path=r"static\img\product-img\1\bandage2.jpg", price="£10"))
add_item(Product(productID="2", brand="Fix-My-Road-Rash", details="Plaster", img1Path=r"static\img\product-img\2\plaster1.jpg", img2Path=r"static\img\product-img\2\plaster2.jpg", price="£20"))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/regular-page')
def regular_page():
    return render_template('regular-page.html')

@app.route('/shop')
def shop():
    products = get_all_entry_type(Product)
    return render_template('shop.html', products=products)

@app.route('/single-blog')
def single_blog():
    return render_template('single-blog.html')

@app.route('/single-product-details')
def single_product_details():
    return render_template('single-product-details.html')





if __name__ == '__main__':
    app.run(debug=True)
