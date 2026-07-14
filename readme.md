# Inmobiliaria Coder

Proyecto final realizado con Django como parte del curso de Python.

## Descripción

Sistema web para la gestión de una inmobiliaria. Permite administrar propiedades, propietarios y clientes mediante una interfaz web desarrollada con Django y Bootstrap 5.

## Funcionalidades

* Listado de propiedades.
* Creación, edición y eliminación de propiedades.
* Carga de imágenes de propiedades.
* Registro y administración de propietarios.
* Registro y administración de clientes.
* Formularios utilizando Django Forms.
* Navegación mediante menú con Bootstrap 5.

## Tecnologías utilizadas

* Python
* Django
* HTML5
* Bootstrap 5
* SQLite
* Git y GitHub

## Estructura del proyecto

El proyecto está organizado en diferentes aplicaciones:

* `propiedades`: gestión de inmuebles.
* `propietarios`: gestión de dueños de propiedades.
* `clientes`: gestión de clientes.
* `templates`: archivos HTML generales del sitio.

## Instalación y ejecución

Clonar el repositorio:

```bash
git clone https://github.com/cjh-87/Inmobiliaria-Coder.git
```

Ingresar a la carpeta del proyecto:

```bash
cd Inmobiliaria-Coder
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Realizar las migraciones:

```bash
python manage.py migrate
```

Ejecutar el servidor:

```bash
python manage.py runserver
```

Abrir en el navegador:

```
http://127.0.0.1:8000/
```

## Autor

Proyecto desarrollado como entrega final del curso de Python/Django.
