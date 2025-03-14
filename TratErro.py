from flask import Flask, jsonify, request

dici = {
    "alunos": [
        {
            "id": 1,
            "nome": "caio",
            "idade": 25,
            "turma_id": 3,
            "data_nascimento": "10/10/2005",
            "nota_primeiro_semestre": 10.00,
            "nota_segundo_semestre": 9.00,
            "media_final": 9.00
        }
    ],
    "professor": [
        {
            "id": 2,
            "nome": "rafael",
            "idade": 15,
            "materia": "Desenvolvimento web",
            "observacoes": "Gosto de lesionar"
        }
    ],
    "turma": [
        {
            "id": 3,
            "descricao": "api's",
            "professor_id": 2,
            "ativo": "Ativa"
        }
    ]
}

app = Flask(__name__)

# POST (CREATE)
@app.route('/alunos', methods=['POST'])
def createAluno():
    try:
        dados = request.json
        if not dados.get("turma_id"): #Perguntar pro Romário
            return jsonify({"error": "O campo 'turma_id' é obrigatório."}), 400
        
        turma_existente = next((turma for turma in dici["turma"] if turma["id"] == dados["turma_id"]), None)
        if not turma_existente:
            return jsonify({"error": "Turma não encontrada."}), 404

        dados['id'] = max([aluno['id'] for aluno in dici["alunos"]]) + 1 if dici["alunos"] else 1
        dici['alunos'].append(dados)
        return jsonify(dados), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/professor', methods=['POST'])
def createProfessores():
    try:
        dados = request.json
        dados['id'] = max([professor['id'] for professor in dici["professor"]]) + 1 if dici["professor"] else 1
        dici['professor'].append(dados)
        return jsonify(dados), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/turma', methods=['POST'])
def createTurma():
    try:
        dados = request.json
        professor_existente = next((professor for professor in dici["professor"] if professor["id"] == dados["professor_id"]), None)
        if not professor_existente:
            return jsonify({"error": "Professor não encontrado."}), 404

        dados['id'] = max([turma['id'] for turma in dici["turma"]]) + 1 if dici["turma"] else 1
        dici['turma'].append(dados)
        return jsonify(dados), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET (READ)
@app.route('/alunos', methods=['GET'])
def getAluno():
    dados = dici['alunos']
    return jsonify(dados)

@app.route("/professor", methods=['GET'])
def getProfessor():
    dados = dici['professor']
    return jsonify(dados)

@app.route('/turma', methods=['GET'])
def getTurma():
    dados = dici['turma']
    return jsonify (dados)

# PUT (UPDATE)
@app.route("/alunos/<int:idAluno>", methods=['PUT'])
def updateAlunos(idAluno):
    try:
        aluno = next((aluno for aluno in dici["alunos"] if aluno["id"] == idAluno), None)
        if not aluno:
            return jsonify({"error": "Aluno não encontrado"}), 404
        
        dados = request.json
        aluno.update(dados)
        return jsonify(aluno)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/professor/<int:idProfessor>", methods=['PUT'])
def updateProfessores(idProfessor):
    try:
        professor = next((professor for professor in dici["professor"] if professor["id"] == idProfessor), None)
        if not professor:
            return jsonify({"error": "Professor não encontrado"}), 404
        
        dados = request.json
        professor.update(dados)
        return jsonify(professor)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/turma/<int:idTurma>", methods=['PUT'])
def updateTurma(idTurma):
    try:
        turma = next((turma for turma in dici["turma"] if turma["id"] == idTurma), None)
        if not turma:
            return jsonify({"error": "Turma não encontrada"}), 404
        
        dados = request.json
        turma.update(dados)
        return jsonify(turma)
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
