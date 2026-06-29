import os
from datetime import datetime

LOG_FILE = "history.log"

def log_calculation(expression, result):
    """Logs the math operation with a clean timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {expression} = {result}\n")

def clear_screen():
    """Clears the terminal for a clean UI."""
    os.system('cls' if os.name == 'nt' else 'clear')

def run_calculator():
    clear_screen()
    print("⚡ [Shadow Script] Advanced Terminal Calculator Initialization...")
    print("Commands: type 'exit' to quit, 'history' to view logs, 'clear' to reset history\n" + "—" * 60)

    while True:
        user_input = input("\n shadow.script ➔ ").strip()

        if user_input.lower() == 'exit':
            print("👋 Exiting Calculator Engine. Execution terminated.")
            break

        if user_input.lower() == 'history':
            print("\n📜 --- Calculation History Logs ---")
            if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 0:
                with open(LOG_FILE, "r", encoding="utf-8") as f:
                    print(f.read().strip())
            else:
                print("No history logs found.")
            print("—" * 35)
            continue

        if user_input.lower() == 'clear':
            if os.path.exists(LOG_FILE):
                os.remove(LOG_FILE)
                print("🧹 History log file completely removed from disk stack.")
            else:
                print("🧹 Log file is already empty.")
            continue

        if not user_input:
            continue

        try:
            result = eval(user_input, {"__builtins__": None}, {})
            print(f" ➔ {result}")
            log_calculation(user_input, result)

        except ZeroDivisionError:
            print(" ❌ Error: Division by zero is mathematically undefined.")
        except Exception:
            print(" ❌ Error: Invalid syntax or unrecognized mathematical expression.")

if __name__ == "__main__":
    run_calculator()