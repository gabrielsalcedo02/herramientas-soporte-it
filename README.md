# Script Automatizado de Diagnóstico de Red para Soporte IT

##  Descripción del Proyecto
Este proyecto consiste en una herramienta automatizada desarrollada en Python para el equipo de Help Desk / Soporte Técnico. Su objetivo es agilizar el diagnóstico de conectividad de red del cliente interno ante incidencias de pérdida de conexión, reduciendo los tiempos de atención en la mesa de ayuda y facilitando la recolección de datos técnicos críticos de la infraestructura.

---

##  Funcionalidades
* **Verificación de Red Local:** Realiza pruebas de conectividad de bucle invertido (Loopback) para validar el estado de la tarjeta de red.
* **Comprobación de Gateway (Puerta de Enlace):** Diagnostica la comunicación directa con el router local.
* **Prueba de Acceso a Internet:** Evalúa la salida a la red externa mediante solicitudes ICMP (Ping) a servidores DNS públicos.
* **Detección de Configuración IP:** Muestra en pantalla los detalles de direccionamiento de la máquina de forma automática.

---

##  Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Módulos Nativos:** `os`, `platform`, `subprocess` (No requiere instalaciones externas, ideal para despliegues rápidos en terminales de usuario).

---

##  Instrucciones de Uso

1. Clonar el repositorio o descargar el archivo `diagnostico_red.py`.
2. Abrir una terminal o consola de comandos en el equipo del cliente interno.
3. Ejecutar el script con el siguiente comando:
```bash
   python diagnostico_red.py
