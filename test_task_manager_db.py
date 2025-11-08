#### ZDE BUDOU TESTY #### 
from src.task_manager_db import add_task, get_tasks, update_task_state, delete_task
import pytest

@pytest.mark.parametrize(
        "name, description, state",
        [
            ("První úkol", "Popis úkolu 1", "pending"),
            ("Druhý úkol", "Popis úkolu 2", "in_progress"),
            ("Třetí úkol", "Popis úkolu 3", "completed"),
            ("Čtvrtý úkol", "Popis úkolu 4", "pending"),
        ]
)
def test_add_task_happy_flow(conn, name, description, state):
    # zavolat funkci add_task()
    add_task(conn, name, description, state)

    # vlastní volání do DB a ověření, že se úkol přidal
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT id, name, description, state FROM tasks WHERE name = %s AND description = %s", (name, description))
    tasks = cursor.fetchall()
    task = tasks[0]

    print(task)

    # kontrola, zda daný úkol existuje
    assert task != None, f"Očekáváme, že se nám vrátí úkol {name} s popisem {description} a stavem {state}"
    assert task['name'] == name
    assert task['description'] == description
    assert task['state'] == state

"""
@pytest.mark.parametrize(
        "name, age, email, error_type, error_message",
        [
            (None, 18, "petr@svetr.cz", ValueError, "Invalid user name."),
            ("Rene", -20, "rene@svetr.cz", ValueError, "Invalid user age."),
        ]
)
def test_add_user_fail_flow(conn, name, age, email, error_type, error_message):
    # zavolame funkci add_user s neplatnymi parametry
    with pytest.raises(error_type) as error:
        add_user(conn, name, age, email)

    assert str(error.value) == error_message, f"Ocekavame chybovou hlasku {error_message}, ale dostali jsme {str(error.value)}"



def test_add_user_fixure(conn):
    # zavolat funkci add_user()
    print("\n☘️ FUNC - ADD USER")
    add_user(conn, "Fixator", 12)

    # vlastni volani do DB a overeni, ze se uzivatel pridal
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT id, name, age, email FROM users WHERE name = %s AND age = %s", ("Fixator", 12))
    users = cursor.fetchall()
    user = users[0]

    print(user)

    # kontrola, zda dany uzivatel existuje
    assert user != None, f"Ocekavame ze se nam vrati uzivatel {"Fixator"} ve veku {12}"
"""