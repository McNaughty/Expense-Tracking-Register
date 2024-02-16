-- SQLite

DROP TABLE Expenses;

CREATE TABLE Expenses (
                expense_id INTEGER PRIMARY KEY,
                expense_name TEXT,
                expense_amount INT,
                cat_id INTEGER,
                FOREIGN KEY (cat_id) REFERENCES Categories(category_id)
            );

DROP TABLE Categories;

CREATE TABLE Categories (
                category_id INTEGER PRIMARY KEY,
                category_name TEXT,
                category_description TEXT
            );



INSERT INTO Categories (category_id, category_name, category_description)
values (1, 'Food','Food items');

INSERT INTO Categories (category_id, category_name, category_description)
values (2, 'Household','Household shopping items');

INSERT INTO Categories (category_id, category_name, category_description)
values (3, 'Enterntainment','Fun times');

INSERT INTO Categories (category_id, category_name, category_description)
values (4, 'Work','Business related');

INSERT INTO Categories (category_id, category_name, category_description)
values (5, 'Black Tax','Family');


select * from categories;
