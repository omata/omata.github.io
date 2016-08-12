Title: Cómo saber qué dispositivos están conectados a nuestra red
Date: 2014-07-18 18:29:00
Author: tektronica
Category: text
Tags: linux, sysadmin, nmap, cli, debian, ubuntu
Slug: 2014-07-18-cómo-saber-qué-dispositivos-están-conectados-a
Status: published

Para esta actividad usaremos la herramienta **nmap**, que nos permite
hacer escaneo de diferentes tipos en servidores o sub redes.

</p>

Para el escaneo de dispositivos usamos el siguiente comando:

</p>
<p>
    sudo nmap -sP 192.168.1.0/24

</p>

Esto revisará todas las direcciones contenidas en la sub red
192.168.1.0/24 (notación CIDR).

</p>

