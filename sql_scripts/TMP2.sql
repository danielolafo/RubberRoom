SELECT * FROM allocation_site als JOIN allocation_site_tag ast ON als.id=ast.allocation_site_id JOIN tag t ON ast.tag_id = t.id JOIN user_interactions ui ON activity_id=als.id AND activity_entity='allocation_site' WHERE ui.user_id<>9 

SELECT * FROM allocation_site als JOIN allocation_site_tag ast ON als.id=ast.allocation_site_id JOIN tag t ON ast.tag_id = t.id order by random() limit 10;
select * from user_interactions;
select * from users; --1 to 14
select * from allocation_site; --29 to 33
delete  from user_interaction;
select * from allocation_site_tag;

SELECT * FROM allocation_site als JOIN allocation_site_tag ast ON als.id=ast.allocation_site_id JOIN tag t ON ast.tag_id = t.id JOIN user_interactions ui ON activity_id=als.id AND activity_entity='allocation_site' WHERE ui.user_id<>9 GROUP BY als.id 

SELECT * from (SELECT * FROM allocation_site als JOIN allocation_site_tag ast ON als.id=ast.allocation_site_id) as sourcet
pivot(sourcet.tag_id FOR ast.tag_id IN (1,2));

SELECT * FROM allocation_site_tag ast JOIN tag t ON ast.tag_id=t.id JOIN 
SELECT t.id, t.description FROM allocation_site als 
        JOIN allocation_site_tag ast ON als.id=ast.allocation_site_id 
        JOIN tag t ON ast.tag_id = t.id 
        JOIN user_interactions ui ON activity_id=als.id AND activity_entity='allocation_site' 
        WHERE ui.user_id<>0 ORDER BY RANDOM() LIMIT 10;

--User viewed tags
SELECT * FROM (SELECT DISTINCT t.id, t.description FROM allocation_site als 
        JOIN allocation_site_tag ast ON als.id=ast.allocation_site_id 
        JOIN tag t ON ast.tag_id = t.id 
        JOIN user_interactions ui ON activity_id=als.id AND activity_entity='allocation_site' 
        WHERE ui.user_id=9) ORDER BY RANDOM() LIMIT 10;

SELECT * FROM user_tags ut JOIN tag t ON ut.tag_id=t.id WHERE ut.user_id0

SELECT * FROM CROSSTAB('SELECT t.id, t.description FROM allocation_site als 
        JOIN allocation_site_tag ast ON als.id=ast.allocation_site_id 
        JOIN tag t ON ast.tag_id = t.id 
        JOIN user_interactions ui ON activity_id=als.id  
        WHERE ui.user_id<>0 ORDER BY RANDOM() LIMIT 10')

INSERT INTO user_interactions(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('20/02/2019','DD/MM/YYYY'),'allocation_site',28,4);
INSERT INTO user_interactions(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('13/08/2021','DD/MM/YYYY'),'allocation_site',28,5);
INSERT INTO user_interactions(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('04/06/2023','DD/MM/YYYY'),'allocation_site',29,6);
INSERT INTO user_interactions(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('08/12/2021','DD/MM/YYYY'),'allocation_site',29,7);
INSERT INTO user_interactions(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('09/11/2020','DD/MM/YYYY'),'allocation_site',30,8);
INSERT INTO user_interactions(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('16/07/2022','DD/MM/YYYY'),'allocation_site',30,9);
INSERT INTO user_interactions(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('01/04/2019','DD/MM/YYYY'),'allocation_site',31,9);
INSERT INTO user_interactions(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('06/06/2016','DD/MM/YYYY'),'allocation_site',31,11);
INSERT INTO user_interactions(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('30/04/2023','DD/MM/YYYY'),'allocation_site',32,12);
INSERT INTO user_interactions(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('15/12/2022','DD/MM/YYYY'),'allocation_site',33,12);