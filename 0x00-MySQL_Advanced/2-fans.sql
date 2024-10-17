-- This script retrieves and ranks the origins of metal bands
-- based on the total number of fans from the imported 'metal_bands' table.

-- The result will include:
-- 1. origin: The country where the band is from.
-- 2. nb_fans: The total number of fans for bands originating from that country.

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
