import os

settings = {
    'url': os.environ.get('ACCOUNT_URL', 'https://giwb2ctest-db.documents.azure.com:443/'),
    'endpoint': os.environ.get('ACCOUNT_ENDPOINT', 'https://giwb2ctest-db.documents.azure.com:443/;AccountKey=HRwjnMDYtjyjO5eGZa5ZKrX73DIVVPkhvcmqnAvefjadqP28YVDCEOpPa0Et5jPM8JbhSCq7XiM9svkOMDtIiQ==;'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'HRwjnMDYtjyjO5eGZa5ZKrX73DIVVPkhvcmqnAvefjadqP28YVDCEOpPa0Et5jPM8JbhSCq7XiM9svkOMDtIiQ=='),
    'database_name': os.environ.get('COSMOS_DATABASE', 'Contacts'),
    'container_name': os.environ.get('COSMOS_CONTAINER', 'Users'),
}
