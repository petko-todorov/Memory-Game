# 🧠 Memory Game

A graphical **Memory Matching Game** built with Python and `customtkinter`. Match all tile pairs on a customizable
grid (4x4, 5x5, or 6x6) and try to beat your best score!

## 📸 Screenshots
<img src="/screenshots/menu.png" alt="img alt" width="300" height="300">
<img src="/screenshots/middle_game.png" alt="img alt" width="300" height="300">
<img src="/screenshots/end_game.png" alt="img alt" width="300" height="300">

---

## 🚀 Features

- 🎮 Interactive, grid-based memory matching gameplay
- 🧩 Choose between **4x4**, **5x5** (with center tile removed), or **6x6** grids
- 💾 Move-based **highscore tracking** stored in `highscore.json`
- 🎨 Smooth tile animations and endgame effects
- 📷 Icon-based tile graphics using custom images
- 🖱️ Custom-styled UI with `customtkinter`

---

## 🛠️ Requirements

- Python 3.8 or later
- Install dependencies:

 ```bash
  pip install -r requirements.txt
```

---

## ▶️ Running the Game

```bash
python main.py
```

- The game will open in a 700x700 window where you can select your desired grid size and start playing.

## 🖼️ Adding Your Own Icons

- Add PNG images (50x50 recommended) to the images/ directory. The game randomly maps them to tile symbols each run.s
- Make sure to keep question-sign.png for the default hidden tile.

## 🏆 High Score

- The game tracks your best performance (least number of moves) for each grid size using the highscore.json file. If you
  beat or tie the previous record, it's updated.
