<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:22c55e,50:2563eb,100:6d28d9&height=220&section=header&text=CareCompass&fontSize=60&fontColor=ffffff&fontAlignY=38&desc=See%20Someone%2C%20Help%20Someone%20%F0%9F%92%99&descAlignY=58&descSize=20&animation=fadeIn"/>

<br/>

[![GitHub](https://img.shields.io/badge/🌐%20GitHub-CareCompass-22c55e?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Nayeem131136/CareCompass)
&nbsp;
[![Django](https://img.shields.io/badge/Django%205.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
&nbsp;
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
&nbsp;
[![UAP](https://img.shields.io/badge/UAP-CSE%20314-ffd60a?style=for-the-badge)](https://uap-bd.edu)

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&pause=1000&color=22C55E&center=true&vCenter=true&width=700&lines=Real-Time+Humanitarian+Aid+Coordination+Platform+%F0%9F%87%A7%F0%9F%87%A9;Report+%E2%80%94+Connect+%E2%80%94+Help+%F0%9F%A4%9D;Role-Based+Dashboards%3A+User+%7C+Volunteer+%7C+NGO+%F0%9F%8F%A2;Built+with+Django+%7C+Leaflet.js+%7C+OpenStreetMap+%F0%9F%97%BA%EF%B8%8F" alt="Typing SVG"/>

<br/><br/>

[![Team Leader](https://img.shields.io/badge/👑%20Team%20Leader-Md.%20Mahdi%20Hasan%20Nayeem-6d28d9?style=for-the-badge)](https://github.com/Nayeem131136)
&nbsp;
[![Group](https://img.shields.io/badge/Group-C1--G5-2563eb?style=for-the-badge)]()

</div>

---

## 📖 About

**CareCompass** is a real-time humanitarian aid coordination platform built for Bangladesh. It bridges the gap between citizens who witness people in need and the NGOs/Volunteers who can help — all in one centralized, transparent system.

> *"See Someone, Help Someone — Technology for Social Good."*

Bangladesh faces critical challenges: thousands of homeless individuals on city streets, annual flood disasters displacing families, and a lack of coordination between NGOs and volunteers. CareCompass solves this by enabling **real-time reporting, instant assignment, and verified proof of help.**

---

## ✨ Key Features

<div align="center">

| Feature | Description |
|---|---|
| 📍 **Live Map Reporting** | Drop a GPS pin via Leaflet.js + OpenStreetMap — no API key needed |
| 👥 **Role-Based Dashboards** | Separate dashboards for User, Volunteer, NGO, and Admin |
| ⚡ **Real-Time Status Tracking** | Pending → Accepted → Completed — every step visible |
| ✅ **Proof of Help** | Volunteers/NGOs upload photo/video proof before marking complete |
| 🏆 **Leaderboard System** | Top Report Submitters, Top Volunteers, Top NGOs |
| 🔐 **Secure Authentication** | Custom user model with role-based access control |
| 📊 **Status Filtering** | Filter reports by Pending, Accepted, Completed, Rejected |
| 👤 **Professional Profile** | View/Edit mode profile with stats, skills, certificates |

</div>

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django%205.2-092E20?style=flat-square&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat-square&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap%205-7952B3?style=flat-square&logo=bootstrap&logoColor=white)
![Leaflet](https://img.shields.io/badge/Leaflet.js-199900?style=flat-square&logo=leaflet&logoColor=white)
![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-7EBC6F?style=flat-square&logo=openstreetmap&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)

</div>

---

## 🏗️ Project Structure (4 Modular Apps)

```
CareCompass/
├── 👤 user/                  # Custom user model & auth
│   ├── models.py             # CustomUser (role: user/volunteer/ngo)
│   ├── views.py              # Login, register, logout, dashboard, profile
│   ├── forms.py              # UserCreationForm, ProfileUpdateForm
│   └── urls.py
│
├── 📋 report/                # Core report management
│   ├── models.py             # Report (title, photo, GPS, status, proof)
│   ├── views.py              # Submit, list, detail, accept/reject/complete
│   └── urls.py
│
├── 🏆 leaderboard/           # Rankings & contributions
│   ├── views.py              # Top users, volunteers, NGOs
│   └── urls.py
│
├── 🏠 home/                  # Landing page with live stats
│   ├── views.py              # Homepage with real-time data
│   └── urls.py
│
└── 🎨 templates/             # All HTML templates
    ├── base.html             # Navbar, footer, dark glass theme
    ├── home.html             # Hero, features, how it works
    ├── dashboard_user.html
    ├── dashboard_volunteer.html
    ├── dashboard_ngo.html
    ├── report_submit.html    # Leaflet map integration
    ├── report_list.html      # With status filters
    ├── report_detail.html    # Accept/Reject/Complete + proof upload
    ├── leaderboard.html
    └── profile.html          # View/Edit mode toggle
```

---

## ⚙️ Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/Nayeem131136/CareCompass.git
cd CareCompass

# 2. Install dependencies
pip install django pillow

# 3. Apply migrations
python manage.py migrate

# 4. Run the server
python manage.py runserver
```

Then visit:
- **App:** `http://127.0.0.1:8000/`
- **Admin:** `http://127.0.0.1:8000/admin`

> ✅ **db.sqlite3 already included** — test accounts and sample reports ready!

---

## 🔑 Test Accounts

<div align="center">

| Role | Username | Password | Access |
|------|----------|----------|--------|
| 👑 Admin | `admin` | `admin123` | Full admin panel |
| 👤 User | `user` | `user123` | Submit & track reports |
| 🤝 Volunteer | `volunteer` | `volunteer123` | Accept & complete reports |
| 🏢 NGO | `ngo` | `ngo123` | Manage aid assignments |

</div>

---

## 🚦 How It Works

```
👤 Citizen sees someone in need
        ↓
📍 Submits Report (map pin + photo + description)
        ↓
📋 Report appears as "PENDING" in system
        ↓
🤝 Volunteer / NGO sees it on their Dashboard
        ↓
✅ Clicks "Accept" → Status becomes "ACCEPTED"
        ↓
🚗 Goes to location, provides help
        ↓
📸 Uploads proof (photo/video) → "COMPLETED"
        ↓
👤 Reporter sees status update on their Dashboard
        ↓
🏆 Volunteer/NGO rises on Leaderboard
```

---

## 🌐 All URLs

<div align="center">

| Page | URL |
|------|-----|
| 🏠 Homepage | `/` |
| 🔐 Login | `/login/` |
| 📝 Register | `/register/` |
| 📊 Dashboard | `/dashboard/` |
| 👤 Profile | `/profile/` |
| ➕ Submit Report | `/report/submit/` |
| 📋 All Reports | `/report/list/` |
| 🏆 Leaderboard | `/leaderboard/` |
| ⚙️ Admin Panel | `/admin/` |

</div>

---

## 📐 Database Models

```
CustomUser ──────────────── Report
 │  (role: user/vol/ngo)      │
 │                      ┌─────┴──────┐
 │                  created_by   accepted_by
 │                      │            │
 └──────────────── FK ──┘            │
                                      │
                              status: pending
                                    ↓ accepted
                                    ↓ completed
                                    ↓ rejected
                              proof: FileField
```

**4 Core Models:**
- `CustomUser` — Extended AbstractUser with role, phone, address, bio, skills, profile_pic, certificate, license_file
- `Report` — title, description, photo, video, location, latitude, longitude, status, created_by, accepted_by, proof, created_at
- `Leaderboard` — Computed via Django ORM annotations (Count + Q filters)

---

## 📊 GitHub Contributions

<div align="center">

| Contributor | Role | ID |
|---|---|---|
| 🥇 **Nayeem131136 (Nayeem)** | **Team Leader** | **22201131** |
| 🥈 tandra136131 (Rupasha) | Member | 22201136 |
| 🥉 ankitahossain (Anushka) | Member | 22201130 |

</div>

---

## 🗺️ Effect on Society

CareCompass directly impacts Bangladesh's most vulnerable populations:

- **🏘️ Urban Homeless** — Faster food, shelter, medical response
- **🌊 Flood Victims** — Real-time disaster reporting and aid coordination  
- **👴 Elderly & Sick** — Citizens can report and get immediate NGO response
- **🤝 Volunteers** — Structured platform to contribute meaningfully
- **🏢 NGOs** — Data-driven, coordinated, transparent operations

---

## 👥 Team

<div align="center">

| Name | ID | GitHub |
|---|---|---|
| **Md. Mahdi Hasan Nayeem** | 22201131 | [@Nayeem131136](https://github.com/Nayeem131136) |
| Rupasha Khan Tandra | 22201136 | [@tandra136131](https://github.com/tandra136131) |
| Ankita Hossain Anushka | 22201130 | [@ankitahossain](https://github.com/ankitahossain) |

**Course:** CSE 314 — Software Engineering Lab  
**Instructor:** Jayonto Dutta Plabon, Lecturer, CSE — University of Asia Pacific  
**Group:** C1-G5

</div>

---

## 📦 Requirements

```txt
django>=5.0
Pillow>=10.0
```

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:6d28d9,50:2563eb,100:22c55e&height=120&section=footer"/>

**⭐ Star this repo if it helped you!**

[![GitHub stars](https://img.shields.io/github/stars/Nayeem131136/CareCompass?style=social)](https://github.com/Nayeem131136/CareCompass/stargazers)
&nbsp;
[![GitHub forks](https://img.shields.io/github/forks/Nayeem131136/CareCompass?style=social)](https://github.com/Nayeem131136/CareCompass/network/members)

*Built with ❤️ for Bangladesh | CSE 314 — University of Asia Pacific*

</div>
