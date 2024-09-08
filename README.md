# Back-Practicas

Activar tu entorno virtual:
  - En Windows (powershell):
    .\venv\Scripts\Activate
  - En Windows (cmd):
    venv\Scripts\activate

Instalar dependencias:
  pip install -r requirements.txt

Migraciones
  - Crear BD llamada "infraestructura"
  - Configurar el archivo settings.py y conectarlo con tu BD
  - python manage.py makemigrations
  - python manage.py migrate
