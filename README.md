<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://stackedit.io/style.css" />
</head>

<body class="stackedit">
  <div class="stackedit__html"><h1 id="bot-telegram-raspberry">Bot-Telegram-Raspberry</h1>
<h1 id="fonctionnalit�s">Fonctionnalit�s</h1>
<ul>
<li>Interagir avec son Raspberry Pi � distance et facilement avec l�application Telegram</li>
<li>Obtenir des informations � travers Telegram comme l�adresse IP publique du Raspberry Pi afin d��tablir des connexions (SSH, FTP, HTTPS) � distance</li>
<li>Utilisation de python, de l�API Telegram et de l�API OpenWeatherMap pour la m�t�o</li>
</ul>
<h1 id="installation">Installation</h1>
<p>Vous devez installer l�API pour communiquer avec Telegram :</p>
<p><code>$ pip install python-telegram-bot</code></p>
<p>Vous devez aussi cr�er votre BOT avec <code>BotFather</code> sur Telegram afin d�obtenir la cl� d�API � renseigner dans le script</p>
<h1 id="utilisation">Utilisation</h1>
<p>Pour que le script soit lanc� d�s le demarage du Raspberry Pi :</p>
<pre><code>sudo nano /etc/rc.local
</code></pre>
<p>puis cette ligne � ajouter : <code>python "chemin du Bot-telegram.py" &amp;</code></p>
<h1 id="pr�sentation">Pr�sentation</h1>
<p>Cet exemple a �t� fait sur l�application Telegram :</p>
<p><img src="images/image1.jpg" alt="" width="190"> <img src="images/image2.jpg" alt="" width="190"> <img src="images/image3.jpg" alt="" width="190"> <img src="images/image4.jpg" alt="" width="190"></p>
</div>
</body>

</html>
