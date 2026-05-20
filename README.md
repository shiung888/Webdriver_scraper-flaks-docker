# Webdriver Scraper with Flask & Docker

A web scraping application built with **Selenium WebDriver**, served via a **Flask** web interface, and containerized with **Docker**. The app scrapes [GeeksforGeeks](https://www.geeksforgeeks.org/) and returns the count of `<h2>` headings found on the page.

---

## 📁 Project Structure

```
├── main.py            # Flask app with route definitions
├── scraper.py         # Selenium scraping logic
├── templates/         # HTML templates (index.html, scrape.html)
├── requirements.txt   # Python dependencies
└── Dockerfile         # Docker image configuration
```

---

## 🚀 Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your machine

### Run with Docker

1. **Clone the repository**

   ```bash
   git clone https://github.com/shiung888/Webdriver_scraper-flaks-docker.git
   cd Webdriver_scraper-flaks-docker
   ```

2. **Build the Docker image**

   ```bash
   docker build -t webdriver-scraper .
   ```

3. **Run the container**

   ```bash
   docker run -p 500:500 webdriver-scraper
   ```

4. **Open your browser and visit**

   ```
   http://localhost:500
   ```

---

## 🌐 Routes

| Route      | Description                                      |
|------------|--------------------------------------------------|
| `/`        | Home page                                        |
| `/scrape`  | Triggers the scraper and displays the result     |

---

## 🛠️ How It Works

1. When you visit `/scrape`, Flask calls the `scraper()` function.
2. Selenium launches a headless Chrome browser inside the container.
3. It navigates to `https://www.geeksforgeeks.org/` and counts all `<h2>` elements on the page.
4. The count is returned and rendered in the `scrape.html` template.

---

## 🧰 Tech Stack

- **Python 3.8**
- **Flask** — web framework
- **Selenium** — browser automation
- **ChromeDriver / Google Chrome** — headless browser
- **Docker** — containerization

---

## 📦 Dependencies

See [`requirements.txt`](./requirements.txt) for the full list. Key packages include:

- `flask`
- `selenium`
- `webdriver-manager`

---

## 📝 Notes

- The app exposes port `500`. Make sure it's not in use before running the container.
- Chrome runs in headless mode (`--no-sandbox`, `--disable-gpu`) to work inside Docker.
