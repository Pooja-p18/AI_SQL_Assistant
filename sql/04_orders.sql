CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    order_status VARCHAR(30) NOT NULL,

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);


INSERT INTO orders
(customer_id, order_date, order_status)
VALUES
(1, '2026-07-01', 'Completed'),
(2, '2026-07-03', 'Completed'),
(1, '2026-07-05', 'Shipped'),
(3, '2026-07-08', 'Completed'),
(4, '2026-07-10', 'Pending'),
(5, '2026-07-12', 'Completed'),
(2, '2026-07-15', 'Shipped'),
(1, '2026-07-18', 'Completed');