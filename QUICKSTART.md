# ⚡ Quick Start (5 Minutes)

Scanned the QR code at the meetup? Here's the fastest way to get started:

## 1️⃣ Clone This Repo
```bash
git clone https://github.com/sarva-20/LLM-Observability-FOSS.git
cd LLM-Observability-FOSS
```

## 2️⃣ Setup (2 minutes)
```bash
# Create virtual environment
python3.12 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

## 3️⃣ Get API Keys (Free)

1. **Gemini API:** https://makersuite.google.com/app/apikey
2. **Langtrace:** https://app.langtrace.ai (sign up free)

## 4️⃣ Configure

Create `.env` file:
```env
GEMINI_API_KEY=your_key_here
LANGTRACE_API_KEY=your_key_here
```

## 5️⃣ Run First Demo
```bash
python chatbot_v1_no_observability.py
```

Ask: "What is machine learning?"

**Notice:** No cost, no token count, no latency info!

## 6️⃣ Run Second Demo (The "Wow" Moment)
```bash
python chatbot_v2_with_langtrace.py
```

Ask the same question, then check: https://app.langtrace.ai

**Now you see everything!** 🎉

---

## 📚 Full Documentation

See [README.md](README.md) for complete setup including Jaeger visualization.

## ❓ Questions?

Open an [issue](https://github.com/sarva-20/LLM-Observability-FOSS/issues) or find me at the meetup!
```

---

