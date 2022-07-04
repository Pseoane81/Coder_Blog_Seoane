# Coder_Blog_Seoane
Coder BLog
Blog Realizado por Pablo Seoane en base Python con framework Django
Se realizo sobre 3 APP de Django
BLOG, tiene todas las paginas del home, about y padre
POSTS, tiene todas las paginas del CRUD de posts, ademas tablas.
USERS, tiene todas las paginas del CRUD de usuarios.



Paginas:

Paginas Base

/ Muestra el Home
/blog / Muestra el Home
/blog/about/` Muestra "Sobre Mi" Para esta Pagina muestra siempre los datos del creador Pablo Seoane


Pagina de Usuarios

/users/perfiles/  Muestra una tabla con todos los perfiles creados
/users/userpost/<int:id> Muestra los datos del perfil seleccionado y los posts creados
/users/editarperfil/<int:id>  Edita el perfil seleciconado
/users/logout Sale del usuario
/users/birrarperfil  Borra el perfil del usurio

Paginas de Posts

/posts/nuevopost/ Crea un nuevo post
/posts/tablapost/ Tabla con todos los post donde se pueden ver, editar y borrar
/posts/post/<int:id>  Visualizacion de un post
/posts/editpost/<int:id> Edicion de post seleccionado
posts/deletepost/<int:id> Eliminar Post seleccionado









 
