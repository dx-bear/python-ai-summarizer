# ⚡ AI Summarizer Scraper

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)
![Asyncio](https://img.shields.io/badge/Asyncio-Enabled-success?style=flat-square)
![Anti-Detect](https://img.shields.io/badge/Anti--Detect-Wreq-orange?style=flat-square)

A simple script to scrape an AI summarizer tool to summarize long text. 

---

## 💎 Sponsored By
[![Proxidize]<img width="1774" height="887" alt="c587a274-35c7-48e6-86cf-0abab000c773" src="https://github.com/user-attachments/assets/a5163de0-7082-44c6-a483-9e52f66161cb" />](https://proxidize.com/get/15149/)


---

## ✨ Features

*   **🚀 Asynchronous:** Built on `asyncio` for non-blocking, high-speed execution.
*   **🛡️ Stealthy:** Utilizes `wreq` with strict browser emulation to bypass bot protections.
*   **🌐 Proxy Support:** Easily route traffic through authenticated proxies via environment variables.

## 🛠️ Installation

Clone the repository and install the required dependencies using `uv` for lightning-fast package resolution.

```bash
git clone https://github.com/ahmed/ai-summarizer-scraper.git
cd ai-summarizer-scraper

# Create a virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
uv pip install wreq python-dotenv
```

## ⚙️ Configuration

Create a `.env` file in the root directory of the project and set your `PROXY_URL`:

```env
PROXY_URL=http://username:password@proxy-domain.com:port
```

*Note: If you are not using a proxy, you can leave this variable empty or comment it out.*

## 🚀 Usage

Run the script directly from your terminal. Wrap the long text you want to summarize in quotes.

```bash
python ai_script.py "Artificial intelligence (AI) is a wide-ranging branch of computer science concerned with building smart machines capable of performing tasks that typically require human intelligence. While AI is an interdisciplinary science with multiple approaches, advancements in machine learning and deep learning are creating a paradigm shift in virtually every sector of the tech industry. Machine learning algorithms are fed massive amounts of data, allowing them to identify patterns and learn how to make predictions and decisions..."
```

**Output Example:**
```text
Artificial intelligence is a branch of computer science focused on creating smart machines. Through advancements in machine learning and deep learning, these systems use massive datasets to recognize patterns and make predictions, causing major shifts across the tech industry.
```

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
