SQL stands for Structured Query Language


# SELECT
SELECT column_name, column_name FROM table_name;
SELECT * FROM table_name;                                  # Selects all the columns from the table_name
SELECT DISTINCT column_name FROM table_name;              # The DISTINCT statement is used to return only distinct (different) values
SELECT COUNT(DISTINCT column_name) FROM table_name;


# WHERE
SELECT * FROM table_name WHERE Country='Mexico';           # The WHERE clause is used to filter records
SELECT * FROM table_name WHERE CustomerID=1;
SELECT * FROM table_name WHERE CustomerID>5;	           # >  <  >=  <=  <>   !=
Select * From table_name WHERE date > dateadd(hour, -1, GETDATE()) AND date <= GETDATE();


# WHERE, MATCH, AGAINST
SELECT ... WHERE MATCH(tablename, headline) AGAINST (+Django -jazz Python IN BOOLEAN MODE);


# BETWEEN
SELECT * FROM table_name WHERE Price BETWEEN 10 AND 20;
SELECT * FROM Products WHERE Price NOT BETWEEN 10 AND 20;  # display the products outside the range between 10 to 20
SELECT * FROM Products WHERE (Price BETWEEN 10 AND 20) AND NOT CategoryID IN (1,2,3); 
# selects all products with a price BETWEEN 10 and 20, but products with a CategoryID of 1,2, or 3 should not be displayed
SELECT * FROM Products WHERE ProductName NOT BETWEEN 'C' AND 'M';
# selects all products with a ProductName beginning with any of the letter NOT BETWEEN 'C' and 'M'
SELECT * FROM Orders WHERE OrderDate BETWEEN #07/04/1996# AND #07/09/1996#;
# selects all orders with an OrderDate BETWEEN '04-July-1996' and '09-July-1996'


# AND, OR, NOT
SELECT * FROM table_name WHERE Country='Germany' AND (City='Berlin' OR City='München');     # "i", "lub"
SELECT * FROM table_name WHERE NOT Country='Germany' AND NOT Country='USA';		# selects all fields where country is NOT "Germany" and NOT "USA"


# LIKE and Wildcard
# % - percent sign represents zero, one, or multiple characters
# _ - underscore represents a single character
SELECT * FROM table_name WHERE City LIKE 's%';             # selects all customers with a City starting with the letter "s"
SELECT * FROM Customers WHERE Country NOT LIKE '%land%';   # selects all customers with a Country NOT containing the pattern "land"
SELECT * FROM Customers WHERE City LIKE '_erlin';          # selects all customers with a City starting with any character, followed by "erlin"
SELECT * FROM Customers WHERE City LIKE '[bsp]%';          # selects all customers with a City starting with "b", "s", or "p"
SELECT * FROM Customers WHERE City NOT LIKE '[bsp]%';      # selects all customers with a City NOT starting with "b", "s", or "p" == LIKE '[!bsp]%'
SELECT * FROM Customers WHERE City LIKE '[a-c]%';		   # selects all customers with a City starting with "a", "b", or "c"
SELECT * FROM WHERE headline ILIKE 'Will%';				   # case-insensitive Like


# IN
SELECT * FROM table_name WHERE City IN ('Paris','London'); # IN operator allows you to specify multiple values in a WHERE clause
SELECT * FROM Customers WHERE Country IN (SELECT Country FROM Suppliers);


# ORDER BY
SELECT * FROM table_name ORDER BY Country, CustomerName;   # sort the result-set.  +DESC sorted DESCENDING
SELECT * FROM table_name ORDER BY Country ASC, CustomerName DESC; 


# GROUP BY
# GROUP BY statement is often used with aggregate functions (COUNT, MAX, MIN, SUM, AVG) to group the result-set by one or more columns
SELECT column_name(s) FROM table_name WHERE condition GROUP BY column_name(s) ORDER BY column_name(s);

# number of customers in each country, sorted high to low
SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country ORDER BY COUNT(CustomerID) DESC;

# lists the number of orders sent by each shipper
SELECT Shippers.ShipperName,COUNT(Orders.OrderID) AS NumberOfOrders FROM Orders LEFT JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID GROUP BY ShipperName;


