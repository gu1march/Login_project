CREATE TABLE login ( 
    ssb VARCHAR2(6),
    password_user VARCHAR2(40),
    id INT
);

INSERT ALL
  INTO login (id, ssb, password_user) VALUES (1, 'ssb111', 'loremip1')
  INTO login (id, ssb, password_user) VALUES (2, 'ssb222', 'loremip2')
  INTO login (id, ssb, password_user) VALUES (3, 'ssb333', 'loremip3')
SELECT * FROM dual;