DROP USER IF EXISTS 'adventures_user'@'localhost';

CREATE USER 'adventures_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'adventures';

GRANT ALL PRIVILEGES ON outland_adventures.* TO 'adventures_user'@'localhost';
