# LLM-Observability-FOSS

##🧠 **LLM Observability Demo (Open Source)**

This repository demonstrates how observability can be added step-by-step to a simple LLM-based chatbot using open-source tools.

The goal of this project is learning, not production readiness.
Each version of the chatbot introduces a new observability concept, starting from no visibility at all and gradually adding tracing and monitoring.

This repo was created as part of a community talk on LLM Observability using FOSS.

##📂 **Repository Structure**

Each file represents a stage in the observability journey:

###1️⃣ **chatbot_v1_no_observability.py**

- A basic chatbot implementation with no observability.

- No tracing

- No logs

- No metrics

- Failures and hallucinations are invisible

- This represents how many LLM apps start.
