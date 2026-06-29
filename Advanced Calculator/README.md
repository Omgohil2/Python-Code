# 🧮 Advanced Calculator Engine

A fast, terminal-based calculation engine running dynamic string processing algorithms with automated, timestamped file system tracking logs.

---

## 🚀 How to Run

Launch the processor inside your VS Code terminal from within your `Advanced Calculator` directory:

```powershell
python calculator.py

```

---

## 🕹️ System Commands

While the shell engine is active, pass these specialized command keywords into the user interface:

| System Command | Action Handled | Output Behavior |
| --- | --- | --- |

| `exit` | Shuts down engine loop immediately | Safely closes terminal process stream |

---

## 🛡️ Usage Rules: The Right vs. Wrong Way

The computation wrapper evaluates raw input mathematically. Review the guidelines below to understand correct application syntax vs. invalid syntax structures.

### ✅ The Correct Way

Use clean, explicit Python math operators. Spacing does not matter.

* **Linear Expressions:** Use normal operational signs.
```text
shadow.script ➔ 5 * 5 + 10
➔ 35

```


* **Scoped Parentheses (Prioritization):** Use brackets to force math sequence steps.
```text
shadow.script ➔ (10 + 2) / 3
➔ 4.0

```


* **Exponents / Powers:** Use a double asterisk `` to calculate power values.
```text
shadow.script ➔ 2 ** 3
➔ 8

```



### ❌ The Wrong Way

The engine includes custom safety catches to ensure bad expressions do not crash your program shell.

* **Zero Division Errors (Math Rules Violation):** Do not divide integers by zero.
```text
shadow.script ➔ 10 / 0
❌ Error: Division by zero is mathematically undefined.

```


* **Implicit Multipliers (Syntax Violation):** Always include structural symbols like `*`. Do not type algebra syntax directly.
```text
shadow.script ➔ 5(10 + 2)
❌ Error: Invalid syntax or unrecognized mathematical expression.

```


*(Correct way: `5 * (10 + 2)`)*
* **Plain Text or Code Injections (Security Violation):** Random text parameters are rejected automatically.
```text
shadow.script ➔ hello
❌ Error: Invalid syntax or unrecognized mathematical expression.

```



---