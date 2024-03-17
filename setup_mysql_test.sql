-- prepares a MySQL server for this project
-- A database hbnb_test_db
-- A new user hbnb_test (in localhost) password set to hbnb_test_pwd
-- hbnb_dev should have all privileges on database hbnb_test_db
-- (and only this database)
-- hbnb_dev should have SELECT privilege on database performance_schema
-- (and only this database)
-- If database hbnb_test_db or user hbnb_dev already exists, script
-- should not fail

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
