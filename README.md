# Desarrollo de web API
Para la ejecución de la aplicación basta con ejecutar en el CMD

    pipenv shell
    pipenv install
    python myapp.py
    
## Rutas de aplicación
La aplicación tiene 5 consultas implementadas
##### Completas
* **url messages/id** esta consulta solo retornaran la información de dicho mensaje con id correspondiente (ya que es 
un resultado).
* **url message/proyect_search** esta consulta retornará un json con el formato
{1: resultado1, 2: resultado2}
* **url message/id (delete)** esta consulta permite borrar el mensaje con la id correspondiente
##### Incompletas
Ambas funciones lanzan error con request.json
* **url message/content-search** esta consulta permite buscar aquellos correos que cumplen con el requisito de la 
palabra o frase requerida o prohibida.
* **url messages** esta consulta permite añadir nuevos correos a la colección

##### PD: como grupo nos faltó tiempo debido a que un integrante tenía problemas con su computador, pues estaba ocupando un computador de la biblioteca y estos no permiten ciertos accesos de administrador
