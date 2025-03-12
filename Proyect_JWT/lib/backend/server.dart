import 'dart:io';
import 'dart:convert';

import 'jwt_manager.dart';

void startServer() async {
  final server = await HttpServer.bind(InternetAddress.loopbackIPv4, 8080);
  print('Servidor escuchando en http://localhost:8080');

  await for (HttpRequest request in server) {
    if (request.uri.path == '/login' && request.method == 'POST') {
      // Manejo de la solicitud de login
      var content = await utf8.decoder.bind(request).join();
      var data = jsonDecode(content);

      String username = data['username'];
      String password = data['password'];

      if (username == 'admin' && password == 'adminpass') {
        String token = JwtManager().generateToken(username);
        request.response
          ..statusCode = HttpStatus.ok
          ..headers.contentType = ContentType.json
          ..write(jsonEncode({'token': token}));
      } else {
        request.response
          ..statusCode = HttpStatus.unauthorized
          ..write(jsonEncode({'error': 'Credenciales inválidas'}));
      }
      await request.response.close();
    } 
    else if (request.uri.path == '/protected' && request.method == 'GET') {
      // Llamada a handleRequest() para la ruta /protected
      await handleRequest(request);
    }
    else {
      request.response
        ..statusCode = HttpStatus.notFound
        ..write('Ruta no encontrada');
      await request.response.close();
    }
  }
}

Future<void> handleRequest(HttpRequest request) async {
  print('Solicitud a /protected recibida');
  String? token = request.headers.value('Authorization');
  if (token != null && token.startsWith('Bearer ')) {
    token = token.substring(7); // Elimina el Bearer
    var result = JwtManager().verifyToken(token);

    print('Resultado de la verificación del token: $result');

    if (result == 'Token valido') {
      request.response
        ..statusCode = HttpStatus.ok
        ..write('Acceso autorizado');
    } else {
      if (result == 'Token expirado, inicie sesión nuevamente.') {
        request.response
          ..statusCode = HttpStatus.unauthorized
          ..write('Vuelve a solicitar un token. Token expirado');
      }
    }
  } else {
    request.response
      ..statusCode = HttpStatus.unauthorized
      ..write('Token faltante');
  }
  
  await request.response.close();
}
