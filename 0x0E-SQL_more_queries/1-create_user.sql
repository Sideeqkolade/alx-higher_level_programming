-- a script that creates the MySQL server user user_0d_1.
-- user_0d_1 should have all privileges on your MySQL server
-- The user_0d_1 password should be set to user_0d_1_pwd
-- If the user user_0d_1 already exists, your script should not fai

CREATE USER user_0d_1 IF NOT EXISTS IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON user_0d_1*.*;

