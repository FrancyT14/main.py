#HTML

m<!DOCTYPE html>
<html>
<head>
    <title>NO alla dipendenza tecnologica!</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Dipendenza ai social</h1>
    <p>La dipendenza ai social ci impedisce di passare del tempo con i nostri amici nel mondo reale al posto di quello virtuale</p>
    <img src="https://media3.giphy.com/media/26BGGxgsEh42ABHFe/giphy.gif?cid=ecf05e47fewnmm2h6vijgpd1768vz8zxo441mpec89684gtw&rid=giphy.gif&ct=g" alt="Image 1">
    <img src="https://media.licdn.com/dms/image/v2/D4D12AQG7xl7ShIVfEQ/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1727283619095?e=2147483647&v=beta&t=dUEryGqYA3NfFrv522ZrUo8pgGw9FunqicBuNhRgL7w" alt="Image 2">
    <img src="https://www.ipsico.it/wp-content/uploads/2021/03/dipendenza-social-network.jpg" alt="Image 3">
    <iframe src="https://www.meteoblue.com/it/tempo/widget/daily?geoloc=detect&days=7&tempunit=CELSIUS&windunit=KILOMETER_PER_HOUR&precipunit=MILLIMETER&coloured=coloured&pictoicon=1&maxtemperature=1&mintemperature=1&windspeed=1&windgust=1&winddirection=1&uv=0&humidity=0&precipitation=1&precipitationprobability=1&spot=1&pressure=1&layout=light"  frameborder="0" scrolling="NO" allowtransparency="true" sandbox="allow-same-origin allow-scripts allow-popups allow-popups-to-escape-sandbox" style="width: 378px; height: 420px"></iframe><div><!-- DO NOT REMOVE THIS LINK --><a href="https://www.meteoblue.com/it/tempo/settimana/index?utm_source=daily_widget&utm_medium=linkus&utm_content=daily&utm_campaign=Weather%2BWidget" target="_blank" rel="noopener">meteoblue</a></div>
    <h2>Cosa ci impedisce di fare?</h2>
             <ul>
                   <li>Conoscere altre persone dal vivo e non tramite i social o tramite internet</li>
                   <li>Giocare a giochi che non siano quelli virtuali</li>
                   <li>Fare qualche attività nel tempo libero oltre a usare il telefono</li>
             </ul>
    <h3>Come possiamo risolvere il problema?</h3>
             <ul>
                   <li>Giocare con i propri amici con giochi che non siano quelli virtuali</li>
                   <img src="https://media.istockphoto.com/id/1250594916/it/foto/posso-fare-qualcosa-con-questa-mano.jpg?s=612x612&w=0&k=20&c=nED_JMFIkUMDQleuXswpzUvFcOLrjFVWuYHgsWQAazA=" alt="Image 4">
                   <li>Organizzarsi per fare qualcosa in famiglia</li>
                   <img src="https://img.freepik.com/foto-gratuito/famiglia-di-viaggiatori-con-zaini-che-camminano-sulla-pista-genitori-e-due-bambini-che-fanno-un-escursione-all-aperto-vista-posteriore-stile-di-vita-attivo-o-concetto-di-turismo-d-avventura_74855-11685.jpg?ga=GA1.1.2005203007.1729537147&semt=ais_hybrid" alt="Image 5">
             </ul>
</body>
</html>

#CSS

body {
    font-family: Arial,  sans-serif; /* La famiglia del font */
    font-size: 18px; /* La dimensione del font principale nei tag <p></p> */
    background-color: #64df54; /* Il colore dello sfondo della pagina web */
    color: #000000; /* Il colore del testo */ 
}
h1 {
    color: #ba14c9; /* Il colore dell'intestazione */
    font-size: 30px; /* La dimensione del font dell'intestazione */
    font-family: Georgia, serif; /* La famiglia del font usata nell'intestazione */
    border:#112ba0
}
@keyframes color-change {
    0% {
      color: red;
    }

    10% {
      color: orangered;
    }

    20% {
      color: yellow;
    }

    30% {
      color:#41cf2e
    }

    40% {
      color: rgb(1, 71, 1);
    }

    50% {
        color: rgb(0, 255, 234);
    }

    60% {
      color: rgb(0, 174, 255);
    }

    70% {
      color: blue;
    }

    80% {
      color: rgb(153, 0, 153);
    }

    90% {
      color:#ff00bf;
    }

    100% {
      color:#eb41a4ee;
    }
  }

  h1 {
    animation: color-change 10s infinite; 
  }
  
  
  h1:hover { 
    font-size: 40px;
  } 

  h2:hover { 
    animation: color-change 10s infinite; 
    font-size: 40px;
  } 

  h3:hover { 
    animation: color-change 10s infinite; 
    font-size: 40px;
  } 


