import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="Aula3"
)

cursor = conexao.cursor()

# ===============================
# método para listar todos os alunos 
# ===============================
def listar_alunos():
    print("\n📌 ALUNOS:")
    cursor.execute("SELECT * FROM ALUNOS")
    for aluno in cursor.fetchall():
        print(aluno)

# ===============================
# 2. método para listar todas as disciplinas distintas
# ===============================
def listar_disciplinas():
    print("\n📌 DISCIPLINAS:")
    cursor.execute("SELECT DISTINCT Disc FROM MATRICULAS")
    for disc in cursor.fetchall():
        print(disc)

# ===============================
# 3. método para listar as matrículas de um semestre específico
# ===============================
def matriculas_semestre(sem):
    print(f"\n📌 MATRÍCULAS DO SEMESTRE {sem}:")
    cursor.execute("SELECT * FROM MATRICULAS WHERE Sem = %s", (sem,))
    for m in cursor.fetchall():
        print(m)

# ===============================
# 4. metodo para listar as matrículas de um aluno específico
# ===============================
def matriculas_aluno(matr):
    print(f"\n📌 MATRÍCULAS DO ALUNO {matr}:")
    cursor.execute("SELECT * FROM MATRICULAS WHERE Matr = %s", (matr,))
    for m in cursor.fetchall():
        print(m)

# ===============================
# 5. método para cancelar a matrícula de um aluno em uma disciplina específica
# ===============================
def cancelar_matricula(matr, disc, sem):
    try:
        print("\n🚨 Iniciando cancelamento...")
        conexao.start_transaction()

        # Verifica se existe
        cursor.execute("""
            SELECT COUNT(*) FROM MATRICULAS
            WHERE Matr = %s AND Disc = %s AND Sem = %s
        """, (matr, disc, sem))

        if cursor.fetchone()[0] == 0:
            raise Exception("Matrícula não encontrada!")

        # Remove matrícula
        cursor.execute("""
            DELETE FROM MATRICULAS
            WHERE Matr = %s AND Disc = %s AND Sem = %s
        """, (matr, disc, sem))

        # Confirma
        conexao.commit()
        print("✅ Matrícula cancelada com sucesso!")

    except Exception as e:
        conexao.rollback()
        print("❌ ROLLBACK executado")
        print("Erro:", e)

# ===============================
# EXECUÇÃO
# ===============================
listar_alunos()
listar_disciplinas()
matriculas_semestre("2026.1")
matriculas_aluno(1)

# Teste de cancelamento
cancelar_matricula(1, "BD", "2026.1")

cursor.close()
conexao.close()