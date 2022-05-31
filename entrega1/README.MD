README
1er Entrega Web 
https://github.com/lemilse73/Entrega1Paulluk.git

Estructura:
Página sobre Información de Running conformada por 3 grupos:
CORREDOR:
•	nombre 
•	apellido 
•	modalidad 
•	email 
•	team 
CARRERAS: 
•	nombre 
•	modalidad 
•	distancia (NUM)
•	fecha (AAAA-MM-DD) 
TEAMS:
•	nombre 
•	modalidad 
•	email 
El detalle de cada grupo/base se direcciona desde la URL o por medio de las siguientes rutas:
app_running/corredor
app_running/carreras
app_running/teams



Altas:
Incluye 3 altas de datos, una por cada grupo:
app_running/alta_corredor
app_running/alta_carreras
app_running/alta_teams




Búsqueda:
Incluye 3 búsquedas, dos relacionadas con el grupo corredor:
	app_running/buscar_corredor (busca por nombre),
    app_running/buscar_corredor _apellido (busca por apellido),
otra búsqueda del grupo carreras, por nombre:
    app_running/buscar_carreras_nombre.
