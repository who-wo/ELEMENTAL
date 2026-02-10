from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'elemental-secret-key-2026'

# ============================================
# Product Data
# ============================================
all_products = [
    {
        'id': 1,
        'name': 'Elemental Tactical Vest',
        'price': 2500,
        'sale_price': 1500,
        'on_sale': True,
        'is_new': False,
        'image': 'fishing_vest.png',
        'category': 'men',
        'category_label': 'ผู้ชาย',
        'description': 'เสื้อกั๊กยุทธวิธีสำหรับนักผจญภัย ผลิตจากวัสดุคุณภาพสูง กันน้ำ กันลม มีกระเป๋าหลายช่อง เหมาะสำหรับกิจกรรมกลางแจ้งทุกรูปแบบ',
        'features': ['กันน้ำ กันลม', 'กระเป๋า 6 ช่อง', 'ผ้า Ripstop คุณภาพสูง', 'น้ำหนักเบา ระบายอากาศดี'],
    },
    {
        'id': 2,
        'name': 'Elemental Classic T-Shirt',
        'price': 890,
        'sale_price': 890,
        'on_sale': False,
        'is_new': True,
        'image': 'coo.png',
        'category': 'women',
        'category_label': 'ผู้หญิง',
        'description': 'เสื้อยืดคลาสสิก ผ้าฝ้ายออร์แกนิค 100% นุ่มสบาย ระบายอากาศดี เหมาะทั้งใส่เที่ยวและออกกำลังกาย',
        'features': ['ผ้าฝ้ายออร์แกนิค 100%', 'ระบายอากาศดี', 'ทนทาน ซักได้หลายครั้ง', 'ตัดเย็บอย่างดี'],
    },
    {
        'id': 3,
        'name': 'Elemental Summit Jacket',
        'price': 4500,
        'sale_price': 2990,
        'on_sale': True,
        'is_new': False,
        'image': 'one.png',
        'category': 'men',
        'category_label': 'ผู้ชาย',
        'description': 'แจ็คเก็ตสำหรับปีนเขา กันน้ำระดับ 10,000mm กันลม ผ้า 3 ชั้น พร้อมฮู้ดถอดได้ เหมาะสำหรับสภาพอากาศหนาวเย็น',
        'features': ['กันน้ำ 10,000mm', 'ผ้า 3 ชั้น', 'ฮู้ดถอดได้', 'ซิปกันน้ำ YKK', 'กระเป๋าซิป 4 ช่อง'],
    },
    {
        'id': 4,
        'name': 'Elemental Trail Runner Tee',
        'price': 790,
        'sale_price': 790,
        'on_sale': False,
        'is_new': True,
        'image': 'coo.png',
        'category': 'men',
        'category_label': 'ผู้ชาย',
        'description': 'เสื้อยืดสำหรับวิ่งเทรล ผ้า Quick-dry แห้งไว ไม่อมเหงื่อ เหมาะสำหรับกิจกรรมกลางแจ้งทุกชนิด',
        'features': ['ผ้า Quick-dry', 'ป้องกัน UV', 'ระบายอากาศดีเยี่ยม', 'น้ำหนักเบาพิเศษ'],
    },
    {
        'id': 5,
        'name': 'Elemental Alpine Hoodie',
        'price': 1990,
        'sale_price': 1490,
        'on_sale': True,
        'is_new': False,
        'image': 'one.png',
        'category': 'women',
        'category_label': 'ผู้หญิง',
        'description': 'ฮู้ดดี้สำหรับปีนเขา ผ้า Fleece เกรด A อบอุ่น นุ่มสบาย เหมาะสำหรับสภาพอากาศเย็น',
        'features': ['ผ้า Fleece เกรด A', 'กระเป๋าซิปด้านหน้า', 'ฮู้ดปรับขนาดได้', 'ปลอกแขนมีรูสำหรับนิ้วโป้ง'],
    },
    {
        'id': 6,
        'name': 'Elemental Storm Shell',
        'price': 3500,
        'sale_price': 3500,
        'on_sale': False,
        'is_new': True,
        'image': 'fishing_vest.png',
        'category': 'men',
        'category_label': 'ผู้ชาย',
        'description': 'เสื้อกันฝนน้ำหนักเบา พับเก็บได้ กันน้ำ 100% เหมาะสำหรับพกพาไปทุกที่',
        'features': ['กันน้ำ 100%', 'น้ำหนักเบาเพียง 200g', 'พับเก็บได้', 'ตะเข็บปิดผนึก'],
    },
    {
        'id': 7,
        'name': 'Elemental Base Layer Top',
        'price': 1290,
        'sale_price': 890,
        'on_sale': True,
        'is_new': False,
        'image': 'coo.png',
        'category': 'women',
        'category_label': 'ผู้หญิง',
        'description': 'เสื้อชั้นในสำหรับกิจกรรมกลางแจ้ง ผ้า Merino Wool ควบคุมอุณหภูมิ ป้องกันกลิ่น',
        'features': ['ผ้า Merino Wool', 'ควบคุมอุณหภูมิร่างกาย', 'ป้องกันกลิ่นอับ', 'ตะเข็บแบน ไม่ระคายผิว'],
    },
    {
        'id': 8,
        'name': 'Elemental Expedition Parka',
        'price': 5900,
        'sale_price': 5900,
        'on_sale': False,
        'is_new': True,
        'image': 'one.png',
        'category': 'men',
        'category_label': 'ผู้ชาย',
        'description': 'เสื้อพาร์กาสำหรับสำรวจพื้นที่หนาวจัด บุขนเป็ดแท้ กันหนาวได้ถึง -30°C',
        'features': ['บุขนเป็ดแท้ 800 Fill Power', 'กันหนาวถึง -30°C', 'กันน้ำ กันลม', 'ฮู้ดขนสัตว์เทียมถอดได้'],
    },
    {
        'id': 9,
        'name': 'Elemental Flex Leggings',
        'price': 1490,
        'sale_price': 990,
        'on_sale': True,
        'is_new': False,
        'image': 'coo.png',
        'category': 'women',
        'category_label': 'ผู้หญิง',
        'description': 'เลกกิ้งสำหรับกิจกรรมกลางแจ้ง ยืดหยุ่นสูง อัตราการระบายอากาศดีเยี่ยม',
        'features': ['ผ้ายืด 4 ทิศทาง', 'ระบายอากาศเยี่ยม', 'กระเป๋าซ่อนที่เอว', 'ป้องกัน UV'],
    },
    {
        'id': 10,
        'name': 'Elemental Down Vest',
        'price': 2990,
        'sale_price': 2990,
        'on_sale': False,
        'is_new': False,
        'image': 'fishing_vest.png',
        'category': 'women',
        'category_label': 'ผู้หญิง',
        'description': 'เสื้อกั๊กบุขนเป็ด น้ำหนักเบา อบอุ่น เหมาะสำหรับสวมทับในวันที่อากาศเย็น',
        'features': ['บุขนเป็ด 700 Fill Power', 'น้ำหนักเบาเพียง 300g', 'พับเก็บในถุงตัวเองได้', 'กันลม'],
    },
]


