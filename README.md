# Calculator-using-python
# 🧮 Python Terminal Calculator

Welcome to the **Python Terminal Calculator** — a simple yet powerful command-line tool to evaluate mathematical expressions, maintain a calculation history, and interact with your past computations.

## 🚀 Features

- ✅ Evaluate any valid Python expression (e.g., `2 + 3 * (4 - 1)`)
- 📜 Automatically saves each calculation in a `History.txt` file
- 🔍 View your complete calculation history
- 🧹 Clear history with a single command
- 🔁 Recalculate new expressions without restarting the program
- ❌ Handles common errors like invalid syntax, division by zero, and undefined variables

## 🛠️ How It Works

1. Run the program — it welcomes you with a prompt.
2. Enter your expression (e.g., `5 + 2 * 3`)
3. The result is displayed and saved to `History.txt`
4. Choose from the following options:
   - `1` → View history
   - `2` → Clear history
   - `3` → Exit
   - `4` → Recalculate

## 📂 File Structure

- `calculator.py`: Main Python script
- `History.txt`: Stores all your past calculations

## ⚠️ Error Handling

The calculator gracefully handles:
- `NameError`: If variables are undefined
- `SyntaxError`: If the expression is malformed
- `ZeroDivisionError`: If division by zero occurs
- `TypeError`: If the input type is invalid

## 📌 Requirements

No external libraries required — just Python 3.x installed.

## 🧠 Note

This calculator uses Python's built-in `eval()` function. While it's great for learning and quick tasks, avoid using it with untrusted input in real-world applications due to security risks.

## 🙌 Author

Made with ❤️ by **sadaiv raj keshri**  
Location: Chirimiri, Chhattisgarh, India  
Date: 02, November 2025

---