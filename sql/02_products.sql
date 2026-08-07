CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INT NOT NULL,
    category_id INT NOT NULL,

    CONSTRAINT fk_category
        FOREIGN KEY(category_id)
        REFERENCES categories(category_id)
);

INSERT INTO products
(product_name, price, stock_quantity, category_id)
VALUES
('Laptop', 65000.00, 25, 1),
('Smartphone', 35000.00, 40, 1),
('SQL for Beginners', 599.00, 120, 2),
('Office Chair', 4500.00, 30, 3),
('T-Shirt', 799.00, 100, 4),
('Rice Bag', 1200.00, 75, 5);