# HAVING
# HAVING clause was added to SQL because the WHERE keyword could not be used with aggregate functions
SELECT column_name(s) FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);

# number of customers in each country, sorted high to low (Only include countries with more than 5 customers)
SELECT COUNT(CustomerID), Country FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5
ORDER BY COUNT(CustomerID) DESC;

# lists the employees that have registered more than 10 orders
SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders
FROM (Orders
INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID)
GROUP BY LastName
HAVING COUNT(Orders.OrderID) > 10;


# SELECT TOP/LIMIT
SELECT TOP number|percent column_name FROM table_name;     # SQL Server / MS Access Syntax
SELECT TOP 50 PERCENT * FROM table_name;

SELECT column_name FROM table_name LIMIT number;           # MySQL, PostgreSQL
SELECT * FROM COMPANY LIMIT 3 OFFSET 2;					   # with offset - select id 3, 4, 5	

SELECT column_name FROM table_name WHERE ROWNUM <= number; # Oracle syntax


# Aliases/AS
SELECT column_name AS alias_name FROM table_name;    # SQL aliases are used to temporarily rename a table or a column heading.
SELECT o.OrderID, o.OrderDate, c.CustomerName FROM Customers AS c, Orders AS o WHERE c.CustomerName="Around the Horn" AND c.CustomerID=o.CustomerID;
# create an alias named "Address" that combine four columns (Address, PostalCode, City and Country)
SELECT CustomerName, Address + ', ' + PostalCode + ' ' + City + ', ' + Country AS Address FROM Customers;

# NULL Value
SELECT column_names FROM table_name WHERE column_name IS NULL;	# IS NOT NULL





# JOIN
# JOIN clause is used to combine rows from two or more tables, based on a related column between them

# (INNER) JOIN 				returns records that have matching values in both tables
SELECT column_name(s) FROM table1 INNER JOIN table2 ON table1.column_name = table2.column_name;

SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID)


# LEFT (OUTER) JOIN 		return all records from the left table, and the matched records from the right table
SELECT column_name(s) FROM table1 LEFT JOIN table2 ON table1.column_name = table2.column_name;


# RIGHT (OUTER) JOIN 	 	return all records from the right table, and the matched records from the left table
SELECT column_name(s) FROM table1 RIGHT JOIN table2 ON table1.column_name = table2.column_name;


# FULL (OUTER) JOIN 		return all records when there is a match in either left or right table
SELECT column_name(s) FROM table1 FULL OUTER JOIN table2 ON table1.column_name = table2.column_name;





# UNION
# UNION operator is used to combine the result-set of two or more SELECT statements
SELECT column_name(s) FROM table1 UNION SELECT column_name(s) FROM table2; 		# only distinct values

SELECT column_name(s) FROM table1 UNION ALL SELECT column_name(s) FROM table2;  # allow duplicate





# INSERT INTO
INSERT INTO table_name VALUES (value1,value2,value3,...);
INSERT INTO table_name (column1,column2,column3,...) VALUES (value1,value2,value3,...);   # null if value doesn't exist


# UPDATE
UPDATE table_name SET ContactName='Alfred Schmidt', City='Hamburg' WHERE CustomerName='Alfreds Futterkiste'   # remember about the WHERE statement


# DELETE
DELETE FROM table_name WHERE CustomerName='Alfreds Futt' AND ContactName='Maria Anders';
DELETE FROM table_name;                                    # delete all rows in a table without deleting the table





# FUNCTIONS

# MIN, MAX
SELECT MIN(Price) AS SmallestPrice FROM Products;

# COUNT function returns the number of rows that matches a specified criteria
SELECT COUNT(column_name) FROM table_name WHERE condition;
# count(*) - with nulls and duplicates
# count() - non null values

# AVG function returns the average value of a numeric column
SELECT AVG(column_name) FROM table_name WHERE condition;

# SUM function returns the total sum of a numeric column
SELECT SUM(column_name) FROM table_name WHERE condition;





# COMMENTS
# Single line comments start with --
# Multi-line comments start with /* and end with */
