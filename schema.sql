CREATE DATABASE `personaldb`;

USE `personaldb`;

CREATE TABLE employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(45),
    designation VARCHAR(45),
    mobile VARCHAR(45),
    address VARCHAR(45)
);

INSERT INTO employee (name, designation, mobile, address) VALUES
('Siraj Chaudhary', 'Senior Java Developer', '9876543210', 'Hyderabad'),
('Amit Kumar', 'Software Engineer', '9123456780', 'Bangalore'),
('Rohit Sharma', 'Backend Developer', '9988776655', 'Pune'),
('Neha Verma', 'QA Engineer', '9090909090', 'Noida'),
('Priya Singh', 'DevOps Engineer', '9012345678', 'Chennai');