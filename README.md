## TMT Phone Repair Price Scraper and Airflow ETL
# Introduction
The TMT Phone Repair Price Scraper and Airflow ETL project is designed to demonstrate the creation of an end-to-end data extraction, transformation, and loading (ETL) pipeline using various technologies. The goal of this project is to automate the scraping of Samsung phone repair prices from the TMT UK website, process the data, and upload it to an AWS S3 bucket. The pipeline is orchestrated using Apache Airflow, while AWS S3 serves as the storage backend.

# Technologies Used
- **Python**: The primary programming language used for scripting, web scraping, and data processing.
- **BeautifulSoup**: A Python library for extracting data from HTML and XML files. Used for web scraping.
- **Apache Airflow**: An open-source platform to programmatically author, schedule, and monitor workflows.
- **AWS S3**: Amazon Simple Storage Service is used to store the processed data in CSV format.
- **AWS EC2**: Created ec2 instance and deployed our dag on it.
- **Boto3**: The AWS SDK for Python, used to interact with AWS services programmatically.

# Project Workflow
- **Web Scraping**: The tmt_scraper.py script utilizes the requests library to fetch the HTML content of the TMT UK website. The BeautifulSoup library is then used to parse the HTML and extract Samsung phone repair cost data.
- **Data Processing**: The scraped data is processed and organized into a structured format. Unnecessary characters are removed, and the data is transformed into a dictionary format.
- **Airflow DAG Definition**: Script defines an Apache Airflow Directed Acyclic Graph (DAG) named tmt_dag. This DAG schedules the execution of the tmt_scraper.py script at a specified interval.
- **Scheduled Execution**: The Airflow scheduler triggers the tmt_scraper.py script execution at the defined schedule interval. This ensures that the latest phone repair price data is scraped and processed periodically.
- **Data Upload to S3**: Processed data is written to a CSV file and then uploaded to an AWS S3 bucket using the boto3 library. The bucket acts as a centralized storage location for the scraped data.

# IAM Roles and Policies
To facilitate the secure execution and data upload to AWS S3, the following IAM roles and policies were implemented:
- IAM Role: AmazonS3FullAccess: This IAM role was created to grant full access to AWS S3. It's attached to the EC2 instance running the Airflow server. The role allows the instance to perform actions on S3, including uploading the processed CSV file.
- IAM Policy: s3:PutObject: A custom IAM policy was created and attached to the fulls3Access role. This policy grants the permission to perform the s3:PutBucketPolicy action, allowing the instance to set a bucket policy to restrict access to the uploaded files.

- Deploying on EC2
To deploy the Airflow DAG on an Amazon EC2 instance, follow these steps:
- Launch an EC2 Instance: Launch an EC2 instance in your AWS account. Make sure the instance has the necessary permissions to interact with AWS services like S3.
- Connect to EC2 Instance: Use SSH to connect to the EC2 instance using the provided public key.
- Clone Repository: Clone this repository onto the EC2 instance.
```
git@github.com:ZeeshanM96/Airflow_ETL.git 
```
- Install Dependencies: Install the required dependencies using pip.
```
pip install -r requirements.txt
```
- Configure AWS Credentials: Set up your AWS credentials on the EC2 instance. You can either use environment variables or create an AWS credentials file.
- Configure Airflow: Configure Airflow on the EC2 instance. Set up the Airflow configurations, including database connection and security settings.
- Place DAG File: Copy the dag_definition.py file into the Airflow DAG folder on the EC2 instance. The exact path will depend on your Airflow installation.
- Start Airflow: Start the Airflow scheduler and web server on the EC2 instance.
```
airflow scheduler
airflow webserver
```
- Access Airflow UI: Access the Airflow web UI by entering the EC2 instance's public IP address or DNS name followed by the port number (usually 8080) in your web browser.

- Trigger DAG: In the Airflow web UI, you can manually trigger the `tmt_dag` or wait for the scheduled runs to start.

# Contributing
Contributions to this project are welcome! Feel free to open issues and submit pull requests.
