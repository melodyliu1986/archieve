DROP TABLE IF EXISTS book_owner;

CREATE TABLE book_owner(
id integer primary key autoincrement,
book NVARCHAR not null,
name NVARCHAR not null,
url  NVARCHAR(1000) not null
);

--INSERT INTO book_owner (book, name) values ("IT项目管理成长手记", "sgao");
--INSERT INTO book_owner (book, name) values ("自动化测试最佳实践", "shihliu");
--INSERT INTO book_owner (book, name) values ("Linux命令行与Shell脚本编程大全", "liliu");
INSERT INTO book_owner
(book, name, url)
values
("IT项目管理成长手记", "sgao", "http://item.jd.com/11162058.html"),
("自动化测试最佳实践", "shihliu", "http://item.jd.com/11221731.html"),
("Linux命令行与Shell脚本编程大全", "liliu", "http://item.jd.com/11075150.html");

--INSERT INTO book_owner (book, name) values ("Linux", "soliu");
