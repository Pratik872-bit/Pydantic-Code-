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

Validate or transform a single field using decorators.

```python
@field_validator("email")
def check_company_email(cls, value):
    if not value.endswith("@hdfc.com"):
        raise ValueError("Invalid company email")
    return value
```

Can transform values too:

```python
@field_validator("name")
def uppercase_name(cls, v):
    return v.upper()
```

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
