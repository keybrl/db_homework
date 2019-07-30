DROP VIEW IF EXISTS branch_detail;

CREATE VIEW branch_detail AS
SELECT
  branch_name AS 'Branch Name',
  a AS 'Deposit Account Number',
  b AS 'Total Deposits',
  c AS 'Loans Customers Number',
  d AS 'Total Loans'
FROM (
    SELECT temp11.branch_name, count(temp11.customer_name) AS a
    FROM (
        SELECT DISTINCT branch191.branch_name, customer_name
        FROM
          depositor191 NATURAL JOIN
          account191
          RIGHT JOIN branch191 ON account191 .branch_name = branch191.branch_name
      ) temp11
    GROUP BY temp11.branch_name
  ) temp1 NATURAL JOIN (
    SELECT branch191.branch_name, sum(balance) AS b
    FROM
      account191
      RIGHT JOIN branch191 ON account191.branch_name = branch191.branch_name
    GROUP BY branch191.branch_name
  ) temp2 NATURAL JOIN (
    SELECT temp31.branch_name, count(customer_name) AS c
    FROM (
        SELECT DISTINCT branch191.branch_name, customer_name
        FROM
          loan191 NATURAL JOIN
          borrower191
          RIGHT JOIN branch191 ON loan191.branch_name = branch191.branch_name
      ) temp31
    GROUP BY temp31.branch_name
  ) temp3 NATURAL JOIN (
    SELECT branch191.branch_name, sum(amount) AS d
    FROM
      loan191
      RIGHT JOIN branch191 ON loan191.branch_name = branch191.branch_name
    GROUP BY branch191.branch_name
  ) temp4;

SELECT * FROM branch_detail;