create database onlinebookstore;
use onlinebookstore;
select * from onlinebookstore;

select * from Books;
select * from Customers;
select * from Orders;

--------------------------------------------------------------- -- QUESTIONS--------------------------------------------------------------------

-- 1) Retrieve all books in the "Fiction genre:
select * from Books 
where Genre="Fiction";

-- 2) Find books published after the year 1950:
select * from Books
where Published_Year>1950;

-- 3) List all customers from the Canada:
select * from Customers
where country="Canada";

-- 4) Show orders placed in November 2023:
select * from Orders
where Order_Date between "2023-11-01" and "2023-11-30";

-- 5) Retrieve the total stock of books available:
select sum(stock) as Total_Stock
from Books;

-- 6) Find the details of the most expensive books:
select * from Books 
order by Price Desc
limit 1;

-- 7) Show all customers who ordered more than 1 quantity od=f a book:
select * from Orders
where quantity>1;

-- 8) Retrieve all orders where the total amount exceeds $20:
select * from Orders
where total_amount>20;

-- 9) List all genres available in the books table:
select distinct Genre from Books;

-- 10) Find the book with the lowest stock
select * from Books 
order by stock
limit 1;

-- 11) Calculate the total revenue generated from all orders:
select sum(total_amount) as Revenue
from Orders;

-- 12) Retrieve the total number of books sold for each genre:
select b.Genre, sum(o.Quantity) as Total_Books_sold
from Orders o
join Books b on o.book_id=b.book_id
group by b.Genre;

-- 13) Find the average price of books in the "Fantasy" genre:
select avg(price) as Average_Price
from Books
where Genre="Fantasy";

-- 14) List customers who have placed at least 2 orders:
select o.customer_id, c.name,count(o.Order_id) as ORDER_COUNT
from Orders o
join Customers c on o.customer_id=c.customer_id 
group by o.customer_id,c.name
Having count(Order_id)>=2;

-- 15) FInd the most frequently ordered book:
select o.Book_ID,b.title,count(o.Order_id) as ORDER_COUNT
from Orders o
join Books b on o.Book_id=b.Book_ID
group by o.Book_ID,b.title
order by ORDER_COUNT desc Limit 1;

-- 16) Show the top 3 most expensive books of "Fantasy" Genre:
select * from Books
where Genre="Fantasy"
order by price desc limit 3;

-- 17) Retrieve the total quantity of books sold by each author:
select b.author, sum(o.quantity) as Total_Books_Spld
from Orders o
join books b on o.Book_ID=b.Book_ID
group by b.author;

-- 18) List the cities where customers who spent over $30 are located:
select distinct c.city, total_amount
from Orders o
join customers c on o.customer_id=c.customer_id
where o.total_amount > 30;

-- 19) Find the customer who spent the most on orders:
select c.customer_id, c.name, sum(o.total_amount) as Total_Spent
from Orders o
join customers c on o.customer_id=c.customer_id
group by c.customer_id, c.name
order by Total_Spent desc limit 1;

