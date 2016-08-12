Title: Cómo hacer ROOT a Milestone/Droid X/Milestone XT720 (Obsoleto)
Date: 2010-07-23 14:26:00
Author: tektronica
Category: text
Tags: motorola, droid x, root, hacks, ¿cómo se hace?, tutoriales, guías
Slug: 2010-07-23-cómo-hacer-root-a-milestonedroid-xmilestone
Status: published

![Droid
X](http://img.skitch.com/20100723-mpj4xn1rmqiww4in8pfkhfuesi.png)



</p>

A penas una semana ha bastado para permitir el acceso a áreas
privilegiadas del sistema **Android** que trae el **Droid X**. A
continuación los pasos necesarios para lograrlo; demás está decir que no
me hago responsable si dañas o no tu dispositivo, **TODOS LOS RIESGOS
CORREN POR TU CUENTA**.



</p>

<!-- more -->Este proceso se puede realizar en una computadora con
**Windows**, **Linux** o **Mac**; el mismo no es demasiado difícil, sólo
debes seguir los pasos que a continuación se describen:



</p>

1.  Descarga [este](http://cl.ly/1kbB "DroidXRoot_v2.zip") archivo y
    descomprimelo en una carpeta de tu preferencia, digamos
    "*C:\\DroidXRoot\_v2*".
2.  Instala la herramienta **ADB**,
    [aquí](http://alldroid.org/Default.aspx?tabid=40&g=posts&m=5167&#post5167)
    se describe el proceso; *(por ahora colocaré las instrucciones que
    encontré en un foro hasta que edite las propias en español)*.
3.  En el teléfono: **Inicio -\> Botón de menú -\> Configuraciones -\>
    Aplicaciones -\> Desarrollo***:* Asegúrate que la opción
    "*Depuración USB*" esté seleccionada/habilitada.
4.  Barra de estado, Conexión USB: Asegúrate de que el "*Modo PC*" esté
    seleccionado.
5.  Abre una interfaz de comandos en **Windows**: **Botón de Inicio -\>
    Ejecutar**: "*cmd*" *(sin comillas)*.
6.  Entra en la carpeta "*tools*" del **Android SDK** desde la interfaz
    de comandos y ejecuta "*adb devices*", si no ves listado tu
    dispositivo en el anunciado "*List of devices attached*", regresa al
    paso 2 para volver a revisar la instalación de la herramienta
    **ADB**, usa esa fuente como material de soporte para solucionar
    cualquier problema relacionado con esta herramienta.
7.  Ejecuta desde la interfaz de comandos "*cd c:\\DroidXRoot\_v2*",
    *(sin las comillas)*, o la ruta donde sea que hayas descomprimido el
    archivo descargado en el paso 1.
8.  Ejecuta desde la interfaz de comandos "*adb push Superuser.apk
    /sdcard/Superuser.apk*" *(sin las comillas)*.
9.  Ejecuta desde la interfaz de comandos "*adb push su /sdcard/su*"
    *(sin las comillas)*.
10. Ejecuta desde la interfaz de comandos "*adb push busybox
    /sdcard/busybox*" *(sin las comillas)*.
11. Ejecutar desde la interfaz de comandos "*adb push exploid
    /sqlite\_stmt\_journals/exploid*" *(sin las comillas)*.
12. Ejecutar desde la interfaz de comandos "*adb shell*" *(sin las
    comillas)*.
13. Ejecutar desde la interfa de comandos "*cd sqlite\_stmt\_journals*"
    *(sin las comillas)*.
14. Ejecutar desde la interfa de comandos "*chmod 755 exploid*" *(sin
    las comillas)*.
15. Desde el teléfono, navega a la pantalla donde se
    "*habilita/deshabilita*" el "*WiFi/Bluetooth*". *(Esto se hace desde
    "Configuraciones" o desde el Control en la pantalla de inicio de
    Android)*.
16. INMEDIATAMENTE después de ejecutar el siguinte paso apaga y enciende
    el WiFi o Bluetooth.
17. Ejecutar desde la interfa de comandos "*./exploid*", *(sin las
    comillas)*, y sigue las instrucciones en pantalla. Una vez
    finalizado el proceso regresarás al shell o interfaz de comandos de
    **Android**.
18. Ejecutar desde la interfa de comandos "*rootshell*", *(sin las
    comillas)*, se te preguntará una contraseña.
19. Introduce la contraseña "*secretlol*", *(sin las comillas)*;
    presiona "*ENTER/INTRO*" y ya eres *ROOT*, *(sabrás que estas en
    ROOT porque la interfaz de comandos mostrará el símbolo "\#" en vez
    de "\$")*.
20. Ejecutar desde la interfa de comandos "*cp /sdcard/Superuser.apk
    /system/app/Superuser.apk*" *(sin las comillas)*.
21. Ejecutar desde la interfa de comandos "*cp /sdcard/su
    /system/bin/su*" *(sin las comillas)*.
22. Ejecutar desde la interfa de comandos "*cp /sdcard/busybox
    /system/bin/busybox*" *(sin las comillas)*.
23. Ejecutar desde la interfa de comandos "*chmod 4755 /system/bin/su*"
    *(sin las comillas)*.
24. Ejecutar desde la interfa de comandos "*chmod 4755
    /system/bin/busybox*" *(sin las comillas)*.
25. Ejecutar desde la interfa de comandos "*rm /system/bin/rootshell*"
    *(sin las comillas)*.
26. Ejecutar desde la interfa de comandos "*exit*", *(sin las
    comillas)*, para salir del modo *ROOT* al modo usuario normal;
    *(esto desde la interfaz de comandos de Android en el teléfono)*.
27. Ejecutar desde la interfa de comandos "*exit*", *(sin las
    comillas)*, para salir de la intefaz de comandos de **Android** y
    regresar a la de tu computadora.

  
Para confirmar que efectivamente pudiste hacer el *ROOT* a tu **Droid
X** sigue los siguientes pasos:



</p>

1.  Ejecutar desde la interfa de comandos "*adb shell*" *(sin las
    comillas)*.
2.  Ejecutar desde la interfa de comandos "*su*", *(sin las comillas)*,
    ahora debería aparecer el símbolo "\#" en la interfaz de comandos
    que indica inequívocamente que estás en modo *ROOT*.
3.  Revisa la pantalla del teléfono para autorizar el acceso a *ROOT*.

¡Gracias a [Birdman](http://stevenbird.info/),
[Rainabba](http://rainabba.blogspot.com/), mbm y **Sebastian Kramer**
por todo su trabajo!



</p>

***Si tienes la posibilidad de agradecer monetariamente al amigo Birdman
quien fue el que encontró el vector de entrada al exploit que hizo
posible el ROOT puedes hacerlo
[aquí](https://www.paypal.com/us/cgi-bin/webscr?cmd=_flow&SESSION=wogCs6jZomawVBKrkiFbIlqyR-Ms4ClFOSG3RWH7Zx-NAqMni8ruHFHDI8G&dispatch=5885d80a13c0db1f8e263663d3faee8d66edfb0b39be7838e3b204755610594d "Hacer Donación"),
Birdman es un estudiante que podría aprovechar cada una de sus
donaciones en su formación.***



</p>

Procedimiento tomado de
[PocketNow](http://pocketnow.com/tweaks-hacks/how-to-root-the-droid-x "PocketNow").

</p>

