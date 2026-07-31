<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:7c3aed,50:ec4899,100:3b82f6&height=220&section=header&text=Fitloom&fontSize=60&fontColor=ffffff&fontAlignY=38&desc=Design%20%E2%86%92%20Perfect%20Mockup%2C%20Instantly%20%F0%9F%8E%A8&descAlignY=58&descSize=20&animation=fadeIn"/>

<br/>

[![Live Demo](https://img.shields.io/badge/🌐%20GitHub-Fitloom-7c3aed?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Nayeem131136/fitloom)
&nbsp;
[![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com)
&nbsp;
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
&nbsp;
[![License](https://img.shields.io/badge/License-MIT-ec4899?style=for-the-badge)](LICENSE)

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&pause=1000&color=7C3AED&center=true&vCenter=true&width=600&lines=Drag%2C+Drop%2C+Auto-Fit+%F0%9F%93%90;Background+Removal+Built-In+%E2%9C%82%EF%B8%8F;HD+Export+Up+to+8x+%F0%9F%93%A6;Zero+Backend%2C+Zero+Signup+%E2%9A%A1" alt="Typing SVG"/>

</div>

---

## 📖 About

**Fitloom** is a free, browser-based mockup generator. Upload any design, drag a placement box onto a product/frame mockup, and the tool automatically fits your artwork into place — with background removal and high-resolution export, all running client-side with zero backend.

> *"Perfect placement shouldn't need Photoshop."*

---

## ✨ Key Features

<div align="center">

| Feature | Description |
|---|---|
| 🖱️ **Drag & Resize Box** | Click-drag placement box with 8-point resize handles — no manual coordinates |
| ✂️ **Auto Background Removal** | Color-distance cutout turns your design into a clean PNG before placing |
| 🎯 **Perfect Auto-Fit** | Design is centered and scaled to fit the exact box you draw |
| 🖼️ **Multi-Mockup Support** | 3 built-in mockups + upload your own custom mockup on the fly |
| 🎚️ **Blend Modes** | Normal / Multiply blending for realistic shadow interaction |
| 📸 **HD Export** | 1x / 2x / 4x / 8x scale PNG download, ready for print or social |
| 🎨 **Animated UI** | Gradient nav, floating blobs, scroll-reveal — Magic UI-style motion |
| ⚡ **No Backend, No Signup** | 100% static — runs entirely in the browser |

</div>

---

## 🛠️ Tech Stack

<div align="center">

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Canvas API](https://img.shields.io/badge/Canvas%20API-FF6F00?style=flat-square&logo=html5&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

</div>

---

## 🏗️ Project Structure

```
fitloom/
├── 🎨 index.html          # Everything — landing page + generator (single file)
│   ├── <style>            # Design tokens, animations, layout
│   ├── <body>              # Nav → Hero → Features → Generator → Footer
│   └── <script>            # Drag/resize box, bg-removal, canvas compositing
├── 📄 README.md
└── 🚫 .gitignore
```

---

## 🔄 How It Works

```mermaid
graph LR
    A[🖼️ Upload Design] -->|Sample corner colors| B[✂️ Auto Background Removal]
    B --> C[📦 Draw Placement Box]
    C -->|Drag / Resize| D[🎯 Contain-Fit Centered]
    D -->|Canvas Composite| E[🖌️ Blend Mode Applied]
    E -->|Scale 1x-8x| F[📥 HD PNG Export]
```

---

## ⚙️ Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/Nayeem131136/fitloom.git
cd fitloom

# 2. Just open it — no build step, no dependencies
open index.html   # macOS
start index.html  # Windows
```

That's it. No `npm install`, no server, no `.env`.

---

## 🚀 Deploy Your Own

```bash
# Push to GitHub
git init
git add .
git commit -m "Initial commit: Fitloom"
git branch -M main
git remote add origin https://github.com/Nayeem131136/fitloom.git
git push -u origin main
```

Then on **[vercel.com/new](https://vercel.com/new)**:
1. Import the `fitloom` repo
2. Framework preset → **Other** (static site, no build command)
3. Click **Deploy** 🚀

Every push to `main` auto-redeploys.

---

## 🧭 Usage

| Step | Action |
|---|---|
| 1️⃣ | Pick a built-in mockup or upload your own |
| 2️⃣ | Drag the green box onto the frame area, resize with the corner handles |
| 3️⃣ | Upload your design — background is auto-removed |
| 4️⃣ | Choose blend mode + export scale (up to 8x HD) |
| 5️⃣ | Click **Generate**, then **Download PNG** |

---

## 🗺️ Roadmap

- [ ] Server-side background removal (remove.bg / Photoroom API) for photo backgrounds
- [ ] Perspective/angled placement (not just axis-aligned box)
- [ ] Save & load mockup presets (needs auth + database)
- [ ] Batch export — multiple designs × multiple mockups at once

---

## 👤 Developer

<div align="center">

| Name | Role | GitHub |
|---|---|---|
| **Md. Mahdi Hasan Nayeem** | 🏆 Creator & Developer | [@Nayeem131136](https://github.com/Nayeem131136) |

**Portfolio:** [mahdi-hasan-nayeem-portfolio.vercel.app](https://mahdi-hasan-nayeem-portfolio.vercel.app/)

</div>

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:3b82f6,50:ec4899,100:7c3aed&height=120&section=footer"/>

**⭐ Star this repo if it helped you! | 🍴 Fork to build your own**

[![GitHub stars](https://img.shields.io/github/stars/Nayeem131136/fitloom?style=social)](https://github.com/Nayeem131136/fitloom/stargazers)
&nbsp;
[![GitHub forks](https://img.shields.io/github/forks/Nayeem131136/fitloom?style=social)](https://github.com/Nayeem131136/fitloom/network/members)

*Built with 🎨 by Md. Mahdi Hasan Nayeem*

</div>
