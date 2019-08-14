-SELECT * FROM demo;
--create table consultation1(pid,fees,health,hiredate,age);
--insert into consultation1(pid,fees,health,hiredate,age)values(142,1000,'normal',date(),19);
--select * from consultation1;
--SELECT pid,fees,health from consultation1;
--create table sample1(available_time char(4) check (available_time in('mor','sun')));
--insert into sample values('mor');
--insert into sample values('sun');
--select *from sample1
--create table patient2(pname,pid,pcity,pgender)
--insert into patient2 values('savi',11,'chennai','female');
--insert into patient2 values('ajay',12,'chennai','male');
--insert into patient2 values('saran',13,'vellore','male');
--select pname from patient2 where pcity='chennai';
--select count(pgender) from patient2 where pgender='male';
select pid,,age,health,pname,pgender from consultation1 c1 join patient2 p1 on c1.cid=p1.pid;

