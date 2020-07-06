backup sql: mysqldump -u root -h localhost -p dbname >fred01.sql
restore sql: mysql -u root -p dbname < dbname
