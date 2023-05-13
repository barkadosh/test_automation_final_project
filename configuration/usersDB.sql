
#################################################################################
# SQL query used for creating the data for test cases in  module test_web_db.py #
#################################################################################


create table UsersFinalProjectAut(
id int,
name varchar(10),
password varchar(10),
comment varchar(20)
);
insert into UsersFinalProjectAut values(1, 'test1', 123456, '');
insert into UsersFinalProjectAut values(2, 'test2', 'abcd', 'test');
insert into UsersFinalProjectAut values(3, 'admin', 'admin', 'correct');
insert into UsersFinalProjectAut values(4, 'test3', '123abc', 'king');


SELECT * FROM automationtestspython.usersfinalprojectaut;