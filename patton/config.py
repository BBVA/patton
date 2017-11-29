import os
import multiprocessing

HTTP_HOST = os.getenv('PATTON_HTTP_HOST', '0.0.0.0')

HTTP_PORT = int(os.getenv('PATTON_HTTP_PORT', '8000'))

HTTP_WORKERS = int(os.getenv('PATTON_HTTP_WORKERS', multiprocessing.cpu_count()))

DB_PASS = os.getenv('POSTGRES_PASSWORD', 'local')

DB_URL = os.getenv('PATTON_DB_URL', f'postgres+pg8000://postgres:{DB_PASS}@localhost:5432/patton')

download_folder = '/tmp/patton'
