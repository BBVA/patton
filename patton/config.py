import os

DB_URL = os.getenv('PATTON_DB_URL', '{db_engine}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}')

engine_url = DB_URL.format(
    db_engine=os.getenv('PATTON_DB_ENGINE', 'postgres+pg8000'),
    db_user=os.getenv('PATTON_DB_USER', 'postgres'),
    db_name=os.getenv('PATTON_DB_NAME', 'patton'),
    db_pass=os.getenv('PATTON_DB_PASS', 'local'),
    db_host=os.getenv('PATTON_DB_HOST', 'localhost'),
    db_port=os.getenv('PATTON_DB_PORT', '5432'),
)

download_folder = '/tmp/patton'
