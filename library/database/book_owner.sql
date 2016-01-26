DROP TABLE IF EXISTS book_owner;

CREATE TABLE book_owner(
id integer primary key autoincrement,
book NVARCHAR not null,
owner NVARCHAR not null,
url  NVARCHAR(1000) not null,
category  NVARCHAR not null,
buytime  NVARCHAR not null
);

--INSERT INTO book_owner (book, name) values ("IT项目管理成长手记", "sgao");
--INSERT INTO book_owner (book, name) values ("自动化测试最佳实践", "shihliu");
--INSERT INTO book_owner (book, name) values ("Linux命令行与Shell脚本编程大全", "liliu");
INSERT INTO book_owner
(book, owner, url, category, buytime)
values
("IT项目管理成长手记", "sgao", "http://item.jd.com/11162058.html", "Management", "Before 2015"),
("自动化测试最佳实践", "shihliu", "http://item.jd.com/11221731.html", "Skill", "Before 2015"),
("Linux命令行与Shell脚本编程大全", "liliu", "http://item.jd.com/11075150.html", "Skill", "Before 2015"),
("Ruby入门权威经典", "soliu", "http://item.jd.com/10286344.html", "Skill", "Before 2015"),
("PostgreSQL 9从零开始学", "gxing", "http://item.jd.com/11209144.html", "Skill", "Before 2015"),
("Linux命令行与Shell脚本编程大全", "qianzhan", "http://item.jd.com/11075150.html", "Skill", "Before 2015"),
("Python Web开发学习实录", "soliu", "http://item.jd.com/10843000.html", "Skill", "Before 2015"),
("从算法到程序", "liliu", "http://item.jd.com/11712426.html", "Skill", "Before 2015"),
("循序渐进Linux基础知识 服务器搭建 系统管理 性能调优 集群应用", "soliu", "http://item.jd.com/10063962.html", "Skill", "Before 2015"),
("情商1-4", "qianzhan", "http://item.jd.com/11461303.html", "Communication", "Q3FY15"),
("跟任何人都聊得来", "qianzhan", "http://item.jd.com/11496924.html", "Communication", "Q3FY15"),
("单元测试的艺术(第二版)", "qianzhan", "http://item.jd.com/11514864.html", "Skill", "Q3FY15"),
("大数据时代", "shihliu", "http://item.jd.com/11143153.html", "Skill", "Q3FY15"),
("OpenStack开源云王者归来", "shihliu", "http://item.jd.com/11521443.html", "Skill", "Q3FY15"),
("XML建明教程", "soliu", "http://item.jd.com/10400009.html", "Skill", "Q3FY15"),
("LEAN IN", "soliu", "http://item.jd.com/19544985.html", "Leadership", "Q4FY15"),
("MySQL必知必会", "soliu", "http://item.jd.com/10063118.html", "Skill", "Q4FY15"),
("Jenkins: The Definitive Guide", "sgao", "http://item.jd.com/1142122822.html", "Skill", "Q1FY16"),
("Getting Things Done: The Art of Stress-Free Productivity", "hsun", "http://item.jd.com/19538697.html", "Skill", "Q2FY16"),
("向死而生：我修的死亡学分", "gxing", "向死而生：我修的死亡学分", "Famous Person", "Q2FY16"),
("乔布斯传", "soliu", "http://item.jd.com/1439168307.html", "Famous Person", "Q2FY16");

--INSERT INTO book_owner (book, name) values ("Linux", "soliu");
