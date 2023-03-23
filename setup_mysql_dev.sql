-- script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS 'hbnb_dev_db'
CREATE USER 'hbnb_test'@'localhost' IDENTITY BY 'hbnb_dev_pwd'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_dev_db'@'localhost'
GRANT SELECT ON performance_schema.* TO 'hbnb_dev_db'@'localhost'