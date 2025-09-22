SELECT * FROM USERS;
SELECT * FROM ALLOCATION_SITE;
SELECT * FROM MEDIA_DATA;
SELECT * FROM USER_CONTACT;
SELECT * FROM countries;
SELECT * FROM states ORDER BY name DESC;
SELECT * FROM cities;
SELECT * FROM TAG;
SELECT * FROM allocation_site_tag;

SELECT s.id, s.name, s.country_id, c.name, s.id as countryid, s.country_code, c.iso3 FROM STATES S 
join countries c on s.country_id=c.id
where c.name like 'Col%'
order by c.name, s.name;

SELECT c.name as name_1 FROM allocation_site als JOIN category_priority cp ON als.id = cp.allocation_site_id  JOIN category c ON cp.category_id = c.id UNION SELECT t.description as name_1 FROM allocation_site als JOIN allocation_site_tag ast ON als.id=ast.allocation_site_id JOIN tag t ON ast.tag_id = t.id
SELECT * FROM allocation_site als JOIN 

SELECT als.id as site_id, t.id tag_id, t.description tag_name FROM allocation_site als JOIN allocation_site_tag ast ON als.id=ast.allocation_site_id JOIN tag t ON ast.tag_id = t.id

SELECT * FROM allocation_site als JOIN allocation_site_tag ast ON als.id=ast.allocation_site_id JOIN tag t ON ast.tag_id = t.id;
SELECT t.description FROM allocation_site als JOIN allocation_site_tag ast ON als.id=ast.allocation_site_id JOIN tag t ON ast.tag_id = t.id
SELECT * FROM USERS;

INSERT INTO allocation_site(city, address, owner_id) VALUES(25222,'Building Number: 98',5);
INSERT INTO allocation_site(city, address, owner_id) VALUES(44856,'Street Address: Funkturm Berlin',9);
INSERT INTO allocation_site(city, address, owner_id) VALUES(27540,'Puerta 792 Paseo María Cristina, 8 Esc. 746, Hospitalet de LLobregat, Com 40234',10);
INSERT INTO allocation_site(city, address, owner_id) VALUES(35186,'Piazza Italo 151, Appartamento 69, Borgo Sarita, TE 93497',12);
INSERT INTO allocation_site(city, address, owner_id) VALUES(59582,'Incrocio Audenico 1, Piano 7, Fortunata laziale, OR 45264',13);
INSERT INTO allocation_site(city, address, owner_id) VALUES(61422,'Rotonda Fior 63, Marini veneto, CI 257187',14);


INSERT INTO USER_CONTACT(FRIENDS_FROM, FIRST_USER_ID, SECOND_USER_ID) VALUES(TO_DATE('20/03/2011','DD/MM/RRRR'),5,6);
INSERT INTO USER_CONTACT(FRIENDS_FROM, FIRST_USER_ID, SECOND_USER_ID) VALUES(TO_DATE('18/04/2013','DD/MM/RRRR'),5,7);
INSERT INTO USER_CONTACT(FRIENDS_FROM, FIRST_USER_ID, SECOND_USER_ID) VALUES(TO_DATE('21/12/2015','DD/MM/RRRR'),5,14);
INSERT INTO USER_CONTACT(FRIENDS_FROM, FIRST_USER_ID, SECOND_USER_ID) VALUES(TO_DATE('13/05/2016','DD/MM/RRRR'),6,11);
INSERT INTO USER_CONTACT(FRIENDS_FROM, FIRST_USER_ID, SECOND_USER_ID) VALUES(TO_DATE('09/06/2018','DD/MM/RRRR'),7,9);
INSERT INTO USER_CONTACT(FRIENDS_FROM, FIRST_USER_ID, SECOND_USER_ID) VALUES(TO_DATE('08/07/2021','DD/MM/RRRR'),7,13);
INSERT INTO USER_CONTACT(FRIENDS_FROM, FIRST_USER_ID, SECOND_USER_ID) VALUES(TO_DATE('04/12/2022','DD/MM/RRRR'),9,14);
INSERT INTO USER_CONTACT(FRIENDS_FROM, FIRST_USER_ID, SECOND_USER_ID) VALUES(TO_DATE('13/05/2022','DD/MM/RRRR'),11,13);
INSERT INTO USER_CONTACT(FRIENDS_FROM, FIRST_USER_ID, SECOND_USER_ID) VALUES(TO_DATE('20/08/2023','DD/MM/RRRR'),12,13);
INSERT INTO USER_CONTACT(FRIENDS_FROM, FIRST_USER_ID, SECOND_USER_ID) VALUES(TO_DATE('13/01/2024','DD/MM/RRRR'),13,14);
INSERT INTO USER_CONTACT(FRIENDS_FROM, FIRST_USER_ID, SECOND_USER_ID) VALUES(TO_DATE('16/10/2025','DD/MM/RRRR'),14,6);


