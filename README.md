# Pydantic – Simple English Notes

## What is Pydantic?

Pydantic is a Python library used for:

* **Type Validation** → making sure the value is of the correct data type.
* **Data Validation** → checking if the data follows certain rules (age must be > 0, email must be valid, etc.)

Python is a dynamically typed language, meaning a variable can hold any type anytime. This is flexible but dangerous in production code. Pydantic solves this problem by enforcing strict types and rules easily.

---

## Why do we need Pydantic?

### **Problem 1 – No Type Safety**

In Python, you can assign a string to a variable expected to be an integer. Code still runs, causing wrong data to enter the database.

### **Problem 2 – Manual Validation**

To validate types and values, we manually write long IF-conditions, which:

* Makes code repetitive
* Is not scalable
* Creates bugs easily

Pydantic eliminates this boilerplate code.

---

## How Pydantic Works?

Pydantic uses **3 simple steps**:

### **Step 1 – Create a Model**

A model is a class that inherits from `BaseModel`. It defines the data fields and their types.

```python
class Patient(BaseModel):
    name: str
    age: int
```

### **Step 2 – Pass Input Data to Model**

Create an object using data. Pydantic automatically validates it.

```python
data = {"name": "Nitish", "age": 30}
patient = Patient(**data)
```

### **Step 3 – Use Validated Object**

If there is any wrong data, Pydantic throws an error.

```python
insert_data(patient)
```

# Pydantic Code Explanation

## Code Overview

This code demonstrates how to use Pydantic models to validate and handle patient data.

```python
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')


patient_info = {'name': 'pratik', 'age': 19}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
```

## Explanation of the Code

### 1. Importing BaseModel

```python
from pydantic import BaseModel
```

`BaseModel` is imported from Pydantic. It helps create a model with strict type validation.

### 2. Creating the `Patient` Model

```python
class Patient(BaseModel):
    name: str
    age: int
```

* `Patient` is a Pydantic model.
* It expects two fields:

  * `name` → must be a string
  * `age` → must be an integer

If the wrong data type is passed, Pydantic will throw a validation error.

### 3. Function That Uses the Model

```python
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')
```

* This function accepts only a `Patient` object.
* It prints the name, age, and a confirmation message.

### 4. Patient Data as a Dictionary

```python
patient_info = {'name': 'pratik', 'age': 19}
```

The patient details are stored in a dictionary.

### 5. Creating a Pydantic Object Using `**`

```python
patient1 = Patient(**patient_info)
```

This line converts the dictionary into keyword arguments.
It is the same as writing:

```python
patient1 = Patient(name='pratik', age=19)
```

## What Does `**patient_info` Mean?

`**` is the **dictionary unpacking operator** in Python.

It takes a dictionary and expands each key-value pair as a named argument.

### Without Unpacking

```python
Patient(name='pratik', age=19)
```

### With Unpacking

```python
patient_info = {'name': 'pratik', 'age': 19}
Patient(**patient_info)
```

➡️ Both produce the same result.

### Why Use `**`?

* Cleaner code
* Useful when there are many fields
* Works dynamically with unknown keys

### 6. Calling the Function

```python
insert_patient_data(patient1)
```

Output:

```
pratik
19
inserted
```

The validated data is now used successfully.

## Summary

* Pydantic validates data types automatically.
* `Patient(**patient_info)` unpacks dictionary values into model arguments.
* The code ensures clean, safe, and structured data handling.


---

## Key Concepts in Pydantic

### **1️⃣ Basic Models (Data Schema)**

You define what data you want, types, and optional fields.

```python
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool = False   # default value
```

---

### **2️⃣ Optional Fields**

If a field is optional, use `Optional[]` and give default `None`.

```python
from typing import Optional

allergies: Optional[list[str]] = None
```

---

### **3️⃣ Complex Types**

Pydantic supports:

* Lists
* Dictionaries
* Nested models

```python
from typing import List, Dict

allergies: List[str]
contact_details: Dict[str, str]
```

---

### **4️⃣ Built-in Data Validators**

Pydantic has special data types for common validations:

```python
email: EmailStr
linkedin_url: AnyUrl
```

It checks format automatically.

---

### **5️⃣ Field Validation Using `Field()`**

Use `Field()` to apply limits like min/max, length, etc.

```python
from pydantic import Field

age: int = Field(gt=0, lt=120)
name: str = Field(max_length=50)
```

