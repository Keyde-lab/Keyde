import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="Aula3"
)

cursor = conexao.cursor()

matr = 1
disc = "BD"
semestre = "2026.1"

try:
    print("Iniciando transação...")
    conexao.start_transaction()

    cursor.execute("SELECT COUNT(*) FROM ALUNOS WHERE Matr = %s", (matr,))
    if cursor.fetchone()[0] == 0:
        raise Exception("Aluno não existe!")

    print("Aluno OK")

    cursor.execute("SELECT COUNT(*) FROM MATRICULAS WHERE Disc = %s", (disc,))
    if cursor.fetchone()[0] == 0:
        raise Exception("Disciplina não existe!")

    print("Disciplina OK")

    cursor.execute("""
        INSERT INTO MATRICULAS (Matr, Disc, T, Sem)
        VALUES (%s, %s, 'A', %s)
    """, (matr, disc, semestre))

    print("Matrícula inserida")

    conexao.commit()
    print("COMMIT realizado")

except Exception as e:
    conexao.rollback()
    print("ROLLBACK executado")
    print("Erro:", e)

finally:
    cursor.close()
    conexao.close()
