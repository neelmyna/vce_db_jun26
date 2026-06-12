# ENTITY
Book
    id, title, author, publisher, category, number_of_pages, price

Book
    id              int primary key auto_increment
    title           varchar(100) not null
    author          varchar(100) not null
    publisher       varchar(100) not null
    category        varchar(32)
    number_of_pages smallint
    price           float default(100) check(price >= 100 price <=10000)

## Description
```Entity```
The entity we have selected is Book. And the table/collection would stores details about the books of different categories

## Steps to Perform an operation (insert/update/delete)
1. Read necessary data from the user
2. Build the Query
3. Make the connection
4. Get the cursor object
5. Execute the query
    Optional: Check if query executed successfully or not.
6. Close the cursor and connection objects