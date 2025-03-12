import 'dart:convert';
import 'package:http/http.dart' as http;

class CLIHandler {
  // Método para iniciar sesión y obtener el token
  Future<String?> login(String username, String password) async {
    var url = Uri.parse('http://localhost:8080/login');
    
    // Crea el cuerpo de la solicitud con el username y password
    var response = await http.post(
      url,
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'username': username, 'password': password}),
    );

    if (response.statusCode == 200) {
      // Si el login es exitoso, retorna el token
      var data = jsonDecode(response.body);
      return data['token'];
    } else {
      // Si las credenciales son incorrectas, devuelve un error
      print('Error de login: ${jsonDecode(response.body)['error']}');
      return null;
    }
  }

  // Método para acceder a la ruta protegida con el token
  Future<void> accessProtectedRoute(String token) async {
    var url = Uri.parse('http://localhost:8080/protected');
    print('Haciendo solicitud a la URL: $url');
    var response = await http.get(
      url,
      headers: {'Authorization': 'Bearer $token'},
    );
    print('Código de estado: ${response.statusCode}');
    if (response.statusCode == 200) {
      print('Acceso autorizado: ${response.body}');
    } else {
      print('Error: ${response.body}');
    }
  }
}