from function import *
'''
Realizar un programa que permita el ingreso de temperaturas a lo largo de una semana 
(Los 7 días de la semana, no necesariamente se ingresan en orden. Por ejemplo, puedo cargar primero el miércoles,
luego el domingo, etc.). Dadas estas temperaturas debemos obtener distintas estadísticas.
Para ello se deberán implementar distintas funciones:

1. Una que permita la carga de todas las temperaturas (día y temperatura).
2. Una que permita el pedido y validación de una temperatura. La misma retornará una temperatura válida.
3. Una que reciba como parámetro la lista y retorne el promedio de temperaturas.
4. Una que calcule la temperatura máxima.
5. Una que gestione un menú de usuario, el cual deberá tener las siguientes opciones:
a. Cargar temperaturas
b. Mostrar temperaturas (junto con sus días)
c. Mostrar máxima temperatura con su día. (tener en cuenta que puede haber varios días con la misma temperatura)
d. Mostrar promedio.
e. Salir

Nota: No se podrá entrar a las opciones b, c y d si no se cargaron los datos en la opción a.
'''

menu()