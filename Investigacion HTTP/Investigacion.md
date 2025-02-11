# Familia de Protocolos de Internet

## Programación Web  
**Maestro**: Gerardo Pineda Zapata  
**Alumno**: Alfredo Giovanni Enciso Solis  
**Número de Control**: 20100192  
**Instituto**: Instituto Tecnológico de Nuevo Laredo  
**Fecha**: 10 de Febrero del 2025

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
4. [Versiones del Protocolo HTTP](#versiones-del-protocolo-http)
5. [¿Qué es el protocolo SSL/TLS?](#qué-es-el-protocolo-ssltls)
6. [Partes de una Petición y una Respuesta HTTP](#partes-de-una-petición-y-una-respuesta-http)
   - [Petición HTTP](#petición-http)
   - [Respuesta HTTP](#respuesta-http)
7. [¿Qué son los Headers en una Petición/Respuesta HTTP?](#qué-son-los-headers-en-una-peticiónrespuesta-http)
8. [Clasificación de los Códigos de Estado en la Respuesta HTTP](#clasificación-de-los-códigos-de-estado-en-la-respuesta-http)
   - [1xx: Informativos](#1xx-informativos)
   - [2xx: Éxito](#2xx-éxito)
   - [3xx: Redirección](#3xx-redirección)
   - [4xx: Errores del Cliente](#4xx-errores-del-cliente)
   - [5xx: Errores del Servidor](#5xx-errores-del-servidor)

---

# Introducción

La familia de protocolos de internet consiste en un conjunto de reglas que permiten la comunicación entre dispositivos en la red. Estos protocolos determinan cómo se deben transmitir, recibir y gestionar los datos a través de internet. A continuación, se muestra una tabla con algunos de los protocolos más comunes:

| **Protocolo** | **Descripción** |
|--------------|----------------|
| **TCP/IP** | El protocolo principal que establece cómo se deben empaquetar, enviar y recibir datos. |
| **HTTP** | Protocolo de Transferencia de Hipertexto; se utiliza para la transmisión de datos en la web. |
| **HTTPS** | Versión segura de HTTP, que usa cifrado para proteger la transferencia de datos. |
| **FTP** | Protocolo de Transferencia de Archivos; se usa para transferir archivos entre cliente y servidor. |
| **SMTP** | Protocolo Simple de Transferencia de Correo; usado para enviar correos electrónicos. |
| **IMAP** | Protocolo de Acceso a Mensajes de Internet; se utiliza para leer correos desde un servidor remoto. |
| **DNS** | Sistema de Nombres de Dominio; traduce los nombres de dominio en direcciones IP. |
| **SSH** | Protocolo para acceder de forma segura a un dispositivo remoto. |

# ¿Qué es el protocolo HTTP y HTTPS?

- **HTTP (Protocolo de Transferencia de Hipertexto)**: Es el protocolo utilizado para la transmisión de información en la web. Permite la comunicación entre un cliente (como un navegador) y un servidor, facilitando la transferencia de páginas web, imágenes, videos y otros contenidos.
  
- **HTTPS (HTTP Seguro)**: Es una versión cifrada de HTTP, que garantiza la privacidad y seguridad de los datos que se intercambian entre el cliente y el servidor. Usa el protocolo SSL/TLS para cifrar la información y protegerla contra posibles ataques.

# Versiones del Protocolo HTTP

El protocolo HTTP ha evolucionado con el tiempo para mejorar la eficiencia y la seguridad en la transmisión de datos. A continuación, se describen sus principales versiones:

- **HTTP/0.9 (1991)**: La primera versión del protocolo, que solo permitía la transferencia de texto sin encabezados ni estructura compleja.
- **HTTP/1.0 (1996)**: Introdujo encabezados HTTP y la posibilidad de transmitir contenido de diferentes tipos.
- **HTTP/1.1 (1997)**: Mejoró la eficiencia al permitir conexiones persistentes y el uso de pipelining.
- **HTTP/2 (2015)**: Introdujo multiplexación, compresión de encabezados y mejor rendimiento en la carga de páginas.
- **HTTP/3 (2022)**: Basado en QUIC, reduce la latencia y mejora la seguridad con cifrado por defecto.

# ¿Qué es el protocolo SSL/TLS?

- **SSL (Secure Sockets Layer)** y **TLS (Transport Layer Security)** son protocolos de seguridad que se utilizan para cifrar la comunicación entre dispositivos en la red. Se utilizan principalmente en HTTPS para garantizar que la información transferida entre el cliente y el servidor esté protegida y no pueda ser interceptada o modificada por terceros.

# Partes de una Petición y una Respuesta HTTP

## Petición HTTP:
1. **Línea de Petición**: Contiene el método HTTP (GET, POST, PUT, DELETE, etc.), el recurso solicitado (URL) y la versión del protocolo (HTTP/1.1, HTTP/2).

   Ejemplo:
   ```http
   GET /index.html HTTP/1.1
   ```

## Headers (Encabezados)
Contienen información adicional sobre la petición, como el tipo de contenido aceptado, las credenciales de autenticación, el agente de usuario, entre otros.

**Ejemplo:**
```http
Host: www.ejemplo.com
User-Agent: Mozilla/5.0
Accept: text/html
```

## Body (Cuerpo)
Contiene los datos que se envían al servidor en métodos como POST o PUT. Puede ser un formulario, datos JSON, etc. No siempre está presente en todas las peticiones.

## Respuesta HTTP

### 1. Línea de Respuesta
Incluye la versión del protocolo HTTP, el código de estado y una breve descripción del estado.

**Ejemplo:**
```http
HTTP/1.1 200 OK
```

### 2. Headers (Encabezados)
Proporcionan metadatos sobre la respuesta, como el tipo de contenido, la longitud del cuerpo, la fecha, las cookies, etc.

**Ejemplo:**
```http
Content-Type: text/html
Content-Length: 3456
```

### 3. Body (Cuerpo)
Contiene los datos solicitados, como el contenido de una página web, un archivo JSON, una imagen, entre otros.

### Respuesta HTTP

1. **Línea de Respuesta**: Versión HTTP, código de estado y descripción.
2. **Headers**: Metadatos como tipo de contenido y longitud.
3. **Body**: Contenido de la respuesta.

## ¿Qué son los Headers en una Petición/Respuesta HTTP?

Los headers proporcionan información adicional en una petición o respuesta HTTP, como tipo de contenido, autenticación y caché.

## Clasificación de los Códigos de Estado en la Respuesta HTTP

### 1xx: Informativos
- **100 Continue:** El cliente puede continuar con la solicitud.

### 2xx: Éxito
- **200 OK:** La solicitud ha tenido éxito.

### 3xx: Redirección
- **301 Moved Permanently:** Recurso movido de forma permanente.

### 4xx: Errores del Cliente
- **404 Not Found:** Recurso no encontrado.

### 5xx: Errores del Servidor
- **500 Internal Server Error:** Error inesperado en el servidor.

## Estructura URL, URN y URI

- **URL (Uniform Resource Locator)**: Dirección completa de un recurso en la web.
  - Ejemplo: `https://www.ejemplo.com/index.html`
- **URN (Uniform Resource Name)**: Nombre único de un recurso dentro de un espacio de nombres.
  - Ejemplo: `urn:isbn:0451450523`
- **URI (Uniform Resource Identifier)**: Identificador general de un recurso, que puede ser una URL o un URN.
