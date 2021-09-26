create_keyspace = """CREATE KEYSPACE keyspace_holder
WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 1};"""

use_keyspace = "USE keyspace_holder;"

create_transactions_events_table = """CREATE TABLE transactions_events(
   id UUID PRIMARY KEY,
   t_datetime timestamp,
   t_epoch_datetime int,
   sender_username text,
   sender_name text,
   receiver_username text,
   receiver_name text,
   source_ip inet,
   destination_ip inet,
   amount decimal,
   currency_code text,
   currency_name text,
   mac_address text,
   success boolean,
   comment text );
   """

create_user_transactions_stats_table = """CREATE TABLE user_transactions_stats(
   id UUID,
   username text,
   sent_transactions counter,
   received_transactions counter,
   currency_code text,
   success boolean,
   sent_total_amount decimal,
   received_total_amount decimal,
   PRIMARY KEY (id, username)
   );
   """