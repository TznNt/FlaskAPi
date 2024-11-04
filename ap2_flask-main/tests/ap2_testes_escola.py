import unittest
from app import app  # Importa o app diretamente do arquivo principal
from models.ap2_escola_models import db, Professor, Turma, Aluno

class SchoolControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Usar um banco de dados em memória para testes
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()  # Cria as tabelas no banco de dados em memória

        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()  # Remove as tabelas após os testes
        self.app_context.pop()

    # Teste para a rota principal
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Sistema de gerenciamento escolar")

    # Testes para Professores
    def test_get_professores(self):
        response = self.client.get('/school/professores')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])  # Inicialmente, não há professores

    def test_create_professor(self):
        response = self.client.post('/school/professores', json={
            'nome': 'Prof. João',
            'idade': 40,
            'materia': 'Matemática',
            'observacoes': 'Especialista em álgebra'
        })
        self.assertEqual(response.status_code, 201)
        data = response.json
        self.assertEqual(data['nome'], 'Prof. João')
        self.assertEqual(data['idade'], 40)

    def test_update_professor(self):
        # Criação inicial de um professor
        self.client.post('/school/professores', json={
            'nome': 'Prof. Maria',
            'idade': 35,
            'materia': 'Biologia'
        })
        response = self.client.put('/school/professores/1', json={
            'nome': 'Prof. Maria Silva',
            'idade': 36
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['nome'], 'Prof. Maria Silva')

    def test_delete_professor(self):
        # Criação inicial de um professor
        self.client.post('/school/professores', json={
            'nome': 'Prof. Carlos',
            'idade': 45,
            'materia': 'História'
        })
        response = self.client.delete('/school/professores/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Professor deletado com sucesso')

    # Testes para Turmas
    def test_create_turma(self):
        # Primeiro cria um professor para associar à turma
        self.client.post('/school/professores', json={
            'nome': 'Prof. Ana',
            'idade': 30,
            'materia': 'Geografia'
        })
        response = self.client.post('/school/turmas', json={
            'descricao': 'Turma 1',
            'ativo': True,
            'professor_id': 1
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['descricao'], 'Turma 1')

    def test_delete_turma(self):
        # Primeiro cria um professor e uma turma
        self.client.post('/school/professores', json={
            'nome': 'Prof. Paulo',
            'idade': 50,
            'materia': 'Química'
        })
        self.client.post('/school/turmas', json={
            'descricao': 'Turma 2',
            'ativo': True,
            'professor_id': 1
        })
        response = self.client.delete('/school/turmas/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Turma deletada com sucesso')

    # Testes para Alunos
    def test_create_aluno(self):
        # Primeiro cria um professor e uma turma para associar ao aluno
        self.client.post('/school/professores', json={
            'nome': 'Prof. Beatriz',
            'idade': 42,
            'materia': 'Física'
        })
        self.client.post('/school/turmas', json={
            'descricao': 'Turma Física',
            'ativo': True,
            'professor_id': 1
        })
        response = self.client.post('/school/alunos', json={
            'nome': 'Carlos',
            'idade': 15,
            'data_nascimento': '2008-06-15',
            'nota_primeiro_semestre': 7.5,
            'nota_segundo_semestre': 8.5,
            'media_final': 8.0,
            'turma_id': 1
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['nome'], 'Carlos')
        self.assertEqual(response.json['idade'], 15)

    def test_delete_aluno(self):
        # Primeiro cria um professor, uma turma e um aluno
        self.client.post('/school/professores', json={
            'nome': 'Prof. Roberto',
            'idade': 48,
            'materia': 'Sociologia'
        })
        self.client.post('/school/turmas', json={
            'descricao': 'Turma Sociologia',
            'ativo': True,
            'professor_id': 1
        })
        self.client.post('/school/alunos', json={
            'nome': 'Ana',
            'idade': 17,
            'data_nascimento': '2006-03-20',
            'nota_primeiro_semestre': 9.0,
            'nota_segundo_semestre': 8.0,
            'media_final': 8.5,
            'turma_id': 1
        })
        response = self.client.delete('/school/alunos/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Aluno deletado com sucesso')

if __name__ == '__main__':
    unittest.main()