/*
Задание №1: Уникальные страны клиентов
Определите, сколько уникальных стран представлено среди клиентов.
Подсказка: Используйте функцию COUNT(DISTINCT ...) для подсчета уникальных
значений
*/

SELECT COUNT(DISTINCT City) AS 'unique_countries' 
FROM Customers c; 


/*
Задание №2: Клиенты из Бразилии
Определите количество клиентов, которые проживают в Бразилии.
Подсказка: Используйте условие WHERE для фильтрации клиентов по стране.
*/

SELECT COUNT(*) AS 'Brazil_customers' 
FROM Customers c 
WHERE Country = 'Brazil';


/*
Задание №3: Средняя цена и количество товаров в категории 5
Посчитайте среднюю цену и общее количество товаров в категории с
идентификатором 5.
Подсказка: Используйте функции AVG и COUNT для получения нужной информации,
примените фильтр по CategoryID.
*/

SELECT 
	AVG(Price) as mean_pirce,
	COUNT(*) AS total_product
FROM Products
WHERE CategoryID = 5;


/*
Задание №4: Средний возраст сотрудников на 2024-01-01
Вычислите средний возраст сотрудников на дату 2024-01-01.
Подсказка: Используйте функцию JULIANDAY для расчета возраста сотрудников и AVG
для получения среднего значения.
*/

SELECT AVG(AGE) AS AverageAge
FROM (
	SELECT (JULIANDAY('2024-01-01') - JULIANDAY(BirthDate))/365 AS AGE 
	FROM Employees 
) AS AgeTable;


/*
Задание №5: Заказы в период 30 дней до 2024-02-15
Найдите заказы, сделанные в период с 16 января по 15 февраля 2024 года, и
отсортируйте их по дате заказа.
Подсказка: Используйте оператор BETWEEN для определения диапазона дат.
*/

SELECT *
FROM Orders
WHERE OrderDate
BETWEEN '2024-01-16' AND '2024-02-13'
ORDER BY OrderDate ;


/*
Задание №6: Количество заказов за ноябрь 2023 года (используя
начальную и конечную дату)
Определите количество заказов, сделанных в ноябре 2023 года, используя
начальную и конечную дату месяца.
Подсказка: Укажите точные даты начала и конца месяца в условии WHERE.
 */

SELECT COUNT(*)
FROM Orders o 
WHERE OrderDate 
BETWEEN '2023-11-01' AND '2023-11-30';


/*
Задание №7: Количество заказов за январь 2024 года (используя LIKE)
Найдите количество заказов за январь 2024 года, используя оператор LIKE для
фильтрации даты.
Подсказка: Преобразуйте дату в текстовый формат и используйте шаблон LIKE для
поиска по месяцу.
*/

SELECT  COUNT(*) AS count_orders
FROM Orders
WHERE OrderDate LIKE '2024-01-%';


/*
Задание №8: Количество заказов за 2024 год
Определите количество заказов за 2024 года, используя функцию STRFTIME для
извлечения года.
Примечание: STRFTIME — это функция в SQLite, используемая для форматирования
даты и времени. Она позволяет извлекать части даты и времени в нужном формате.
 */

SELECT COUNT(*) AS count_orders
FROM Orders
WHERE STRFTIME('%Y', OrderDate) == '2024'