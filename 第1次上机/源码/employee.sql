DROP TABLE IF EXISTS manages;
DROP TABLE IF EXISTS works;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS company;


CREATE TABLE employee (
  employee_name CHAR(64) PRIMARY KEY,
  street CHAR(128),
  city CHAR(64)
);

CREATE TABLE company (
  company_name CHAR(64) PRIMARY KEY,
  city CHAR(64)
);

CREATE TABLE works (
  employee_name CHAR(64) PRIMARY KEY,
  company_name CHAR(64),
  salary NUMERIC(10, 2),
  FOREIGN KEY (employee_name) REFERENCES employee (employee_name),
  FOREIGN KEY (company_name) REFERENCES company (company_name)
);

CREATE TABLE manages (
  employee_name CHAR(64) PRIMARY KEY,
  manager_name CHAR(64),
  FOREIGN KEY (employee_name) REFERENCES employee (employee_name),
  FOREIGN KEY (manager_name) REFERENCES employee (employee_name)
);


INSERT INTO employee VALUES
  ('Albert', 'A', 'Tianjin'),
  ('Baker', 'A', 'Shenzhen'),
  ('Cole', 'A', 'Tianjin'),
  ('David', 'A', 'Shenzhen'),
  ('Elbert', 'A', 'Shenzhen'),
  ('Franklin', 'A', 'Shenzhen'),
  ('Green', 'A', 'Tianjin'),
  ('Harley', 'C', 'Tianjin'),
  ('Ida', 'B', 'Shanghai'),
  ('Jeanne', 'A', 'New York'),
  ('Kennedy', 'B', 'New York'),
  ('Layton', 'B', 'New York'),
  ('Mitchell', 'B', 'Foshan'),
  ('Nolan', 'B', 'Washington'),
  ('Oliver', 'B', 'New York'),
  ('Peterson', 'B', 'ChiZhou'),
  ('Quinton', 'B', 'Hong Kong'),
  ('Roman', 'B', 'Shanghai'),
  ('Scott', 'C', 'Beijing'),
  ('Tony', 'C', 'Guangzhou'),
  ('Ulysses', 'C', 'Shanghai'),
  ('Victor', 'C', 'Shanghai'),
  ('Web', 'C', 'Guangzhou'),
  ('Xidian', 'C', 'Beijing'),
  ('York', 'C', 'Beijing'),
  ('Zebulon', 'C', 'Shanghai');

INSERT INTO company VALUES
  ('HUAWEI', 'Shenzhen'),
  ('Tencent', 'Shenzhen'),
  ('NetEase', 'Guangzhou'),
  ('Alibaba', 'Shanghai'),
  ('Baidu', 'Beijing'),
  ('ICBC', 'Washington'),
  ('ABC', 'Beijing'),
  ('CCB', 'Shanghai'),
  ('BOC', 'Beijing'),
  ('BOCOM', 'Washington'),
  ('First Bank Corporation', 'New York'),
  ('Small Bank Corporation', 'Washington');

INSERT INTO works VALUES
  ('Albert', 'HUAWEI', 5456),
  ('Baker', 'NetEase', 1231),
  ('Cole', 'HUAWEI', 9999),
  ('David', 'NetEase', 620),
  ('Elbert', 'Alibaba', 530),
  ('Franklin', 'Alibaba', 3332),
  ('Green', 'ICBC', 22222),
  ('Harley', 'HUAWEI', 54355),
  ('Ida', 'Alibaba', 23233),
  ('Jeanne', 'HUAWEI', 54353),
  ('Kennedy', 'ICBC', 2332),
  ('Layton', 'Tencent', 23413),
  ('Mitchell', 'NetEase', 980928),
  ('Nolan', 'BOC', 24816),
  ('Oliver', 'Small Bank Corporation', 9876),
  ('Peterson', 'CCB', 12345),
  ('Quinton', 'First Bank Corporation', 99823),
  ('Roman', 'Tencent', 666),
  ('Scott', 'Tencent', 2333),
  ('Tony', 'Tencent', 500),
  ('Ulysses', 'Small Bank Corporation', 13500),
  ('Victor', 'BOCOM', 600),
  ('Web', 'Tencent', 550),
  ('Xidian', 'Tencent', 540),
  ('York', 'First Bank Corporation', 1000),
  ('Zebulon', 'First Bank Corporation', 10001);

