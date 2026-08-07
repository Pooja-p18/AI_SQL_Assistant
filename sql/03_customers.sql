CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    city VARCHAR(100) NOT NULL,
    phone VARCHAR(15)
);

INSERT INTO customers
(customer_name, email, city, phone)
VALUES
('Rahul Sharma', 'rahul.sharma@gmail.com', 'Hyderabad', '9876543210'),
('Priya Reddy', 'priya.reddy@gmail.com', 'Bengaluru', '9123456780'),
('Arjun Kumar', 'arjun.kumar@gmail.com', 'Chennai', '9988776655'),
('Sneha Patel', 'sneha.patel@gmail.com', 'Mumbai', '9876501234'),
('Vikram Singh', 'vikram.singh@gmail.com', 'Delhi', '9765432109');