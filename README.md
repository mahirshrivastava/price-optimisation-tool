# Price Optimization Tool

## 📌 Overview

The **Price Optimization Tool** is a full-stack web application built using **Angular** (frontend) and **Flask** (backend).  
It enables businesses to manage products, analyze demand forecasts, and determine optimized pricing strategies based on market conditions and demand trends.

This project was developed as part of a **hiring assessment** for a global enterprise to demonstrate scalable architecture, secure role management, data visualization, and pricing optimization logic.

---

## 🎯 Problem Understanding

In today’s competitive digital environment, pricing accuracy directly impacts revenue and customer demand.  
The objective of this application is to provide:

- Secure **product management**
- **Demand forecasting visualization**
- **Optimized pricing recommendations**
- **Role-based user access**
- A **client-presentable UI** with strong performance

The system is designed to be modular, scalable, and easy to extend as business requirements evolve.

---

## ✨ Key Features

### 🔐 Authentication & Authorization
- User registration and login
- Email verification
- Role-Based Access Control (RBAC)
  - Admin
  - Buyer
  - Supplier
  - Support for custom roles
- Secure session handling

---

### 📦 Product Management
- Create, view, update, and delete products
- Product attributes:
  - Product ID
  - Name
  - Description
  - Category
  - Cost Price
  - Selling Price
  - Stock Available
  - Units Sold
  - Customer Rating
- Advanced product search (by name)
- Category-based filtering
- Secure data handling aligned with privacy best practices

---

### 📈 Demand Forecast Integration
- View demand forecast for individual products
- Linear visualization of:
  - **Demand vs Selling Price**
- Helps users understand pricing elasticity and demand trends
- Implemented using charting libraries in Angular

---

### 💰 Pricing Optimization
- Calculates optimized selling prices based on:
  - Cost price
  - Demand forecast
  - Sales history
- Results displayed in a **tabular format**
- Enables data-driven pricing decisions

---

## 🧱 Tech Stack

### Frontend
- **Angular**
- TypeScript
- HTML / SCSS
- Chart.js / D3.js (for demand visualization)
- Responsive UI design

### Backend
- **Python Flask**
- RESTful API architecture
- Secure authentication & authorization
- Modular service-based structure

### Database
- PostgreSQL / MySQL
- Normalized schema
- Indexed columns for optimized search and filtering

---

## 🗂️ Project Structure

price-optimization-tool/
│
├── backend/
│ ├── app/
│ │ ├── models/
│ │ ├── routes/
│ │ ├── services/
│ │ └── auth/
│ ├── config.py
│ ├── requirements.txt
│ └── run.py
│
├── frontend/
│ ├── src/
│ │ ├── app/
│ │ ├── components/
│ │ ├── services/
│ │ └── modules/
│ ├── angular.json
│ └── package.json
│
├── database/
│ └── schema.sql
│
├── screenshots/
│
└── README.md


---

## ⚙️ Installation & Setup

### Prerequisites
- Node.js (v20+)
- Angular CLI
- Python (v3.10+)
- PostgreSQL / MySQL
- Git

---

### 🔧 Backend Setup (Flask)

```bash
cd backend
python -m venv virtualEnv
source virtualEnv/bin/activate (Linux)
pip install -r requirements.txt
python run.py

- Backend will start on:
    http://localhost:5000

---

### 🎨 Frontend Setup (Angular)

```bash
cd frontend
npm install
ng serve

- Frontend will start on:
    http://localhost:4200
    
---

### 🗄️ Database Setup

Create a database in PostgreSQL/MySQL

Run schema.sql

Update database credentials in Flask configuration

---

**## 📊 UI & Visualization**

Clean and client-presentable interface

Responsive layout

Demand forecast charts

Pricing optimization tables

Screenshots are included in the /screenshots directory as per submission instructions

---

**## 🧠 Key Learnings & Takeaways**

Implementing RBAC in Flask

Designing REST APIs for scalable Angular applications

Optimizing database queries using indexing

Integrating business logic with data visualization

Building maintainable, modular frontend components

Translating business requirements into technical solutions

---

**## 🚀 Future Enhancements**

ML-based demand forecasting

Real-time pricing updates

Export pricing reports (PDF / Excel)

Audit logs for pricing changes

Multi-region and multi-currency support

---

**## 📎 Submission Notes**

Codebase includes both frontend and backend

UI screenshots provided

README includes:

Setup instructions

Feature overview

Understanding of the problem statement

---

**## Developed as part of a Pricing Optimization Tool – Hiring Assessment using Angular & Flask.**
