from flask import Blueprint, jsonify, request
from models.ap2_escola_models import db, Professor, Aluno, Turma
from datetime import datetime

school_blueprint = Blueprint('school', __name__)

# Rotas para Professores
@school_blueprint.route('/professores', methods=['GET'])
def get_professores():
    professores = Professor.query.all()
    return jsonify([p.to_dict() for p in professores])

@school_blueprint.route('/professor', methods=['GET'])
def get_professor():
    id = request.args.get('id')  # Captura o ID da query string
    if id is not None:
        professor = Professor.query.get(id)
        if professor:
            return jsonify(professor.to_dict())
        return jsonify({'message': 'Professor não encontrado'}), 404
    return jsonify({'message': 'ID não fornecido'}), 400

@school_blueprint.route('/professores', methods=['POST'])
def create_professor():
    data = request.form
    new_professor = Professor(
        nome=data['nome'],
        idade=data['idade'],
        materia=data['materia'],
        observacoes=data.get('observacoes')
    )
    db.session.add(new_professor)
    db.session.commit()
    return jsonify(new_professor.to_dict()), 201

@school_blueprint.route('/professores/update', methods=['POST'])
def update_professor():
    # Verifica se o método é um PUT simulado
    if request.form.get('_method') == 'PUT':
        id = request.form.get('id')
        if id is None:
            return jsonify({'message': 'ID não fornecido'}), 400

        try:
            id = int(id)
        except ValueError:
            return jsonify({'message': 'ID inválido'}), 400

        professor = Professor.query.get(id)
        if not professor:
            return jsonify({'message': 'Professor não encontrado'}), 404

        # Atualiza os campos do professor
        professor.nome = request.form.get('nome', professor.nome)
        professor.idade = request.form.get('idade', professor.idade)
        professor.materia = request.form.get('materia', professor.materia)
        professor.observacoes = request.form.get('observacoes', professor.observacoes)

        db.session.commit()
        return jsonify(professor.to_dict())

    # Se não for PUT, trate como um POST normal (ou retorne um erro)
    return jsonify({'message': 'Método não permitido'}), 405



@school_blueprint.route('/professores/delete', methods=['POST'])
def delete_professor():
    # Verifica se o método é um DELETE simulado
    if request.form.get('_method') == 'DELETE':
        id = request.form.get('id')
        if id is None:
            return jsonify({'message': 'ID não fornecido'}), 400

        try:
            id = int(id)
        except ValueError:
            return jsonify({'message': 'ID inválido'}), 400

        professor = Professor.query.get(id)
        if not professor:
            return jsonify({'message': 'Professor não encontrado'}), 404

        db.session.delete(professor)
        db.session.commit()
        return jsonify({'message': 'Professor deletado com sucesso'})

    # Se não for um DELETE simulado, retorne um erro ou trate de acordo
    return jsonify({'message': 'Método não permitido'}), 405


# Rotas para Turmas
@school_blueprint.route('/turmas', methods=['GET'])
def get_turmas():
    turmas = Turma.query.all()
    return jsonify([t.to_dict() for t in turmas])

@school_blueprint.route('/turma', methods=['GET'])
def get_turma():
    id = request.args.get('id')  # Captura o ID da query string
    if id is not None:
        turma = Turma.query.get(id)
        if turma:
            return jsonify(turma.to_dict())
        return jsonify({'message': 'Turma não encontrada'}), 404
    return jsonify({'message': 'ID não fornecido'}), 400

@school_blueprint.route('/turmas', methods=['POST'])
def create_turma():
    data = request.form
    ativo = data.get('ativo', 'true').lower() == 'true'  # Converte para booleano
    new_turma = Turma(
        descricao=data['descricao'],
        ativo=ativo,
        professor_id=data['professor_id']
    )
    db.session.add(new_turma)
    db.session.commit()
    return jsonify(new_turma.to_dict()), 201

