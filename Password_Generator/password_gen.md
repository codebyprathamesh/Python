# 🔐 Random Password Generator

A simple Python script that generates **secure, random passwords** using a combination of lowercase letters, uppercase letters, digits, hex digits, octal digits, and punctuation symbols.  

This project is perfect for beginners learning how to use Python’s built-in **`random`** and **`string`** modules.

---

## 🧠 How It Works

1. The script imports various character sets from Python’s `string` module:
   - `ascii_lowercase` → `abcdefghijklmnopqrstuvwxyz`
   - `ascii_uppercase` → `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
   - `ascii_letters` → Both lowercase and uppercase letters combined.
   - `digits` → `0123456789`
   - `octdigits` → `01234567`
   - `hexdigits` → `0123456789abcdefABCDEF`
   - `punctuation` → Special characters like `!@#$%^&*()_+[]{}|;:'",.<>?/`

2. All these sets are concatenated into a single string named `all`.

3. The user enters the desired password length.

4. The program randomly selects characters from `all` to generate a secure password.

---

## ⚙️ How to Run

1. Make sure **Python 3** is installed.
2. Save the script as `password_generator.py`.
3. Open your terminal or command prompt.
4. Run this command:

python password_generator.py

text

5. Enter the desired password length when prompted.

---

## 💡 Example Output

Enter the size of password
12
Your generated password:
Fq^eGx12$h9P

text

*(Each run will generate a completely different password.)*

---

## 🧩 Key Concepts

- **Randomization:** Using `random.choice()` to pick characters.
- **String Handling:** Combining multiple sources of characters.
- **User Input:** Interactive CLI input for password length.

---

## 🚀 Customization

You can modify the script to:
- Exclude specific character types for stricter password rules.
- Automatically copy the generated password to the clipboard using `pyperclip`.
- Generate multiple passwords at once.

---

## 🧑‍💻 Built With

- **Python 3**
- **random** and **string** modules

---

## 📜 License

This project is licensed under the **MIT License**.  
You are free to use and modify it with attribution.

---

### 💡 Author
Made with ❤️ in Python by *Prathamesh More*.





