CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,

    CONSTRAINT fk_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    CONSTRAINT fk_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

INSERT INTO order_items
(order_id, product_id, quantity)
VALUES
(9, 1, 1),
(9, 3, 2),
(10, 2, 1),
(10, 6, 3),
(11, 4, 2),
(12, 1, 1),
(12, 5, 3),
(13, 6, 2),
(14, 3, 1),
(15, 2, 2),
(16, 1, 1),
(16, 4, 1);