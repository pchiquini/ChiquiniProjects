-- Generated by Oracle SQL Developer Data Modeler 4.1.1.888
--   at:        2015-11-18 18:12:17 CST
--   site:      Oracle Database 11g
--   type:      Oracle Database 11g




DROP TABLE F15F4_Auth CASCADE CONSTRAINTS ;

DROP TABLE F15F4_Comment CASCADE CONSTRAINTS ;

DROP TABLE F15F4_Contact CASCADE CONSTRAINTS ;

DROP TABLE F15F4_Doc CASCADE CONSTRAINTS ;

DROP TABLE F15F4_Emp CASCADE CONSTRAINTS ;

DROP TABLE F15F4_Hist CASCADE CONSTRAINTS ;

DROP TABLE F15F4_Lab CASCADE CONSTRAINTS ;

DROP TABLE F15F4_RFE CASCADE CONSTRAINTS ;

DROP TABLE F15F4_Role CASCADE CONSTRAINTS ;

DROP TABLE F15F4_Status CASCADE CONSTRAINTS ;

DROP TABLE F15F4_Task CASCADE CONSTRAINTS ;

CREATE TABLE F15F4_Auth
  ( auth_id INTEGER NOT NULL , RIGHT VARCHAR2 (10)
  ) ;
ALTER TABLE F15F4_Auth ADD CONSTRAINT F15F4_Auth_PK PRIMARY KEY ( auth_id ) ;


CREATE TABLE F15F4_Comment
  (
    comment_id       INTEGER NOT NULL ,
    entry_date       DATE ,
    comments         VARCHAR2 (4000) ,
    F15F4_RFE_rfe_id INTEGER ,
    F15F4_Emp_emp_id INTEGER
  ) ;
ALTER TABLE F15F4_Comment ADD CONSTRAINT F15F4_Comment_PK PRIMARY KEY ( comment_id ) ;


CREATE TABLE F15F4_Contact
  (
    contact_id         INTEGER NOT NULL ,
    eff_date           DATE ,
    comments           VARCHAR2 (4000) ,
    F15F4_RFE_rfe_id   INTEGER NOT NULL ,
    F15F4_Emp_emp_id   INTEGER NOT NULL ,
    F15F4_Role_role_id INTEGER
  ) ;
ALTER TABLE F15F4_Contact ADD CONSTRAINT F15F4_Contact_PK PRIMARY KEY ( contact_id ) ;


CREATE TABLE F15F4_Doc
  (
    doc_id   INTEGER NOT NULL ,
    name     VARCHAR2 (4000) ,
    mimetype VARCHAR2 (512) ,
    charset  VARCHAR2 (512) ,
    BLOB BLOB ,
    comments         VARCHAR2 (4000) ,
    tags             VARCHAR2 (4000) ,
    F15F4_RFE_rfe_id INTEGER
  ) ;
ALTER TABLE F15F4_Doc ADD CONSTRAINT F15F4_Doc_PK PRIMARY KEY ( doc_id ) ;


CREATE TABLE F15F4_Emp
  (
    emp_id             INTEGER NOT NULL ,
    emp_name           VARCHAR2 (30) ,
    emp_email          VARCHAR2 (100) ,
    emp_office         VARCHAR2 (12) ,
    emp_phone          VARCHAR2 (8) ,
    emp_status         VARCHAR2 (1) ,
    status_eff_date    DATE ,
    sys_admin          VARCHAR2 (1) ,
    lab_dir            VARCHAR2 (1) ,
    exec_dir           VARCHAR2 (1) ,
    chairperson        VARCHAR2 (1) ,
    F15F4_Lab_lab_id   INTEGER ,
    F15F4_Auth_auth_id INTEGER
  ) ;
ALTER TABLE F15F4_Emp ADD CONSTRAINT F15F4_Emp_PK PRIMARY KEY ( emp_id ) ;


CREATE TABLE F15F4_Hist
  (
    hist_id                INTEGER NOT NULL ,
    eff_date               DATE ,
    F15F4_RFE_rfe_id       INTEGER ,
    F15F4_Status_status_id INTEGER ,
    F15F4_Emp_emp_id       INTEGER
  ) ;
ALTER TABLE F15F4_Hist ADD CONSTRAINT F15F4_Hist_PK PRIMARY KEY ( hist_id ) ;


CREATE TABLE F15F4_Lab
  ( lab_id INTEGER NOT NULL
  ) ;
ALTER TABLE F15F4_Lab ADD CONSTRAINT F15F4_Lab_PK PRIMARY KEY ( lab_id ) ;


CREATE TABLE F15F4_RFE
  (
    rfe_id             INTEGER NOT NULL ,
    explanation        VARCHAR2 (4000) ,
    alt_protections    VARCHAR2 (4000) ,
    approval_date      DATE ,
    F15F4_Emp_emp_id   INTEGER ,
    F15F4_Task_task_id INTEGER
  ) ;
