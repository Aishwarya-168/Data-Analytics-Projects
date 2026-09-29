create database customer_order;
use customer_order;
select * from customer_data;

ALTER TABLE customer_data
CHANGE COLUMN `ï»¿Customer ID` Customer_ID INT;
ALTER TABLE customer_data
CHANGE COLUMN `Review Rating` Review_Rating decimal(2,2);
ALTER TABLE customer_data
CHANGE COLUMN `Purchase Amount (USD)` Purchase_Amount int;
ALTER TABLE customer_data
CHANGE COLUMN `Subscription Status` Subscription_status varchar(15);
ALTER TABLE customer_data
CHANGE COLUMN `Discount Applied` Discount_applied varchar(15);
ALTER TABLE customer_data
CHANGE COLUMN `Previous Purchases` Previous_purchases int;
ALTER TABLE customer_data
CHANGE COLUMN `Payment Method` Payment_method varchar(50);
ALTER TABLE customer_data
CHANGE COLUMN `Frequency of Purchases` frequency_purchases varchar(50);

----------------------------------------------------- QUESTIONS----------------------------------------------------------------------------

-- Display all records from the customer_data table --
select * from customer_data;

-- Display customer id ,Gender and purchase amount --
select Customer_Id,Gender,Purchase_Amount from customer_data;

-- Display all frmale customers --
select Gender from customer_data where Gender="Female";

-- Display all male customers --
select Gender from customer_data where Gender="Male";

-- Find customers whose purchase amount is greater than 100 USD --
select Customer_ID,Purchase_Amount from customer_data where Purchase_Amount>100;

-- Display customers who have an active subscription --
select Customer_ID, Subscription_status from customer_data where Subscription_status="Yes";

-- FInd customers who received a discount --
select Customer_ID , Discount_applied from customer_data where Discount_applied="Yes";

-- Display customers from New York --
select Customer_ID, Location from customer_data where Location="New York";

-- Display customers whose age is greater than 40 --
select Customer_ID,Age from customer_data where Age>40;

-- Display customers whose review rating is greater than 4 --
select Customer_ID, Review_Rating from customer_data where Review_Rating>4;

-- Display all unique locations --
select distinct(Location) from customer_data;

-- Display all unique payment methods --
select distinct(Payment_method) from customer_data;

-- Display all unique seasons --
select distinct(Season) from customer_data;

-- Display the first 20 records --
select * from customer_data Limit 20;

-- Display customers who purchased during winter --
select Customer_ID, Season from customer_data where Season="Winter";

-- Find the total purchase amount --
select sum(Purchase_Amount) as total_purchase_amt from customer_data;

-- Find the average purchase amount --
select avg(Purchase_Amount)as Average_purchase_amt from customer_data;

-- Find the Highest purchase amount --
select max(Purchase_Amount) as Highest_purchase_amt from customer_data;

-- Find the Lowest purchase amount --
select min(Purchase_Amount) as Lowest_purchase_amt from customer_data;

-- Count the total number of customers --
select count(Customer_ID) from customer_data;

-- Find the total purchase amount by gender --
select Gender ,count(Purchase_Amount) as Total_purchase_amt from customer_data group by Gender;

-- Find the average purchase amount bt season -- 
select Season, avg(Purchase_Amount) as Average_purchase_amt from customer_data group by Season;

-- Count customers by gender --
select Gender,count(Customer_ID) from customer_data group by Gender;

-- Count customers by subscription status --
select Subscription_status,count(Customer_ID) from customer_data group by Subscription_status;

-- Find the average review rating for each season --
select Season,avg(Review_Rating) as Avg_review_rating from customer_data group by Season;

-- Find the highest purchase amount in each location --
select Location,max(Purchase_Amount) as Highest_purchase_amt from customer_data group by Location;

-- Find the lowest purchase amount for each payment method --
select Payment_method,min(Purchase_Amount) as Lowest_purchase_amt from customer_data group by Payment_method;

-- Find the Average age by gender --
select Gender,avg(age) as Average_Age from customer_data group by Gender;

