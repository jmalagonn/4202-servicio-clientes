# 4202-Grupo4-ArquitecturasAgiles
Instrucciones de Ejecucion
Para esta semana estaremos realizando el experimento nuemero 1 que aplica las tacticas que favorece la disponibilidad sobre un servicio que detectan las fallas de conexión y las enmascaran basados en tácticas de redundancia y reintento de conexión.​

## Integrantes
| Nombre | Email |
|------|----------------------------------------------|
|Juan Nicolas Malagón Navarro | jn.malagon@uniandes.edu.co |
|Manuel Sanchez Ballen| mg.sanchezb1@uniandes.edu.co |
|Sergio Arturo Perez Rincon | sa.perezr12@uniandes.edu.co |
|Oscar Ivan Manco Racines| o.manco@uniandes.edu.co |

## Pasos para la ejecución

Descargar los codigos y ejecutar en el editor de su preferencia y en cada uno realizar los siguientes pasos 
- py -m pip --version
- py -m pip install --upgrade pip
  
### crear entorno virtual
- py -m venv venv
- .\venv\Scripts\activate

### ejecutar los requerimientos
- pip install -r requirements.txt  


# ApiGateway
## Descargar código 
- https://github.com/saperezr/ApiGateway
- flask run --port=5000

# Servidor de cliente

## Descargar código 

- https://github.com/jmalagonn/4202-servicio-clientes
- flask run --port=5001
- flask run --port=5002 (servicio de respaldo)

# Simular solicitudes

- Luego ejecutar el script para simular solicitudes ubicado en el repositorio del gateway:
- node experimento1.js
