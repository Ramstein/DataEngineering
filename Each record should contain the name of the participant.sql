


CREATE table participation (
    name varchar(30) not null,
    year int not null,
    unique (name, year)
);


insert into participation values ('John', 2003);
insert into participation values ('Lyla', 1994);
insert into participation values ('Faith', 1996);
insert into participation values ('John', 2002);
insert into participation values ('Carol', 2000);
insert into participation values ('Carol', 1999);
insert into participation values ('John', 2001);
insert into participation values ('Carol', 2002);
insert into participation values ('Lyla', 1996);
insert into participation values ('Lyla', 1997);
insert into participation values ('Carol', 2001);
insert into participation values ('John', 2009);



/*
Write an SQL query that returns a table containing one column "name". Each record should contain the name of the participant
who took part for at least three years in a row. THe result table should be sorted alphabetically by the "name" column.
*/


select distinct name
from (select pp.*,
             lead(year, 2) over (partition by name order by year) as year2
      from participation pp
     ) pp
where year2 = year + 2;

select distinct name from (
    select participation.*,
           lag(year, 2) over (partition by name order by year) as year2
    from participation
) participation
where year2 = year - 2;