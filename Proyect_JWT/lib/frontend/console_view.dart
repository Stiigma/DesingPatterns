import 'dart:io';
import 'cli_handler.dart';

void main() async {
  var cliHandler = CLIHandler();
  
  print('Bienvenido al sistema de autenticación');
  
  // Solicitar credenciales de login
  print('Ingresa tu nombre de usuario:');
  String? username = stdin.readLineSync();
  
  print('Ingresa tu contraseña:');
  String? password = stdin.readLineSync();

  // Hacer login y obtener el token
  String? token = await cliHandler.login(username!, password!);
  
  if (token != null) {
    print('Login exitoso. Token recibido: $token');

    // Ahora puedes acceder a la ruta protegida
    print('¿Deseas acceder a la ruta protegida? (s/n)');
    String? choice = stdin.readLineSync();
    
    if (choice == 's' || choice == 'S') {
      await cliHandler.accessProtectedRoute(token);
    }
  } else {
    print('Login fallido');
  }
}
