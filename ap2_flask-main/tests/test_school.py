# tests/test_school.py
import unittest
from app import app
from models.ap2_escola_models import db, Professor, Turma, Aluno
from datetime import datetime

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
        db.drop_all()
        self.app_context.pop()

    # Teste para a rota principal
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Sistema de gerenciamento escolar", response.data.decode())

    # Testes para Professores
    def test_get_professores(self):
        response = self.client.get('/school/professores')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])  # Inicialmente, não há professores

    def test_create_professor(self):
        response = self.client.post('/school/professores', data={
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
        self.client.post('/school/professores', data={
            'nome': 'Prof. Maria',
            'idade': 35,
            'materia': 'Biologia'
        })
        response = self.client.post('/school/professores/update', data={
            '_method': 'PUT',
            'id': 1,
            'nome': 'Prof. Maria Silva',
            'idade': 36
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['nome'], 'Prof. Maria Silva')

    def test_delete_professor(self):
        # Criação inicial de um professor
        self.client.post('/school/professores', data={
            'nome': 'Prof. Carlos',
            'idade': 45,
            'materia': 'História'
        })
        response = self.client.post('/school/professores/delete', data={'_method': 'DELETE', 'id': 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Professor deletado com sucesso')

    # Testes para Turmas
    def test_create_turma(self):
        # Primeiro cria um professor para associar à turma
        self.client.post('/school/professores', data={
            'nome': 'Prof. Ana',
            'idade': 30,
            'materia': 'Geografia'
        })
        response = self.client.post('/school/turmas', data={
            'descricao': 'Turma 1',
            'ativo': 'true',
            'professor_id': 1
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['descricao'], 'Turma 1')

    def test_delete_turma(self):
        # Primeiro cria um professor e uma turma
        self.client.post('/school/professores', data={
            'nome': 'Prof. Paulo',
            'idade': 50,
            'materia': 'Química'
        })
        self.client.post('/school/turmas', data={
            'descricao': 'Turma 2',
            'ativo': 'true',
            'professor_id': 1
        })
        response = self.client.post('/school/turmas/delete', data={'_method': 'DELETE', 'id': 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Turma deletada com sucesso')

    # Testes para Alunos
    def test_create_aluno(self):
        # Primeiro cria um professor e uma turma para associar ao aluno
        self.client.post('/school/professores', data={
            'nome': 'Prof. Beatriz',
            'idade': 42,
            'materia': 'Física'
        })
        self.client.post('/school/turmas', data={
            'descricao': 'Turma Física',
            'ativo': 'true',
            'professor_id': 1
        })
        response = self.client.post('/school/alunos', data={
            'nome': 'Carlos',
            'idade': 15,
            'data_nascimento': '2008-06-15',
            'turma_id': 1
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['nome'], 'Carlos')
        self.assertEqual(response.json['idade'], 15)

    def test_delete_aluno(self):
        # Primeiro cria um professor, uma turma e um aluno
        self.client.post('/school/professores', data={
            'nome': 'Prof. Roberto',
            'idade': 48,
            'materia': 'Sociologia'
        })
        self.client.post('/school/turmas', data={
            'descricao': 'Turma Sociologia',
            'ativo': 'true',
            'professor_id': 1
        })
        self.client.post('/school/alunos', data={
            'nome': 'Ana',
            'idade': 17,
            'data_nascimento': '2006-03-20',
            'turma_id': 1
        })
        response = self.client.post('/school/alunos/delete', data={'_method': 'DELETE', 'id': 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Aluno deletado com sucesso')

if __name__ == '__main__':
    unittest.main()