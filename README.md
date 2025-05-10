# 📡 Raspberry Pi Pico W + Flask API + WebSocket Frontend

Este projeto integra um microcontrolador **Raspberry Pi Pico W**, programado em **C bare metal**, com uma **API Flask hospedada na nuvem (Render)**. O Pico W envia dados de sensores e entradas físicas via **requisições HTTP** para a API Flask, que por sua vez **transmite essas informações em tempo real via WebSocket para um frontend web**.

---

## 🧠 Visão Geral do Projeto

* O **Raspberry Pi Pico W** atua como cliente HTTP, enviando `POST` requests para a rota `/update` dessa API Flask.
* A API Flask está **hospedada na plataforma Render**, acessível publicamente.
* O **frontend web** mantém uma conexão WebSocket com o servidor para **atualizações em tempo real** dos dados recebidos do microcontrolador.

### Dados Enviados pelo Pico W:

* Estado de dois botões físicos
* Direção do joystick analógico (eixo X e Y)
* Temperatura medida pelo sensor analógico interno

---

## 🔀 Fluxo de Comunicação

```plaintext
[Pico W (HTTP POST /update)] → [API Flask (Render)]
                                      ↓
                              [WebSocket Broadcast]
                                      ↓
                          [Frontend Web (tempo real)]
```

---

## 📂 Estrutura do Projeto

```plaintext
.
│
├── app.py             # Servidor Flask com rotas HTTP e WebSocket   
├── requirements.txt   # Dependências do backend Pico W
├── README.md
└── render.yaml        # Arquivos de configuração de deploy
```

---

## ☁️ Backend (Flask + WebSocket)

### Requisitos

* Python 3.8+
* Flask
* Flask-SocketIO
* eventlet
* Flask-CORS

### Instalação local para testes:

```bash
cd backend
pip install -r requirements.txt
python app.py
```

O servidor expõe:

* `POST /update`: Recebe dados do Pico W (em JSON)
* WebSocket: Envia dados atualizados para os clientes conectados em tempo real

---

### Visualização:

Abra a página do frontend no seu navegador [LINK FALTANDO]

---

## 🤖 Raspberry Pi Pico W

* Programado em **C bare metal**, utilizando o SDK oficial
* Realiza leitura dos sensores e entradas
* Envia os dados via HTTP para a API no Render:

```http
POST https://pico-windrose-backend.onrender.com/update
Content-Type: application/json
{
  "btn_a": true,
  "btn_b": false,
  "joystick_x": 127,
  "joystick_y": 240,
  "temp": 36.5
}
```

---

## 📡 Deploy

* Backend Flask: Hospedado na [Render](https://pico-windrose-backend.onrender.com)
* Frontend: Pode ser hospedado no GitHub Pages, Netlify, Vercel, ou junto do backend
* Pico W: Requer conectividade Wi-Fi para enviar dados periodicamente

---

## 🔧 Tecnologias Utilizadas

* Raspberry Pi Pico W (C Bare Metal)
* Flask (API REST)
* Flask-SocketIO (WebSocket)
* HTML, JavaScript (Frontend)
* Render (Hospedagem backend)

---

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

