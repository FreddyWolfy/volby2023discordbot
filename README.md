# Volební Discord bot
Discord bot pro prezidentské volby ČR 2023

Bot dokáže brát data z Českého statistického úřadu a zobrazoval je v channelu.

Taktéž odpočítává do druhého kola voleb, v den voleb oznaci "@everyone" a připomene volby.

Do 27.1.2023 se bot aktualizuje co hodinu, od 28.1.2023 se aktualizuje co 5 minut od 29.1.2023 každých 13 hodin



## Instalace a použití

Musíte obdržet discord token, stačí na https://discord.com/developers/applications vytvorit novou aplikaci a bota, pak zkoirovat token a vlozit ho do "discordtoken" promněné.


Na stránce "URL Generator" v Discord Developer Portalu zaškrtnout "Bot" a "Administrator" a pozvat skrze odkaz bota na server.

Na hostingu dle vašeho výběru stačí naistalovat

```
pip install discord.py
```
a následně StringProgressBar od Sparker-99 - https://github.com/Sparker-99/string-progressbar

```
pip install StringProgressBar
```

pak spustit na pozadí python soubor volebnibot.py

V discord serveru pak stačí v jakémkoliv discord channelu napsat ".hello" a bot bude spustěn.