ALTER TABLE F15F4_RFE ADD CONSTRAINT F15F4_RFE_PK PRIMARY KEY ( rfe_id ) ;


CREATE TABLE F15F4_Role
  (
    role_id     INTEGER NOT NULL ,
    role_type   VARCHAR2 (30) ,
    description VARCHAR2 (500)
  ) ;
ALTER TABLE F15F4_Role ADD CONSTRAINT F15F4_Role_PK PRIMARY KEY ( role_id ) ;


CREATE TABLE F15F4_Status
  (
    status_id   INTEGER NOT NULL ,
    rfe_status  VARCHAR2 (30) ,
    description VARCHAR2 (500)
  ) ;
ALTER TABLE F15F4_Status ADD CONSTRAINT F15F4_Status_PK PRIMARY KEY ( status_id ) ;


CREATE TABLE F15F4_Task
  (
    task_id     INTEGER NOT NULL ,
    eff_date    DATE ,
    task_abbrev VARCHAR2 (15) ,
    task_desc   VARCHAR2 (4000)
  ) ;
ALTER TABLE F15F4_Task ADD CONSTRAINT F15F4_Task_PK PRIMARY KEY ( task_id ) ;


ALTER TABLE F15F4_Comment ADD CONSTRAINT F15F4_Comment_F15F4_Emp_FK FOREIGN KEY ( F15F4_Emp_emp_id ) REFERENCES F15F4_Emp ( emp_id ) ;

ALTER TABLE F15F4_Comment ADD CONSTRAINT F15F4_Comment_F15F4_RFE_FK FOREIGN KEY ( F15F4_RFE_rfe_id ) REFERENCES F15F4_RFE ( rfe_id ) ;

ALTER TABLE F15F4_Contact ADD CONSTRAINT F15F4_Contact_F15F4_Emp_FK FOREIGN KEY ( F15F4_Emp_emp_id ) REFERENCES F15F4_Emp ( emp_id ) ;

ALTER TABLE F15F4_Contact ADD CONSTRAINT F15F4_Contact_F15F4_RFE_FK FOREIGN KEY ( F15F4_RFE_rfe_id ) REFERENCES F15F4_RFE ( rfe_id ) ;

ALTER TABLE F15F4_Contact ADD CONSTRAINT F15F4_Contact_F15F4_Role_FK FOREIGN KEY ( F15F4_Role_role_id ) REFERENCES F15F4_Role ( role_id ) ;

ALTER TABLE F15F4_Doc ADD CONSTRAINT F15F4_Doc_F15F4_RFE_FK FOREIGN KEY ( F15F4_RFE_rfe_id ) REFERENCES F15F4_RFE ( rfe_id ) ;

ALTER TABLE F15F4_Emp ADD CONSTRAINT F15F4_Emp_F15F4_Auth_FK FOREIGN KEY ( F15F4_Auth_auth_id ) REFERENCES F15F4_Auth ( auth_id ) ;

ALTER TABLE F15F4_Emp ADD CONSTRAINT F15F4_Emp_F15F4_Lab_FK FOREIGN KEY ( F15F4_Lab_lab_id ) REFERENCES F15F4_Lab ( lab_id ) ;

ALTER TABLE F15F4_Hist ADD CONSTRAINT F15F4_Hist_F15F4_Emp_FK FOREIGN KEY ( F15F4_Emp_emp_id ) REFERENCES F15F4_Emp ( emp_id ) ;

ALTER TABLE F15F4_Hist ADD CONSTRAINT F15F4_Hist_F15F4_RFE_FK FOREIGN KEY ( F15F4_RFE_rfe_id ) REFERENCES F15F4_RFE ( rfe_id ) ;

ALTER TABLE F15F4_Hist ADD CONSTRAINT F15F4_Hist_F15F4_Status_FK FOREIGN KEY ( F15F4_Status_status_id ) REFERENCES F15F4_Status ( status_id ) ;

ALTER TABLE F15F4_RFE ADD CONSTRAINT F15F4_RFE_F15F4_Emp_FK FOREIGN KEY ( F15F4_Emp_emp_id ) REFERENCES F15F4_Emp ( emp_id ) ;

ALTER TABLE F15F4_RFE ADD CONSTRAINT F15F4_RFE_F15F4_Task_FK FOREIGN KEY ( F15F4_Task_task_id ) REFERENCES F15F4_Task ( task_id ) ;

-- Oracle SQL Developer Data Modeler Summary Report: 
-- 
-- CREATE TABLE                            11
-- CREATE INDEX                             0
-- ALTER TABLE                             24
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0


INSERT INTO F15F4_Lab (lab_id) VALUES (111);
INSERT INTO F15F4_Lab (lab_id) VALUES (222);
INSERT INTO F15F4_Lab (lab_id) VALUES (333);

