---🚀 Challenge #41 — CTE + filtering 
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
HAVING total_spending >= 500
ORDER BY total_spending DESC;


-- 🚀 Challenge #42 — CTE + multiple aggregates
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
    COUNT(*) as expense_count,
    SUM(amount) AS total_spending,
    AVG(amount) AS avg_spending
FROM cleaned_expenses
GROUP BY normalized_category
HAVING total_spending >= 500 AND expense_count >= 1
ORDER BY total_spending DESC;



-- 🚀 Challenge #43 — CTE + percentage
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
    SUM(amount) AS total_spending,
    ROUND(SUM(amount) * 100.0 / SUM(SUM(amount)) OVER (), 2) as percentage_of_total
FROM cleaned_expenses
GROUP BY normalized_category
HAVING total_spending >= 500 
ORDER BY total_spending DESC;





-- 🚀 Challenge #44 — Percentage of the ORIGINAL total
WITH cleaned_expenses AS (
    SELECT
        CASE
            WHEN category = 'transpo' THEN 'Transportation'
            ELSE category
        END AS normalized_category,
        amount
    FROM expenses
),

category_totals AS (
    SELECT 
        normalized_category,
        SUM(amount) as total_spending,
        SUM(SUM(amount)) OVER () as grand_total
    FROM cleaned_expenses
    GROUP BY normalized_category
)

SELECT
    normalized_category,
    total_spending,
    CONCAT(ROUND(total_spending * 100.0 / grand_total, 2),'%')as percentage_of_total
FROM category_totals
ORDER BY total_spending DESC;




-- 🚀 Challenge #45 — Window Function Ranking
WITH cleaned_expenses AS (
    SELECT
        CASE
            WHEN category = 'transpo' THEN 'Transportation'
            ELSE category
        END AS normalized_category,
        amount
    FROM expenses
),

category_totals AS (
    SELECT 
        normalized_category,
        SUM(amount) as total_spending,
        SUM(SUM(amount)) OVER () as grand_total
    FROM cleaned_expenses
    GROUP BY normalized_category
)

SELECT
    normalized_category,
    total_spending,
    RANK() OVER (ORDER BY total_spending DESC) AS rank
FROM category_totals
ORDER BY total_spending DESC;



-- 🚀 Challenge #46 — Ranking + percentage together
WITH cleaned_expenses AS (
    SELECT
        CASE
            WHEN category = 'transpo' THEN 'Transportation'
            ELSE category
        END AS normalized_category,
        amount
    FROM expenses
),

category_totals AS (
    SELECT 
        normalized_category,
        SUM(amount) as total_spending,
        SUM(SUM(amount)) OVER () as grand_total
    FROM cleaned_expenses
    GROUP BY normalized_category
)

SELECT
    normalized_category,
    total_spending,
    CONCAT(ROUND(total_spending * 100.0 / grand_total, 2),'%')as percentage_of_total,
    RANK() OVER (ORDER BY total_spending DESC) AS rank
FROM category_totals
ORDER BY total_spending DESC;



-- 🚀 Challenge #47 — ROW_NUMBER() vs RANK()
WITH cleaned_expenses AS (
    SELECT
        CASE
            WHEN category = 'transpo' THEN 'Transportation'
            ELSE category
        END AS normalized_category,
        amount
    FROM expenses
),

category_totals AS (
    SELECT 
        normalized_category,
        SUM(amount) as total_spending,
        SUM(SUM(amount)) OVER () as grand_total
    FROM cleaned_expenses
    GROUP BY normalized_category
)

SELECT
    normalized_category,
    total_spending,
    ROW_NUMBER() OVER (ORDER BY total_spending DESC) AS rank
FROM category_totals
ORDER BY total_spending DESC;


-- 🚀 Challenge #48 — Make the ranking deterministic

WITH cleaned_expenses AS (
    SELECT
        CASE
            WHEN category = 'transpo' THEN 'Transportation'
            ELSE category
        END AS normalized_category,
        amount
    FROM expenses
),

category_totals AS (
    SELECT 
        normalized_category,
        SUM(amount) as total_spending,
        SUM(SUM(amount)) OVER () as grand_total
    FROM cleaned_expenses
    GROUP BY normalized_category
)

SELECT
    normalized_category,
    total_spending,
    ROW_NUMBER() OVER (ORDER BY total_spending DESC, normalized_category ASC) as rank
FROM category_totals
ORDER BY total_spending DESC;




-- 🚀 Challenge #49 — RANK() vs DENSE_RANK()
WITH cleaned_expenses AS (
    SELECT
        CASE
            WHEN category = 'transpo' THEN 'Transportation'
            ELSE category
        END AS normalized_category,
        amount
    FROM expenses
),

category_totals AS (
    SELECT 
        normalized_category,
        SUM(amount) as total_spending,
        SUM(SUM(amount)) OVER () as grand_total
    FROM cleaned_expenses
    GROUP BY normalized_category
)

SELECT
    normalized_category,
    total_spending,
    DENSE_RANK() OVER (ORDER BY total_spending DESC, normalized_category ASC) as rank
FROM category_totals
ORDER BY total_spending DESC;





-- 🚀 Challenge #50

WITH cleaned_expenses AS (
    SELECT
        CASE
            WHEN category = 'transpo' THEN 'Transportation'
            ELSE category
        END AS normalized_category,
        amount
    FROM expenses
),

category_totals AS (
    SELECT 
        normalized_category,
        SUM(amount) as total_spending,
        SUM(SUM(amount)) OVER () as grand_total
    FROM cleaned_expenses
    GROUP BY normalized_category
)

SELECT
    normalized_category,
    total_spending,

    RANK() OVER (
        ORDER BY total_spending DESC
    ) AS rank,

    ROW_NUMBER() OVER (
        ORDER BY total_spending DESC
    ) AS row_number,

    DENSE_RANK() OVER (
        ORDER BY total_spending DESC
    ) AS dense_rank

FROM category_totals

ORDER BY total_spending DESC, normalized_category ASC;