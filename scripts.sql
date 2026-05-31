CREATE USER restaurante_estevez_user WITH PASSWORD 'restaurante_estevez_pass';
CREATE DATABASE restaurante_estevez_db OWNER restaurante_estevez_user;
GRANT ALL PRIVILEGES ON DATABASE restaurante_estevez_db TO restaurante_estevez_user;
\q
uv add django djangorestframework djangorestframework-simplejwt  django-filter django-cors-headers psycopg2-binary python-decouple
uv run python manage.py startapp restaurante
ALTER USER restaurante_estevez_user CREATEDB;
New-Item -ItemType Directory -Force restaurante\models, restaurante\serializers, restaurante\views, restaurante\tests
# Django
SECRET_KEY=django-insecure-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1


# PostgreSQL
DB_NAME=restaurante_estevez_db
DB_USER=restaurante_estevez_user
DB_PASSWORD=restaurante_estevez_pass
DB_HOST=localhost
DB_PORT=5432


# CORS
CORS_ALLOW_ALL_ORIGINS=True


# Test database (Django la crea automáticamente)
TEST_DB_NAME=restaurante_estevez_test_db
$files = @(
    "restaurante\models\__init__.py",
    "restaurante\serializers\__init__.py",
    "restaurante\views\__init__.py",
    "restaurante\tests\__init__.py",
    "restaurante\filters.py",
    "restaurante\permissions.py"
)
$files | ForEach-Object { New-Item -ItemType File -Force $_ }

