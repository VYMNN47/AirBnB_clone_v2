-- prepares a MySQL server for this project
-- A database hbnb_dev_db
-- A new user hbnb_dev (in localhost) password set to hbnb_dev_pwd
-- hbnb_dev should have all privileges on database hbnb_dev_db
-- (and only this database)
-- hbnb_dev should have SELECT privilege on database performance_schema
-- (and only this database)
-- If database hbnb_dev_db or user hbnb_dev already exists, script
-- should not fail

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
