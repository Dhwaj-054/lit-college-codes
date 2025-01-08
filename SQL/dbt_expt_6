create database expt_6;
use expt_6;

create table customer
(
c_no int primary key,
c_name varchar(40), 
c_age  int,
c_add varchar(40)
);
desc customer;

create table loan
(
 c_no int ,
 l_no int primary key ,
 loan_amt int,
 l_date varchar(40),
 foreign key (c_no) references customer(c_no)
 );
 desc loan;
 
 insert into customer values(001, 'Jenny', 25, '6th street NY');
 insert into customer values(002, 'John', 45, 'South street Delhi');
 insert into customer values(003, 'Sam', 31, 'North street Mumbai');
 insert into customer values(004, 'Mariam', 39, 'Forier Chennai');
 
 insert into loan values(001, 10, 56000, '6th feb');
 insert into loan values(002, 12, 76000, '10th dec');
 insert into loan values(003, 14, 450000, '1st jan');
 insert into loan values(004, 16, 90000, '8th apr');
 
  select * from customer;
 select * from loan;
 
          
  -- q1 
  create view Customer_detail
  as (select c.c_no, c.c_name, l.loan_amt
  from customer c inner join loan l on c.c_no=l.c_no
  where c.c_no=l.c_no and l.loan_amt between 50000 and 100000);
  select * from Customer_detail;
  
   -- q2
  select c_name  
  from Customer_detail
  where loan_amt <80000;
  
   -- q3
  select c_name 
  from Customer_detail
  where c_name like "%m" and loan_amt =90000;
