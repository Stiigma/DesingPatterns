import 'dart:io';
import 'dart:convert';
import 'package:http/http.dart' as http;

Future <void> loginUser() async {
  stdout.write('Ingresa su nombre de usuario: ');
  String username = stdin.readLineSync()!;

  stdout.write('Ingresa su nombre de contrasena: ');
  String password = stdin.readLineSync()!;

  var response = await http.post(
    Uri.parse('http://localhost:8080/login'),
    headers: {'Content-Type': 'application/json'},
    body: jsonEncode({'username' : username, 'password' : password})
  );

  if(response.statusCode == 200){
    var data = jsonDecode(response.body);
    print('JWT recibido : ${data['token']}');
  }
  else{
    print('Error: ${response.body}');
  } 
}
Future<void> accessProtected() async{
  stdout.write('Ingrese su JWT: ');
  String token = stdin.readLineSync()!;

  var response = await http.get(
    Uri.parse('http://localhost:8080/protected'),
    headers: {'Authorization': 'Bearer $token'},
  );

  if(response.statusCode == 200){
    print('Acceso Autorizado');

  }else
  {
    print('Error de autorizacion: ${response.body}');
  }
}

void main() {
  print('1. Iniciar sesión');
  print('2. Acceder a ruta protegida');
  stdout.write('Seleccione una opción: ');
  String? choice = stdin.readLineSync();

  if (choice == '1') {
    loginUser();
  } else if (choice == '2') {
    accessProtected();
  } else {
    print('Opción no válida');
  }
}