-- Count customers in each location --
select Location,count(Customer_ID) from customer_data group by Location;

-- Find the total previous purchases by subscription status --
select Subscription_status ,sum(Previous_purchases) as Total_previous_purchase from customer_data 
group by Subscription_status;

-- Find locations where the total purchase amount is greater than 5000 --
select Location,sum(Purchase_Amount) as total_purchase_amt  from customer_data group by location
having sum(Purchase_Amount)>5000;

-- Find payment methods used by more than 100 customers --
select Payment_method,count(*) as total_customers from customer_data 
group by Payment_method having count(*)>100;

-- Find Seasons where the average purchase amount is greater than 80 USD --
select Season,avg(Purchase_Amount) as avg_purchase_amt from customer_data 
group by Season having avg(Purchase_Amount)>80;

-- Find Locations having more than 50 customers --
select Location,count(Customer_ID) from customer_data 
group by location having count(Customer_ID)>50;

-- Find genders whose average age is greater than 35 years --
select Gender,avg(Age) as Avg_Age from customer_data 
group by Gender having avg(Age)>35;

-- Find subscription groups having total previous purchases greater than 1000 --
select Subscription_status,sum(Previous_purchases) as Total_previous_purchases from customer_data
group by Subscription_status having sum(Previous_purchases)>1000;

-- Find payment methods where the average review rating is greater than 4 --
select Payment_method,avg(Review_Rating) as Avg_review_rating from customer_data 
group by Payment_method having avg(Review_Rating)>4;

-- Find Seasons with more than 200 customers --
select Season,count(*) as Total_customer from customer_data group by Season having count(*)>200;

-- Find locations where the highest purchase amount exceeds 200 USD --
select Location,max(Purchase_Amount) as Highest_purchase_amt from customer_data 
group by Location having max(Purchase_Amount)>200;

-- Find payment methods whose average purchase amount exceeds 90 USD --
select Payment_method,avg(Purchase_Amount) as Avg_purchase_amt from customer_data 
group by Payment_method having avg(Purchase_Amount)>90;

-- Which location has the highest total purchase amount --
select Location, sum(Purchase_Amount) as Total_purchase_amt from customer_data 
group by Location  order by Total_purchase_amt desc limit 1;

-- which payment method is used the most --
select Payment_method,count(*)as payment_method from customer_data 
group by Payment_method order by payment_method desc limit 1;

-- Which season generated the highest sales --
select Season,count(*) as Highest_sale from customer_data 
group by Season order by Highest_sale desc limit 1;

-- Which gender spends more on average? --
select Gender,count(*) as avg_gender from customer_data 
group by Gender order by avg_gender desc limit 1;

-- Find the average purchase amount for each payment method.--
select Payment_method,avg(Purchase_Amount) as Avg_purchase_amt from customer_data 
group by Payment_method;

-- Find the average review rating for each location --
select Location,avg(Review_Rating) as Avg_review_rating from customer_data 
group by Location;

-- Find the total purchase amount for subscribed customers--
select Subscription_status,sum(Purchase_Amount) as Total_purchase_amt from customer_data
where Subscription_status="Yes";

-- Find the total purchase amount for non-subscribed customers--
select Subscription_status,sum(Purchase_Amount) as Total_purchase_amt from customer_data
where Subscription_status="No";

-- Find the total previous purchases made by each gender --
select Gender,sum(Previous_purchases) as Total_previous_purchases from customer_data
group by Gender;

-- Find the average purchase amount by clothing size --
select Size,avg(Purchase_Amount) as Avg_purchase_amt from customer_data
group by Size order by Avg_purchase_amt;

-- Find the most preferred clothing colour --
select Color,count(*) as Preferred_cloth_color from customer_data group by Color
order by Preferred_cloth_color desc limit 1;

-- Find the average purchase amount based on discount availability --
select Discount_applied,avg(Purchase_Amount) as Avg_purchase_amt from customer_data
group by Discount_applied;
