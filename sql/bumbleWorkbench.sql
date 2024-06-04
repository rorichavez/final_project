-- Import dataset
USE bumble;
SELECT * 
FROM profiles;

-- Created a general view.
CREATE VIEW about AS
SELECT age, location, job, education 
FROM profiles;

SELECT * FROM about;

-- Created a view to see from which profile came and the gender.
CREATE VIEW genderProfiles AS
SELECT name, gender, profile
FROM profiles;

SELECT * FROM genderProfiles;

-- Created a view to see family plan according to gender.
CREATE VIEW familyPlans AS
SELECT intentions, childrens, gender
FROM profiles;

SELECT * FROM familyPlans;

-- Created a view to see idiology according to gender.
CREATE VIEW idiology AS
SELECT politics, religion, zodiacSign, gender
FROM profiles;

SELECT * FROM idiology;

-- Created a view to see lifestyle according to gender.
CREATE VIEW lifestyle AS
SELECT drinking, smoking, exercise, gender
FROM profiles;

SELECT * FROM lifestyle;



 
