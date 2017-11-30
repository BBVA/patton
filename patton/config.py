import os
import multiprocessing

HTTP_HOST = os.getenv('PATTON_HTTP_HOST', '0.0.0.0')

HTTP_PORT = int(os.getenv('PATTON_HTTP_PORT', '8000'))

HTTP_WORKERS = int(os.getenv('PATTON_HTTP_WORKERS', multiprocessing.cpu_count()))

HTTP_DEBUG = True if os.getenv('PATTON_HTTP_DEBUG', 'False') == 'True' else False

DB_PASS = os.getenv('POSTGRES_PASSWORD', 'postgres')

DB_URL = os.getenv('PATTON_DB_URL', f'postgres+psycopg2://postgres:{DB_PASS}@localhost:5432/patton')

DOWNLOAD_FOLDER = os.getenv('PATTON_DOWNLOAD_FOLDER', '/tmp/patton')
