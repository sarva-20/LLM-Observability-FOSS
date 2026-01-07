# 🧠 LLM Observability Demo (Open Source)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

This repository demonstrates how to add observability to LLM applications **step by step** using **Free and Open Source Software (FOSS)**.

> 💡 **Created for FOSS United Coimbatore Meetup - December 27, 2025 @ KlyONIX Pvt Ltd, Pollachi**

---

## 🎯 The Problem

Without observability, LLM applications are **black boxes**:
- ❌ Unknown costs and token usage
- ❌ No visibility into failures or hallucinations  
- ❌ Can't debug slow responses
- ❌ Production issues are invisible

**This demo shows you how to fix it using open-source tools.**

---

## 📂 What's Inside

Each file shows a different stage of adding observability:

| File | What It Shows | Key Learning |
|------|---------------|--------------|
| `chatbot_v1_no_observability.py` | The problem - no visibility | Why observability matters |
| `chatbot_v2_with_langtrace.py` | Auto-instrumentation (2 lines!) | Quick wins with Langtrace |
| `chatbot_v3_with_opentelemetry.py` | Manual instrumentation | OpenTelemetry foundation |
| `chatbot_v4_with_jaeger.py` | Trace visualization | Debugging with Jaeger UI |
| `chatbot_unified_observability.py` | All frameworks together | Compare 4 tools simultaneously |

---

## 🚀 Quick Start

### 1. Clone & Setup

```bash
git clone https://github.com/<your-username>/llm-observability-demo.git
cd llm-observability-demo

# Create virtual environment (Python 3.12 recommended)
python3.12 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Keys

Create `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
LANGTRACE_API_KEY=your_langtrace_api_key
# Optional for unified demo:
OPIK_API_KEY=your_opik_api_key
OPIK_WORKSPACE=your_workspace
```

**Get API keys:**
- Gemini: https://makersuite.google.com/app/apikey
- Langtrace: https://app.langtrace.ai
- Opik (optional): https://www.comet.com/signup

### 3. Start Jaeger (for visualization)

```bash
docker run -d --name jaeger \
  -e COLLECTOR_OTLP_ENABLED=true \
  -p 16686:16686 \
  -p 4318:4318 \
  jaegertracing/all-in-one:latest
```

Verify: http://localhost:16686

### 4. Run the Demos

```bash
# Demo 1: No observability (the problem)
python chatbot_v1_no_observability.py

# Demo 2: Quick win with Langtrace
python chatbot_v2_with_langtrace.py
# Then check: https://app.langtrace.ai

# Demo 3: OpenTelemetry foundation
python chatbot_v3_with_opentelemetry.py

# Demo 4: Jaeger visualization
python chatbot_v4_with_jaeger.py
# Then check: http://localhost:16686

# Demo 5: All frameworks together
python chatbot_unified_observability.py
# Compare all dashboards!
```

---

## 📊 Tool Comparison

| Tool | Setup | Best For |
|------|-------|----------|
| **Langtrace** | 2 lines of code | Quick starts, MVPs |
| **OpenTelemetry** | Manual instrumentation | Enterprise, custom needs |
| **OpenLLMetry** | Auto + OTel standards | LLM-specific conventions |
| **Opik** | Simple integration | Evaluation + monitoring |
| **Jaeger** | Docker container | Trace visualization |

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────────────────────┐
│                           Your LLM Application                            │
│                                                                          │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐             │
│  │   User Input │ ──▶ │   Prompt     │ ──▶ │   LLM Call   │             │
│  │              │     │   Handling   │     │              │             │
│  └──────────────┘     └──────────────┘     └───────┬──────┘             │
│                                                     │                    │
│                                  ┌──────────────────┼─────────────────┐ │
│                                  │                  │                 │ │
│                         ┌────────▼────────┐ ┌───────▼────────┐ ┌──────▼─────┐
│                         │    LangTrace     │ │ OpenTelemetry   │ │ OpenLLMetry │
│                         │  (LLM / RAG      │ │  (Traces,       │ │ (LLM-Specific│
│                         │   Tracing)       │ │   Metrics, Logs)│ │  Signals)    │
│                         └────────┬─────────┘ └────────┬────────┘ └──────┬─────┘
│                                  │                  │                 │
│                                  └──────────┬───────┴───────┬─────────┘
│                                             │               │
│                                     OTLP Protocol (Export)  │
└─────────────────────────────────────────────┼───────────────┘
                                              │
                                              ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                       Observability Backends (FOSS)                       │
│                                                                          │
│     ┌──────────────┐      ┌──────────────┐      ┌──────────────┐        │
│     │    Jaeger    │      │   Grafana    │      │     Opik     │        │
│     │ (Trace View) │      │ (Metrics &   │      │ (Evals &    │        │
│     │              │      │  Dashboards) │      │  Quality)   │        │
│     └──────────────┘      └──────────────┘      └──────────────┘        │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘


```

---

## 💡 Key Concepts

**Trace:** A single request's journey through your system  
**Span:** One operation within a trace (e.g., LLM API call)  
**Attributes:** Metadata attached to spans (tokens, cost, latency)

---

## 🐛 Troubleshooting

**Packages not found?**
```bash
which python  # Should show venv/bin/python
pip install -r requirements.txt
```

**Jaeger not working?**
```bash
docker ps | grep jaeger  # Check if running
docker restart jaeger    # Restart if needed
```

**Traces not appearing?**
- Wait 5-10 seconds for sync
- Check API keys in `.env`
- Refresh dashboard

---

## 📚 Resources

### Documentation
- [Langtrace](https://docs.langtrace.ai) | [OpenTelemetry](https://opentelemetry.io/docs) | [Jaeger](https://www.jaegertracing.io/docs) | [Opik](https://www.comet.com/docs/opik)

### Related Projects
- [OpenLLMetry](https://github.com/traceloop/openllmetry)
- [Langfuse](https://langfuse.com)
- [Weights & Biases](https://wandb.ai)

---

## 🤝 Contributing

Contributions welcome! Ideas:
- Examples with OpenAI/Anthropic
- RAG pipeline demo
- Agent workflow examples
- Documentation improvements

---

## 📝 License

MIT License - see [LICENSE](LICENSE) file

---

## 🙏 Acknowledgments

Built with: [Langtrace](https://langtrace.ai) • [OpenTelemetry](https://opentelemetry.io) • [Jaeger](https://www.jaegertracing.io) • [Google Gemini](https://ai.google.dev)

---
## 📬 Contact & Feedback

**Author:** Sarvatarshan Sankar  
**GitHub:** [@sarva-20](https://github.com/sarva-20)
**LinkedIn** [@Sarvatarshan Sankar](https://www.linkedin.com/in/sarvaponns20/)

Questions? Found this helpful?
- 💬 [Open an Issue](https://github.com/sarva-20/LLM-Observability-FOSS/issues)
- ⭐ Star this repo if it helped you!
- 🔄 Share with others learning about LLM observability
