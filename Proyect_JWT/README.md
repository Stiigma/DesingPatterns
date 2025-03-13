
# Sistema de Autenticación con JWT y Dart

Este proyecto es una implementación práctica de un sistema de autenticación utilizando JSON Web Tokens (JWT) en un servidor Dart, junto con un cliente de consola para interactuar con él. Su objetivo principal es demostrar cómo proteger rutas en un servidor mediante JWT y explorar el uso del patrón Singleton para gestionar la generación y verificación de tokens.

---

## Características principales
- **Servidor HTTP**: Maneja rutas para login (`/login`) y una ruta protegida (`/protected`).
- **JWT Manager**: Clase encargada de generar y verificar tokens JWT usando la biblioteca `dart_jsonwebtoken`.
- **Cliente CLI**: Interfaz de consola para autenticarse y acceder a la ruta protegida.
- **Validación de tokens**: Verificación de expiración y autenticidad del token en cada solicitud protegida.

---

## Justificación del uso de JWT
1. **Seguridad**: JWT permite firmar tokens con una clave secreta, asegurando que no puedan ser modificados por terceros.
2. **Stateless**: Elimina la necesidad de almacenar sesiones en el servidor, ideal para arquitecturas escalables.
3. **Autocontenido**: El token incluye metadatos (como el tiempo de expiración) y datos del usuario, reduciendo consultas a bases de datos.
4. **Estándar ampliamente adoptado**: Compatible con múltiples lenguajes y frameworks, facilitando la integración con futuros clientes (web, móvil, etc.).

---

## Uso del patrón Singleton en `JwtManager`
El proyecto utiliza el patrón Singleton en la clase `JwtManager` para garantizar que:
- Exista **una única instancia** encargada de gestionar los tokens, evitando duplicaciones innecesarias.
- La configuración de la clave secreta y métodos de generación/verificación se centralice en un único punto.
- Se optimicen recursos, ya que no se recrea la instancia en cada solicitud.

### ¿Por qué es relevante aquí?
Este es un proyecto práctico diseñado específicamente para entender el funcionamiento del patrón Singleton. Al implementarlo en `JwtManager`, se asegura:
- Consistencia en la firma y verificación de tokens.
- Un punto único de control para futuras modificaciones (ej: rotación de claves).
- Aprendizaje sobre cómo los Singletons previenen problemas en entornos concurrentes.

---

## Ejecución del proyecto
1. **Iniciar el servidor**:
   ```bash
   dart run server.dart
   ```
2. **Ejecutar cliente**
    ```bash
   dart run console_view.dart
   ```
3. **Usar credenciales de prueba**
   - Usuario: **admin**
   - contrasena: **adminpass**

### Notas Adicionales

* **Propósito educativo**: Este proyecto es una primera aproximación al uso de JWT y Singletons en Dart. No incluye características avanzadas como refresh tokens, almacenamiento seguro de claves, o roles de usuario.

* **Mejoras futuras**:: Se podría agregar registro de usuarios, múltiples claves JWT, o integración con bases de datos.

* **Advertencia**: La clave secreta ('Stiigma') está hardcodeada solo con fines demostrativos. En entornos reales, debe almacenarse de forma segura (ej: variables de entorno).
