# Mini CRM System

A complete portfolio-ready CRM system with three integrated layers: Excel data backend, Python sync server, and beautiful HTML/JS frontend.

## 🚀 **Live Demo**

**[🔗 Try the Live Demo](https://mini-crm-demo.onrender.com)**

> **Note**: The live demo may take a moment to load as it's hosted on a free tier. The demo includes sample data and all features are fully functional.

⚠️ **Demo Limitations**: Since this uses a free hosting service, the Excel file resets periodically and concurrent users may affect each other's data. For production use, deploy your own instance following the instructions below.

## Architecture

- **Layer 1**: Excel Backend (`customers.xlsx`) - Data storage with styled sheets
- **Layer 2**: Python Backend (`server.py`) - Flask REST API bridge
- **Layer 3**: Frontend (`index.html`) - Beautiful single-page application

## ✨ Features

### 🎯 **Core Functionality**
- **Dashboard**: Interactive KPI cards, status breakdown charts, recent activity feed
- **Customer Management**: Full CRUD operations, inline editing, advanced search & filtering
- **Activity Logging**: Timeline view, add activities per customer, bulk operations
- **Data Export**: Export to CSV, JSON, or Excel formats
- **Responsive Design**: "Refined Cream & Ink" theme with smooth micro-interactions
- **Real-time Updates**: Live data sync between Excel and frontend

### 🎨 **Advanced Features**
- **Dark Mode**: Toggle between light and dark themes with persistent preferences
- **Keyboard Shortcuts**: Power-user shortcuts (Ctrl+D, Ctrl+K, Ctrl+N, etc.)
- **Interactive Charts**: Deal value distribution and monthly trends visualization
- **Advanced Search**: Filter by deal value range, dates, tags, and more
- **Bulk Operations**: Select multiple customers for bulk actions
- **Loading States**: Professional loading animations and error handling
- **Performance Optimized**: Virtual scrolling, sticky headers, efficient rendering

## 🚀 Quick Start (3 steps)

### **Local Development**

1. **Install dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
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

4. **Open the application**
   - Open `index.html` in your browser, or
   - Visit `http://localhost:8000` (if using Python's built-in server)

### **Keyboard Shortcuts**
- `Ctrl + D` - Toggle dark mode
- `Ctrl + K` - Focus search
- `Ctrl + N` - Add new customer
- `Ctrl + E` - Export data
- `Ctrl + R` - Refresh page

Click the "Shortcuts" button in the app for more help.

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

## 🛠 Technology Stack

### **Backend**
- **Python 3**: Core language
- **Flask**: REST API framework
- **openpyxl**: Excel file manipulation
- **Flask-CORS**: Cross-origin resource sharing
- **Gunicorn**: Production WSGI server

### **Frontend**
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with CSS variables
- **JavaScript (ES6+)**: Vanilla JS with modern features
- **Canvas API**: Custom chart implementations
- **Web APIs**: Fetch, LocalStorage, Blob

### **Data & Design**
- **Excel Workbook**: Database alternative with styled sheets
- **Google Fonts**: Playfair Display (headings), DM Mono (data)
- **CSS Grid & Flexbox**: Responsive layouts
- **CSS Variables**: Theme management

### **Development Tools**
- **Python Virtual Environment**: Dependency isolation
- **Git**: Version control
- **Render**: Cloud deployment platform

## 📁 File Structure

```
mini-crm/
|-- setup_excel.py              # Generates customers.xlsx with sample data
|-- server.py                   # Flask REST API server
|-- index.html                  # Complete frontend application
|-- customers.xlsx              # Auto-generated Excel database
|-- requirements.txt            # Development dependencies
|-- requirements_production.txt  # Production dependencies
|-- Procfile                    # Heroku/Render deployment config
|-- gunicorn_config.py          # Gunicorn server configuration
|-- .gitignore                  # Git ignore file
|-- README.md                   # This documentation
|-- venv/                       # Python virtual environment (gitignored)
```

## 🚀 Deployment Guide

### **Option 1: Render.com (Recommended - Free)**

1. **Fork this repository** to your GitHub account
2. **Create a Render account** at [render.com](https://render.com)
3. **Connect your GitHub** account to Render
4. **Create a New Web Service**:
   - Choose your forked repository
   - Use the following build settings:
     - Build Command: `pip install -r requirements_production.txt && python setup_excel.py`
     - Start Command: `gunicorn server:app`
   - Add Environment Variable: `PYTHON_VERSION=3.9`
5. **Deploy!** Your app will be live at `https://your-app-name.onrender.com`

### **Option 2: PythonAnywhere (Free Tier)**

1. Create a PythonAnywhere account
2. Upload your files via Web interface or Git
3. Install dependencies in a virtual environment
4. Configure a web app using the Flask template
5. Set the working directory and point to `server.py`

### **Option 3: Railway / Heroku**

Similar to Render - both support Flask apps with Git deployment.

### **Local Production Setup**

```bash
# Install production dependencies
pip install -r requirements_production.txt

# Generate Excel data (if needed)
python setup_excel.py

# Start with Gunicorn
gunicorn server:app
```

## ⚙️ Development Notes

- **Excel as Database**: All operations read/write directly to `customers.xlsx`
- **CORS Enabled**: Works with local development and cross-origin requests
- **No Build Tools**: Pure HTML/CSS/JS - runs in any modern browser
- **Virtual Environment**: Recommended for dependency isolation
- **Production Ready**: Includes Gunicorn configuration and deployment setup
- **Data Persistence**: Excel file maintains data between server restarts
- **Concurrent Safety**: File locking prevents data corruption

## 🔧 Customization

### **Adding New Fields**
1. Modify `setup_excel.py` to add columns to the Excel file
2. Update the frontend forms and table headers
3. Adjust API endpoints to handle new fields

### **Changing the Theme**
Edit the CSS variables in `index.html`:
```css
:root {
    --bg-primary: #your-color;
    --accent: #your-accent;
    /* etc */
}
```

### **Adding Charts**
The chart system is extensible - add new chart types in the JavaScript section.

## 📞 Support & Contributing

- **Issues**: Report bugs or request features via GitHub Issues
- **Contributions**: Pull requests are welcome!
- **Questions**: Check the keyboard shortcuts help (Ctrl+H) in the app

---

**Built with ❤️ for demonstrating full-stack development capabilities**

*This project is designed to showcase modern web development skills and is perfect for portfolios, interviews, or learning purposes.*

## 🌟 Portfolio Highlights

This project showcases advanced full-stack development skills:

### **Architecture & Design**
- **Creative Data Layer**: Using Excel as a database alternative with styled sheets
- **Three-Layer Architecture**: Clean separation between data, API, and presentation
- **RESTful API Design**: Well-structured endpoints with proper HTTP methods
- **Modern UI/UX**: Professional "Refined Cream & Ink" design system

### **Technical Excellence**
- **Frontend Engineering**: Vanilla JavaScript with ES6+, custom charts, state management
- **Backend Development**: Flask API with CORS, error handling, and data validation
- **Performance Optimization**: Loading states, virtual scrolling, efficient rendering
- **Accessibility**: Keyboard navigation, semantic HTML, ARIA support

### **Professional Features**
- **Dark Mode**: Theme switching with CSS variables and localStorage
- **Keyboard Shortcuts**: Power-user productivity features
- **Data Visualization**: Custom canvas-based charts and graphs
- **Advanced Search**: Multi-field filtering with range queries
- **Bulk Operations**: Selection management and batch actions
- **Export Functionality**: Multiple format support (CSV, JSON, Excel)

### **Deployment & DevOps**
- **Production Ready**: Gunicorn configuration and deployment setup
- **Cloud Deployment**: Render.com integration with GitHub
- **Environment Management**: Development vs production dependencies
- **Version Control**: Proper Git workflow and ignore patterns

### **User Experience**
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Micro-interactions**: Smooth animations and hover states
- **Error Handling**: User-friendly toast notifications and validation
- **Real-time Updates**: Live data synchronization across components
