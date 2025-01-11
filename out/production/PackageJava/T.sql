create database yygl;
use yygl;
# 科室表
create table subject(
    Sname varchar(50) not null primary key,
    Spho varchar(20) not null default " ",
    Saddr varchar(255)
)engine=Innodb;
# 病房表
create table ward(
    Wno varchar(50) not null primary key,
    Sname varchar(50) not null,
    Waddr varchar(255),
    foreign key (Sname) references subject (Sname)
)engine=Innodb;
# 病人表
create table patient(
    Pno varchar(50) not null,
    Wno varchar(50) not null,
    Pname varchar(50),
    Psex varchar(4),
    primary key (Pno),
    foreign key (Wno) references ward(Wno)
)engine=innodb;


create database xsgl;
use xsgl;
create table student(
    s_no bigint primary key auto_increment not null unique,
    s_name varchar(50) not null ,
    s_sex char(1),
    s_birthd date,
    phone varchar(13) unique ,
    email varchar(50) unique
);

show tables;
desc student;

insert into student(s_no, s_name, s_sex, s_birthd, phone, email) values ('18122221321','owen','m','1999/5/4','13945678548','ABTHE@SOHU.COM'),
       ('18122221322','john','m','2001/8/1','13675678545','12344@qq.com'),
       ('18122221323','nice','f','2000/1/10','13565678548', '55454@qq.com');
# 3
INSERT INTO student(s_name, s_birthd, phone) VALUES ('rose', '2002/1/11', '1234567891');
# 4
UPDATE student set s_name='owenwang', phone='12345566666' where s_no='18122221321';
# 5
UPDATE student set email='1234@qq.com' where s_name='owenwang';
# 6
delete from student where email='1234@qq.com';
# 7
TRUNCATE TABLE student;
# 8
DROP TABLE student;
# 9
select * from student where s_birthd < '2000';
# 10
select * from student where s_name like '赵%';
# 11
select * from student where s_name like 'o%' OR s_name like 'm%';
# 12
SELECT * FROM student WHERE s_birthd BETWEEN '1999/01/01' AND ' 2001/12/31' LIMIT 2;

SELECT * FROM student WHERE s_birthd BETWEEN '1999-01-01' AND ' 2001-12-31';

drop database xsgl;
Create Database  XSGL
use xsgl;
create table student(
                        Sno int  ,
                        Sname varchar(20),
                        Ssex char(2),
                        Sage smallint,
                        Sdept varchar(50)
);

drop table student;
create table student(
                        Sno int  primary key, /*设置sno为主键 列级约束*/
                        Sname varchar(20),
                        Ssex char(2),
                        Sage smallint,
                        Sdept varchar(50)
);

CREATE TABLE person(
                       id int unsigned   auto_increment not null ,
                       name char(20)  not null  default ' ',
                       age    int not null default 0 check(age>=0),
                       info    char(20) null,
                       primary key(id)
);
insert into person (id , name ,age , info)
values(1  , 'Green' , 21 , 'Lawyer');

insert into person (id , name ,age , info)
values(2  , 'Green2' , 21 , 'Lawyer2'),
      (3  , 'Green3' , 22 , 'Lawyer3'),
      (4  , 'Green4' , 23 , 'Lawyer4');

update  person
set        age      = 15 ,
           name   = 'LiMing'
where   id = 11;

create table fruits
(
    f_id char(10) not null primary key,
    s_id int not null,
    f_name char(255) not null,
    f_price decimal(8,2) null
);

INSERT INTO fruits
VALUES('a1',101,'apple',5.2),
      ('b1',101,'blackberry',10.2),
      ('bs1',102,'orange',11.2),
      ('bs2',105,'melon',8.2),
      ('t1',102,'banana',10.3),
      ('t2',102,'grape',5.3),
      ('o2',103,'coconut',9.2),
      ('c0',101,'cherry',3.2),
      ('a2',103,'apricot',2.2),
      ('l2',104,'lemom',6.4),
      ('b2',104,'berry',7.6),
      ('m1',106,'mango',15.7),
      ('m2',105,'xbabay',2.6),
      ('t4',107,'xbababa',3.6),
      ('m3',105,'xxtt',11.6),
      ('b5',107,'xxxx',3.6);

drop table if exists t_student;
drop table if exists t_class;

CREATE TABLE t_class(
                        cno CHAR(8) PRIMARY KEY,
                        classname CHAR(20) NOT NULL
)engine = innodb;


CREATE TABLE t_student(
                          sno CHAR(8) not null PRIMARY KEY,
                          name CHAR(20) NOT NULL,
                          sex char(1) NOT NULL,
                          cno CHAR (8) NULL,
                          foreign key (cno) references t_class(cno)
)ENGINE=innodb;

INSERT INTO t_class(cno,classname)
VALUES('101','软工1班'),
      ('102','软工2班'),
      ('103','软工3班'),
      ('104','软工4班');


INSERT INTO t_student(sno,name,sex,cno)
VALUES('202001','July','男','101'),
      ('202002','Lisa','女','101'),
      ('202003','Python','男','102'),
      ('202004','Java','男','104');

SELECT sName as '姓名', sNo as '学号', sbDate as '出生日期', sPhone as '电话号码' FROM student WHERE sBDate BETWEEN '2013-01-01' AND '2016-12-31' AND sName LIKNE '邓%' AND sPhone IS NOT NULL;

SELECT tno,cno, COUNT(clsNo) FROM class GROUP BY tNo HAVING COUNT(clsNo) BETWEEN 2 AND 4 ORDER BY COUNT(clsNo);

