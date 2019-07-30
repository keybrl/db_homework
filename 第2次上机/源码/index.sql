DROP TABLE IF EXISTS account191_tryindex;
CREATE TABLE account191_tryindex (
  account_number CHAR(10),
  branch_name CHAR(15),
  balance NUMERIC(12, 2),
  CONSTRAINT chk_balance CHECK (balance >= 0)
);

DROP INDEX an_index ON account191_tryindex;
SELECT count(*) FROM account191_tryindex;
SELECT * FROM account191_tryindex WHERE account_number = 'M-00002333';

CREATE INDEX an_index ON account191_tryindex(account_number);
SELECT * FROM account191_tryindex WHERE account_number = 'M-00002333';