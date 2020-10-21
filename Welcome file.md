
# Création d'un horloge à mots

Matériel :
- Un raspberry pi zéro W
- Un ruban de Leds
- Une photo résistance
- Un condensateur 47µF (entre 10 et 100)


# Préparation Raspberry

Récupération de l'OS [sur le site officiel](https://www.raspberrypi.org/downloads/raspberry-pi-os/)
Prendre la version Buster lite, (Minimal image based on Debian Buster)

Transférer l'image sur la flash grâce à [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/)
Edition des fichiers suivants dans le file system éditable (/boot)

 - ssh: créer un fichier vide
 - wpa_supplicant.conf : créer le fichier de destination :
 

    enter code here

## Possibilité de passer en systemd
avec le tutoriel [https://hackaday.io/project/162164/instructions](ici)

Seul modifcation LinkLocalAddress=yes 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc3NzU3MDE0MSwtODMwMDg5MTEyXX0=
-->