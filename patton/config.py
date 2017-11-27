import os

HTTP_PORT = int(os.getenv('PATTON_HTTP_PORT', '8000'))

DB_URL = os.getenv('PATTON_DB_URL', 'postgres+pg8000://postgres:local@localhost:5432/patton')

download_folder = '/tmp/patton'
