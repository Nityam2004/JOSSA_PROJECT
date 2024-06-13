import os
import sys
import django
import csv
from django.db.utils import IntegrityError

# Set the base directory (the root of the project)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the project root to the Python path
sys.path.append(BASE_DIR)

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'college_finder.settings')

# Setup Django
django.setup()

from finder.models import College  # Import models after setting up Django

def load_college_data():
    csv_file_path = os.path.join(BASE_DIR, 'data', 'college_data.csv')

    # Check if data is already imported to avoid duplication
    if not College.objects.exists():
        try:
            with open(csv_file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        opening_rank = int(float(row['opening_rank']))
                        closing_rank = int(float(row['closing_rank']))
                        College.objects.create(
                            college_name=row['college name'],
                            branch=row['branch'],
                            unknown=row['unknown'],
                            category=row['candidates_category'],
                            gender=row['gender'],
                            opening_rank=opening_rank,
                            closing_rank=closing_rank,
                        )
                    except ValueError as e:
                        print(f"Error converting rank values: {e}")
        except IntegrityError:
            print("Integrity error occurred while loading data.")
        print('Data loaded successfully')
    else:
        print('Data already loaded, skipping...')

if __name__ == "__main__":
    load_college_data()