INSERT INTO F15F4_Auth (auth_id, RIGHT) VALUES (0, 'View');
INSERT INTO F15F4_Auth (auth_id, RIGHT) VALUES (1, 'Edit');

INSERT INTO F15F4_Task (task_id, eff_date, task_abbrev, task_desc)
VALUES (1, SYSDATE, 'Eat', 'Go get some munchies to gobble on');      
INSERT INTO F15F4_Task (task_id, eff_date, task_abbrev, task_desc)
VALUES (2, SYSDATE, 'Sleep', 'Errbody has to go get some Zzzs'); 
INSERT INTO F15F4_Task (task_id, eff_date, task_abbrev, task_desc)
VALUES (3, SYSDATE, 'Rave', 'Skrillex, Calvin Harris, and the like');

INSERT INTO F15F4_Emp (emp_id, 
                       emp_name,
                       emp_email,
                       emp_office,
                       emp_phone,
                       emp_status,
                       status_eff_date,
                       sys_admin,
                       lab_dir,
                       exec_dir,
                       chairperson,
                       F15F4_Lab_lab_id,
                       F15F4_Auth_auth_id)
VALUES
                      (1,
                       'Patty ChickTeeny',
                       'PC@NotARealEmail.com',
                       'GDC 1.1',
                       '11111111',
                       'A',
                       SYSDATE,
                       'Y',
                       'Y',
                       'N',
                       'Y',
                       111,
                       1);


INSERT INTO F15F4_Emp (emp_id, 
                       emp_name,
                       emp_email,
                       emp_office,
                       emp_phone,
                       emp_status,
                       status_eff_date,
                       sys_admin,
                       lab_dir,
                       exec_dir,
                       chairperson,
                       F15F4_Lab_lab_id,
                       F15F4_Auth_auth_id)
VALUES
                      (2,
                       'Justine ChooChooTran',
                       'JC@NotARealEmail.com',
                       'GDC 2.2',
                       '22222222',
                       'A',
                       SYSDATE,
                       'Y',
                       'Y',
                       'Y',
                       'N',
                       111,
                       1);

INSERT INTO F15F4_Emp (emp_id, 
                       emp_name,
                       emp_email,
                       emp_office,
                       emp_phone,
                       emp_status,
                       status_eff_date,
                       sys_admin,
                       lab_dir,
                       exec_dir,
                       chairperson,
                       F15F4_Lab_lab_id,
                       F15F4_Auth_auth_id)
VALUES
                      (3,
                       'Nick ShamWow',
                       'NS@NotARealEmail.com',
                       'GDC 3.3',
                       '33333333',
                       'I',
                       SYSDATE,
                       'Y',
                       'N',
                       'N',
                       'N',
                       222,
                       0);

INSERT INTO F15F4_Emp (emp_id, 
                       emp_name,
                       emp_email,
                       emp_office,
                       emp_phone,
                       emp_status,
                       status_eff_date,
                       sys_admin,
                       lab_dir,
                       exec_dir,
                       chairperson,
                       F15F4_Lab_lab_id,
                       F15F4_Auth_auth_id)
VALUES
                      (4,
                       'Jack Heinekin',
                       'JH@NotARealEmail.com',
                       'GDC 4.4',
                       '44444444',
                       'I',
                       SYSDATE,
                       'N',
                       'Y',
                       'N',
                       'N',
                       222,
                       1);

INSERT INTO F15F4_Emp (emp_id, 
                       emp_name,
                       emp_email,
                       emp_office,
                       emp_phone,
                       emp_status,
                       status_eff_date,
                       sys_admin,
                       lab_dir,
                       exec_dir,
                       chairperson,
                       F15F4_Lab_lab_id,
                       F15F4_Auth_auth_id)
VALUES
                      (5,
                       'Josephine Canadian',
                       'JC@NotARealEmail.com',
                       'GDC 5.5',
                       '55555555',
                       'A',
                       SYSDATE,
                       'Y',
                       'Y',
                       'N',
                       'N',
                       333,
                       1);      


INSERT INTO F15F4_RFE (rfe_id, explanation, alt_protections, approval_date, F15F4_Emp_emp_id, F15F4_Task_task_id)
VALUES (1, 'Eat an Apple', 'N/A', SYSDATE, 1, 1);  
INSERT INTO F15F4_RFE (rfe_id, explanation, alt_protections, approval_date, F15F4_Emp_emp_id, F15F4_Task_task_id)
VALUES (2, 'Eat an Orange', 'N/A', SYSDATE, 2, 2);  
INSERT INTO F15F4_RFE (rfe_id, explanation, alt_protections, approval_date, F15F4_Emp_emp_id, F15F4_Task_task_id)
VALUES (3, 'Eat a Banana', 'N/A', SYSDATE, 3, 3);  
