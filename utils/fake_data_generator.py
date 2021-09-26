######################## Notes ########################
# Transactions columns
## t_datetime, t_epoch_datetime, sender_username, sender_name, receiver_username, 
## receiver_name, source_ip, destination_ip, amount, currency_code, currency_name, 
## mac_address, success, comment

######################## END Notes ########################

from faker import Faker
from random import randint, random
from uuid import uuid4

fake = Faker()

def generate_transaction_data():
    dtime = fake.date_time_between(start_date='-5y', end_date='now')
    t_datetime = dtime.strftime('%Y-%m-%dT%H:%M:%S')
    t_epoch_datetime = dtime.strftime('%s')
    sender_name = fake.name()
    sender_username = fake.user_name()
    receiver_name = fake.name()
    receiver_username = fake.user_name()
    source_ip = fake.ipv4_public()
    destination_ip = fake.ipv4_public()
    amount = round(random() * (10**randint(2,6)), 2)
    currency_code = fake.currency_code()
    currency_name = fake.currency_name()
    mac_address = fake.hexify(text='^^:^^:^^:^^:^^:^^')
    success = fake.pybool()
    comment = fake.sentence()

    return (t_datetime, t_epoch_datetime, sender_username, sender_name, receiver_username, receiver_name, 
            source_ip, destination_ip, amount, currency_code, currency_name, mac_address, success, comment)

def generate_profile(username: str, name: str) -> dict:
    profile = fake.profile()
    profile.update({'username': username, 'name': name})
    return profile
