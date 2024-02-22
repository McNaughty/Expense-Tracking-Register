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
values (6, 'Full Month','All expenses combined');



==== Bulk insert Expenses ====

INSERT INTO Expenses (expense_id, expense_name, expense_amount, cat_id, userid)
values (7, 'Gondwana','5000','3','1');

INSERT INTO Expenses (expense_id, expense_name, expense_amount, cat_id, userid)
values (8, 'Stationaries','1000','4','1');

INSERT INTO Expenses (expense_id, expense_name, expense_amount, cat_id, userid)
values (9, 'Electrical Repairds','5000','2','1');

INSERT INTO Expenses (expense_id, expense_name, expense_amount, cat_id, userid)
values (10, 'Contribution towards medical cover','2000','5','1');



update budgets set category_id = 6 where user_id = 15



select category_id from categories where category_name = 'Enterntainment';

select * from expenses;


update Categories set category_name = 'Entertainment' where category_id = 3


SELECT e.*, c.category_name 
            FROM Expenses e 
            JOIN Categories c ON e.cat_id = c.category_id
            WHERE e.userid = (SELECT user_id FROM Users WHERE username = ?)