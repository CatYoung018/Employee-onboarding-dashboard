# Employee Onboarding Dashboard

An interactive web dashboard for tracking employee onboarding metrics, built with Flask and Chart.js.

![Dashboard Preview](screenshot.png)
*Replace with actual screenshot once deployed*

## 🎯 Project Overview

This dashboard provides HR teams and managers with real-time visualization of onboarding performance metrics including:
- Total tasks completed
- Employee satisfaction scores
- Weekly task completion trends
- Employee engagement over 3 months
- Task breakdown by category (Paperwork, Training, IT Setup, Orientation, Meet & Greets)

## 🛠️ Technologies Used

**Backend:**
- Python 3.x
- Flask (web framework)

**Frontend:**
- HTML5
- CSS3
- JavaScript
- Chart.js (data visualization)

**Accessibility:**
- WCAG 2.1 AA compliant
- Keyboard navigation support
- Screen reader friendly
- Reduced motion suppor

## ✨ Features

- **Interactive Charts**: Hover over data points to see detailed information
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Accessible**: Built with ARIA labels and semantic HTML
- **Clean Code**: Well-organized project structure following best practices
- **Professional UI**: Modern card-based layout with smooth animations

## 📁 Project Structure
```
onboarding-dashboard/
│
├── app.py                  # Main Flask application
├── data.py                 # Sample onboarding metrics data
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
│
├── templates/
│   └── index.html         # Dashboard HTML template
│
└── static/
    └── style.css          # Dashboard styling
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/YOUR_USERNAME/onboarding-dashboard.git
   cd onboarding-dashboard
```

2. **Create a virtual environment**
```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Run the application**
```bash
   python app.py
```

5. **View in browser**
   
   Open http://127.0.0.1:5000 in your web browser

## 📊 Sample Data

The dashboard currently uses sample data defined in `data.py`. In a production environment, this would connect to a database or API to display real-time metrics.

## 🎨 Customization

**To modify the data:**
- Edit the values in `data.py`

**To change colors:**
- Update the color codes in `static/style.css` (main color: `#3498db`)
- Modify chart colors in the JavaScript section of `templates/index.html`

**To add new metrics:**
1. Add data to `data.py`
2. Pass data through Flask in `app.py`
3. Create new chart section in `index.html`
4. Style the new section in `style.css`

## 🌐 Live Demo

[View Live Dashboard](https://your-app-name.onrender.com)
*Link will be added after deployment*

## 📝 Development Process

This project was built as a portfolio piece to demonstrate:
- Full-stack web development skills
- Data visualization capabilities
- Accessibility best practices
- Clean, maintainable code structure

## 🔮 Future Enhancements

- [ ] Connect to real database (PostgreSQL/MongoDB)
- [ ] Add user authentication
- [ ] Export reports to PDF
- [ ] Add date range filters
- [ ] Implement real-time data updates
- [ ] Add more chart types (pie charts, gauges)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Your Name**
- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Portfolio: [Your Website](https://yourwebsite.com)

## 🙏 Acknowledgments

- Chart.js for the excellent charting library
- Flask documentation and community
- Anthropic's Claude for development guidance

---

⭐ If you found this project helpful, please consider giving it a star!
