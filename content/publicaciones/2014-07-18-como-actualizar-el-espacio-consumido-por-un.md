Title: Como actualizar el espacio consumido por un dominio en un servidor basado en Plesk versión 12.X
Date: 2014-07-18 17:05:00
Author: tektronica
Category: text
Tags: sysadmin, linux, plesk, servidor, cli, centos
Slug: 2014-07-18-como-actualizar-el-espacio-consumido-por-un
Status: published

Se utiliza la interfaz de comandos entrando como usuario root.

</p>

Luego vamos a la ruta: *`'/usr/local/psa/admin/sbin'`* y ejecutamos el
siguiente comando:

</p>
<p>
    ./statistics --calculate-one --domain-name=dominio.tld

</p>

Esto debe actualizar el espacio consumido por el dominio.

</p>

