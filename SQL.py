SQL stands for Structured Query Language


# SELECT
SELECT column_name,column_name FROM table_name;
SELECT * FROM table_name;                                  # Selects all the columns from the "Customers" table
SELECT DISTINCT column_names FROM table_name;              # The DISTINCT statement is used to return only distinct (different) values


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


# LIKE and Wildcard
SELECT * FROM table_name WHERE City LIKE 's%';             # selects all customers with a City starting with the letter "s"
SELECT * FROM Customers WHERE Country NOT LIKE '%land%';   # selects all customers with a Country NOT containing the pattern "land"
SELECT * FROM Customers WHERE City LIKE '_erlin';          # selects all customers with a City starting with any character, followed by "erlin"
SELECT * FROM Customers WHERE City LIKE '[bsp]%';          # selects all customers with a City starting with "b", "s", or "p"
SELECT * FROM Customers WHERE City NOT LIKE '[bsp]%';      # selects all customers with a City NOT starting with "b", "s", or "p"

SELECT * FROM WHERE headline ILIKE 'Will%';				   # case-insensitive Like


# IN
SELECT * FROM table_name WHERE City IN ('Paris','London'); # IN operator allows you to specify multiple values in a WHERE clause


# AND, OR
SELECT * FROM table_name WHERE Country='Germany' AND (City='Berlin' OR City='München');     # "i", "lub"


# ORDER BY
SELECT * FROM table_name ORDER BY Country, CustomerName;   # sort the result-set.  +DESC sorted DESCENDING


# INSERT INTO
INSERT INTO table_name VALUES (value1,value2,value3,...);
INSERT INTO table_name (column1,column2,column3,...) VALUES (value1,value2,value3,...);   # null if value doesn't exist


# UPDATE
UPDATE table_name SET ContactName='Alfred Schmidt', City='Hamburg' WHERE CustomerName='Alfreds Futterkiste'   # remember about the WHERE statme

# DELETE
DELETE FROM table_name WHERE CustomerName='Alfreds Futt' AND ContactName='Maria Anders';
DELETE FROM table_name;                                    # delete all rows in a table without deleting the table


# SELECT TOP/LIMIT
SELECT TOP number|percent column_name FROM table_name;     # SQL Server / MS Access Syntax
SELECT column_name FROM table_name LIMIT number;           # MySQL, PostgreSQL
SELECT * FROM COMPANY LIMIT 3 OFFSET 2;					   # with offset - select id 3, 4, 5	

# Aliases/ AS
SELECT column_name AS alias_name FROM table_name;    # SQL aliases are used to temporarily rename a table or a column heading.
SELECT o.OrderID, o.OrderDate, c.CustomerName FROM Customers AS c, Orders AS o WHERE c.CustomerName="Around the Horn" AND c.CustomerID=o.CustomerID; 



# To Do
Distinct on
group by
count(*) - with nulls and duplicates
count() - non null values
have to