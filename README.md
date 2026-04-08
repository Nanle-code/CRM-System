# Mini CRM System

A complete portfolio-ready CRM system with three integrated layers: Excel data backend, Python sync server, and beautiful HTML/JS frontend.

## Architecture

- **Layer 1**: Excel Backend (`customers.xlsx`) - Data storage with styled sheets
- **Layer 2**: Python Backend (`server.py`) - Flask REST API bridge
- **Layer 3**: Frontend (`index.html`) - Beautiful single-page application

## Features

- **Dashboard**: KPI cards, status breakdown, recent activity feed
- **Customer Management**: Full CRUD operations, inline editing, search/filter
- **Activity Logging**: Timeline view, add activities per customer
- **Responsive Design**: "Refined Cream & Ink" theme with micro-interactions
- **Real-time Updates**: Live data sync between Excel and frontend

## Quick Start (3 steps)

1. **Install dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Generate Excel data**
   ```bash
   python setup_excel.py
   ```

3. **Start the server**
   ```bash
   python server.py
   ```

Then open `index.html` in your browser to use the CRM system.

## API Endpoints

- `GET /customers` - Get all customers
- `GET /customers/<id>` - Get customer with activity log
- `POST /customers` - Add new customer
- `PUT /customers/<id>` - Update customer
- `DELETE /customers/<id>` - Delete customer
- `POST /customers/<id>/log` - Add activity log entry
- `GET /stats` - Get aggregate statistics
- `GET /health` - Health check

## Design System

- **Colors**: Warm off-white (#f7f3ee), deep ink (#1a1410), terracotta accent (#c1440e)
- **Typography**: Playfair Display (headings), DM Mono (data)
- **Interactions**: Hover states, smooth animations, toast notifications
- **Layout**: Sidebar navigation, card-based content, responsive design

## Sample Data

The system comes pre-populated with:
- 15 realistic customer records
- 20 activity log entries
- Various status types (Lead, Active, Churned, Prospect)
- Different deal values and company types

## Technology Stack

- **Backend**: Python 3, Flask, openpyxl, Flask-CORS
- **Frontend**: Vanilla HTML5, CSS3, JavaScript (ES6+)
- **Data**: Excel workbook with styled sheets
- **Fonts**: Google Fonts (Playfair Display, DM Mono)

## File Structure

```
mini-crm/
|-- setup_excel.py       # Generates customers.xlsx with sample data
|-- server.py            # Flask REST API server
|-- customers.xlsx       # Auto-generated Excel database
|-- index.html           # Complete frontend application
|-- requirements.txt     # Python dependencies
|-- README.md           # This file
|-- venv/               # Python virtual environment
```

## Development Notes

- The Excel file serves as the "database" - all operations read/write directly to it
- CORS is enabled for local development
- The server runs in debug mode with auto-restart
- Virtual environment is recommended for dependency isolation
- No build tools required - everything runs in the browser

## Portfolio Highlights

This project demonstrates:
- **Full-stack thinking** - Frontend, backend, and data layer integration
- **Creative architecture** - Using Excel as a database alternative
- **Modern UI/UX** - Professional design with attention to detail
- **API design** - RESTful endpoints with proper error handling
- **Data management** - CRUD operations with real-time sync
- **Responsive design** - Works on desktop and mobile devices
