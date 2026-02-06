# Use uma imagem base Python oficial
FROM python:3.11-slim-buster

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de requisitos e instale as dependências
# Certifique-se de ter um arquivo requirements.txt com fastapi e uvicorn
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do seu código da aplicação
COPY . .

# Comando para iniciar o servidor Uvicorn com o FastAPI
# Assumindo que seu aplicativo FastAPI está em app/main.py e a instância FastAPI é chamada de "app"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
