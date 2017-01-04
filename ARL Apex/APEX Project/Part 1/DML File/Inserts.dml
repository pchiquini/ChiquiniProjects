truncate table F15F4_Auth;
truncate table F15F4_Comment;
truncate table F15F4_Contact;
truncate table F15F4_Doc;
truncate table F15F4_Emp;
truncate table F15F4_Hist;
truncate table F15F4_Lab;
truncate table F15F4_RFE;
truncate table F15F4_Role;
truncate table F15F4_Status;
truncate table F15F4_Task;

alter trigger F15F4_Auth_PK_trig disable;
alter trigger F15F4_Comment_PK_trig disable;
alter trigger F15F4_Contact_PK_trig disable;
alter trigger F15F4_Doc_PK_trig disable;
alter trigger F15F4_Emp_PK_trig disable;
alter trigger F15F4_Hist_PK_trig disable;
alter trigger F15F4_Lab_PK_trig disable;
alter trigger F15F4_RFE_PK_trig disable;
alter trigger F15F4_Role_PK_trig disable;
alter trigger F15F4_Status_PK_trig disable;
alter trigger F15F4_Task_PK_trig disable;

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
                       'Chairperson: Patty ChickTeeny',
                       'PC@NotARealEmail.com',
                       'GDC 1.1',
                       '11111111',
                       'A',
                       SYSDATE,
                       'N',
                       'N',
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
                       'Exec Dir: Justine ChooChooTran',
                       'JC@NotARealEmail.com',
                       'GDC 2.2',
                       '22222222',
                       'A',
                       SYSDATE,
                       'N',
                       'N',
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
                       'Lab Dir: Nick ShamWow',
                       'NS@NotARealEmail.com',
                       'GDC 3.3',
                       '33333333',
                       'I',
                       SYSDATE,
                       'N',
                       'Y',
                       'N',
                       'N',
                       111,
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
                       'Sys Admin: Jack Heinekin',
                       'JH@NotARealEmail.com',
                       'GDC 4.4',
                       '44444444',
                       'I',
                       SYSDATE,
                       'Y',
                       'N',
                       'N',
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
                      (5,
                       'Basic Emp: Josephine Canadian',
                       'JC@NotARealEmail.com',
                       'GDC 5.5',
                       '55555555',
                       'A',
                       SYSDATE,
                       'N',
                       'N',
                       'N',
                       'N',
                       222,
                       1);      


INSERT INTO F15F4_RFE (rfe_id, explanation, alt_protections, approval_date, F15F4_Emp_emp_id, F15F4_Task_task_id)
VALUES (1, 'Eat an Apple', 'N/A', SYSDATE, 1, 1);  
INSERT INTO F15F4_RFE (rfe_id, explanation, alt_protections, approval_date, F15F4_Emp_emp_id, F15F4_Task_task_id)
VALUES (2, 'Eat an Orange', 'N/A', SYSDATE, 2, 2);  
INSERT INTO F15F4_RFE (rfe_id, explanation, alt_protections, approval_date, F15F4_Emp_emp_id, F15F4_Task_task_id)
VALUES (3, 'Eat a Banana', 'N/A', SYSDATE, 3, 3);  

INSERT INTO F15F4_Status (status_id, rfe_status, description)
VALUES (1, 'Entered', 'The RFE has been created but has not yet been submitted for approval.');
INSERT INTO F15F4_Status (status_id, rfe_status, description)
VALUES (2, 'Submitted', 'The RFE has been submitted to the Lab System Administrator for approval.');
INSERT INTO F15F4_Status (status_id, rfe_status, description)
VALUES (3, 'Returned', 'The RFE has been returned for further information or clarification. Once
Submitted again, it will follow the same routing as an Entered RFE.');
INSERT INTO F15F4_Status (status_id, rfe_status, description)
VALUES (4, 'Recalled', 'The requestor has recalled an RFE that has not yet reached final approval.
Once Submitted again, it will follow the same routing as an Entered RFE.');
INSERT INTO F15F4_Status (status_id, rfe_status, description)
VALUES (5, 'Rejected', 'The RFE has been rejected and cannot be implemented.');
INSERT INTO F15F4_Status (status_id, rfe_status, description)
VALUES (6, 'SA Approved', 'The Lab System Administrator has approved the RFE; it has been submitted for
Lab Director approval.');
INSERT INTO F15F4_Status (status_id, rfe_status, description)
VALUES (7, 'LD Approved', 'The Lab Director has approved the RFE; it has been submitted for Network
Security Panel approval.');
INSERT INTO F15F4_Status (status_id, rfe_status, description)
VALUES (8, 'ED Approved', 'The Lab Director has approved the RFE; it has been submitted to the
Chairperson of Security Panel approval.');
INSERT INTO F15F4_Status (status_id, rfe_status, description)
VALUES (9, 'CP Approved', 'The Executive Directors Office has given final approval for the RFE and it may
be implemented.');

INSERT INTO F15F4_Role (role_id ,role_type, description)
VALUES (1, 'Approver', 'Employee(s) who approved the RFE');
INSERT INTO F15F4_Role (role_id ,role_type, description)
VALUES (2, 'FYI Reviewer', 'Employee(s) who review the RFE');

alter trigger F15F4_Auth_PK_trig enable;
alter trigger F15F4_Comment_PK_trig enable;
alter trigger F15F4_Contact_PK_trig enable;
alter trigger F15F4_Doc_PK_trig enable;
alter trigger F15F4_Emp_PK_trig enable;
alter trigger F15F4_Hist_PK_trig enable;
alter trigger F15F4_Lab_PK_trig enable;
alter trigger F15F4_RFE_PK_trig enable;
alter trigger F15F4_Role_PK_trig enable;
alter trigger F15F4_Status_PK_trig enable;
alter trigger F15F4_Task_PK_trig enable;
