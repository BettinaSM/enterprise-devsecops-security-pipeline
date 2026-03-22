# 🔐 Enterprise DevSecOps Security Pipeline

An automated DevSecOps security pipeline built with GitHub Actions, focused on vulnerability detection, secret scanning, and secure code analysis.

---

## 🚀 Objective

This project demonstrates how to integrate **DevSecOps practices** into a CI/CD pipeline, ensuring that security checks are automatically enforced during the development lifecycle.

---

![Security Pipeline](https://github.com/BettinaSM/enterprise-devsecops-security-pipeline/actions/workflows/security.yml/badge.svg)

## 📌 Overview
This project demonstrates a DevSecOps pipeline integrating automated security scanning into CI/CD workflows.

It simulates a real enterprise scenario where security validation is enforced before deployment.

---

## 🧠 Technologies & Tools

* GitHub Actions (CI/CD)
* Trivy (vulnerability scanner)
* Gitleaks (secret detection)
* Semgrep (SAST - static code analysis)
* Python (intentionally vulnerable sample app)
* Docker (ready for container scanning)

---

## ⚙️ Pipeline Architecture

```text
Developer Push → GitHub Actions →
    ├── Secret Scan (Gitleaks)
    ├── SAST (Semgrep)
    ├── Vulnerability Scan (Trivy)
    └── Security Gate (FAIL on high risk)
```

---

## ⚠️ Pipeline Behavior

> ⚠️ This pipeline is intentionally designed to FAIL.

This repository contains intentionally vulnerable code to demonstrate:

* Automated vulnerability detection
* Security enforcement in CI/CD
* DevSecOps best practices in action

If **HIGH or CRITICAL vulnerabilities** are detected:

❌ The pipeline fails automatically
✅ Unsafe code is blocked

👉 This simulates a real-world enterprise security gate.

---

## 📦 Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── security.yml
├── app.py
├── requirements.txt
├── Dockerfile
├── .env.example
└── README.md
```

---

## 🔍 Tooling Breakdown

### 🔐 Gitleaks

Detects potential credential leaks (API keys, tokens, passwords)

### 🧠 Semgrep

Performs static code analysis to identify insecure patterns

### 🐳 Trivy

Scans dependencies and container images for known vulnerabilities

---

## 🧪 Simulated Vulnerabilities

This project includes intentionally insecure elements such as:

* Hardcoded secrets
* Vulnerable dependencies
* Insecure coding patterns

---

## 🛠️ How It Works

1. A commit is pushed
2. GitHub Actions triggers automatically
3. Security scanners execute
4. If critical issues are found:

❌ Pipeline fails
✅ Security is enforced

---

## 🔒 Secrets Management

* `.env` files are NOT committed
* Sensitive data is stored using GitHub Secrets
* `.env.example` provides a safe template

---

## 📊 Future Improvements

* SIEM integration
* Vulnerability dashboards
* Automated notifications (Slack / Email)
* Secure deployment pipeline after approval

---

## 💡 Real-World Impact
This pipeline demonstrates how organizations can:

- Prevent insecure code from reaching production
- Reduce risk of credential exposure
- Enforce security policies automatically

----

## 👩‍💻 Author

Bettina Santana de Meirelles
Unix/Linux Infrastructure | DevOps | Security | Cloud

🔗 GitHub: https://github.com/BettinaSM

---

## ⭐ Project Highlights

This project goes beyond a simple pipeline by demonstrating:

✔ DevSecOps culture
✔ Security as Code
✔ Real security enforcement
✔ Enterprise-grade pipeline behavior

---

## 📌 Conclusion

This repository simulates a real-world scenario where security is embedded into the development process, ensuring safer and more reliable software delivery.
