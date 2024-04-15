# mongodb_excel/views.py
from django.http import HttpResponse
from django_pandas.io import read_frame
from pymongo import MongoClient
from io import BytesIO
import pandas as pd

def download_excel(request):
    # Connect to MongoDB
    mongo_uri = "mongodb+srv://abrardar988651:Abrardar123@freeserver.wc1ytkf.mongodb.net/?retryWrites=true&w=majority&appName=freeServer"

    # Connect to MongoDB Atlas
    client = MongoClient(mongo_uri)
    db = client['test']
    collection = db['users']

    # Query the data
    cursor = collection.find({})  # You can add filters if needed

    # Convert cursor to list of dictionaries
    data = list(cursor)

    # Create DataFrame from the list of dictionaries
    df = pd.DataFrame(data)

    # Create Excel file in memory
    excel_output = BytesIO()
    df.to_excel(excel_output, index=False)
    excel_output.seek(0)

    # Set up HTTP response
    response = HttpResponse(
        excel_output.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=mongodb_data.xlsx'

    return response