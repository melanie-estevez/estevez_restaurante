CREATE USER restaurante_estevez_user WITH PASSWORD 'restaurante_estevez_pass';
CREATE DATABASE restaurante_estevez_db OWNER restaurante_estevez_user;
GRANT ALL PRIVILEGES ON DATABASE restaurante_estevez_db TO restaurante_estevez_user;
\q
uv add django djangorestframework djangorestframework-simplejwt  django-filter django-cors-headers psycopg2-binary python-decouple
uv run python manage.py startapp restaurante

New-Item -ItemType Directory -Force restaurante\models, restaurante\serializers, restaurante\views, restaurante\tests

$files = @(
    "restaurante\models\__init__.py",
    "restaurante\serializers\__init__.py",
    "restaurante\views\__init__.py",
    "restaurante\tests\__init__.py",
    "restaurante\filters.py",
    "restaurante\permissions.py"
)
$files | ForEach-Object { New-Item -ItemType File -Force $_ }

{
  "info": {
    "name": "ShopAPI — Stage 2: Auth + Users",
    "_postman_id": "shopapi-stage-02",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Auth",
      "item": [
        {
          "name": "Register",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Status 201', () => pm.response.to.have.status(201));",
            "const j = pm.response.json();",
            "pm.collectionVariables.set('access',  j.access);",
            "pm.collectionVariables.set('refresh', j.refresh);"
          ]}}],
          "request": {
            "method": "POST",
            "header": [{ "key": "Content-Type", "value": "application/json" }],
            "body": { "mode": "raw", "raw": "{\n  \"username\": \"john\",\n  \"email\": \"john@test.com\",\n  \"password\": \"Pass1234!\",\n  \"password2\": \"Pass1234!\"\n}" },
            "url": "{{base_url}}/auth/register/"
          }
        },
        {
          "name": "Login",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Status 200', () => pm.response.to.have.status(200));",
            "const j = pm.response.json();",
            "pm.collectionVariables.set('access',  j.access);",
            "pm.collectionVariables.set('refresh', j.refresh);"
          ]}}],
          "request": {
            "method": "POST",
            "header": [{ "key": "Content-Type", "value": "application/json" }],
            "body": { "mode": "raw", "raw": "{\n  \"username\": \"admin\",\n  \"password\": \"Admin1234!\"\n}" },
            "url": "{{base_url}}/auth/login/"
          }
        },
        {
          "name": "Refresh Token",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Status 200', () => pm.response.to.have.status(200));",
            "const j = pm.response.json();",
            "pm.collectionVariables.set('access',  j.access);",
            "pm.collectionVariables.set('refresh', j.refresh);"
          ]}}],
          "request": {
            "method": "POST",
            "header": [{ "key": "Content-Type", "value": "application/json" }],
            "body": { "mode": "raw", "raw": "{\n  \"refresh\": \"{{refresh}}\"\n}" },
            "url": "{{base_url}}/auth/token/refresh/"
          }
        },
        {
          "name": "Logout",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Status 200', () => pm.response.to.have.status(200));"
          ]}}],
          "request": {
            "method": "POST",
            "header": [
              { "key": "Content-Type",  "value": "application/json" },
              { "key": "Authorization", "value": "Bearer {{access}}" }
            ],
            "body": { "mode": "raw", "raw": "{\n  \"refresh\": \"{{refresh}}\"\n}" },
            "url": "{{base_url}}/auth/logout/"
          }
        }
      ]
    },
    {
      "name": "Users",
      "item": [
        {
          "name": "Get my profile",
          "request": {
            "method": "GET",
            "header": [{ "key": "Authorization", "value": "Bearer {{access}}" }],
            "url": "{{base_url}}/users/profile/"
          }
        },
        {
          "name": "Update my profile",
          "request": {
            "method": "PATCH",
            "header": [
              { "key": "Content-Type",  "value": "application/json" },
              { "key": "Authorization", "value": "Bearer {{access}}" }
            ],
            "body": { "mode": "raw", "raw": "{\n  \"first_name\": \"John\",\n  \"last_name\": \"Doe\"\n}" },
            "url": "{{base_url}}/users/profile/"
          }
        },
        {
          "name": "Change password",
          "request": {
            "method": "POST",
            "header": [
              { "key": "Content-Type",  "value": "application/json" },
              { "key": "Authorization", "value": "Bearer {{access}}" }
            ],
            "body": { "mode": "raw", "raw": "{\n  \"current_password\": \"Pass1234!\",\n  \"new_password\": \"New5678!\",\n  \"new_password2\": \"New5678!\"\n}" },
            "url": "{{base_url}}/users/change-password/"
          }
        },
        {
          "name": "[Staff] List users",
          "request": {
            "method": "GET",
            "header": [{ "key": "Authorization", "value": "Bearer {{access}}" }],
            "url": {
              "raw": "{{base_url}}/users/?search=john&is_active=true&ordering=username",
              "query": [
                { "key": "search",    "value": "john" },
                { "key": "is_active", "value": "true" },
                { "key": "ordering",  "value": "username" }
              ]
            }
          }
        },
        {
          "name": "[Staff] Create user",
          "request": {
            "method": "POST",
            "header": [
              { "key": "Content-Type",  "value": "application/json" },
              { "key": "Authorization", "value": "Bearer {{access}}" }
            ],
            "body": { "mode": "raw", "raw": "{\n  \"username\": \"mary\",\n  \"email\": \"mary@test.com\",\n  \"password\": \"Pass1234!\",\n  \"first_name\": \"Mary\",\n  \"last_name\": \"Smith\"\n}" },
            "url": "{{base_url}}/users/"
          }
        },
        {
          "name": "[Staff] Toggle active",
          "request": {
            "method": "POST",
            "header": [{ "key": "Authorization", "value": "Bearer {{access}}" }],
            "url": "{{base_url}}/users/2/toggle-active/"
          }
        },
        {
          "name": "[Staff] Stats",
          "request": {
            "method": "GET",
            "header": [{ "key": "Authorization", "value": "Bearer {{access}}" }],
            "url": "{{base_url}}/users/stats/"
          }
        }
      ]
    }
  ],
  "variable": [
    { "key": "base_url", "value": "http://localhost:8000/api" },
    { "key": "access",   "value": "" },
    { "key": "refresh",  "value": "" }
  ]
}