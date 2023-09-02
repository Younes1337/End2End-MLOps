import requests
from bs4 import BeautifulSoup
import boto3
from datetime import datetime

# --------------------------------------------- Connecting to S3 Bucket and Store the Coming Data -------------------------------------------
def store_data_in_s3(bucket_name, file_name, data):
    try:
        s3 = boto3.client('s3')
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=data.encode('utf-8'))
        return f"Stored data in S3: s3://{bucket_name}/{file_name}"
    except Exception as e:
        return f"An error occurred while storing data in S3: {e}"


# ----------------------------------------------------------- Lambda Handler Function ---------------------------------------------------------
def lambda_handler(event, context):
    base_url = event["base_url"]
    query = event["Query"]
    page_size = 200
    total_pages = 900
    bucket_name = "<your-s3-bucket-name>"  # Replace with your S3 bucket name

    # Create a file name with the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    file_name = f"{timestamp}_api_data.txt"

    try:
        data_to_store = ""

        for page in range(1, total_pages + 1):
            params = {
                "query": query,
                "searchtype": "all",
                "abstracts": "show",
                "order": "-announced_date_first",
                "size": page_size,
                "start": (page - 1) * page_size + 1
            }

            response = requests.get(base_url, params=params, timeout=10)
            response.raise_for_status()

            doc = BeautifulSoup(response.text, "html.parser")

            links = [a['href'] for a in doc.find_all('a', href=True) if 'https://arxiv.org/abs/' in a['href']]

            for link in links:
                try:
                    response = requests.get(link, timeout=10)
                    response.raise_for_status()

                    doc = BeautifulSoup(response.text, "html.parser")

                    title = doc.find('h1', class_='title mathjax').text.strip()
                    abstract = doc.find('blockquote', class_='abstract mathjax').text.strip()

                    question = f"Q: Can you give me an abstract for my research paper with the {title}?"
                    answer = f"A: {abstract}"

                    data_to_store += question + "\n" + answer + "\n\n"

                except Exception as e:
                    return f"Error scraping link {link}: {e}"

        result = store_data_in_s3(bucket_name, file_name, data_to_store)
        return result

    except Exception as e:
        return f"An error occurred: {e}"

# ---------------------------------------------------------------------More Features to add here ----------------------------------------------
# Write your code here
#----------------------------------------------------------------------------------------------------------------------------------------------
