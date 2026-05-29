**Python (Pytest)**
```python
import pytest

def parol_uzunligini_tekshir(parol):
    return len(parol) >= 8

@pytest.mark.parametrize("parol, natija", [
    ("1234567", False),
    ("12345678", True),
    ("123456789", True),
    ("1234567a", True),
    ("1234567A", True),
    ("1234567!", True),
    ("1234567@", True),
    ("1234567#", True),
    ("1234567$", True),
])
def test_parol_uzunligini_tekshir(parol, natija):
    assert parol_uzunligini_tekshir(parol) == natija
```

**JavaScript (Jest)**
```javascript
describe('parol_uzunligini_tekshir', () => {
    it('8 ta belgidan kam bo\'lgan parolni qaytaradi false', () => {
        expect(parol_uzunligini_tekshir('1234567')).toBe(false);
    });

    it('8 ta belgidan ko\'proq bo\'lgan parolni qaytaradi true', () => {
        expect(parol_uzunligini_tekshir('12345678')).toBe(true);
    });

    it('8 ta belgidan ko\'proq bo\'lgan parolni qaytaradi true (katta harf)', () => {
        expect(parol_uzunligini_tekshir('1234567A')).toBe(true);
    });

    it('8 ta belgidan ko\'proq bo\'lgan parolni qaytaradi true (harf va belgi)', () => {
        expect(parol_uzunligini_tekshir('1234567!')).toBe(true);
    });

    function parol_uzunligini_tekshir(parol) {
        return parol.length >= 8;
    }
});
```
