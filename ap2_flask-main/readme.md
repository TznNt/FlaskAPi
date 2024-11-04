markdown
Copiar código
# Sistema de Gerenciamento Escolar

Este projeto é uma API Flask para gerenciamento de um sistema escolar, onde é possível gerenciar professores, turmas e alunos. O projeto utiliza Flask e Flask-SQLAlchemy para manipulação de dados.

## Requisitos

- Python 3.7 ou superior
- pip

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://seu-repositorio-url.git
   cd nome-do-repositorio
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar código
python -m venv venv
Ative o ambiente virtual:

Windows:
bash
Copiar código
venv\Scripts\activate
Linux/Mac:
bash
Copiar código
source venv/bin/activate
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Configuração
Certifique-se de que o arquivo config.py está presente com as configurações necessárias. Um exemplo de configuração pode ser:

python
Copiar código
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST = '0.0.0.0'
    PORT = 8000
    DEBUG = True
Execução
Execute o servidor Flask:

bash
Copiar código
python app.py
Acesse a API no navegador ou no Insomnia/Postman:

bash
Copiar código
http://localhost:8000/school
Testando as Rotas
Utilize um cliente HTTP como Insomnia ou Postman para testar as rotas da API. Aqui estão alguns exemplos de como testar as rotas:

Rotas de Professor
Adicionar um Professor

Método: POST
URL: http://localhost:8000/school/professores
Body (JSON):
json
Copiar código
{
    "nome": "João Silva",
    "idade": 30,
    "materia": "Matemática",
    "observacoes": "Professor experiente"
}
Listar Professores

Método: GET
URL: http://localhost:8000/school/professores
Obter Detalhes de um Professor

Método: GET
URL: http://localhost:8000/school/professores/{id}
Atualizar um Professor

Método: PUT
URL: http://localhost:8000/school/professores/{id}
Body (JSON):
json
Copiar código
{
    "nome": "João Silva",
    "idade": 31,
    "materia": "Matemática",
    "observacoes": "Atualizado"
}
Deletar um Professor

Método: DELETE
URL: http://localhost:8000/school/professores/{id}
Rotas de Turma
Adicionar uma Turma

Método: POST
URL: http://localhost:8000/school/turmas
Body (JSON):
json
Copiar código
{
    "descricao": "Turma de Matemática",
    "professor_id": 1
}
Listar Turmas

Método: GET
URL: http://localhost:8000/school/turmas
Obter Detalhes de uma Turma

Método: GET
URL: http://localhost:8000/school/turmas/{id}
Atualizar uma Turma

Método: PUT
URL: http://localhost:8000/school/turmas/{id}
Body (JSON):
json
Copiar código
{
    "descricao": "Turma de Matemática Avançada",
    "professor_id": 1
}
Deletar uma Turma

Método: DELETE
URL: http://localhost:8000/school/turmas/{id}
Rotas de Aluno
Adicionar um Aluno

Método: POST
URL: http://localhost:8000/school/alunos
Body (JSON):
json
Copiar código
{
    "nome": "Maria Oliveira",
    "idade": 16,
    "data_nascimento": "2007-05-20",
    "nota_primeiro_semestre": 7.5,
    "nota_segundo_semestre": 8.0,
    "turma_id": 1
}
Listar Alunos

Método: GET
URL: http://localhost:8000/school/alunos
Obter Detalhes de um Aluno

Método: GET
URL: http://localhost:8000/school/alunos/{id}
Atualizar um Aluno

Método: PUT
URL: http://localhost:8000/school/alunos/{id}
Body (JSON):
json
Copiar código
{
    "nome": "Maria Oliveira",
    "idade": 17,
    "turma_id": 1
}
Deletar um Aluno

Método: DELETE
URL: http://localhost:8000/school/alunos/{id}