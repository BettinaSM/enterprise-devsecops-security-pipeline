# ⚠️ Código propositalmente vulnerável (para demonstração DevSecOps)

import os

# Hardcoded secret (erro de segurança)
password = "admin123"

def login(user_input):
    # Simulação insegura (sem validação)
    if user_input == password:
        print("Login sucesso")
    else:
        print("Falha")

# Execução
user = input("Digite a senha: ")
login(user)
