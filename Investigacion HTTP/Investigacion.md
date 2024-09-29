# Familia de Protocolos de Internet

## Programación Web  
**Maestro**: Gerardo Pineda Zapata  
**Alumno**: Alfredo Giovanni Enciso Solis  
**Número de Control**: 20100192  
**Instituto**: Instituto Tecnológico de Nuevo Laredo  
**Fecha**: 29 de Septiembre de 2024

---

## Índice

1. [Introducción](#familia-de-protocolos-de-internet)
2. [Protocolos de Internet](#familia-de-protocolos-de-internet-1)
   - [TCP/IP](#tcpip)
   - [HTTP](#http)
   - [HTTPS](#https)
   - [FTP](#ftp)
   - [SMTP](#smtp)
   - [IMAP](#imap)
   - [DNS](#dns)
   - [SSH](#ssh)
3. [¿Qué es el protocolo HTTP y HTTPS?](#qué-es-el-protocolo-http-y-https)
4. [¿Qué es el protocolo SSL/TLS?](#qué-es-el-protocolo-ssltls)
5. [Partes de una Petición y una Respuesta HTTP](#partes-de-una-petición-y-una-respuesta-http)
   - [Petición HTTP](#petición-http)
   - [Respuesta HTTP](#respuesta-http)
6. [¿Qué son los Headers en una Petición/Respuesta HTTP?](#qué-son-los-headers-en-una-peticiónrespuesta-http)
7. [Clasificación de los Códigos de Estado en la Respuesta HTTP](#clasificación-de-los-códigos-de-estado-en-la-respuesta-http)
   - [1xx: Informativos](#1xx-informativos)
   - [2xx: Éxito](#2xx-éxito)
   - [3xx: Redirección](#3xx-redirección)
   - [4xx: Errores del Cliente](#4xx-errores-del-cliente)
   - [5xx: Errores del Servidor](#5xx-errores-del-servidor)

---
# Introduccion

La familia de protocolos de internet consiste en un conjunto de reglas que permiten la comunicación entre dispositivos en la red. Estos protocolos determinan cómo se deben transmitir, recibir y gestionar los datos a través de internet. A continuación, se muestra una tabla con algunos de los protocolos más comunes:

| **Protocolo** | **Descripción** |
|---------------|-----------------|
| **TCP/IP**    | El protocolo principal que establece cómo se deben empaquetar, enviar y recibir datos. |
| **HTTP**      | Protocolo de Transferencia de Hipertexto; se utiliza para la transmisión de datos en la web. |
| **HTTPS**     | Versión segura de HTTP, que usa cifrado para proteger la transferencia de datos. |
| **FTP**       | Protocolo de Transferencia de Archivos; se usa para transferir archivos entre cliente y servidor. |
| **SMTP**      | Protocolo Simple de Transferencia de Correo; usado para enviar correos electrónicos. |
| **IMAP**      | Protocolo de Acceso a Mensajes de Internet; se utiliza para leer correos desde un servidor remoto. |
| **DNS**       | Sistema de Nombres de Dominio; traduce los nombres de dominio en direcciones IP. |
| **SSH**       | Protocolo para acceder de forma segura a un dispositivo remoto. |

# ¿Qué es el protocolo HTTP y HTTPS?

- **HTTP (Protocolo de Transferencia de Hipertexto)**: Es el protocolo utilizado para la transmisión de información en la web. Permite la comunicación entre un cliente (como un navegador) y un servidor, facilitando la transferencia de páginas web, imágenes, videos y otros contenidos.
  
- **HTTPS (HTTP Seguro)**: Es una versión cifrada de HTTP, que garantiza la privacidad y seguridad de los datos que se intercambian entre el cliente y el servidor. Usa el protocolo SSL/TLS para cifrar la información y protegerla contra posibles ataques.

# ¿Qué es el protocolo SSL/TLS?

- **SSL (Secure Sockets Layer)** y **TLS (Transport Layer Security)** son protocolos de seguridad que se utilizan para cifrar la comunicación entre dispositivos en la red. Se utilizan principalmente en HTTPS para garantizar que la información transferida entre el cliente y el servidor esté protegida y no pueda ser interceptada o modificada por terceros.

# Partes de una Petición y una Respuesta HTTP

## Petición HTTP:
1. **Línea de Petición**: Contiene el método HTTP (GET, POST, PUT, DELETE, etc.), el recurso solicitado (URL) y la versión del protocolo (HTTP/1.1, HTTP/2).

   Ejemplo:
   ```http
   GET /index.html HTTP/1.1

## Headers (Encabezados)
Contienen información adicional sobre la petición, como el tipo de contenido aceptado, las credenciales de autenticación, el agente de usuario, entre otros.

**Ejemplo:**

Host: www.ejemplo.com
User-Agent: Mozilla/5.0
Accept: text/html


## Body (Cuerpo)
Contiene los datos que se envían al servidor en métodos como POST o PUT. Puede ser un formulario, datos JSON, etc. No siempre está presente en todas las peticiones.

## Respuesta HTTP

### 1. Línea de Respuesta
Incluye la versión del protocolo HTTP, el código de estado y una breve descripción del estado.

**Ejemplo:**
HTTP/1.1 200 OK


### 2. Headers (Encabezados)
Proporcionan metadatos sobre la respuesta, como el tipo de contenido, la longitud del cuerpo, la fecha, las cookies, etc.

**Ejemplo:**

Content-Type: text/html
Content-Length: 3456


### 3. Body (Cuerpo)
Contiene los datos solicitados, como el contenido de una página web, un archivo JSON, una imagen, entre otros.

## ¿Qué son los Headers en una Petición/Respuesta HTTP?
Los Headers (encabezados) en una petición o respuesta HTTP son líneas de metadatos que proporcionan información adicional sobre la comunicación entre el cliente y el servidor. Sirven para:

- Definir el tipo de contenido enviado o solicitado (por ejemplo, `Content-Type: application/json`).
- Especificar el tamaño del cuerpo de la respuesta (`Content-Length`).
- Proporcionar información sobre el cliente (como el navegador o sistema operativo, mediante el encabezado `User-Agent`).
- Gestionar el almacenamiento en caché (`Cache-Control`).
- Incluir credenciales de autenticación (mediante el encabezado `Authorization`).

En resumen, los headers ayudan a personalizar, optimizar y asegurar la comunicación HTTP entre cliente y servidor.

## Clasificación de los Códigos de Estado en la Respuesta HTTP
Los códigos de estado en HTTP indican el resultado de una petición. Se clasifican de la siguiente manera:

### 1xx: Informativos
- **100 Continue:** El servidor ha recibido la solicitud y el cliente puede continuar enviando el cuerpo.
- **101 Switching Protocols:** El servidor acepta cambiar el protocolo según la solicitud del cliente.

### 2xx: Éxito
- **200 OK:** La solicitud ha tenido éxito y el servidor devuelve los datos solicitados.
- **201 Created:** La solicitud ha sido completada y un nuevo recurso ha sido creado.

### 3xx: Redirección
- **301 Moved Permanently:** El recurso solicitado ha sido movido a una nueva URL de forma permanente.
- **302 Found:** El recurso ha sido encontrado en una ubicación temporalmente diferente.

### 4xx: Errores del Cliente
- **400 Bad Request:** El servidor no puede procesar la solicitud debido a un error del cliente (por ejemplo, formato incorrecto).
- **401 Unauthorized:** La autenticación es requerida para acceder al recurso.
- **404 Not Found:** El recurso solicitado no se ha encontrado en el servidor.

### 5xx: Errores del Servidor
- **500 Internal Server Error:** El servidor ha encontrado un error inesperado y no puede cumplir con la solicitud.
- **503 Service Unavailable:** El servidor no está disponible temporalmente, generalmente debido a mantenimiento o sobrecarga.
