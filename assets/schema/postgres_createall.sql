CREATE TABLE IF NOT EXISTS transactions_events(
   id serial PRIMARY KEY,
   t_datetime timestamp,
   t_epoch_datetime int,
   sender_username text,
   sender_name text,
   receiver_username text,
   receiver_name text,
   source_ip inet,
   destination_ip inet,
   amount numeric,
   currency_code text,
   currency_name text,
   mac_address macaddr,
   success boolean,
   comment text 
);


CREATE TABLE IF NOT EXISTS user_profile(
   id serial PRIMARY KEY,
   username text,
   name text,
   job text,
   company text,
   ssn text,
   residence text,
   current_location point,
   blood_group text,
   website text,
   sex text,
   address text,
   mail text,
   birthdate date
);