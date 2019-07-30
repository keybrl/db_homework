DROP TABLE IF EXISTS borrower191;
DROP TABLE IF EXISTS loan191;
DROP TABLE IF EXISTS depositor191;
DROP TABLE IF EXISTS account191;
DROP TABLE IF EXISTS branch191;
DROP TABLE IF EXISTS customer191;


CREATE TABLE customer191 (
  customer_name CHAR(20),
  customer_street CHAR(30),
  customer_city CHAR(30),
  PRIMARY KEY (customer_name)
);

CREATE TABLE branch191 (
  branch_name CHAR(15),
  branch_city CHAR(30),
  assets NUMERIC(16, 2),
  PRIMARY KEY (branch_name)
);

CREATE TABLE account191 (
  account_number CHAR(10),
  branch_name CHAR(15),
  balance NUMERIC(12, 2),
  PRIMARY KEY (account_number),
  FOREIGN KEY (branch_name) REFERENCES branch191 (branch_name),
  CONSTRAINT chk_balance CHECK (balance >= 0 )
);

CREATE TABLE depositor191 (
  customer_name CHAR(20),
  account_number CHAR(10),
  PRIMARY KEY (customer_name, account_number),
  FOREIGN KEY (customer_name) REFERENCES customer191 (customer_name),
  FOREIGN KEY (account_number) REFERENCES account191 (account_number)
);

CREATE TABLE loan191 (
  loan_number CHAR(15),
  branch_name CHAR(15),
  amount NUMERIC(12, 2),
  PRIMARY KEY (loan_number),
  FOREIGN KEY (branch_name) REFERENCES branch191 (branch_name)
);

CREATE TABLE borrower191 (
  customer_name CHAR(20),
  loan_number CHAR(15),
  PRIMARY KEY (customer_name, loan_number),
  FOREIGN KEY (loan_number) REFERENCES loan191 (loan_number)
);


INSERT INTO customer191 VALUES
  ('Adams', 'Spring', 'Pittsfield'),
  ('Brooks', 'Senator', 'Brooklyn'),
  ('Curry', 'North', 'Rye'),
  ('Glenn', 'Sand Hill', 'Woodside'),
  ('Green', 'Walnut', 'Stamford'),
  ('Hayes', 'Main', 'Harrison'),
  ('Johnson', 'Alma', 'Palo Alto'),
  ('Jones', 'Main', 'Harrison'),
  ('Lindsay', 'Park', 'Pittsfield'),
  ('Smith', 'North', 'Rye'),
  ('Turner', 'Putnam', 'Stamford'),
  ('Williams', 'Nassau', 'Princeton');

INSERT INTO branch191 VALUES
  ('Brighton', 'Brooklyn', 7100000),
  ('Downtown', 'Brooklyn', 9000000),
  ('Mianus', 'Horseneck', 400000),
  ('North Town', 'Rye', 3700000),
  ('Perryridge', 'Horseneck', 1700000),
  ('Pownal', 'Bennington', 300000),
  ('Redwood', 'Palo Alto', 2100000),
  ('Round Hill', 'Horseneck', 8000000);

INSERT INTO account191 VALUES
  ('A-101', 'Downtown', 500),
  ('A-102', 'Perryridge', 400),
  ('A-201', 'Brighton', 900),
  ('A-215', 'Mianus', 700),
  ('A-217', 'Brighton', 750),
  ('A-222', 'Redwood', 700),
  ('A-305', 'Round Hill', 350);

INSERT INTO depositor191 VALUES
  ('Hayes', 'A-102'),
  ('Johnson', 'A-101'),
  ('Johnson', 'A-201'),
  ('Jones', 'A-217'),
  ('Lindsay', 'A-222'),
  ('Smith', 'A-215'),
  ('Turner', 'A-305');

INSERT INTO loan191 VALUES
  ('L-11','Round Hill', 900),
  ('L-14','Downtown', 1500),
  ('L-15','Perryridge', 1500),
  ('L-16','Perryridge', 1300),
  ('L-17','Downtown', 1000),
  ('L-23','Redwood', 2000),
  ('L-93','Mianus', 500);

INSERT INTO borrower191 VALUES
  ('Adams', 'L-16'),
  ('Curry', 'L-93'),
  ('Hayes', 'L-15'),
  ('Jackson', 'L-14'),
  ('Jones', 'L-17'),
  ('Smith', 'L-11'),
  ('Smith', 'L-23'),
  ('Williams', 'L-17');


SELECT * FROM customer191;
SELECT * FROM branch191;
SELECT * FROM account191;
SELECT * FROM depositor191;
SELECT * FROM loan191;
SELECT * FROM borrower191;
