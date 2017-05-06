C�mo extraer una o varias extensiones de un proyecto
=====================================================

Tenemos un proyecto enviado por un tercero, y no sabemos qu� extensiones tiene.
Creemos que algunas de las extensiones, pero no todas, las tenemos ya extra�das
y funcionando en el sistema. 

Para extraer las restantes, el procedimiento propuesto es el siguiente:

Calcular el parche entre el proyecto y los m�dulos
-----------------------------------------------------
Hay que tener en cuenta que los parches se deben calcular contra lo que se envia
, sin las personalizaciones propias. Cuantas menos personalizaciones tenga el 
proyecto, mejor.

Si es un proyecto de GIT, y se control� separadamente los env�os, hay que recordar
hacer un checkout a la rama apropiada.

Para calcular un parche manualmente, har�amos algo as�::

    $ eneboo-mergetool folder-diff /tmp/projectpatch ~/git/eneboo-modules ~/git/abanq.modules/myproject/

Esto crear� una carpeta /tmp/projectpatch (atenci�n: en /tmp normalmente se borra
al reiniciar el equipo). 

Esta carpeta contiene las diferencias encontradas.

Creamos el proyecto interno
------------------------------
Usaremos la utilidad de autodetecci�n de eneboo-assembler new para que nos cree
un proyecto::

    $ eneboo-assembler new prjX101-project "Proyecto miProyecto" /tmp/projectpatch

Esto nos crear� un proyecto con una extensi�n "unida" que lo incluye todo, con 
extensiones que ten�amos ya creadas incluso. Nos habr� detectado autom�ticamente
los m�dulos, pero no las extensiones, ya que el parche se extray� desde los 
m�dulos oficiales.

Hay que recordar actualizar la base de datos de assembler:

    $ eneboo-assembler dbupdate

Crear carpeta de source
--------------------------
Antes de continuar, debemos compilar la carpeta de c�digo fuente para que la tome
como referencia en el trabajo de extracci�n::

    $ eneboo-assembler build project src

Esto nos crear� la carpeta build/src para el futuro.


Analizar las dependencias m�s extensivamente
----------------------------------------------

Para encontrar qu� dependencias nos faltaban por agregar, usaremos la acci�n
test-deps, que analiza esto mucho m�s a fondo. Nos dar� un listado de extensiones::

    $ eneboo-assembler test-deps project
    
Agregamos las extensiones que nos indica a conf/required_features.

Recompilamos los objetivos base y test-fullpatch::

    $ eneboo-assembler build project base

    $ eneboo-assembler build project test-fullpatch
    
Cuando termine el proceso, revisaremos m�s a fondo las diferencias usando kdiff3::

    $ cd path/to/project/build/
    $ kdiff3 base test-fullpatch
    
Analizaremos primero unos tipos de fichero m�s sencillos, y luego los m�s 
complejos, para intentar encontrar qu� extensiones puedan haber m�s y hayan
pasado inadvertidas y determinar qu� extensiones estamos extrayendo.

Cuando se modifican las dependencias, se debe recompilar "base", "fullpatch" y "test-fullpatch".
