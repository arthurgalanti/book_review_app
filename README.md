# Book Review App

Bem-vindo ao Book Review App! Esta aplicação permite que os usuários registrem livros, adicionem comentários e obtenham análises de sentimentos para esses comentários utilizando a API do Gemini.

## Pré-requisitos

Antes de rodar o projeto, você precisa ter o seguinte instalado:

- **Python 3.6 ou superior**: Certifique-se de que você tem o Python instalado na sua máquina. Você pode verificar a versão do Python instalada executando `python --version` no terminal.

## Configuração do Ambiente

### 1. Clonar o Repositório

Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/book-review-app.git
cd book-review-app
```
### 2. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto e adicione a chave da API do Gemini:

```
GEMINI_API_KEY=sua_api_key_aqui
```

### 2.1. Configuração da API do Gemini
Para obter a chave da API do Gemini, siga os passos abaixo:

1.  Acesse [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  Faça login com sua conta do Google.  
3.  Crie um novo projeto ou selecione um projeto existente.  
4.  Navegue até a seção de "Chaves de API" e siga as instruções para gerar sua chave de API. 
5.  Adicione a chave de API ao arquivo .env na raiz do seu projeto conforme descrito acima.  

### 3. Explicação do setup_and_run.bat
O arquivo setup_and_run.bat é um script batch para facilitar a configuração e execução do projeto no Windows.  
Ele realiza as seguintes tarefas:

Cria o banco de dados:  
Executa python init_db.py para inicializar o banco de dados.  
<br> 
Instala as dependências:   
Executa pip install -r requirements.txt para instalar todas as dependências necessárias listadas no arquivo requirements.txt.  
<br> 
Iniciar o Projeto:   
Executa python main.py para iniciar a aplicação.  
<br> 
Para usar o script setup_and_run.bat, basta executá-lo clicando duas vezes nele ou executando-o no terminal:

```
setup_and_run.bat
```

### 4. Executar Manualmente sem o setup_and_run.bat
Se você preferir configurar e executar o projeto manualmente, siga os passos abaixo:
<br>  
### 4.1. Criar o Banco de Dados
Execute o seguinte comando para criar e inicializar o banco de dados:
```
python init_db.py
```
### 4.2. Instalar Dependências
Instale todas as dependências necessárias usando o pip:
```
pip install -r requirements.txt
```
### 4.3. Iniciar o Projeto
Inicie a aplicação executando o seguinte comando:
```
python main.py
```
<br> 
<br> 
<br> 