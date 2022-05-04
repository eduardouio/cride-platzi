### Apuntes de l curso de django

## Apuntes de Entornos
<pre>docker-compose -f local.yml build </pre>

### para listar todas las imagenes creadas por docker
<pre>docker images</pre>

### para levantar los servicios del entrono de desarrollo
<pre>docker-compose -f local.yml up</pre> 

### Para interactual con el manage de django

<pre>docker-compose run --rm django [command]</pre>

#### ejemplo
<pre>docker-compose run --rm django python manage.py createsuper user</pre>


### Administrar los servicio del stack

<ul>
    <li><pre>docker-compose -f local.yml up </pre> Levanta todos los servicios</li>
    <li><pre>docker-compose -f local.yml ps</pre> Lista los servicios que se encuentran ejecutando </li>
    <li><pre>docker rm -f [ID]</pre>detiene la ejecución de uno de los serivicio</li>
    <li><pre>docker-componse run --rm --service-ports [django]</pre></li>
</ul>

### comandos de docker

<pre>docker container</pre>
<pre>docker images </pre>
<pre>docker volume</pre>
<pre>docker network</pre>


# Apuntes de Django

### Herencia de modelos

Se aplica los mismos conceptos de herencia de programación
Creamos un modelo absracto para que los demás modelos heren de ella, en este caso creamos un modelo de django con el valor en meta de abstract


