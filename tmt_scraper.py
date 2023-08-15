import requests
from bs4 import BeautifulSoup
import boto3
import csv
from io import StringIO
from datetime import datetime, timedelta

def tmt_dag():
    # The URL from which data will be scraped.
    URL = "https://www.tmtfirst.co.uk/samsung-screen-repair-costs"  
    response = requests.get(URL)
    if response.status_code != 200:
        print("Failed to fetch the webpage.")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all tables in the webpage.
    tables = soup.find_all('table')
    
    all_data = []

    for table in tables:
        headers = [header.get_text(strip=True) for header in table.find_all('th')]
        rows = table.find_all('tr')[1:]

        for row in rows:
            phone_data = {}
            phone_name = row.find_all('td')[0].get_text(strip=True)
            phone_data['Phone Name'] = phone_name

            for index, cell in enumerate(row.find_all('td')[1:]):
                header_name = headers[index + 1]
                if header_name != "Arrange Repair":
                    value = cell.get_text(strip=True).replace('£', '')
                    phone_data[header_name] = value
            all_data.append(phone_data)

    fieldnames = set()
    for phone_data in all_data:
        fieldnames.update(phone_data.keys())
    fieldnames = list(fieldnames)
    fieldnames.remove('Phone Name')
    fieldnames.insert(0, 'Phone Name')

    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    for phone_data in all_data:
        writer.writerow(phone_data)

    try:
        boto3.setup_default_session(region_name='eu-north-1')
        bucket_name = 'etl-tmtbucket'
        object_name = 'phones_data.csv'
        boto3.client('s3').put_object(Bucket=bucket_name, Key=object_name, Body=output.getvalue())
        print("Data saved to phones_data.csv in S3 bucket.")
    except Exception as e:
        print(f"Failed to upload to S3: {e}")

if __name__ == "__main__":
    tmt_dag()
