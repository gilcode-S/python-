-- 🚀 Challenge #51 — PARTITION BY

WITH cleaned_expenses AS (
    SELECT
        CASE
            WHEN category = 'transpo' THEN 'Transportation'
            ELSE category
        END AS normalized_category,
        amount,
        EXTRACT(YEAR FROM date) AS year,
        EXTRACT(MONTH FROM date) AS month_num,
        STRFTIME(date, '%B %Y') AS month
    FROM expenses
),

monthly_category_totals AS (
    SELECT
        year,
        month_num,
        month,
        normalized_category,
        SUM(amount) AS total_spending
    FROM cleaned_expenses
    GROUP BY year, month_num, month, normalized_category
)

SELECT
    month,
    normalized_category,
    total_spending,
    RANK() OVER (
        PARTITION BY year, month_num
        ORDER BY total_spending DESC
    ) AS rank
FROM monthly_category_totals
ORDER BY year, month_num, rank;


-- 🚀 Challenge #52 — Find the top category per month

WITH cleaned_expenses AS (
    SELECT
        CASE
            WHEN category = 'transpo' THEN 'Transportation'
            ELSE category
        END AS normalized_category,
        amount,
        EXTRACT(YEAR FROM date) AS year,
        EXTRACT(MONTH FROM date) AS month_num,
        STRFTIME(date, '%B %Y') AS month
    FROM expenses
),

monthly_category_totals AS (
    SELECT
        year,
        month_num,
        month,
        normalized_category,
        SUM(amount) AS total_spending
    FROM cleaned_expenses
    GROUP BY year, month_num, month, normalized_category
),

ranked_monthly as (
    SELECT 
        month,
        normalized_category,
        total_spending,
        RANK() OVER (
                PARTITION BY year, month_num  
                ORDER BY total_spending DESC
                ) as rank
    FROM monthly_category_totals
)

SELECT
    month,
    normalized_category,
    total_spending,
    rank
FROM ranked_monthly
WHERE rank = 1
ORDER BY month;



--- 🚀 Challenge #53 — Top 2 categories per month

WITH cleaned_expenses AS (
    SELECT
        CASE
            WHEN category = 'transpo' THEN 'Transportation'
            ELSE category
        END AS normalized_category,
        amount,
        EXTRACT(YEAR FROM date) AS year,
        EXTRACT(MONTH FROM date) AS month_num,
        STRFTIME(date, '%B %Y') AS month
    FROM expenses
),

monthly_category_totals AS (
    SELECT
        year,
        month_num,
        month,
        normalized_category,
        SUM(amount) AS total_spending
    FROM cleaned_expenses
    GROUP BY year, month_num, month, normalized_category
),

ranked_monthly as (
    SELECT 
        month,
        normalized_category,
        total_spending,
        RANK() OVER (
                PARTITION BY year, month_num  
                ORDER BY total_spending DESC
                ) as rank
    FROM monthly_category_totals
)

SELECT
    month,
    normalized_category,
    total_spending,
    rank
FROM ranked_monthly
WHERE rank = 1 OR rank = 2
ORDER BY month;




-- 🚀 Challenge #54 — Top 2 with ties

WITH cleaned_expenses AS (
    SELECT
        CASE
            WHEN category = 'transpo' THEN 'Transportation'
            ELSE category
        END AS normalized_category,
        amount,
        EXTRACT(YEAR FROM date) AS year,
        EXTRACT(MONTH FROM date) AS month_num,
        STRFTIME(date, '%B %Y') AS month
    FROM expenses
),

monthly_category_totals AS (
    SELECT
        year,
        month_num,
        month,
        normalized_category,
        SUM(amount) AS total_spending
    FROM cleaned_expenses
    GROUP BY year, month_num, month, normalized_category
),

ranked_monthly as (
    SELECT 
        month,
        normalized_category,
        total_spending,
        RANK() OVER (
                PARTITION BY year, month_num  
                ORDER BY total_spending DESC
                ) as rank
    FROM monthly_category_totals
)

SELECT
    month,
    normalized_category,
    total_spending,
    rank
FROM ranked_monthly
WHERE rank <= 2
ORDER BY month;



---🚀 Challenge #55 — ROW_NUMBER() for exactly Top 2
WITH cleaned_expenses AS (
    SELECT
        CASE
            WHEN category = 'transpo' THEN 'Transportation'
            ELSE category
        END AS normalized_category,
        amount,
        EXTRACT(YEAR FROM date) AS year,
        EXTRACT(MONTH FROM date) AS month_num,
        STRFTIME(date, '%B %Y') AS month
    FROM expenses
),

monthly_category_totals AS (
    SELECT
        year,
        month_num,
        month,
        normalized_category,
        SUM(amount) AS total_spending
    FROM cleaned_expenses
    GROUP BY year, month_num, month, normalized_category
),

ranked_monthly as (
    SELECT 
        month,
        normalized_category,
        total_spending,
        ROW_NUMBER() OVER (
                PARTITION BY year, month_num  
                ORDER BY total_spending DESC
                ) as rank
    FROM monthly_category_totals
)

SELECT
    month,
    normalized_category,
    total_spending,
    rank
FROM ranked_monthly
WHERE rank <= 2
ORDER BY month;



-- 🚀 Challenge #56 — Running total
