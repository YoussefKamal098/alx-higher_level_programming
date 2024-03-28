-- The script that creates the database hbtn_0d_2 and the user user_0d_2.
CREATE IF NOT EXISTS DATABASE hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTITY BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