SELECT cName, cPrice, psDate, psTimes FROM course INNER JOIN perstore ON course.cNo=perstore.cNo WHERE cname IN ('初中数学', '初数1');

SELECT clsNo, ConsDate FROM consume WHERE clsNo IN (SELECT clsNo FROM class WHERE clsName IN ('23秋原版周五1班', '23秋原版周六1班'));

SELECT sName, sNo FROM student s WHERE sNo IN(SELECT sNo FROM consume WHERE sNo=s.sno AND clsNo='cls008');

SELECT c.cNo, c.cName, MAX(psTimes), MIN(psTime), AVG(psTime) FROM course AS c INNER JOIN prestore AS p ON c.cNo=p.sno GROUP BY cNo HAVING AVG(psTime) > 15;

ALTER TABLE student ADD INDEX phone_idx(phone DESC);

CREATE UNIQUE INDEX cname_idx ON course(c_name, t_no);

CREATE TABLE suppliers (

                           supplier_id INT(11) PRIMARY KEY, /*供应商编号*/

                           supplier_name VARCHAR(50) NOT NULL UNIQUE /*供应商名称*/

);

drop table if exists fruits;

CREATE TABLE fruits (

                        fruit_id INT(11) PRIMARY KEY,  /*水果编号*/

                        fruit_name VARCHAR(50) NOT NULL, /*水果名称*/

                        price DECIMAL(8, 2),  /*水果单价*/

                        supplier_id INT(11), /*供应商编号*/

                        FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)  /*供应商编号外键*/

) engine = innodb;

INSERT INTO suppliers (supplier_id, supplier_name)

VALUES

    (1, 'ACME'),

    (2, 'XYZ Suppliers'),

    (3, 'ABC Fruits'),

    (5, 'Good Set'),

    (6, 'FNK Inc');

INSERT INTO fruits (fruit_id, fruit_name, price, supplier_id)

VALUES

    (1, '苹果', 5.99, 1),

    (2, '香蕉', 3.99, 2),

    (3, '橙子', 2.99, 1),

    (4, '草莓', 9.99, 3),

    (5, '葡萄', 4.99, 2),

    (6, '柠檬', 3.49, 1),

    (7, '桃子', 6.99, 3),

    (8, 'berry', 7.2, 5),

    (9, 'lemom', 3.8, 5),

    (10, '樱桃', 8.8, 6),

    (11, '西瓜', 2.1, 6),

    (12, '榴莲', 10, 2),

    (13, '橘子', 5.49, 1),

    (14, '蟠桃', 6.99, 5);

select f.fruit_name as '水果名称', f.price as '水果单价', s.supplier_name as 供应商名称
from suppliers s join fruits f on s.supplier_id = f.supplier_id;

select s.supplier_name as 供应商名称, count(*) as 水果种类
from suppliers s join fruits f on s.supplier_id = f.supplier_id
group by s.supplier_name;

select f.fruit_name as '水果名称', f.price as '水果单价'
from suppliers s join fruits f on s.supplier_id = f.supplier_id
where s.supplier_name = 'ACME'
order by f.price desc;

select f.fruit_name as '水果名称', count(*) as '供应商数量'
from suppliers s join fruits f on s.supplier_id = f.supplier_id
group by f.fruit_name having count(*) > 1
order by count(*) desc;

delimiter $$
create procedure p802test(IN vsNo varchar(10), out vconSum int(7))
begin
    select sum(consflay) into vconSum from consume where vsNo = '00056';
end $$
delimiter ;
set @sno = '00056';
call p802test(@sno, @conSum);
select @sno '学号', @consum '耗课总数';

create database GMS;
create table contestants(
    cid varchar(10) not null primary key comment '选手编号',
    cname varchar(30) comment '选手姓名',
    cage int comment '选手年龄',
    csex varchar(4) comment '选手性别'
);
create table goods(
    gid varchar(10) not null primary key comment '商品代码',
    gname varchar(50) comment '商品名称',
    gprice decimal(10, 2) comment '商品单价'
);
create table sales(
    cid varchar(10) not null comment '选手编号',
    gid varchar(10) not null comment '商品代码',
    sdate date not null comment '销售日期',
    samount int comment '销售数量',
    primary key(cid, gid, sdate)
);
insert into contestants values ('c000101', '李丽', 18, '女'),('c000102', '张凯', 17, '男');
update contestants set cname='张美丽' where cid='c000101';
delete from goods where gprice between 10 and 20;
select g.gid, gname, s.samount from goods g join sales s on g.gid=s.gid;
select cname, gname, sdate, samount from contestants c join goods g join sales s on s.cid=c.cid and g.gid=s.gid
where c.cname = '李丽'
order by sdate desc limit 2;
create view v_contestants as select cid, cname, cage from contestants where cage < 18;
delimiter $$
create procedure p_getInfo(in d_date date)
begin
    select c.cid, g.gid, sdate, samount from contestants c join goods g join sales s on s.cid=c.cid and g.gid=s.gid
    where sdate > d_date;
end $$
delimiter ;

create database testdb;
use testdb;
create table book(
    id int not null auto_increment primary key ,
    book_name varchar(50),
    book_author varchar(50)
)engine=innodb character set "utf8";
insert into book(book_name, book_author) values ("Java程序设计", "龚自珍"), ("Python程序设计", "杨文思");

create TABLE student(
    id int not null auto_increment primary key ,
    name varchar(50),
    age int
);