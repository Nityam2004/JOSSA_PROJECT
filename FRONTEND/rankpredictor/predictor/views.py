import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
from django.shortcuts import render

# Function to perform linear extrapolation on a given file and predict ranks for given marks
def predict_ranks(file_name, marks_to_predict):
    # Load the data
    data = pd.read_csv(file_name)
    
    # Print the columns for debugging
    print(f"Columns in {file_name}: {data.columns.tolist()}")
    
    # Assuming the file has columns named 'rank' and 'marks'
    ranks = data['Rank']
    marks = data['Marks']
    
    # Ensure data is sorted by marks
    sorted_indices = np.argsort(marks)
    ranks = ranks.iloc[sorted_indices]
    marks = marks.iloc[sorted_indices]

    # Create the extrapolation function
    extrapolate = interp1d(marks, ranks, fill_value="extrapolate")

    # Predict ranks for the given marks
    predicted_ranks = extrapolate(marks_to_predict)
    
    # Convert predicted ranks to integers
    predicted_ranks = np.round(predicted_ranks).astype(int)
    
    return predicted_ranks

# Function to get the file name based on category
def get_file_name(category):
    file_names = {
        'crl': 'data/crl.csv',
        'ews': 'data/ews.csv',
        'sc': 'data/sc.csv',
        'st': 'data/st.csv',
        'obc': 'data/obc.csv'
    }
    return file_names.get(category.lower())

def index(request):
    if request.method == 'POST':
        category = request.POST['category']
        marks_input = request.POST['marks']
        marks_to_predict = [float(mark.replace(',', '')) for mark in marks_input.split(',')]
        file_name = get_file_name(category)
        if file_name:
            predicted_ranks = predict_ranks(file_name, marks_to_predict)
        else:
            predicted_ranks = []
        return render(request, 'predictor/index.html', {'predicted_ranks': predicted_ranks})
    return render(request, 'predictor/index.html')
