🌐 Network Monitor

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

## 📅 Roadmap Diário

### ✅ Dia 1
- Criar repositório.
- Subir script básico de ping (`monitor.py`).
- Mostrar status de alguns hosts no terminal.

### 🔜 Dia 2
- Ler lista de hosts de um arquivo (`hosts.json` ou `hosts.txt`).
- Permitir personalizar os hosts monitorados.

### 🔜 Dia 3
- Melhorar saída no terminal (cores, tempo de resposta em ms).
- Criar um mini-dashboard no console.

### 🔜 Dia 4
- Criar API com **FastAPI** (`/status?host=...`).
- Retornar resultado em JSON.

### 🔜 Dia 5
- Criar página HTML simples que consome a API e exibe hosts.

### 🔜 Dia 6
- Salvar histórico em banco de dados (SQLite).

### 🔜 Dia 7
- Criar gráficos de uptime (Chart.js).

---

## 🛠️ Como rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/ranierinmoreira/network-monitor.git

   cd network-monitor
