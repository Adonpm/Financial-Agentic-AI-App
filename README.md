# Financial Agentic AI App 🤖💰

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)

A sophisticated multi-agent AI system that combines web search capabilities with comprehensive financial analysis. Built using FastAPI and the Phi framework, this application leverages multiple AI agents to provide intelligent financial insights and research.

## 🚀 Live Demo

**Application URL**: [https://financial-agentic-ai-app.onrender.com/]

## ✨ Features

### 🔍 Multi-Agent Architecture
- **Web Search Agent**: Powered by DuckDuckGo for real-time web information
- **Financial Analysis Agent**: Advanced financial data analysis using YFinance
- **Multi-Agent Orchestration**: Combines both agents for comprehensive responses

### 📊 Financial Capabilities
- Real-time stock prices and market data
- Analyst recommendations and ratings
- Company fundamentals analysis
- Latest financial news and updates
- Tabular data presentation for better readability

### 🌐 Web Interface
- Clean, responsive UI built with HTML/CSS/JavaScript
- Real-time query processing
- Markdown-formatted responses
- Mobile-friendly design

## 🏗️ Architecture

```
Financial-Agentic-AI-App/
├── app.py                 # Main FastAPI application
├── playground.py          # Alternative Phi playground interface
├── Dockerfile             # Docker containerization
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not tracked)
├── templates/
│   └── index.html         # Frontend template
├── static/css/
│   └── styles.css         # Application styling
└── .github/
    └── workflows/
        └── deploy.yml     # CI/CD pipeline
```

## 🐳 Docker Support

### Build and Run Locally
```bash
# Build the Docker image
docker build -t financial-ai-app .

# Run the container
docker run -p 7860:7860 --env-file .env financial-ai-app
```

## 🚀 Deployment

### Render Deployment
This application is configured for automatic deployment on Render with:
- Automatic builds from GitHub
- Environment variable management
- Health checks and monitoring
- SSL certificate provisioning

### CI/CD Pipeline
- **Continuous Integration**: Automated testing and linting
- **Continuous Deployment**: Auto-deploy to Render on main branch updates
- **Docker Integration**: Containerized deployment for consistency

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.9+
- Docker (optional)
- Git

### Local Development
1. **Clone the repository**
   ```bash
   git clone https://github.com/Adonpm/Financial-Agentic-AI-App.git
   cd Financial-Agentic-AI-App
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Open your browser to `http://localhost:7860`

### Environment Variables
Create a `.env` file with the following variables:
```env
GROQ_API_KEY=your_groq_api_key_here
PHI_API_KEY=your_phi_api_key_here 
```

## 🔧 API Endpoints

### Main Endpoints
- `GET /` - Home page with web interface
- `POST /query` - Submit queries to the multi-agent system

### API Usage Example
```python
import requests

response = requests.post("http://localhost:7860/query", 
                        json={"query": "What's the current stock price of AAPL?"})
print(response.json())
```

## 🤖 Agent Capabilities

### Web Search Agent
- Real-time web information retrieval
- Source attribution and verification
- DuckDuckGo integration for privacy-focused search

### Financial Analysis Agent
- **Stock Data**: Real-time prices, historical data, technical indicators
- **Fundamentals**: P/E ratios, market cap, financial statements
- **News**: Company-specific news and market updates
- **Recommendations**: Analyst ratings and price targets

### Multi-Agent Coordination
- Intelligent query routing
- Cross-agent information synthesis
- Comprehensive response generation

## 🛠️ Technology Stack

- **Backend**: FastAPI, Python 3.9+
- **AI Framework**: Phi (Multi-agent orchestration)
- **LLM**: Groq (Llama 3.3 70B)
- **Financial Data**: YFinance API
- **Web Search**: DuckDuckGo API
- **Frontend**: HTML5, CSS3, JavaScript
- **Containerization**: Docker
- **Deployment**: Render
- **CI/CD**: GitHub Actions

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Ensure Docker builds successfully

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support & Issues

- **Issues**: [GitHub Issues](https://github.com/Adonpm/Financial-Agentic-AI-App/issues)
- **Documentation**: This README and inline code comments
- **Community**: Feel free to reach out for questions or suggestions

## 🙏 Acknowledgments

- [Phi Framework](https://github.com/phidatahq/phidata) for multi-agent capabilities
- [Groq](https://groq.com/) for fast LLM inference
- [YFinance](https://github.com/ranaroussi/yfinance) for financial data
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework

## 📊 Project Status

- ✅ Core functionality implemented
- ✅ Docker containerization complete
- ✅ CI/CD pipeline configured
- ✅ Production deployment on Render
- 🔄 Ongoing improvements and feature additions

---

**Built with ❤️ by [Adonpm](https://github.com/Adonpm)**

*For the latest updates and announcements, please star ⭐ this repository!*