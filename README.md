# Обчислення визначеного інтеграла методом Монте-Карло

## Завдання

- Реалізувати чисельне обчислення визначеного інтеграла функції \( f(x) = x^2 \) на проміжку \([0, 2]\) за допомогою методу Монте-Карло.
- Порівняти результат із аналітичним обчисленням, виконаним через функцію `quad` з бібліотеки `scipy.integrate`.
- Побудувати візуалізацію з поясненням обчислень.

---

## Метод Монте-Карло


1. Генерується велика кількість випадкових точок (x, y) у прямокутнику, який обмежує область під кривою функції:
   - x випадково обирається в діапазоні від a до b,
   - y випадково обирається від 0 до f(b) (максимум функції на цьому проміжку).

2. Визначається, яка частина цих точок лежить під кривою, тобто y <= f(x).

3. Обчислюється частка точок, що потрапили під графік: кількість таких точок ділиться на загальну кількість точок (N).

4. Результат множиться на площу прямокутника:
   Площа ≈ (b - a) * f(b) * (кількість точок під графіком / N)

5. Таким чином отримується наближене значення визначеного інтеграла.
---

## Результати

| Метод              | Результат   |
|--------------------|-------------|
| Аналітичний (`quad`)| ≈ 2.6667    |
| Монте-Карло (N=10000)| ≈ 2.6448     |

*Результати можуть трохи відрізнятись при кожному запуску через випадковість.*

---

## Графік
![Графік інтегрування](monte-carlo.jpg)

---

## Висновок

Метод Монте-Карло дає оцінку площі під кривою на основі випадкових точок. Для великої кількості точок точність достатньо висока.  
В результаті, значення, отримане за допомогою методу Монте-Карло, **наближене до точного аналітичного результату**, що свідчить про правильність реалізації.