Uses:

* Custom validation
* Constraints (length, range)
* Metadata (title, description, examples)

---

### **6️⃣ Field Validators**
# Pydantic `field_validator` – Simple Explanation

## 🚀 What is `field_validator`?

`field_validator` is a decorator in **Pydantic v2** used to:

* Validate a **single field**
* Modify or clean the field value
* Raise **custom errors** if the value is incorrect

Think of `field_validator` as a **security guard** that checks a specific field before the model object is created.

## 🧠 When do we need `field_validator`?

Use it when:

* You want to validate a specific field
* The default Pydantic type validation is not enough

### Common Use Cases

* Name must be in **uppercase**
* Age must be **greater than 18**
* Email must belong to a specific domain like `@gmail.com`
* Phone number must have **10 digits**

## 🔍 Syntax (Pydantic v2)

```python
from pydantic import BaseModel, field_validator

class ModelName(BaseModel):
    field_name: type

    @field_validator("field_name")
    def validate_field(cls, value):
        # check value here
        return value
```

## 🎯 Example 1: Validate Email Domain

**Only allow Gmail email addresses**

```python
from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    email: EmailStr

    @field_validator("email")
    def check_gmail(cls, value):
        if not value.endswith("@gmail.com"):
            raise ValueError("Only Gmail addresses are allowed")
        return value

user = User(email="pratik@gmail.com")  # ✔ Works
```

### ❌ Invalid Case

```python
User(email="pratik@yahoo.com")
```

**Output:**

```
ValidationError: Only Gmail addresses are allowed
```

## 🎯 Example 2: Transform Name Automatically

**Make every name uppercase**

```python
from pydantic import BaseModel, field_validator

class Person(BaseModel):
    name: str

    @field_validator("name")
    def upper_case_name(cls, value):
        return value.upper()

p = Person(name="pratik")
print(p.name)   # Output: PRATIK
```

Here, the validator **modifies the input value**.

## 🎯 Example 3: Validate Phone Number Format

**Phone number must be exactly 10 digits**

```python
from pydantic import BaseModel, field_validator

class Contact(BaseModel):
    phone: str

    @field_validator("phone")
    def check_phone(cls, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits")
        return value
```

## 🔥 Key Points

| Feature                           | Meaning |
| --------------------------------- | ------- |
| Runs on a single field            | Yes     |
| Can modify the value              | Yes     |
| Can raise custom errors           | Yes     |
| Runs before model object creation | Yes     |

## 🛑 Common Mistake

Pydantic v1 syntax **does NOT work** in v2:

```python
# ❌ Wrong
@validator("name")
```

### ✔ Correct for v2

```python
@field_validator("name")
```

## 🧾 Summary

Use `field_validator` when:

✔ You want **extra validation**
✔ You want to **transform** a field value
✔ You need **custom rules**

It ensures that **invalid data never enters your system**.

---


---

### **7️⃣ Model Validators**

Used when validation depends on multiple fields.

Example: If age > 60, then emergency contact must exist.

```python
@model_validator(mode="after")
def check_emergency_contact(cls, model):
    if model.age > 60 and "emergency" not in model.contact_details:
        raise ValueError("Emergency number required")
    return model
```

---

### **8️⃣ Computed Fields**

Fields that are calculated from other fields.

Example: Calculate BMI

```python
@computed_field
@property
def bmi(self) -> float:
    return round(self.weight / (self.height ** 2), 2)
```

User doesn’t give BMI — Pydantic computes it automatically.

---

### **9️⃣ Nested Models**

Use one model inside another for structured data.

```python
class Address(BaseModel):
    city: str
    state: str
    pincode: int

class Patient(BaseModel):
    name: str
    age: int
    address: Address
```

**Benefits:**

* Cleaner code
* Reusable components
* Better readability
* Automated validation

---

### **🔟 Serialization**

Convert Pydantic objects into:

#### Python Dictionary

```python
patient.model_dump()
```

#### JSON

```python
patient.model_dump_json()
```

Control exported fields using:

* `include`
* `exclude`
* `exclude_unset`

Example:

```python
patient.model_dump(include={"name", "age"})
```

---

## Conclusion

Pydantic helps you:

✔ Define clean data models
✔ Validate input automatically
✔ Avoid manual IF checks
✔ Work safely in production code
✔ Integrate smoothly with FastAPI

If you know these topics, you can confidently use Pydantic in real-world projects.
