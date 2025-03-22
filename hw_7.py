import sqlite3

def create_database():
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        product_title TEXT NOT NULL CHECK(length(product_title) <= 200),
                        price REAL NOT NULL DEFAULT 0.0 CHECK(price >= 0),
                        quantity INTEGER NOT NULL DEFAULT 0 CHECK(quantity >= 0))''')
    conn.commit()
    conn.close()

def add_products():
    products = [
        ("Мыло детское", 75.5, 10),
        ("Жидкое мыло с запахом ванили", 90.0, 15),
        ("Шампунь", 150.0, 8),
        ("Гель для душа", 120.0, 20),
        ("Зубная паста", 95.0, 5),
        ("Щетка зубная", 50.0, 30),
        ("Крем для рук", 180.0, 12),
        ("Крем для лица", 250.0, 7),
        ("Лосьон для тела", 200.0, 6),
        ("Дезодорант", 140.0, 25),
        ("Маска для волос", 300.0, 4),
        ("Скраб для лица", 220.0, 9),
        ("Пена для бритья", 130.0, 10),
        ("Бритвенный станок", 190.0, 18),
        ("Одеколон", 350.0, 3)
    ]
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)", products)
    conn.commit()
    conn.close()

def product_exists(product_id):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM products WHERE id = ?", (product_id,))
    result = cursor.fetchone()
    conn.close()
    return result is not None


def update_quantity(product_id, new_quantity):
    if not product_exists(product_id):
        print(f"Товар с id {product_id} не найден.")
        return

    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
    conn.commit()
    conn.close()


def update_price(product_id, new_price):
    if not product_exists(product_id):
        print(f"Товар с id {product_id} не найден.")
        return

    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    conn.commit()
    conn.close()


def delete_product(product_id):
    if not product_exists(product_id):
        print(f"Товар с id {product_id} не найден.")
        return

    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()

    print("\nСписок товаров:")
    print("-" * 50)
    for product in products:
        print(f"ID: {product[0]}, Название: {product[1]}, Цена: {product[2]} сом, Количество: {product[3]} шт.")
    print("-" * 50)


def get_filtered_products(price_limit, quantity_limit):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE price < ? AND quantity > ?", (price_limit, quantity_limit))
    products = cursor.fetchall()
    conn.close()

    if products:
        print(f"\nТовары дешевле {price_limit} сом и с количеством больше {quantity_limit}:")
        print("-" * 50)
        for product in products:
            print(f"ID: {product[0]}, Название: {product[1]}, Цена: {product[2]} сом, Количество: {product[3]} шт.")
        print("-" * 50)
    else:
        print("Нет подходящих товаров.")


def search_products_by_name(keyword):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE product_title LIKE ?", (f"%{keyword}%",))
    products = cursor.fetchall()
    conn.close()

    if products:
        print(f"\nРезультаты поиска по '{keyword}':")
        print("-" * 50)
        for product in products:
            print(f"ID: {product[0]}, Название: {product[1]}, Цена: {product[2]} сом, Количество: {product[3]} шт.")
        print("-" * 50)
    else:
        print(f"Товары с '{keyword}' в названии не найдены.")


# Тестирование функций
if __name__ == "__main__":
    create_database()
    add_products()
    update_quantity(1, 20)
    update_price(2, 80.0)
    delete_product(15)
    get_all_products()
    get_filtered_products(100, 5)
    search_products_by_name("мыло")