# ============================================
# Routes
# ============================================

@app.route('/')
def index():
    return render_template('index.html', products=all_products, active_page='home')


@app.route('/products')
def products():
    return render_template('products.html', products=all_products, active_page='products')


@app.route('/search')
def search_page():
    query = request.args.get('q', '').strip()
    results = []
    if query:
        q_lower = query.lower()
        results = [p for p in all_products if q_lower in p['name'].lower() or q_lower in p['description'].lower()]
    return render_template('search.html', query=query, results=results, active_page='search')


@app.route('/promotions')
def promotions():
    sale_products = [p for p in all_products if p['on_sale']]
    return render_template('promotions.html', products=sale_products, active_page='promotions')


@app.route('/men')
def men():
    men_products = [p for p in all_products if p['category'] == 'men']
    return render_template('men.html', products=men_products, active_page='men')


@app.route('/women')
def women():
    women_products = [p for p in all_products if p['category'] == 'women']
    return render_template('women.html', products=women_products, active_page='women')


@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in all_products if p['id'] == product_id), None)
    if not product:
        return "ไม่พบสินค้า", 404
    return render_template('product_detail.html', product=product, active_page='products')


@app.route('/order/<int:product_id>', methods=['GET', 'POST'])
def order(product_id):
    product = next((p for p in all_products if p['id'] == product_id), None)
    if not product:
        return "ไม่พบสินค้า", 404

    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        phone = request.form['phone']
        print(f"🧾 สั่งซื้อ {product['name']} | {name} | {address} | {phone}")
        flash(f"🎉 สั่งซื้อ {product['name']} สำเร็จแล้ว! ขอบคุณที่อุดหนุนครับ/ค่ะ", 'success')
        return redirect(url_for('index'))

    return render_template('order.html', product=product, active_page='products')


if __name__ == '__main__':
    # ดึงค่า PORT จากระบบที่ Render กำหนดมาให้ ถ้าหาไม่เจอจะใช้ 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)