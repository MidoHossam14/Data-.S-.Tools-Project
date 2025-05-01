CREATE DATABASE BooksDB;

CREATE TABLE Books (
    id INT IDENTITY(1,1) PRIMARY KEY,
    title NVARCHAR(255),
    price DECIMAL(10, 2),
    rating NVARCHAR(50),
    availability NVARCHAR(100),
    category NVARCHAR(100),
    source NVARCHAR(100),
    rating_num INT
);

select * from Books;