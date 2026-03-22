# 🔐 Enterprise DevSecOps Security Pipeline

![GitHub Actions](https://img.shields.io/badge/Security-Pipeline-red?style=for-the-badge\&logo=githubactions)

Enterprise-grade DevSecOps pipeline built with GitHub Actions, designed to enforce security controls through automated scanning and fail-fast mechanisms.

---

## 🚀 Overview

This project demonstrates how to integrate **security into the CI/CD pipeline** using a real-world DevSecOps approach.

It implements automated checks to detect:

* Vulnerabilities in dependencies
* Hardcoded secrets
* Insecure coding patterns

---

## ⚙️ Pipeline Architecture

```text
Developer Push → GitHub Actions →
    ├── Secret Scan (Gitleaks)
    ├── SAST (Semgrep)
    ├── Vulnerability Scan (Trivy)
    └── Security Gate (FAIL on HIGH/CRITICAL)
```

---

## ⚠️ Pipeline Behavior (Important)

> ⚠️ This pipeline is intentionally designed to FAIL.

This repository includes intentionally vulnerable code to simulate a **real enterprise security scenario**.

When HIGH or CRITICAL issues are detected:

* ❌ Pipeline fails
* 🔒 Code is blocked

This demonstrates **security enforcement, not misconfiguration**.

---

## 🧠 Technologies

* GitHub Actions
* Trivy
* Gitleaks
* Semgrep
* Python
* Docker

---

## 📦 Project Structure

```text
.
├── .github/workflows/security.yml
├── app.py
├── requirements.txt
├── Dockerfile
├── .env.example
└── README.md
```

---

## 🔍 Security Layers

### 🔐 Secret Detection

Gitleaks scans for exposed credentials such as API keys and tokens.

### 🧠 Static Analysis (SAST)

Semgrep detects insecure coding patterns.

### 🐳 Dependency & Image Scanning

Trivy identifies known vulnerabilities in dependencies and containers.

---

## 🧪 Simulated Risks

This project intentionally includes:

* Hardcoded credentials
* Vulnerable dependencies
* Insecure application logic

---

## 🛠️ Execution Flow

1. Developer pushes code
2. GitHub Actions triggers pipeline
3. Security tools execute
4. Security gate evaluates results

If risk is detected:

→ ❌ Pipeline fails
→ 🔒 Deployment is blocked

---

## 🔒 Secrets Management

* `.env` is excluded via `.gitignore`
* Secrets stored in GitHub Actions Secrets
* `.env.example` provided as template

---

## 📊 Future Improvements

* Security dashboard
* SIEM integration
* Notification system (Slack / Email)
* Policy-as-Code (OPA / Conftest)

---

## 🏷️ Topics

devsecops, github-actions, security, cicd, trivy, gitleaks, semgrep, cloud-security, automation

---

## 👩‍💻 Author

Bettina Santana de Meirelles
Unix/Linux Infrastructure | DevOps | Security | Cloud

🔗 https://github.com/BettinaSM

---

## ⭐ Key Takeaways

✔ Security integrated into CI/CD
✔ Automated vulnerability detection
✔ Real enforcement (fail-fast strategy)
✔ Production-like DevSecOps pipeline

---

## 📌 Final Note

This project reflects how modern organizations adopt DevSecOps by embedding security into every stage of the development lifecycle.
