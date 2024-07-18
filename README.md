![Logo](https://images.squarespace-cdn.com/content/v1/60056c48dfad4a3649200fc0/1613294634908-3HTA3TR74HYYSNEIZSIJ/UniCT-Logo.jpg?format=1000w)

# Internet Security 2023-24 Project Repository

## Descrizione

Benvenuti nel repository del progetto realizzato per la materia **Internet Security 2023-24**. 
Questo corso è tenuto dai docenti **Prof. Giampaolo Bella** e **Sergio Esposito**. 
Lo scopo di questa repository è di documentare e discutere il progetto effettuato al termine del corso.

## Descrizione del progetto 

Questo progetto è progettato per dimostrare il concetto e l'implementazione degli attacchi brute force nel contesto della sicurezza informatica. Utilizzeremo la Damn Vulnerable Web Application (DVWA) come applicazione target e Burp Suite come proxy di intercettazione. Il progetto include uno script Python che esegue un attacco brute force in modalità di sicurezza elevata.

## Requisiti

1. **DVWA**: Un'applicazione web vulnerabile per scopi educativi.
2. **Burp Suite**: Un potente scanner di vulnerabilità web e strumento di proxy.
3. **Python**: Linguaggio di programmazione per la scrittura dello script di brute force.
4. **Librerie Aggiuntive**: `requests` per gestire le richieste HTTP e analizzare l'HTML.

## Setup

1. **Installazione di DVWA**:
    - Clonare il repository DVWA da GitHub.
    - Configurare un server locale (XAMPP, WAMP, ecc.) e posizionare i file DVWA nella directory radice del server.
    - Configurare le impostazioni di DVWA (`config.inc.php`) e configurare il database.
    - Accedere a DVWA tramite il browser web e completare la configurazione.

2. **Installazione di Burp Suite**:
    - Scaricare e installare Burp Suite Community Edition dal sito web ufficiale.
    - Configurare il browser per utilizzare Burp Suite come proxy.

3. **Installazione di Python e delle librerie necessarie**:
    ```sh
    sudo apt-get install python3
    python3 -m pip install requests
    ```

### Esecuzione

1. Salvare lo script Python in un file, ad esempio `brute_force.py`.
2. Eseguire lo script:
    ```sh
    python3 brute_force.py 127.0.0.1 [PHPSESSIONID]
    ```



