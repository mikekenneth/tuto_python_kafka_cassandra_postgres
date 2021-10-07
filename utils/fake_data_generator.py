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

def _get_columns(datatype: str) -> tuple:
    """Get tuple containing the columns of a datatype in the respective order

    Args:
        datatype (str): Specify the datatype to get the appropriate columns

    Returns:
        tuple: A tuple containing the list of colmns
    """
    datatypes = {
        'transactions_events': ('t_datetime','t_epoch_datetime','sender_username','sender_name',
                                'receiver_username','receiver_name','source_ip','destination_ip',
                                'amount','currency_code','currency_name','mac_address','success','comment'),
    }
    return datatypes.get(datatype)

def generate_transaction_data(start_date: str='-5y', end_date: str='now') -> tuple:
    """Generate Transactions Data using Faker module

    Returns:
        tuple: Data genarated
    """    
    dtime = fake.date_time_between(start_date=start_date, end_date=end_date)
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