@school_blueprint.route('/turmas/update', methods=['POST'])
def update_turma():
    # Verifica se o método é um PUT simulado
    if request.form.get('_method') == 'PUT':
        id = request.form.get('id')
        if id is None:
            return jsonify({'message': 'ID não fornecido'}), 400

        try:
            id = int(id)
        except ValueError:
            return jsonify({'message': 'ID inválido'}), 400

        turma = Turma.query.get(id)
        if not turma:
            return jsonify({'message': 'Turma não encontrada'}), 404

        # Atualiza os campos da turma
        turma.descricao = request.form.get('descricao', turma.descricao)
        
        # Aqui convertemos o valor 'ativo' para booleano
        turma.ativo = request.form.get('ativo') == 'on'  # Converte 'on' para True e não-setado para False
        
        turma.professor_id = request.form.get('professor_id', turma.professor_id)
        db.session.commit()
        return jsonify(turma.to_dict())

    # Se não for PUT, trate como um POST normal (ou retorne um erro)
    return jsonify({'message': 'Método não permitido'}), 405


@school_blueprint.route('/turmas/delete', methods=['POST'])
def delete_turma():
    # Verifica se o método é um DELETE simulado
    if request.form.get('_method') == 'DELETE':
        id = request.form.get('id')
        if id is None:
            return jsonify({'message': 'ID não fornecido'}), 400

        try:
            id = int(id)
        except ValueError:
            return jsonify({'message': 'ID inválido'}), 400

        turma = Turma.query.get(id)
        if not turma:
            return jsonify({'message': 'Turma não encontrada'}), 404

        db.session.delete(turma)
        db.session.commit()
        return jsonify({'message': 'Turma deletada com sucesso'})

    # Se não for um DELETE simulado, retorne um erro ou trate de acordo
    return jsonify({'message': 'Método não permitido'}), 405


# Rotas para Alunos
@school_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = Aluno.query.all()
    return jsonify([a.to_dict() for a in alunos])

@school_blueprint.route('/aluno', methods=['GET'])
def get_aluno():
    id = request.args.get('id')  # Captura o ID da query string
    if id is not None:
        aluno = Aluno.query.get(id)
        if aluno:
            return jsonify(aluno.to_dict())
        return jsonify({'message': 'Aluno não encontrado'}), 404
    return jsonify({'message': 'ID não fornecido'}), 400

@school_blueprint.route('/alunos', methods=['POST'])
def create_aluno():
    data = request.form
    try:
        # Converte a string de data_nascimento para um objeto date
        data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
        
        new_aluno = Aluno(
            nome=data['nome'],
            idade=data['idade'],
            data_nascimento=data_nascimento,
            turma_id=data['turma_id']
        )
        
        db.session.add(new_aluno)
        db.session.commit()
        return jsonify(new_aluno.to_dict()), 201
    except ValueError:
        return jsonify({'message': 'Data de nascimento inválida'}), 400
    except Exception as e:
        return jsonify({'message': 'Erro ao criar aluno: {}'.format(str(e))}), 500

@school_blueprint.route('/alunos/update', methods=['POST'])
def update_aluno():
    # Verifica se o método é um PUT simulado
    if request.form.get('_method') == 'PUT':
        id = request.form.get('id')
        if id is None:
            return jsonify({'message': 'ID não fornecido'}), 400

        try:
            id = int(id)
        except ValueError:
            return jsonify({'message': 'ID inválido'}), 400

        aluno = Aluno.query.get(id)
        if not aluno:
            return jsonify({'message': 'Aluno não encontrado'}), 404

        # Atualiza os campos do aluno
        aluno.nome = request.form.get('nome', aluno.nome)
        aluno.idade = request.form.get('idade', aluno.idade)
        aluno.turma_id = request.form.get('turma_id', aluno.turma_id)
        db.session.commit()
        return jsonify(aluno.to_dict())

    # Se não for PUT, trate como um POST normal (ou retorne um erro)
    return jsonify({'message': 'Método não permitido'}), 405

@school_blueprint.route('/alunos/delete', methods=['POST'])
def delete_aluno():
    # Verifica se o método é um DELETE simulado
    if request.form.get('_method') == 'DELETE':
        id = request.form.get('id')
        if id is None:
            return jsonify({'message': 'ID não fornecido'}), 400

        try:
            id = int(id)
        except ValueError:
            return jsonify({'message': 'ID inválido'}), 400

        aluno = Aluno.query.get(id)
        if not aluno:
            return jsonify({'message': 'Aluno não encontrado'}), 404

        db.session.delete(aluno)
        db.session.commit()
        return jsonify({'message': 'Aluno deletado com sucesso'})

    # Se não for um DELETE simulado, retorne um erro ou trate de acordo
    return jsonify({'message': 'Método não permitido'}), 405