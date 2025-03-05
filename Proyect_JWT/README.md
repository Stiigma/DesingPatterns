
## PROYECTO PRACTICO DEL PATRON SINGLETON
#### Proyecto
- **Autentificacion con JW** dirigido a un servidor

# Resumen sobre JWT 

**JSON Web Token (JWT)** es un formato compacto y seguro para transmitir información entre dos partes en aplicaciones web. Se utiliza comúnmente en la autenticación y autorización de usuarios.

Un JWT está compuesto por tres partes:

1. **Encabezado (Header)**: Especifica el tipo de token (JWT) y el algoritmo de firma (por ejemplo, HMAC SHA256 o RSA).
2. **Cuerpo (Payload)**: Contiene las "reclamaciones" o datos que se quieren transmitir, como el ID de usuario, tiempo de expiración, etc.
3. **Firma (Signature)**: Asegura que el token no haya sido alterado en tránsito. Se genera firmando el encabezado y el cuerpo con una clave secreta o una clave pública/privada.

## Tipos de JWT

Existen dos tipos de JWT:

- **JWS (JSON Web Signature)**: El contenido está firmado digitalmente para asegurar que no se haya alterado, pero el contenido sigue siendo visible.
- **JWE (JSON Web Encryption)**: El contenido está cifrado para proteger la información sensible, asegurando tanto la integridad como la confidencialidad.

