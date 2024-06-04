-- Import dataset
USE bumble;

SELECT gender, COUNT(*) AS total
FROM profiles
GROUP BY gender
ORDER BY COUNT(*) DESC;

SELECT gender, profile, COUNT(*) AS total
FROM profiles
GROUP BY gender, profile
ORDER BY total DESC;

SELECT FLOOR(AVG(age)) AS ageAVG 
FROM profiles;

SELECT location
FROM profiles
GROUP BY location
ORDER BY COUNT(*) DESC
LIMIT 10;

SELECT job
FROM profiles
GROUP BY job
ORDER BY COUNT(*) DESC
LIMIT 10;
