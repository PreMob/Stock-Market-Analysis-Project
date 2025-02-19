# Stock-Market-Analysis-Project
This repo contains all the details about our project on Stock Market Analysis website.
## **Stock Market Analysis (Beginner-Friendly Project)**
A simple web-based stock market analysis project to apply basic web development and Python skills. It fetches and visualizes stock price data interactively.

### **📌 Overview**
This project allows users to enter a stock symbol and view an interactive graph displaying the stock's price movements over the last three months. It also provides a brief description of stock trends.  

### **🛠️ Features**
- **Homepage (index.html):** A simple UI where users can enter a stock symbol.  
- **Graph Page (Graph.html):** Displays an interactive stock price graph and stock insights.  
- **Flask API:** Fetches stock data using `yfinance` and sends it to the frontend.  
- **Data Visualization:** Uses **Plotly** for interactive stock price charts.  
- **Static Assets:** Includes a logo, stock images, a video, a stock names PDF, and a CSS file for styling.

### **📊 Project Workflow**
1. **Frontend (index.html & Graph.html)**
   - Users enter a stock symbol on `index.html` and are redirected to `Graph.html`.  
   - `Graph.html` fetches stock data from a **Flask API** and displays it using Plotly.  
   - A paragraph explaining the stock's trends dynamically updates with the stock name.

2. **Backend (Flask API)**
   - `FlaskApi.py` handles API requests from `Graph.html`.  
   - It calls a function from `Smain.py`, which fetches stock price data using `yfinance`.  
   - The data is converted into a JSON format suitable for Plotly and sent back to the frontend.

### **📂 Project Structure**
```
📁 StockMarketAnalysis
│── 📄 index.html       # Homepage with stock search
│── 📄 Graph.html       # Displays stock graph & description
│── 📄 FlaskApi.py      # Flask API for handling stock data requests
│── 📄 Smain.py         # Fetches & processes stock data from yfinance
│── 📁 static/          # Contains images, CSS, video, and stock names PDF
│── ├── stock.css       # Stylesheet for frontend design
│── ├── logo.png        # Logo image
│── ├── stock.jpg       # Stock-related image
│── ├── stockv.mp4      # Stock market video
│── ├── stock_names.pdf # List of stock symbols
```

### **🛠️ Technologies Used**
- **Frontend:** HTML, CSS, JavaScript, Plotly  
- **Backend:** Python, Flask, yfinance ,Plotly 

### **🚀 How to Run the Project**
1. **Clone the repository**  
   ```bash
   git clone <repo-url>
   cd StockMarketAnalysis
   ```
2. **Install dependencies**  
   ```bash
   pip install flask yfinance plotly
   ```
3. **Run the Flask API**  
   ```bash
   python FlaskApi.py
   ```
4. **Open `index.html` in a browser** and start searching for stock data.

### **🎯 Purpose**
This is a beginner-friendly project designed to help practice **basic Python, Flask, API integration, data visualization, and frontend development.** It's a great way to get hands-on experience with stock data analysis.
