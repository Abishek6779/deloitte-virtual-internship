# Deloitte Virtual Internship - Task 2

## 📌 Project Overview
This project was completed as part of the Deloitte Technology Virtual Experience Program.

The goal of this task is to unify two different data models into a single consistent format using Python.

---

## ⚙️ Problem Statement
Different systems store user data in different formats. For example:

- System 1:
  - name
  - age

- System 2:
  - full_name
  - years

The challenge is to standardize this data into a single unified structure.

---

## 💡 Solution
A Python function `unify()` is created to:

- Extract relevant fields from different formats
- Convert them into a standard structure:
  - full_name
  - age

---

## 🧾 Code Example
```python
def unify(data):
    return {
        "full_name": data.get("name") or data.get("full_name"),
        "age": data.get("age") or data.get("years")
    }