INSERT INTO manages VALUES
  ('Albert', 'Peterson'),
  ('Baker', 'Oliver'),
  ('Cole', 'Layton'),
  ('David', 'Cole'),
  ('Elbert', 'Cole'),
  ('Franklin', 'Elbert'),
  ('Green', 'Cole'),
  ('Harley', 'Jeanne'),
  ('Ida', 'David'),
  ('Jeanne', 'Mitchell'),
  ('Kennedy', 'Mitchell'),
  ('Layton', 'Green'),
  ('Mitchell', 'Roman'),
  ('Nolan', 'Roman'),
  ('Oliver', 'Roman'),
  ('Peterson', 'David'),
  ('Quinton', 'Ida'),
  ('Roman', 'Ida'),
  ('Scott', 'Xidian'),
  ('Tony', 'Mitchell'),
  ('Ulysses', 'Albert'),
  ('Victor', 'Ulysses'),
  ('Web', 'Albert'),
  ('Xidian', 'Quinton'),
  ('York', 'Ulysses'),
  ('Zebulon', 'Zebulon');

# 3.2 a
SELECT employee_name, city
FROM employee NATURAL JOIN works
WHERE company_name = 'First Bank Corporation';

# 3.2 b
SELECT employee_name, street, city
FROM employee NATURAL JOIN works
WHERE company_name = 'First Bank Corporation' AND salary > 10000;

# 3.2 c
SELECT employee_name
FROM works
WHERE company_name != 'First Bank Corporation';

# 3.2 d
SELECT employee_name
FROM works
WHERE salary > (
  SELECT max(salary)
  FROM works
  WHERE company_name = 'Small Bank Corporation'
);

# 3.2 e
SELECT company_name
FROM company
WHERE city = (
  SELECT city
  FROM company
  WHERE company_name = 'Small Bank Corporation'
);

# 3.2 f
# Method 1:
SELECT company_name
FROM works
GROUP BY company_name
ORDER BY count(company_name) DESC
LIMIT 1;
# Method 2:
SELECT temp1.company_name
FROM (
  SELECT company_name, count(company_name) as emp_num
  FROM works
  GROUP BY company_name
) temp1
WHERE emp_num = (
  SELECT max(temp2.emp_num)
  FROM (
    SELECT company_name, count(company_name) as emp_num
    FROM works
    GROUP BY company_name
  ) temp2
);

# 3.2 g
SELECT temp1.company_name
FROM (
  SELECT company_name, avg(salary) as salary_avg
  FROM works
  GROUP BY company_name
) temp1
WHERE temp1.salary_avg > (
  SELECT avg(salary)
  FROM works
  WHERE company_name = 'First Bank Corporation'
);

# 3.9 a Find the names of all employees who work for First Bank Corporation.
SELECT employee_name
FROM works
WHERE company_name = 'First Bank Corporation';

# 3.9 b Find all employees in the database who live in the same cities as the companies for which they work.
SELECT employee_name
FROM employee NATURAL JOIN company NATURAL JOIN works;

# 3.9 c Find all employees in the database who live in the same cities and on the same streets as do their managers.
SELECT employee_name
FROM
  employee NATURAL JOIN
  (
    SELECT employee_name as manager_name,  street, city
    FROM employee
  ) temp1 NATURAL JOIN
  manages;

# 3.9 d Find all employees who earn more than the average salary of all employees of their company.
SELECT employee_name
FROM
  works NATURAL JOIN
  (
    SELECT company_name, avg(salary) as salary_avg
    FROM works
    GROUP BY company_name
  ) temp1
WHERE salary > salary_avg;

# 3.9 e Find the company that has the smallest payroll.
# 如果翻译为：找出工资总额最小的公司...那就
SELECT company_name
FROM works
GROUP BY company_name
ORDER BY sum(salary)
LIMIT 1;
