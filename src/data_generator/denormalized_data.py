import dognames
from faker import Faker
import random
import pandas as pd
from datetime import datetime, timedelta
import uuid
import boto3
from botocore.exceptions import ClientError
from io import StringIO
import os
import json
import snowflake.connector


class DogDataGenerator:
    def __init__(self, num_records):
        self.num_records = num_records
        self.fake = Faker('fr_FR')
        self.breeds_list = self.fetch_dog_breeds()
        self.generated_data = self.generate_data()

    def fetch_dog_breeds(self):
        return [
            'Labrador Retriever', 'German Shepherd', 'Golden Retriever', 'French Bulldog', 'Bulldog', 'Poodle',
            'Beagle', 'Rottweiler', 'Siberian Husky', 'Dachshund', 'Boxer', 'Shih Tzu', 'Great Dane',
            'Doberman Pinscher', 'Australian Shepherd', 'Chihuahua', 'Shetland Sheepdog', 'Border Collie',
            'Shiba Inu', 'Pomeranian', 'Cocker Spaniel', 'Yorkshire Terrier', 'Saint Bernard', 'Akita',
            'Australian Cattle Dog'
        ]

    def generate_owner(self):
        owner_gender = self.fake.random_element(['Male', 'Female'])
        owner_first_name = self.fake.first_name_male() if owner_gender=="Male" else self.fake.first_name_female()
        owner_last_name = self.fake.last_name()
        return {
            'owner_id': str(uuid.uuid4()),
            'owner_first_name': owner_first_name,
            'owner_last_name': owner_last_name,
            'owner_age': random.randint(18,85),
            'owner_gender': owner_gender,
            'owner_email': f"{owner_first_name.lower()}.{owner_last_name.lower()}@{self.fake.random_element(['gmail.com', 'outlook.com'])}",
            'owner_phone': self.fake.phone_number(),
            'owner_address': self.fake.address(),
        }

    def generate_dog(self, breeds_list):
        dog_gender = self.fake.random_element(['Male', 'Female'])
        dog_name = dognames.male() if dog_gender == 'Male' else dognames.female()

        return {
            'dog_id': str(uuid.uuid4()),
            'dog_name': dog_name,
            'dog_breed': random.choice(breeds_list),
            'dog_age': random.randint(1, 120),
            'dog_gender': dog_gender,
        }

    def generate_order(self, owner_id):
        order_id = str(uuid.uuid4())  # Each order gets a new order_id
        order_date = self.fake.date_between(start_date='-120d', end_date='today')
        
        return {
            'order_id': order_id,
            'order_date': order_date,
            'owner_id': owner_id,
        }

    def generate_product(self, order_id):
        synthetic_product_data = pd.read_csv('../synthetic_product_data.csv')
        product = synthetic_product_data.sample().to_dict(orient='records')[0]
        quantity = random.randint(1, 10)
        subtotal = round(product['product_price'] * quantity, 2)

        product_data = {
            'product_id': str(uuid.uuid4()),  # Each product gets a new product_id
            'order_id': order_id,  # Each product has the same order_id
            'quantity': quantity,
            'subtotal': subtotal,
            **product
        }

        return product_data

    def generate_transaction(self, product_data):
        if not isinstance(product_data, dict):
            return {}
        
        product_id = product_data['product_id']
        order_id = product_data['order_id']
        quantity = int(product_data['quantity'])
        subtotal = float(product_data['subtotal'])
        
        # Include the order date in the transaction_id
        transaction_id = f"{order_id}_{self.fake.date_time_this_decade().strftime('%Y%m%d%H%M%S')}"

        transaction_data = {
            'transaction_id': transaction_id,
            'order_id': order_id,
            'product_id': product_id,
            'quantity': quantity,
            'subtotal': subtotal,
        }

        return transaction_data
    
    def generate_veterinarian(self):
        vet_id = str(uuid.uuid4())
        veterinarian_gender = self.fake.random_element(['Male', 'Female'])
        veterinarian_first_name = self.fake.first_name_male() if veterinarian_gender == "Male" else self.fake.first_name_female()

        return {
            'veterinarian_id': vet_id,
            'veterinarian_first_name': veterinarian_first_name,
            'veterinarian_last_name': self.fake.last_name(),
            'veterinarian_gender': veterinarian_gender,
            'veterinarian_age': random.randint(28, 85),
            'veterinarian_contact': self.fake.phone_number(),
        }
    
    def generate_appointment(self):
        appointment_date = self.fake.date_between(start_date='today', end_date='+120d')

        # Load the data from the CSV file
        synthetic_product_data = pd.read_csv('../synthetic_specialists_data.csv')
        specialist_data = synthetic_product_data.sample().to_dict(orient='records')[0]

        # Extract required values
        veterinarian_specialization_id = specialist_data.get('specialty_id')
        specialty_name = specialist_data.get('specialty_name')
        fees = specialist_data.get('fees')
        description = specialist_data.get('description')

        return {
            'appointment_id': str(uuid.uuid4()),
            'appointment_date': appointment_date,
            'appointment_purpose': description,
            'veterinarian_specialization_id': veterinarian_specialization_id,
            'specialty_name': specialty_name,
            'fees': fees,
        }
    
    def generate_data(self):
        data = []
        for _ in range(self.num_records):
            owner = self.generate_owner()
            dog = self.generate_dog(self.breeds_list)
            order = self.generate_order(owner['owner_id'])

            order_id = order['order_id']
            num_products = random.randint(1, 5)
            products = [self.generate_product(order_id) for _ in range(num_products)]
            transactions = [self.generate_transaction(product) for product in products]

            veterinarian = self.generate_veterinarian()
            appointment = self.generate_appointment()

            data.extend([{**owner, **dog, **order, **product, **transaction, **veterinarian, **appointment} for product, transaction in zip(products, transactions)])
        return data

    def create_dataframe(self):
        return pd.DataFrame(self.generated_data)

    def save_to_csv(self, filename):
        df = self.create_dataframe()
        df.to_csv(filename, index=False)





