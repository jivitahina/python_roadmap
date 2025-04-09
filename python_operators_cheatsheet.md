# 🐍 Python Operators – Full Cheat Sheet with Explanations

## 1. 🧮 Arithmetic Operators

| Operator | Name            | Example | Explanation |
|----------|-----------------|---------|-------------|
| `+`      | Addition         | `5 + 3` → `8` | Adds two numbers. |
| `-`      | Subtraction      | `10 - 4` → `6` | Subtracts the right operand from the left. |
| `*`      | Multiplication   | `6 * 3` → `18` | Multiplies two numbers. |
| `/`      | Division         | `10 / 2` → `5.0` | Divides left by right (returns float). |
| `//`     | Floor Division   | `9 // 2` → `4` | Integer division result (floor value). |
| `%`      | Modulus          | `9 % 2` → `1` | Remainder of division. |
| `**`     | Exponentiation   | `2 ** 3` → `8` | Raises left to the power of right. |

---

## 2. 🧾 Assignment Operators

| Operator | Name               | Example    | Explanation |
|----------|--------------------|------------|-------------|
| `=`      | Assignment         | `x = 5`    | Assigns value to variable. |
| `+=`     | Add and Assign     | `x += 2`   | `x = x + 2` |
| `-=`     | Subtract and Assign| `x -= 1`   | `x = x - 1` |
| `*=`     | Multiply and Assign| `x *= 3`   | `x = x * 3` |
| `/=`     | Divide and Assign  | `x /= 2`   | `x = x / 2` |
| `//=`    | Floor Div and Assign | `x //= 2` | `x = x // 2` |
| `%=`     | Modulus and Assign | `x %= 3`   | `x = x % 3` |
| `**=`    | Power and Assign   | `x **= 2`  | `x = x ** 2` |

---

## 3. 🔍 Comparison Operators

| Operator | Name         | Example       | Explanation |
|----------|--------------|---------------|-------------|
| `==`     | Equal to     | `5 == 5` → `True` | Check if values are equal. |
| `!=`     | Not equal to | `4 != 5` → `True` | Check if values are different. |
| `>`      | Greater than | `7 > 3` → `True` | True if left is greater. |
| `<`      | Less than    | `2 < 8` → `True` | True if left is smaller. |
| `>=`     | Greater or equal | `6 >= 6` → `True` | Left >= Right |
| `<=`     | Less or equal | `3 <= 4` → `True` | Left <= Right |

---

## 4. 🔗 Logical Operators

| Operator | Name      | Example            | Explanation |
|----------|-----------|--------------------|-------------|
| `and`    | Logical AND | `True and False` → `False` | True if both are True. |
| `or`     | Logical OR  | `True or False` → `True` | True if at least one is True. |
| `not`    | Logical NOT | `not True` → `False` | Inverts the Boolean value. |

---

## 5. 🧠 Identity Operators

| Operator | Name     | Example | Explanation |
|----------|----------|---------|-------------|
| `is`     | Is       | `x is y` | True if both refer to same object in memory. |
| `is not` | Is Not   | `x is not y` | True if not same object. |

---

## 6. 📦 Membership Operators

| Operator | Name    | Example            | Explanation |
|----------|---------|--------------------|-------------|
| `in`     | In      | `'a' in 'apple'` → True | True if element is in sequence. |
| `not in` | Not In  | `'z' not in 'apple'` → True | True if element is not present. |

---

## 7. 🧮 Bitwise Operators

| Operator | Name      | Example      | Explanation |
|----------|-----------|--------------|-------------|
| `&`      | AND       | `5 & 3 = 1`  | Binary AND |
| `|`      | OR        | `5 | 3 = 7`  | Binary OR |
| `^`      | XOR       | `5 ^ 3 = 6`  | Binary XOR |
| `~`      | NOT       | `~5 = -6`    | Binary inversion |
| `<<`     | Left Shift| `5 << 1 = 10`| Shift bits left (x2) |
| `>>`     | Right Shift| `5 >> 1 = 2`| Shift bits right (÷2) |

---

## ✅ Sample Practice Code

```python
a = 10
b = 3

print("Addition:", a + b)
print("Modulus:", a % b)
print("Power:", a ** b)
print("Logical AND:", a > 5 and b < 5)
print("Membership:", 3 in [1, 2, 3])
