# Bekircraft: Einfache Terrain-Generation in Python mit Ursina

Einfache prozedurale Welterstellung für Minecraft-ähnliche Umgebungen

## Beispielsfoto
![Screenshot 2025-05-25 224753](https://github.com/user-attachments/assets/d18b7a6a-5a5d-43d2-9011-8654b9553cbf)

## Einführung

**Bekircraft** ist mein Python-basiertes Programm zur Generierung komplexer Minecraft-ähnlicher Gelände. Es ermöglicht eine einfache Anpassung und Erweiterung seiner Generierungsalgorithmen. Jedoch erlebt man in Python viele verschiedene Effizienzprobleme wodurch es, trotz mehrerer Code- und Generationsoptimierung, immer noch Perfomanceprobleme gibt. Es wurde von mir entwickelt um prozedurale Geländegenerierung mit Python zu erforschen. Es nutzt die Bibliothek `ursina` zur Visualisierung. Da dies eines meiner ersten Python-Projekte ist, wusste ich zu Beginn noch nicht wie Objekt-orientiertes Programmieren in Python abläuft. Daher war dieses Projekt ein guter Einstieg. Trotzdem würde ich es nicht weiterempfehlen, da die Performancemängel in Python echt stark sind. Ich hoffe in Zukunft dieses Projekt ebenfalls in einer schnelleren Sprache, wie C++ oder C, schreiben zu können, sodass ich auch komplexere Features wie Biome und größere Terrains erschaffen kann.

---

## Funktionen

- **Voxel-basiertes Terrain** auf Basis von Perlin‑Noise  
- **Dynamische Baumgeneration** (Stamm + Blattkrone)  
- **First‑Person‑Steuerung** mit benutzerdefiniertem Fadenkreuz  
- **Interaktion**: Blöcke setzen/abbauen + Soundeffekte  
- **Texture-Auswahl** via Mausrad  
- Hintergrundmusik für Atmosphäre

---

## Leistungsoptimierungen

- **Chunk‑Nachladen mit Radius**  
  Nur Blöcke im Umkreis des Spielers werden geladen → bessere Performance.

- **Sichtbarkeitsprüfung vor Mesh‑Generierung**  
  Nur sichtbare Flächen erzeugen Meshes → deutlich weniger Polygone.

- **Asynchrone Nachladung via `invoke()`**  
  Blöcke werden gestaffelt über mehrere Frames gerendert → keine Frame-Drops.

- **Position‑Überprüfung vor Update**  
  Welt wird nur neu geladen, wenn sich der Spieler bewegt.

- **Caching von geladenen Positionen**  
  `rendered_positions` verhindert doppelte Verarbeitung/Rendering.

---

## Code-Struktur & Modularität

| Pfad                     | Beschreibung                                                             |
| ------------------------ | ------------------------------------------------------------------------ |
| `main.py`                | Einstiegspunkt zur Initialisierung und Steuerung der Geländegenerierung. |
| `terrain_generator.py/`  | Kernlogik der Generierung: Rauschfunktionen, Biome, Chunks.              |
| `Block.py`               | Logik der einzelnen Blöcke                                               |
| `playerSetup.py`         | Charakter Controller                                                     |
| `README.md`              | Diese Dokumentation.                                                     |

# Footage

![Screenshot 2025-05-14 211535](https://github.com/user-attachments/assets/2948ee09-d669-401d-95ce-1fc08937e17a)
![Bild_2025-05-27_184746067](https://github.com/user-attachments/assets/5d21484e-9d9b-4e1b-866e-e16ee7b73d6b)


