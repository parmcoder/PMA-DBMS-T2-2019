
/*BEFORE RUNNING THIS SQL, PLEASE IMPORT YOUR DATA ONTO SERVER FIRST */
create unlogged table medicine_import (doc json); --To hold medicine.json and so on
create unlogged table patient_import (doc json);

/*FILE PROCESS REQUIRED TO FORMAT VALID JSON INTO IMPORT READY VALID JSON */
-- # sed -i 's/\\/\\\\/g'        -Backslash will be accepted now
-- # sed -i 's/\\\"/\\\\\"/g'    -Double quoting will be accepted now

/*RUN THIS COMMAND ON YOUR SERVER ON EACH JSON*/
-- \copy YOUR_FILE_import from '/home/parmcoder/dataLab_101/yelp_academic_2018/YOUR_FILE.json';
-- This is the recommended method by postgresql to import JSON data. We will keep these files forever as a backup.
-- CONSTRAINT : Nothing is perfect, except the JSON files the run in using this command. It must be IDEAL.

CREATE TABLE medicine(
                         stock_id integer,
                         exp_date date,
                         company_name varchar,
                         brand_name varchar,
                         description varchar,
                         price float,
                         quantity integer,
                         PRIMARY KEY (stock_id));

CREATE TABLE patient(
                         pid integer,
                         p_name varchar,
                         allergy varchar,
                         PRIMARY KEY (pid));

CREATE TABLE receipt(
                         rid integer,
                         total integer,
                         pid integer,
                         r_date date,
                         PRIMARY KEY (rid),
                         FOREIGN KEY (pid) REFERENCES patient(pid));


CREATE TABLE prescription(
                         rid integer,
                         stock_id integer,
                         quantity integer,
                         FOREIGN KEY (stock_id) REFERENCES medicine(stock_id),
                         FOREIGN KEY (rid) REFERENCES receipt(rid));


insert into medicine(
                         stock_id,
                         exp_date,
                         company_name,
                         brand_name,
                         description,
                         price,
                         quantity )
select (p.doc->>'stock_id')::integer,
       (p.doc->>'exp_date')::date,
       p.doc->>'company_name',
       p.doc->>'brand_name',
       p.doc->>'description',
       (p.doc->>'price')::float,
       (p.doc->>'quantity')::integer
from medicine_import as p
on conflict (stock_id) do update
  set stock_id     = excluded.stock_id,
      exp_date     = excluded.exp_date,
      company_name = excluded.company_name,
      brand_name   = excluded.brand_name,
      description  = excluded.description,
      price        = excluded.price,
      quantity     = excluded.quantity;

insert into patient(
                         pid,
                         p_name,
                         allergy  )
select (p.doc->>'pid')::integer,
       p.doc->>'p_name',
       p.doc->>'allergy'
from patient_import as p
on conflict (pid) do update
  set pid     = excluded.pid,
      p_name  = excluded.p_name,
      allergy = excluded.allergy;