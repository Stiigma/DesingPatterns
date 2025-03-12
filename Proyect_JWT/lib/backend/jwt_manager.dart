import 'package:dart_jsonwebtoken/dart_jsonwebtoken.dart';

class JwtManager {
  // Instancia estática privada
  static final JwtManager _instance = JwtManager._internal();

  // Constructor privado
  JwtManager._internal();

  // Método para acceder a la instancia única
  factory JwtManager() {
    return _instance;
  }

  // Método para generar el JWT
  String generateToken(String userId) {
    final jwt = JWT({
      'id': userId,
      'exp': DateTime.now().add(Duration(hours: 1)).millisecondsSinceEpoch ~/ 1000, 
    });

    return jwt.sign(SecretKey('Stiigma'));
  }

// Método para verificar el JWT
  String verifyToken(String token) {
    try {
      final jwt = JWT.verify(token, SecretKey('Stiigma'));
      return "Token valido";
    } catch (e) {
      if (e is JWTExpiredException) {
        return "Token expirado, inicie sesión nuevamente.";
      }
      return "Token inválido.";
    }
  }
}
