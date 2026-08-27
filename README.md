# 🌐 Network Monitor

Projeto simples de monitoramento de rede (mini-NOC).  
A ideia é evoluir o projeto **um pouco por dia**, mostrando passo a passo como construir uma ferramenta real de monitoramento.

---

## 🚀 Objetivo
Criar um sistema que:
- Monitora hosts (ping, ICMP).
- Exibe status em tempo real.
- Armazena histórico em banco de dados.
- Mostra dashboard com gráficos.
- Envia alertas em caso de falha.

---

## ✨ Funcionalidades atuais
- Ping em múltiplos hosts (compatível com Windows e Linux/Mac).
- Lista de hosts personalizável via arquivo `host.txt`.
- Saída colorida no terminal (verde = online ✅, vermelho = offline ❌).
- Exibição do tempo de resposta em ms.
- Registro de histórico com data/hora no arquivo `monitor.log`.

---

## 📅 Roadmap Diário

### ✅ Dia 1
- Criar repositório.
- Subir script básico de ping (`monitor.py`).
- Mostrar status de alguns hosts no terminal.

### ✅ Dia 2
- Ler lista de hosts de um arquivo (`host.txt`).
- Permitir personalizar os hosts monitorados.

### ✅ Dia 3
- Melhorar saída no terminal (cores, tempo de resposta em ms).
- Salvar histórico das verificações em arquivo de log (`monitor.log`).

### 🔨 Dia 4 (em progresso)
- Criar API com **FastAPI** (`/status?host=...`).
- Retornar resultado em JSON.

### 🔜 Dia 5
- Criar página HTML simples que consome a API e exibe hosts.

### 🔜 Dia 6
- Salvar histórico em banco de dados (SQLite).

### 🔜 Dia 7
- Criar gráficos de uptime (Chart.js).

---

## 📂 Estrutura do projeto

```
network-monitor/
│── monitor.py        # Script principal de monitoramento
│── host.txt          # Lista de hosts a monitorar (um por linha)
│── monitor.log       # Histórico das verificações (gerado automaticamente)
│── requirements.txt  # Dependências do projeto
│── README.md
```

---

## 🛠️ Como rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/ranierinmoreira/network-monitor.git
   cd network-monitor
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Edite o arquivo `host.txt` com os hosts que deseja monitorar (um por linha):
   ```
   8.8.8.8
   1.1.1.1
   github.com
   ```

4. Execute o monitor:
   ```bash
   python monitor.py
   ```

5. Confira o histórico no arquivo `monitor.log`.
