```markdown
# Personal Portfolio & Contact Platform (Django)

A dynamic, full-stack personal portfolio and contact management web application built with **Django 6.0** and **PostgreSQL**[cite: 10]. Designed to showcase professional engineering and development projects, dynamic resume details, and provide a persistent client messaging gateway[cite: 10].

---

## 🚀 Key Features

* **Dynamic Portfolio Showcase (`AMapp`):** Dynamic portfolio model managing project titles, media assets, project descriptions, and external direct links[cite: 10].
* **Messaging & Inquiry System (`ContactUsapp`):** Form backend handling client inquiries with validated database storage (`MassageMe` model) and customizable contact channels (LinkedIn, Socials, Phone, Email)[cite: 10].
* **Full-Cycle Production Infrastructure:** Architected for production deployment using PostgreSQL, Gunicorn WSGI server, and Nginx reverse proxy with SSL[cite: 1, 10].
* **Django Admin Integration:** Fully customized administrative dashboard with models registered for effortless content and message management[cite: 10].
* **Responsive Frontend:** Integrated with modern UI components (Bootstrap 5, GLightbox, Swiper, and AOS animations)[cite: 10].

---

## 🛠️ Tech Stack

* **Backend:** Python 3.13, Django 6.0[cite: 10]
* **Database:** PostgreSQL (with SQLite compatibility for local development)[cite: 10]
* **Frontend & Assets:** HTML5, CSS3, JavaScript, Bootstrap 5, GLightbox, Swiper, AOS[cite: 10]
* **Media & File Handling:** Pillow[cite: 10]
* **Deployment Stack:** Ubuntu Linux VPS, Gunicorn, Nginx[cite: 1, 10]

---

## 📁 Project Structure

```text
AboutMe_project/
├── AboutMe_project/       # Project core configuration (settings, urls, wsgi, asgi)
├── AMapp/                 # Portfolio showcase application (models, admin, migrations)
├── ContactUsapp/          # Contact details & inbox message handling
├── templates/             # Jinja/Django HTML templates (modular layout)
├── assets/                # Static assets (CSS, JS, Vendor libraries, Images)
├── media/                 # User-uploaded dynamic media files
├── manage.py
└── requirements.txt

```

---

## ⚙️ Quick Start & Installation

### 1. Clone Repository

```bash
git clone [https://github.com/Ali-PM/AboutMe.git](https://github.com/Ali-PM/AboutMe.git)
cd AboutMe/AboutMe_project

```

### 2. Environment Setup

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

```

### 3. Database Configuration & Migrations

Configure your PostgreSQL credentials in `AboutMe_project/settings.py` (or use default SQLite for local testing), then run:

```bash
python manage.py makemigrations
python manage.py migrate

```

### 4. Create Superuser (Admin)

```bash
python manage.py createsuperuser

```

### 5. Run Development Server

```bash
python manage.py runserver

```

Visit `http://127.0.0.1:8000/` in your browser. Access the admin dashboard at `http://127.0.0.1:8000/admin/`.

---

## 👨‍💻 Author

**Ali Molaei**

M.Sc. in Mechatronics Engineering | Python Backend & AI Developer

* Email: [molaeiali24@gmail.com](https://www.google.com/search?q=mailto%3Amolaeiali24%40gmail.com)
* Telegram: [@AliMoj4z](https://www.google.com/search?q=https://t.me/AliMoj4z)