def get_secret():
    secret_name = "S3-cred"
    region_name = "eu-west-3"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    secret_string = get_secret_value_response['SecretString']
    
    # Parse the JSON string into a dictionary
    secret = json.loads(secret_string)
    
    return secret

def create_s3_bucket(bucket_name, aws_access_key_id, aws_secret_access_key, region_name='eu-west-3'):
    s3 = boto3.client(
        's3',
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )

    try:
        s3.head_bucket(Bucket=bucket_name)
        print(f"S3 bucket '{bucket_name}' already exists.")
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            location_constraint = region_name if region_name != 'us-east-1' else ''
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': location_constraint}
            )
            print(f"S3 bucket '{bucket_name}' created.")
        else:
            # Other error, print the error message
            print(f"Error: {e.response['Error']['Message']}")


def upload_to_s3(df, bucket_name, file_key, aws_access_key_id, aws_secret_access_key):
    create_s3_bucket(bucket_name, aws_access_key_id, aws_secret_access_key)

    s3 = boto3.client(
        's3',
        region_name='eu-west-3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)

    s3.put_object(Body=csv_buffer.getvalue(), Bucket=bucket_name, Key=file_key)
    print(f"Data uploaded to S3 bucket '{bucket_name}' with file key '{file_key}'.")



if __name__ == "__main__":
    try:
        secret = get_secret()
        aws_access_key_id = secret.get('aws_access_key_id')
        aws_secret_access_key = secret.get('aws_secret_access_key')
        
        data_generator = DogDataGenerator(num_records=5000)
        
        generated_data_file = 'denormalized_data.csv'
        data_generator.save_to_csv(generated_data_file)

        bucket_name = 'dogspipeline-personal'
        file_key = 'data/denormalized_data.csv'

        df = pd.read_csv(generated_data_file)

        upload_to_s3(df, bucket_name, file_key, aws_access_key_id, aws_secret_access_key)
    except Exception as e:
        print(f"An error occurred: {e}")