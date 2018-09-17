from flask import Flask, render_template

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
    return render_template('shop.html')

@app.route('/single-blog')
def single_blog():
    return render_template('single-blog.html')

@app.route('/single-product-details')
def single_product_details():
    return render_template('single-product-details.html')





if __name__ == '__main__':
    app.run(debug=True)
