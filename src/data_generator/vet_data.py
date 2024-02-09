import pandas as pd

class VeterinarySpecialistsDataGenerator:
    def __init__(self):
        self.specialists_data = [
            {'specialty_id': 1, 'specialty_name': 'Anesthesia and Analgesia', 'fees': 500, 'description': 'Manage pain and complications during surgery'},
            {'specialty_id': 2, 'specialty_name': 'Animal Welfare', 'fees': 600, 'description': 'Advance animal well-being and provide accurate information'},
            {'specialty_id': 3, 'specialty_name': 'Behavioral Medicine', 'fees': 550, 'description': 'Address behavioral issues in animals beyond basic obedience'},
            {'specialty_id': 4, 'specialty_name': 'Clinical Pharmacology', 'fees': 700, 'description': 'Specialized in drug development and usage for animals'},
            {'specialty_id': 5, 'specialty_name': 'Dentistry', 'fees': 800, 'description': 'Qualified to clean, adjust, and extract teeth in animals'},
            {'specialty_id': 6, 'specialty_name': 'Dermatology', 'fees': 750, 'description': 'Treat various skin diseases and related health problems in animals'},
            {'specialty_id': 7, 'specialty_name': 'Emergency and Critical Care', 'fees': 900, 'description': 'Provide prompt medical attention in emergency situations'},
            {'specialty_id': 8, 'specialty_name': 'Internal Medicine (Cardiology)', 'fees': 1000, 'description': 'Treat uncommon or complicated diseases related to the heart'},
            {'specialty_id': 9, 'specialty_name': 'Laboratory Animal Medicine', 'fees': 650, 'description': 'Ensure proper care for animals used in laboratory settings'},
            {'specialty_id': 10, 'specialty_name': 'Microbiology', 'fees': 720, 'description': 'Research bacteria, parasites, and microorganisms causing diseases'},
            {'specialty_id': 11, 'specialty_name': 'Nutrition', 'fees': 580, 'description': 'Manage animals diets and develop nutrition plans for sick animals'},
            {'specialty_id': 12, 'specialty_name': 'Ophthalmology', 'fees': 850, 'description': 'Specialize in treating eye diseases in animals'},
            {'specialty_id': 13, 'specialty_name': 'Pathology', 'fees': 780, 'description': 'Diagnose diseases by examining tissue or fluid samples'},
            {'specialty_id': 14, 'specialty_name': 'Poultry Veterinary Medicine', 'fees': 670, 'description': 'Work with domestic birds like chickens, turkeys, and ducks in food production'},
            {'specialty_id': 15, 'specialty_name': 'Preventive Medicine', 'fees': 630, 'description': 'Detect and control diseases affecting both animals and humans'},
        ]

    def generate_csv(self, filename='/tmp/synthetic_specialists_data.csv'):
        specialists_df = pd.DataFrame(self.specialists_data)
        specialists_df.to_csv(filename, index=False)
        return specialists_df


if __name__ == "__main__":
    specialists_generator = VeterinarySpecialistsDataGenerator()
    csv_filename = '/tmp/synthetic_specialists_data.csv'
    specialists_generator.generate_csv(csv_filename)

