import pandas as pd

class ProductDataGenerator:
    def __init__(self):
        self.product_data = [
            {'product_id': 1, 'product_name': 'Dog Food', 'product_price': 20.99, 'product_description': 'High-quality dog food'},
            {'product_id': 2, 'product_name': 'Dog Toy', 'product_price': 9.99, 'product_description': 'Interactive dog toy'},
            {'product_id': 3, 'product_name': 'Dog Bed', 'product_price': 39.99, 'product_description': 'Comfortable dog bed'},
            {'product_id': 4, 'product_name': 'Dog Collar', 'product_price': 12.99, 'product_description': 'Stylish dog collar'},
            {'product_id': 5, 'product_name': 'Chew Bone', 'product_price': 7.49, 'product_description': 'Natural chew bone'},
            {'product_id': 6, 'product_name': 'Dog Shampoo', 'product_price': 15.99, 'product_description': 'Gentle dog shampoo'},
            {'product_id': 7, 'product_name': 'Pet Brush', 'product_price': 8.99, 'product_description': 'Soft pet grooming brush'},
            {'product_id': 8, 'product_name': 'Puppy Training Pads', 'product_price': 19.99, 'product_description': 'Absorbent training pads'},
            {'product_id': 9, 'product_name': 'Dog Leash', 'product_price': 14.99, 'product_description': 'Durable dog leash'},
            {'product_id': 10, 'product_name': 'Dog Treats', 'product_price': 5.99, 'product_description': 'Tasty dog treats'},
            {'product_id': 11, 'product_name': 'Dog Ball', 'product_price': 6.99, 'product_description': 'Fetch and play ball'},
            {'product_id': 12, 'product_name': 'Dog Crate', 'product_price': 34.99, 'product_description': 'Secure dog crate'},
            {'product_id': 13, 'product_name': 'Dog Grooming Kit', 'product_price': 29.99, 'product_description': 'Complete grooming kit for dogs'},
            {'product_id': 14, 'product_name': 'Dog Dental Chews', 'product_price': 11.99, 'product_description': 'Dental chews for oral health'},
            {'product_id': 15, 'product_name': 'Dog GPS Tracker', 'product_price': 49.99, 'product_description': 'GPS tracker for dogs'},
            {'product_id': 16, 'product_name': 'Reflective Dog Harness', 'product_price': 18.99, 'product_description': 'Reflective harness for night walks'},
            {'product_id': 17, 'product_name': 'Dog Raincoat', 'product_price': 24.99, 'product_description': 'Water-resistant dog raincoat'},
            {'product_id': 18, 'product_name': 'Squeaky Plush Toy', 'product_price': 8.49, 'product_description': 'Cute squeaky plush toy for dogs'},
            {'product_id': 19, 'product_name': 'Dog Sunglasses', 'product_price': 15.99, 'product_description': 'UV-protective sunglasses for dogs'},
            {'product_id': 20, 'product_name': 'Dog Bandana', 'product_price': 6.99, 'product_description': 'Stylish bandana for dogs'},
            {'product_id': 21, 'product_name': 'Portable Dog Water Bottle', 'product_price': 12.99, 'product_description': 'Convenient water bottle for dogs on the go'},
            {'product_id': 22, 'product_name': 'Interactive Fetch Ball', 'product_price': 11.49, 'product_description': 'Interactive ball for fetch games'},
            {'product_id': 23, 'product_name': 'Dog Nail Clippers', 'product_price': 9.99, 'product_description': 'Safe and easy-to-use nail clippers for dogs'},
            {'product_id': 24, 'product_name': 'Dog Harness with Leash', 'product_price': 29.99, 'product_description': 'Adjustable harness with matching leash'},
            {'product_id': 25, 'product_name': 'Dog Backpack', 'product_price': 19.99, 'product_description': 'Backpack for dogs to carry essentials on walks'},
            {'product_id': 26, 'product_name': 'Dog Frisbee', 'product_price': 7.99, 'product_description': 'Durable frisbee for outdoor play'},
            {'product_id': 27, 'product_name': 'Dog Paw Balm', 'product_price': 13.99, 'product_description': 'Moisturizing paw balm for dogs'},
            {'product_id': 28, 'product_name': 'Dog Puzzle Toy', 'product_price': 16.99, 'product_description': 'Brain-stimulating puzzle toy for dogs'},
            {'product_id': 29, 'product_name': 'Dog Dental Spray', 'product_price': 10.99, 'product_description': 'Oral hygiene dental spray for dogs'},
            {'product_id': 30, 'product_name': 'Dog Poop Bags', 'product_price': 5.49, 'product_description': 'Biodegradable poop bags for easy cleanup'},
            {'product_id': 31, 'product_name': 'Dog Grooming Gloves', 'product_price': 14.49, 'product_description': 'Gentle grooming gloves for dogs'},
            {'product_id': 32, 'product_name': 'Dog Cooling Mat', 'product_price': 22.99, 'product_description': 'Cooling mat for hot days'},
            {'product_id': 33, 'product_name': 'Dog Training Clicker', 'product_price': 3.99, 'product_description': 'Training clicker for positive reinforcement'},
            {'product_id': 34, 'product_name': 'Dog Tug Toy', 'product_price': 9.49, 'product_description': 'Interactive tug-of-war toy for dogs'},
            {'product_id': 35, 'product_name': 'Dog Ear Cleaner', 'product_price': 11.49, 'product_description': 'Gentle ear cleaner solution for dogs'},
        ]
    
    def add_products(self, new_products):
        self.product_data.extend(new_products)

    def generate_csv(self, filename='synthetic_product_data.csv'):
        synthetic_df = pd.DataFrame(self.product_data)
        synthetic_df.to_csv(filename, index=False)
        return synthetic_df


data_generator = ProductDataGenerator()
csv_filename = 'synthetic_product_data.csv'
data_generator.generate_csv(csv_filename)
