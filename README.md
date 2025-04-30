# Problema numero 3 de clinica y Ejercios de Pilas 
# Autores: Anthony Flores, Juan Putoy, Dosson Narváez, Roberto Lopez

Problema: Una clínica recibe pacientes en orden de llegada. Cada paciente debe ser ingresado al sistema
con los siguientes datos: nombre completo, edad, síntoma principal y prioridad (de 1 a 5). El
sistema debe permitir insertar nuevos pacientes, recorrer la lista para mostrar el orden de
atención, y eliminar a un paciente una vez atendido. 

1.Implementa un método que reciba una pila de enteros como único parámetro. Este método llamado “separarParImpar” deberá retornar la pila con los números pares en la parte inferior y los impares en la superior.
 Ejemplo:
Entrada –> [ 2, 3, 6, 8, 11, 13, 18, 21]
Salida –> [ 2, 6, 8, 18, 3, 11, 13, 21] PARES / IMPARES
 Nota: No hace falta que los números estén ordenados de menor a mayor, esto solo es un ejemplo. Lo importante es separar los pares de los impares.
 
 2. Implementa un método llamado “ordena” que reciba una pila de enteros como parámetro y devuelva la pila ordenada de mayor (fondo de la pila) a menor (top de la pila).
Ejemplo:
Entrada –> [ 1, 3, 2, 4]
Salida –> [ 4, 3, 2, 1]
 
 3. Diseñar un método “Convbinario” que reciba un entero como parámetro. La función, usando una pila, deberá mostrar el número en código binario.
 Ejemplo:
Entrada –> 12
Salida –> [1100]
