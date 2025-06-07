Here's a well-written **README.md** for your enhanced **Right-Angle Triangle** Python program with conditional formatting using `*` and `+`:

---

# 🔺 Right-Angle Triangle Pattern with Conditional Formatting – Python Program

This Python program prints a **right-angled triangle pattern**, using a combination of `*` and `+` symbols. It includes conditional logic for formatting specific elements of the triangle.

## 📌 Description

* The user enters a number `a` (height of the triangle).
* The program uses nested `for` loops to print a **right-angled triangle**:

  * When `row + col == a - 1`, it prints a row of `*` symbols (slant edge).
  * On the **last row**, it prints `+` symbols across the row.

### 🧾 Sample Input & Output

**Input:**

```
Enter height: 5
```

**Output:**

```
        * * 
      * * 
    * * 
  * * 
+ + + + + 
```

> 💡 The triangle builds from the top-right corner down to the base, with the last row filled with `+` symbols.

## 🧠 Logic

* The outer loop (`row`) controls the number of rows.
* The inner loop (`col`) checks:

  * If it's on the left diagonal (`row + col == a - 1`), it prints a line of `*`.
  * If it's the last row (`row == a`), it prints `+`.
* `end=" "` ensures elements print on the same line with spacing.

## 🧾 Code

```python
a = int(input("Enter height: "))
for row in range(1, a + 1):
    for col in range(a):
        if row + col == a - 1:
            print("* " * row, end=" ")
        elif row == a:
            print("+", end=" ")
    print("")
```

## 🛠️ How to Run

1. Save the code to a file, for example: `right_triangle_pattern.py`
2. Run the file using Python:

```bash
python right_triangle_pattern.py
```

3. Enter a height value when prompted to see the pattern output.

## 🎯 Use Case

* Good for practicing:

  * Nested `for` loops
  * Conditional statements
  * Creative pattern printing

* Can be customized to:

  * Use different characters
  * Add alignment or spacing improvements
  * Build other triangle styles (left-aligned, inverted, etc.)

## 📄 License

This project is open-source under the **MIT License**.
Feel free to use, modify, and learn from it!

---

Let me know if you'd like help turning this into a **hollow triangle**, **right-aligned triangle**, or a version with **numeric patterns**!
