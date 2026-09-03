# LEVEL 0 - Preparation

## Voraussetzungen

Für die folgenden Schritte werden benötigt:
- Python 3
- Git
- pip
- eine Shell / ein Terminal

## 1. Virtuelle Umgebung anlegen

<details>
    <summary>Wieso, Weshalb und Warum?</summary>

    Eine virtuelle Umgebung ist eine isolierte Python-Umgebung innerhalb des bestehenden Systems. Sie ist kein eigenes System und enthlält auch nicht zwingend eine vollständig unabhängige Betriebssysteumgebung. Da auf einem Betriebssystem bereits Python läuft (globale Umgebung), möchte man nicht mit diesen Abhängigkeiten korrelieren und die globale Umgebung möglicherweise beschädigen. Deshalb erstellt man sich eine virtuelle Umgebung. In Python gibt es dafür ein eingebautes Modul namens <venv> (virtual envirionment). 

</details>
<br>

<details>
    <summary>Wie</summary>
  
    Um dann eine neue virtuelle Umgebung zu erstellen navigiert man zu dem Pfad wo sie erstellt werden soll und führt folgenden Befehl aus:

    ```
    python3 -m venv <name_of_venv>
    ```

    Um diese erstellte, virtuelle Umgebung nun auch zu nutzen, muss diese zunächst aktiviert werden und dies macht man unter Linux mit folgendem Befehl:

    ```
    source path_to_your_venv/bin/activate
    ```

    Jetzt ist diese virtuelle Umgebung aktiviert und man kann nun mit dem Paketmanager pip Abhängigkeiten installieren, welche lediglich in dieser aktivierten, virtuellen Umgebung landen und die globale Python-Umgebung nicht beeinflussen.

    Sollte man in der Konsole wieder in die globale Umgebung wechseln wollen geht diese mit folgendem Befehl:

    ```
    deactivate
    ```

</details>
<br>

## 2. Gewünschte Version auschecken
    Dieses Projekt beseteht aus sechs Ausbaustufen. Jede Ausbaustufe kann dabei mehrere Versionen besitzen. Die einzelnen Versionen werden durch Git-Tags gekennzeichnet.

    Wenn du einen bestimmten Stand des Projekts verwenden oder darauf aufbauen möchtest, solltest du den entsprechenden Tag auschecken. Dadurch erhältst du exakt den zu diesem Tag gehörenden Projektstand.

    Dafür führst du im Hauptverzeichnis des Repos folgenden Befehl aus:

    ```
    git checkout <your_preferred_tag>
    ```

## 3. Abhängigkeiten installieren
<details>
    <summary>Was ist pip und wofür ist requirements.txt?</summary>
    Pip ist das Standardwerkzeug zum Installieren und Verwalten von Python-Paketen. Hiermit können verschiedene Module heruntergeladen und installiert werden, damit diese einen bei der Entwicklung unterstützen. Die jeweils für das Projekt benötigten Abhängigkeiten werden in der Datei requirements.txt festgehalten und von dort aus auch installiert.

</details>
<br>

<details>
    <summary>Wie installiere ich die Abhängigkeiten?</summary>
    Mit folgendem Befehl können alle für diese Ausbaustufe benötigten Abhängigkeiten installiert werden:
    ```pip install -r requirements.txt```

</details>
<br>
    

## 4. App starten

    Es wird immer einen Startpunkt geben und dieser wird immer die Datei 'run.py' sein. 
    Wenn die virtuelle Umgebung aktiviert ist, folgenden Befehl ausführen:
    ```
    python3 run.py
    ```

## Ergebnis

Nach Abschluss dieser Schritte ist die Entwicklungsumgebung vorbereitet:
- eine virtuelle Python-Umbegung wurde erstellt und aktiviert
- der gewünschte Projektstand wurde ausgechekct
- alle benötigten Abhängigkeiten wurden installiert
- die Flask-Anwendung kann gestartet werden