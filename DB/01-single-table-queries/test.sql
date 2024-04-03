CREATE TABLE examples (
    ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL
);

PRAGMA table_info('examples');

ALTER TABLE examples
ADD COLUMN
Country VARCHAR(100) NOT NULL DEFAULT 'default value';

ALTER TABLE examples
ADD COLUMN
Age INTEGER NOT NULL DEFAULT 0;

PRAGMA table_info('examples');

ALTER TABLE examples
ADD COLUMN
Address VARCHAR(100) NOT NULL DEFAULT 'default value';

ALTER TABLE 
examples
RENAME COLUMN Address to 