-- This script retrieves and ranks bands whose main style is Glam rock
-- based on their longevity, calculated until the year 2022.

-- The result will include:
-- 1. band_name: The name of the band.
-- 2. lifespan: The number of years the band has been active until 2022.

SET @current_year = 2022;

SELECT band_name,
       (@current_year - IFNULL(formed, @current_year)) AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
ORDER BY lifespan DESC;
