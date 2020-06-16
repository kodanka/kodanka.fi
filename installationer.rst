.. _installationer:

Installationer
==============

Här finns instruktioner för hur man installerar **Python** samt den mest populära kod redigeraren, **Visual Studio Code.**
Observera (detta gäller för alla operativsystem) att ifall man har Python färdigt på sin dator men det är en gammal version så
kan man ändå göra allt i materialet. Vissa delar i **Fördjupat** och **Projekt** kräver mera funktioner som man kan ladda ned med 
pakethanteraren **pip.** Den kommer färdigt med Python **3.4** och **nyare versioner**. Så har man en äldre version än det (vilket vi kommer att checka) 
så kan man helt bra installera nyare så som instruktionerna visar för att vara på säkra sidan.

Windows
#######

Windows kommer inte med Python färdigt, men man får det lätt från Microsoft Store. Visual Studio Code är också lätt att installera, 
det är trots allt Microsoft som har skapat det.

Python
******

- Börja med att öppna **Command Prompt** och se om Python är installerat genom att skriva:

::

  python --version

och

::

  python3 --version

Om båda säger "not recognized as an internal or external command" så kan man installera Python så här:

- Öppna **Microsoft Store**
- Sök på **Python 3.8** och tryck på **Hämta**
- När det är klart kan du igen öppna Command Prompt och skriva samma sak för att se att det fungerade

Visual Studio Code
******************

- Gå till https://code.visualstudio.com/download och tryck på ladda ner för Windows
- Kör **.exe** installeraren när det har laddat klart

Mac
###

Mac har alltid Python 2 installerat. Det går som sagt bra att lära sig programmera med det, 
men här är instruktioner för hur man installerar en nyare version.

Python
******

- Börja med att öppna **Terminal**
- Kolla om en ny version av Python redan är installerad genom att skriva:

::

  python --version
  python3 --version

- Om inte, gå till https://www.python.org/downloads
- Tryck på **Download** knappen som laddar ner den senaste Python versionen för Mac Os
- Kör den nerladdade **.pkg** filen och följ dialogen för att installera Python
- Testa att det fungerar genom att skriva samma sak i **Terminal** igen, ena kommandot borde ge en Python 3.x version.

Visual Studio Code
******************

- Gå till https://code.visualstudio.com/download och tryck på ladda ner för Mac
- Öppna **Visual Studio Code** när det har laddat klart
- Nästa steg är att byta mapp för **Visual Studio Code** 
- Öppna **Finder** > **Downloads**
- Dra **Visual Studio Code** till **Applications** mappen.
- Nu kan man öppna **Visual Studio Code** från **Launch Pad**

Linux
#####

Här finns installations-instruktioner för Debian/Ubuntu. Ifall man har en annan Linux distribution finns det mera information på nätet.
Linux kommer ofta med Python färdigt installerat.

Python
******

- Börja med att öppna **Terminal**
- Kolla om Python redan är installerat:

::

  python --version
  python3 --version

- Om ingetdera kommando visar en installerad Python version, eller om den är mindre än 3.4 kan man installera det så här:

::

  sudo add-apt-repository ppa:deadsnakes/ppa
  sudo apt-get update
  sudo apt-get install python3.8

Visual Studio Code
******************

- Det är lättast att ladda ned som ett Snap paket:

::
  
  sudo snap install --classic code

- För mera information eller ifall man har en annan linux distribution: https://code.visualstudio.com/docs/setup/linux

Chromebook
##########

- Vi rekommenderar att koda på nätet med Chromebooks, följ det som står under :ref:`python-online`
- Chrome OS applikationer är i allmänhet på webben så det är lite krångligt att försöka installera något men det ska ändå gå att `göra det via terminalen <https://installpython3.com/chromebook>`_ om man först aktiverar Linux på sin maskin.