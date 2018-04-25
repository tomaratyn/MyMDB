CREATE DATABASE mymdb;
 
CREATE USER mymdb;
 
GRANT ALL ON DATABASE mymdb to "mymdb";
 
ALTER USER mymdb PASSWORD 'development';
ALTER USER mymdb CREATEDB;

