# Pravis Boutique

A comprehensive e-commerce platform with advanced analytics, LinkedIn scraping capabilities, and modern web technologies.

## Project Structure

This repository contains two main projects:

### 1. Main E-commerce Platform (`backend/` & `frontend/`)
- **Backend**: FastAPI-based REST API with PostgreSQL database
- **Frontend**: Nuxt.js 3 with Vue 3, Tailwind CSS, and PWA capabilities
- **Features**: User authentication, product management, analytics, Azure integration

### 2. LinkedIn Scraper - **SEPARATE REPOSITORY**
- **Standalone LinkedIn scraping toolkit**
- **Features**: Profile extraction, job search API, skill matching, Excel export, AI-powered analysis
- **Repository**: [https://github.com/Rish2204/LinkedinScraper.git](https://github.com/Rish2204/LinkedinScraper.git)
- **Status**: ✅ Successfully migrated to dedicated repository

## Quick Start

### Main Platform
```bash
# Backend
cd backend
pip install -r requirements.txt
python main.py

# Frontend
cd frontend/pravis-boutique
npm install
npm run dev
```

### LinkedIn Scraper (Separate Repository)
```bash
# Clone the dedicated repository
git clone https://github.com/Rish2204/LinkedinScraper.git
cd LinkedinScraper

# Quick test (no setup required)
./quick_test.sh
python3 test_scraper.py

# Full setup
./setup.sh
python3 linkedin_profile_scraper.py  # For profile scraping
python3 app.py                       # For FastAPI server
```

## Documentation

- [Backend Documentation](backend/README.md)
- [Frontend Documentation](frontend/pravis-boutique/README.md)
- [LinkedIn Scraper Repository](https://github.com/Rish2204/LinkedinScraper.git)
- [Project Structure](PROJECT_STRUCTURE.md)
- [Setup Guide](SETUP_QUICK.md)

## Technologies

- **Backend**: FastAPI, SQLAlchemy, PostgreSQL, Azure
- **Frontend**: Nuxt.js 3, Vue 3, Tailwind CSS, PWA
- **LinkedIn Scraper**: Selenium, BeautifulSoup, OpenAI, Pandas
- **DevOps**: Docker, GitHub Actions, Monitoring

## License

This project is proprietary and confidential.