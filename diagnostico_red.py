```python
import os
import platform
import subprocess

def limpiar_pantalla():
    # Limpia la consola dependiendo del Sistema Operativo
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")

def ejecutar_ping(host):
    # Adapta los parámetros del comando ping según el sistema operativo
    parametro = "-n" if platform.system().lower() == "windows" else "-c"
    comando = ["ping", parametro, "2", host]
    
    try:
        # Ejecuta el comando ocultando la salida excesiva para mantener la interfaz limpia
        resultado = subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
        return resultado.returncode == 0
    except Exception:
        return False

def mostrar_configuracion_ip():
    print("\n[+] OBTENIENDO CONFIGURACIÓN DE RED LOCAL...")
    if platform.system().lower() == "windows":
        os.system("ipconfig | findstr /i \"IPv4 Subnet Gateway\"")
    else:
        os.system("ifconfig | grep -E \"inet \" || ip addr show")

def iniciar_diagnostico():
    limpiar_pantalla()
    print("====================================================")
    print("      HERRAMIENTA AUTOMATIZADA DE SOPORTE IT       ")
    print("           DIAGNÓSTICO DE CONECTIVIDAD              ")
    print("====================================================\n")
    
    # Paso 1: Probar tarjeta de red local
    print("[1/3] Verificando la tarjeta de red local (Loopback)...")
    if ejecutar_ping("127.0.0.1"):
        print("    -> ¡EXITOSO! La tarjeta de red responde correctamente.\n")
    else:
        print("    -> [ALERTA] Falla en hardware o controladores de red local.\n")

    # Paso 2: Probar salida a Internet
    print("[2/3] Comprobando conexión de salida a Internet...")
    # Prueba con los DNS de Google
    if ejecutar_ping("8.8.8.8"):
        print("    -> ¡EXITOSO! El equipo tiene salida a Internet externa.\n")
    else:
        print("    -> [ALERTA] Sin acceso a Internet. Posible fallo en Gateway o proveedor (ISP).\n")

    # Paso 3: Mostrar datos de red actuales
    print("[3/3] Extrayendo direccionamiento actual de la interfaz:")
    mostrar_configuracion_ip()
    
    print("\n====================================================")
    print("             DIAGNÓSTICO FINALIZADO                 ")
    print("====================================================")

if __name__ == "__main__":
    iniciar_diagnostico()