INSERT INTO TAG(DESCRIPTION) values('City');
INSERT INTO TAG(DESCRIPTION) values('Urban');
INSERT INTO TAG(DESCRIPTION) values('Beach');
INSERT INTO TAG(DESCRIPTION) values('Cold');
INSERT INTO TAG(DESCRIPTION) values('Sunset');
INSERT INTO TAG(DESCRIPTION) values('Winter');
INSERT INTO TAG(DESCRIPTION) values('Summer');
INSERT INTO TAG(DESCRIPTION) values('France');
INSERT INTO TAG(DESCRIPTION) values('Italy');
INSERT INTO TAG(DESCRIPTION) values('Spain');
INSERT INTO TAG(DESCRIPTION) values('Relax');
INSERT INTO TAG(DESCRIPTION) values('Chill');
INSERT INTO TAG(DESCRIPTION) values('Friends');
INSERT INTO TAG(DESCRIPTION) values('Food');
INSERT INTO TAG(DESCRIPTION) values('Music');

INSERT INTO ALLOCATION_SITE_TAG(ALLOCATION_SITE_ID, TAG_ID) VALUES(28,1); --"Frankfurt am Main"
INSERT INTO ALLOCATION_SITE_TAG(ALLOCATION_SITE_ID, TAG_ID) VALUES(29,11); --"Munich"
INSERT INTO ALLOCATION_SITE_TAG(ALLOCATION_SITE_ID, TAG_ID) VALUES(30,6); --"Madrid"
INSERT INTO ALLOCATION_SITE_TAG(ALLOCATION_SITE_ID, TAG_ID) VALUES(30,10);--"Madrid"
INSERT INTO ALLOCATION_SITE_TAG(ALLOCATION_SITE_ID, TAG_ID) VALUES(31,13);--"Paris"
INSERT INTO ALLOCATION_SITE_TAG(ALLOCATION_SITE_ID, TAG_ID) VALUES(31,14);--"Paris"
INSERT INTO ALLOCATION_SITE_TAG(ALLOCATION_SITE_ID, TAG_ID) VALUES(32,11);--"Rome"
INSERT INTO ALLOCATION_SITE_TAG(ALLOCATION_SITE_ID, TAG_ID) VALUES(32,14);--"Rome"
INSERT INTO ALLOCATION_SITE_TAG(ALLOCATION_SITE_ID, TAG_ID) VALUES(32,12);--"Rome"
INSERT INTO ALLOCATION_SITE_TAG(ALLOCATION_SITE_ID, TAG_ID) VALUES(33,14);--"Toscanella"


INSERT INTO user_interaction(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('20/02/2019','DD/MM/RRRR'),'allocation_site',28,4);
INSERT INTO user_interaction(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('13/08/2021','DD/MM/RRRR'),'allocation_site',28,5);
INSERT INTO user_interaction(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('04/06/2023','DD/MM/RRRR'),'allocation_site',29,6);
INSERT INTO user_interaction(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('08/12/2021','DD/MM/RRRR'),'allocation_site',29,7);
INSERT INTO user_interaction(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('09/11/2020','DD/MM/RRRR'),'allocation_site',30,8);
INSERT INTO user_interaction(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('16/07/2022','DD/MM/RRRR'),'allocation_site',30,9);
INSERT INTO user_interaction(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('01/04/2019','DD/MM/RRRR'),'allocation_site',31,9);
INSERT INTO user_interaction(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('06/06/2016','DD/MM/RRRR'),'allocation_site',31,11);
INSERT INTO user_interaction(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('30/04/2023','DD/MM/RRRR'),'allocation_site',32,12);
INSERT INTO user_interaction(registry_date,activity_entity,activity_id,user_id) VALUES(TO_DATE('15/12/2022','DD/MM/RRRR'),'allocation_site',33,12);

