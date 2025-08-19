-- Create customers table --
CREATE OR REPLACE TABLE customers (
    customer_id INTEGER AUTOINCREMENT PRIMARY KEY,
    first_name STRING NOT NULL,
    last_name STRING NOT NULL,
    email STRING,
    signup_date DATE DEFAULT CURRENT_DATE
);
