

CREATE table test_groups (
    name varchar(40) not null,
    test_value integer not null,
    unique(name)
);


CREATE table test_cases (
    id integer not null,
    group_name varchar(40) not null,
    status varchar(5) not null,
    unique(id)
);


insert into test_groups values ('performance', 15);
insert into test_groups values ('corner cases', 10);
insert into test_groups values ('numerical stability', 20);
insert into test_groups values ('memory usage', 10);
insert into test_cases values (13, 'memory usage', 'OK');
insert into test_cases values (14, 'numerical stability', 'OK');
insert into test_cases values (15, 'memory usage', 'ERROR');
insert into test_cases values (16, 'numerical stability', 'OK');
insert into test_cases values (17, 'numerical stability', 'OK');
insert into test_cases values (18, 'performance', 'ERROR');
insert into test_cases values (19, 'performance', 'ERROR');
insert into test_cases values (20, 'memory usage', 'OK');
insert into test_cases values (21, 'numerical stability', 'OK');


/*
Write an sql query that summarizes each group of tests. The table of result should contain four columns:
name: the name of the group;
all_test_cases: the number of all test cases in the group;
passed_test_cases: the number of passed test cases in the group;
total_value: the total value of passed test cases in the group.

ROws should be ordered be ordered by decreeasing total_value. In the case of a tie,
rows should be sorted lexicographically by name.
*/





/*
WRONG ANSWER (row 2: got ('memory usage', '3', '3', '30'), expected ('memory usage', '3', '2', '20'))
*/


SELECT CASE WHEN test_groups.name = test_cases.group_name THEN test_cases.group_name ELSE test_groups.name END AS name,
        count(test_cases.group_name) AS all_test_cases,
        count(CASE WHEN test_cases.status = 'OK' THEN 1 END) AS all_test_cases,
        sum(CASE WHEN test_cases.status = 'OK' THEN test_groups.test_value ELSE 0 END) AS total_value
FROM test_groups
LEFT JOIN test_cases ON test_groups.name = test_cases.group_name
GROUP BY CASE WHEN test_groups.name = test_cases.group_name THEN test_cases.group_name ELSE test_groups.name END
ORDER BY total_value DESC, name ASC;





SELECT test_cases.group_name, count(test_cases.group_name) AS all_test_cases, count(CASE WHEN test_cases.status = 'OK' THEN 1 END) AS all_test_cases, sum(CASE WHEN test_cases.status = 'OK' THEN test_groups.test_value ELSE 0 END) AS total_value
FROM test_groups
LEFT JOIN test_cases ON test_groups.name = test_cases.group_name
GROUP BY test_cases.group_name
ORDER BY total_value DESC, test_cases.group_name ASC;





SELECT IF(test_groups.name = test_cases.group_name)
        test_cases.group_name ELSE test_groups.name,
    count(test_cases.group_name) AS all_test_cases,
    count(IF(test_cases.status = 'OK')
        test_cases.group_name ELSE test_groups.name) AS all_test_cases,
    sum(IF(test_cases.status = 'OK') test_groups.test_value ELSE 0 END) AS total_value
FROM test_groups
LEFT JOIN test_cases ON test_groups.name = test_cases.group_name
GROUP BY IF(test_groups.name = test_cases.group_name) test_cases.group_name ELSE test_groups.name
ORDER BY total_value DESC, test_cases.group_name ASC;