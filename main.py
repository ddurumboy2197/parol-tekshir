def parolni_tekshir(parol):
    if len(parol) < 8:
        return False
    return True

parol = input("Parolni kiriting: ")
if parolni_tekshir(parol):
    print("Parol qabul qilindi.")
else:
    print("Parol kamida 8 ta belgidan iborat bo'lishi kerak.")
```

```python
def parolni_tekshir(parol):
    return len(parol) >= 8

parol = input("Parolni kiriting: ")
if parolni_tekshir(parol):
    print("Parol qabul qilindi.")
else:
    print("Parol kamida 8 ta belgidan iborat bo'lishi kerak.")
