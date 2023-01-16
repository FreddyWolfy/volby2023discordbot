# Volební Discord bot
Discord bot pro prezidentské volby ČR 2023

![ukazka](https://user-images.githubusercontent.com/59704825/212625003-b33bdaa6-9bf5-4a5b-bca4-6e90502151db.png)


Bot dokáže brát data z Českého statistického úřadu a zobrazoval je v channelu.

Taktéž odpočítává do druhého kola voleb, v den voleb oznaci "@everyone" a připomene volby.

Do 27.1.2023 se bot aktualizuje co hodinu, od 28.1.2023 se aktualizuje co 5 minut od 29.1.2023 každých 13 hodin



## Instalace a použití

Musíte obdržet discord token, stačí na https://discord.com/developers/applications vytvorit novou aplikaci a bota, pak zkoirovat token a vlozit ho do "discordtoken" promněné.

![create](https://user-images.githubusercontent.com/59704825/212624483-3a2aaf75-1674-4e5f-816e-ed0be07e2420.png)

![addbot](https://user-images.githubusercontent.com/59704825/212624495-66ad698b-b371-43e2-a7d2-abf2570b73b0.png)

![token](https://user-images.githubusercontent.com/59704825/212624498-cdd3f5c7-f2d1-4342-8169-b7ad5221e448.png)


Na stránce "URL Generator" v Discord Developer Portalu zaškrtnout "Bot" a "Administrator" a pozvat skrze odkaz bota na server.


![urlgen](https://user-images.githubusercontent.com/59704825/212623953-3a65f2d4-d608-42ce-bba9-9a946301162a.png)

V sekci bot je ještě nutné povolit "Privileged Gateway Intents" a přesně "SERVER MEMBERS INTENT" a "MESSAGE CONTENT INTENT"


![provileges](https://user-images.githubusercontent.com/59704825/212624180-e76b712b-3f91-40c6-8bec-da4587f33f3b.png)



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




