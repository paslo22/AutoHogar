# AutoHogar
Proyecto final de la carrera Ingenieria en Sistema de Información. Automatización del Hogar.

Requisitos:
* Python 3.5
* Pip3
* VirtualEnv

Luego crear el entorno virtual:
```shell
virtualenv -p python3 env
```

Instalar los requisitos del paquete:
```shell
pip install -r requirements.txt
```

Crear la base de datos:
```python
python manage.py makemigrations
python manage.py migrate
```

Y levantar el servidor:
```python
python manage.py runserver
```

Accediendo a localhost se podrá visualizar la página.
