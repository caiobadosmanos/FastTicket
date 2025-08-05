from cs50 import SQL

# Conecta ao banco de dados
db = SQL("sqlite:///tickets.db")

def adicionar_ticket(valor):
    db.execute(
        "INSERT INTO tickets (valor, use) VALUES (?, ?)",
        valor, "no"
    )
    print(f"Ticket adicionado: valor={valor}")

