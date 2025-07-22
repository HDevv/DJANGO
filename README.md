# 🧾 Facturator – Application de gestion de factures avec Django

Facturator est une application web développée avec Django permettant de gérer des **factures**, **clients**, **catégories** et leur état de **paiement**, avec une interface moderne utilisant **Bootstrap**.

---

## 🚀 Installation du projet en local

### 1. Cloner le dépôt

```bash
git clone <url_du_dépôt_git>
cd facturator
```

### 2. Créer un environnement virtuel

```bash
python -m venv envdjangofacturator
source envdjangofacturator/bin/activate     # Sur Linux/macOS
# ou
envdjangofacturator\Scripts\activate.bat    # Sur Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations

```bash
python manage.py migrate
```

### 5. Lancer le serveur

```bash
python manage.py runserver
```

Accéder au site : [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 Accès à l'interface Django Admin

URL : [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

**Identifiants :**
- Utilisateur : `admin`
- Email : `admin@admin.com`
- Mot de passe : `admin`

---

## ✅ Fonctionnalités

- 🧾 CRUD complet des factures
- 👥 Liaison avec des clients
- 📂 Gestion de catégories (avec assignation automatique à "Autres")
- ✅ Champ "payée" (facture réglée ou non)
- 💰 Calcul automatique du TTC
- 🔍 Filtrage des factures par client
- 🧩 Middleware qui enregistre en base chaque création de facture
- 🔎 Interface d'administration enrichie avec recherche et filtres
- 🧪 Tests unitaires (vues listage, détail et création)

---

## 🧪 Lancer les tests

```bash
python manage.py test
```

---

## 🧩 Middleware personnalisé

Un middleware enregistre automatiquement dans le modèle `FactureLog` chaque **création de facture**.

---

## ⚙️ Structure du projet

```
facturator/
├── factures/
│   ├── migrations/
│   ├── templates/factures/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── middleware.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── db.sqlite3
```

---

## 🎨 Interface utilisateur

L'interface utilise **Bootstrap 5** via CDN :
- Formulaires stylisés
- Boutons clairs et responsive
- Tableaux dynamiques

---

## 💡 Exemples d'améliorations futures

- Export PDF des factures
- Système de recherche global
- Intégration d’un tableau de bord (statistiques)
- Authentification multi-utilisateurs
- API REST

---

## 👨‍💻 Auteur

Projet réalisé dans le cadre d’un apprentissage avancé de Django.