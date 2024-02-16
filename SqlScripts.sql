-- SQLite

DROP TABLE Users;

CREATE TABLE Users (
                user_id INTEGER PRIMARY KEY,
                username TEXT
            );


DROP TABLE Expenses;

CREATE TABLE Expenses (
    expense_id INTEGER PRIMARY KEY,
    expense_name TEXT,
    expense_amount INT,
    cat_id INTEGER,
    userid INTEGER,
    FOREIGN KEY (cat_id) REFERENCES Categories(category_id),
    FOREIGN KEY (userid) REFERENCES Users(user_id)
);

DROP TABLE Categories;

CREATE TABLE Categories (
                category_id INTEGER PRIMARY KEY,
                category_name TEXT,
                category_description TEXT
            );


CREATE TABLE Budgets (
    budget_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    category_id INTEGER,
    budget_amount REAL,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
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

select * from expenses;
