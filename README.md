# 🔐 Enterprise DevSecOps Security Pipeline

![Security Pipeline](https://github.com/BettinaSM/enterprise-devsecops-security-pipeline/actions/workflows/security.yml/badge.svg)

## 📌 Overview
This project demonstrates a DevSecOps pipeline integrating automated security scanning into CI/CD workflows.

It simulates a real enterprise scenario where security validation is enforced before deployment.

## 🚀 Key Features
- 🔍 Static Application Security Testing (SAST)
- 🔐 Secrets detection
- 📦 Dependency vulnerability scanning
- 🐳 Container image scanning
- 🚫 Security gate enforcement (pipeline fails on critical issues)

## 🛠️ Tools Used
- GitHub Actions
- Gitleaks (Secrets detection)
- Semgrep (SAST)
- Trivy (Vulnerability & container scanning)

## 🔍 Example Findings
- Hardcoded credentials detected
- Vulnerable dependencies identified
- Insecure coding patterns flagged

## ⚠️ Security Approach
Sensitive data is NOT stored in the repository.

Secrets are securely managed using GitHub Secrets.

## 💡 Real-World Impact
This pipeline demonstrates how organizations can:

- Prevent insecure code from reaching production
- Reduce risk of credential exposure
- Enforce security policies automatically

## 📂 Project Structure
