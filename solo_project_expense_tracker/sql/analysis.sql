SELECT category, SUM(amount)
FROM 
    expenses
WHERE amount > 300
GROUP BY category;


-- challenge 14
SELECT category, SUM(amount) as total_amount
FROM expenses
GROUP BY category
HAVING SUM(amount) > 400;


-- challenge 15
SELECT category, SUM(amount) as total_amount
FROM expenses
GROUP BY category
HAVING total_amount > 400
ORDER BY total_amount DESC;


-- challenge 16
SELECT category, amount,
    CASE 
        WHEN amount >= 800 THEN 'High'
        WHEN amount >= 400 THEN 'Medium'
        ELSE 'Low'
    END AS spending_level
FROM expenses
ORDER BY amount DESC;


-- challenge 17
SELECT
    CASE
        WHEN amount >= 800 THEN 'High'
        WHEN amount >= 400 THEN 'Medium'
        ELSE 'Low'
    END AS spending_level,

    SUM(amount) AS total_spending

FROM expenses

GROUP BY spending_level
ORDER BY total_spending DESC;



-- challenge 18
SELECT
    CASE
        WHEN amount >= 800 THEN 'High'
        WHEN amount >= 400 THEN 'Medium'
        ELSE 'Low'
    END AS spending_level,
    COUNT(*) as expense_count,
    SUM(amount) AS total_spending

FROM expenses

GROUP BY spending_level
ORDER BY total_spending DESC;



--challenge 19
SELECT
    category,
    COUNT(*) as expense_count,
    SUM(amount) AS total_spending,
    AVG(amount) as avg_spending

FROM expenses

GROUP BY category
ORDER BY total_spending DESC;



-- Challenge #20 — Filter the Aggregated Results
-- Expected result:

-- category    expense_count    total_spending    avg_spending
-- bills       1                1000              1000
-- food        1                 500               500
-- savings     1                 500               500
-- transpo     1                 500               500


SELECT
    category,
    COUNT(*) as expense_count,
    SUM(amount) AS total_spending,
    AVG(amount) as avg_spending

FROM expenses

GROUP BY category
HAVING avg_spending > 400
ORDER BY total_spending DESC;


-- Challenge #21 — Now let's make it actually interesting
SELECT 
    category,
    COUNT(*) as expense_count,
    SUM(amount) as total_spending,
    AVG(amount) as avg_spending
FROM expenses
GROUP BY category
HAVING expense_count >= 2 AND total_spending > 500
ORDER BY avg_spending DESC;





--Challenge #22 Using your date column, find:total spending per month
SELECT 
     STRFTIME(date, '%B') AS month,
     SUM(amount) as total_spending
FROM expenses
GROUP BY month, EXTRACT(MONTH FROM date)
ORDER BY EXTRACT(MONTH FROM date);


-- challenge 23 add year
SELECT 
     STRFTIME(date, '%B %Y') AS month,
     SUM(amount) AS total_spending
FROM expenses
GROUP BY  month, EXTRACT(YEAR FROM date), EXTRACT(MONTH FROM date)
ORDER BY EXTRACT(YEAR FROM date), EXTRACT(MONTH FROM date);




-- Next SQL Challenge — Date Filtering

SELECT 
     STRFTIME(date, '%B %Y') AS month,
     SUM(amount) AS total_spending
FROM expenses
WHERE EXTRACT(YEAR FROM date) = 2026 AND EXTRACT(MONTH FROM date) = 10
GROUP BY  month, EXTRACT(YEAR FROM date), EXTRACT(MONTH FROM date)
ORDER BY EXTRACT(YEAR FROM date), EXTRACT(MONTH FROM date);



-- Tiny challenge Modify your query so it returns:

SELECT date, category, amount
from expenses
WHERE EXTRACT(YEAR FROM date) = 2026 AND EXTRACT(MONTH FROM date) = 10;





--- Next Challenge: Date Range
SELECT date, category, amount
from expenses
WHERE date >= '2026-09-10'
  AND date <= '2026-09-15'; 


-- challenge between
SELECT date, category, amount
from expenses
WHERE date BETWEEN '2026-09-10' AND '2026-09-15'; 



-- challenge Next Challenge — Combining Filters

SELECT date, category, amount
from expenses
WHERE date BETWEEN '2026-09-10' AND '2026-09-15' AND amount >= 400; 



-- Next challenge: OR

SELECT date, category, amount
from expenses
WHERE category = 'food ' or amount >= 800; 




-- Challenge #27 Show expenses where the category is food OR transpo, AND the amount is at least ₱400.

SELECT date, category, amount 
FROM 
    expenses
WHERE (category = 'food ' OR category = 'transpo') AND amount >= 400;

-- Next challenge: IN
SELECT date, category, amount 
FROM expenses
WHERE category IN ('food', 'transpo') AND amount >= 400;

SELECT date, category, amount
FROM expenses
WHERE TRIM(category) IN ('food', 'transpo')
  AND amount >= 400;


-- 🚀 Next challenge: NULL
SELECT date, category, amount
FROM expenses
WHERE category IS NOT NULL;



-- 🎯 Your actual Challenge #29

SELECT * 
FROM expenses
WHERE category is NULL OR description is NULL OR amount is NULL OR date is NULL;




-- 🚀 Challenge #30 — Find dirty text data
SELECT category
FROM expenses
WHERE category != TRIM(category);


-- 🚀 Challenge #31 — Make the result more useful
SELECT 
category AS original_category, 
TRIM(category) AS cleaned_category
FROM expenses
WHERE category != TRIM(category);


--🚀 Challenge #32 — Actually clean the data
SELECT category
FROM expenses
WHERE category != TRIM(category);

-- 🚀 Challenge #33 — DISTINCT

SELECT DISTINCT category from expenses;



-- 🚀 Challenge #34 — LIKE
SELECT * 
FROM expenses
WHERE description LIKE '%trans%';



-- 🚀 Challenge #35 — LIKE + OR

SELECT * FROM expenses
WHERE (description LIKE '%trans%') OR (description LIKE '%bill%');


-- 🚀 Challenge #36 — NOT LIKE
SELECT * 
FROM expenses
WHERE description NOT LIKE '%trans%';


-- 🚀 Challenge #37 — NOT IN

SELECT 
    date, category, amount
FROM 
    expenses
WHERE category NOT IN ('food', 'bills', 'load');


-- 🚀 Challenge #38 — Category normalization

SELECT 
    CASE
        WHEN category = 'transpo' THEN 'Transportation'
        ELSE category 
    END as normalized_category
 
FROM expenses


-- 🚀 Challenge #39 — Aggregate the normalized categories


SELECT
    CASE
        WHEN category = 'transpo' THEN 'Transportation'
        ELSE category
    END AS normalized_category,
    SUM(amount) AS total_spending
FROM expenses
GROUP BY
    CASE
        WHEN category = 'transpo' THEN 'Transportation'
        ELSE category
    END
ORDER BY total_spending DESC;





-- 🚀 Challenge #40 — Make the query cleaner

WITH cleaned_expenses AS (
    SELECT
        CASE
            WHEN category = 'transpo' THEN 'Transportation'
            ELSE category
        END AS normalized_category,
        amount
    FROM expenses
)

SELECT
    normalized_category,
    SUM(amount) AS total_spending
FROM cleaned_expenses
GROUP BY normalized_category
ORDER BY total_spending DESC;



