# README: Aplicación Streamlit para EC2

## Descripción
Esta aplicación, desarrollada en Python utilizando Streamlit, está diseñada para ejecutarse en un servidor EC2 en AWS. Su propósito es desplegar un panel interactivo basado en datos preprocesados en un archivo Jupyter Notebook. La configuración para el servidor EC2 debe ser personalizada según las credenciales específicas de su cuenta de AWS.

## Estructura del Proyecto
El proyecto contiene los siguientes archivos:

1. **Dashboard.py**  
   - Es el archivo principal que contiene la aplicación Streamlit. Este archivo genera un panel interactivo basado en los datos preprocesados.

2. **EDA.ipynb**  
   - Es un cuaderno Jupyter que realiza el preprocesamiento de datos. Toma los datos originales, los limpia y los transforma en un conjunto de datos listo para ser usado en el panel.

3. **GymCleanData.csv**  
   - Archivo CSV que contiene los datos preprocesados generados a partir de `EDA.ipynb`. Este archivo es utilizado por la aplicación `Dashboard.py`.

## Requisitos Previos

1. **AWS EC2**
   - Una instancia EC2 configurada y en ejecución.
   - Configuración de acceso SSH mediante una clave privada válida.

2. **Credenciales Necesarias**
   - `EC2_SSH_KEY`: Ruta al archivo de clave SSH para conectarse a la instancia EC2.
   - `EC2_PUBLIC_IP`: Dirección IP pública de la instancia EC2.

3. **Dependencias**
   - Python 3.8 o superior.
   - Bibliotecas requeridas enumeradas en el archivo `requirements.txt` (asegúrese de instalarlo con `pip install -r requirements.txt`).

## Configuración y Despliegue

### Paso 1: Configurar las Credenciales
Asegúrese de definir las variables de entorno necesarias:

- `EC2_SSH_KEY`: Ruta completa al archivo de clave privada de SSH.
- `EC2_PUBLIC_IP`: Dirección IP pública de la instancia EC2.

Ejemplo:
```bash
export EC2_SSH_KEY="/ruta/a/tu/llave.pem"
export EC2_PUBLIC_IP="xx.xx.xx.xx"
```

### Paso 2: Subir Archivos a EC2
Utilice `scp` para transferir los archivos a la instancia EC2. Ejemplo:
```bash
scp -i $EC2_SSH_KEY Dashboard.py EDA.ipynb GymCleanData.csv ec2-user@$EC2_PUBLIC_IP:~/app/
```

### Paso 3: Conectar al Servidor
Conéctese a la instancia EC2 mediante SSH:
```bash
ssh -i $EC2_SSH_KEY ec2-user@$EC2_PUBLIC_IP
```

### Paso 4: Instalar Dependencias en EC2
En la instancia EC2, instale las dependencias necesarias:
```bash
cd ~/app
pip install -r requirements.txt
```

### Paso 5: Ejecutar la Aplicación con `nohup`
Inicie la aplicación en segundo plano utilizando `nohup`:
```bash
nohup streamlit run Dashboard.py --server.port 8501 &
```

La aplicación estará disponible en el navegador en `http://<EC2_PUBLIC_IP>:8501`.

## Cómo Personalizar

1. **Preprocesamiento de Datos**  
   Modifique el archivo `EDA.ipynb` para ajustar el procesamiento de datos según sus necesidades. Asegúrese de guardar el archivo procesado como `GymCleanData.csv`.

2. **Interfaz del Dashboard**  
   Personalice `Dashboard.py` para cambiar el diseño o funcionalidad del panel.

## Notas Adicionales

- **Seguridad**: Configure las reglas de seguridad en AWS para permitir el tráfico entrante en el puerto 8501.
- **Detención del Servidor**: Detenga la aplicación si es necesario identificando y terminando el proceso de Streamlit:
  ```bash
  ps aux | grep streamlit
  kill <PID>
  ```

## Contacto
Si tiene preguntas o problemas, no dude en comunicarse con el desarrollador principal o enviar un ticket al repositorio correspondiente.

¡Disfruta usando la aplicación! 🚀
