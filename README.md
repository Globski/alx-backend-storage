# Alx Backend Storage - MySQL advanced

## Description

This repository contains a series of SQL scripts designed to demonstrate various database management tasks, including table creation, indexing, functions, views, and stored procedures. Each task builds on foundational SQL concepts to manipulate and retrieve data effectively.

## Project Structure

| Task Number | Description                                                                                     | Source Code Link                             |
|-------------|-------------------------------------------------------------------------------------------------|----------------------------------------------|
| 0           | Initialize Database                                                                           | [0-init.sql](0-init.sql)                   |
| 1           | Simple SELECT Queries                                                                          | [1-select.sql](1-select.sql)                |
| 2           | Filtering Results                                                                               | [2-filter.sql](2-filter.sql)                |
| 3           | Aggregate Functions                                                                             | [3-aggregate.sql](3-aggregate.sql)          |
| 4           | Grouping Data                                                                                  | [4-group.sql](4-group.sql)                  |
| 5           | Joining Tables                                                                                 | [5-join.sql](5-join.sql)                    |
| 6           | Subqueries                                                                                     | [6-subquery.sql](6-subquery.sql)            |
| 7           | Creating Views                                                                                 | [7-view.sql](7-view.sql)                    |
| 8           | Triggers                                                                                       | [8-trigger.sql](8-trigger.sql)              |
| 9           | Indexing                                                                                       | [9-index_name_score.sql](9-index_name_score.sql) |
| 10          | User-Defined Functions                                                                         | [10-div.sql](10-div.sql)                    |
| 11          | Views with Conditions                                                                          | [11-need_meeting.sql](11-need_meeting.sql)  |
| 12          | Stored Procedures for Weighted Scores                                                           | [100-average_weighted_score.sql](100-average_weighted_score.sql) |
| 13          | Compute Average Weighted Scores for All Users                                                 | [101-average_weighted_score.sql](101-average_weighted_score.sql) |

## Environment
- Ubuntu 18.04 LTS
- MySQL 5.7 (version 5.7.30)
- MySQL Workbench (optional for GUI)

## Requirements
- All your files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- The length of your files will be tested using wc
- Comments for your SQL file:
```sql
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

## Learning Objectives
By the end of this project, you should be able to:
- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL

## Prototypes Used in the Project

| Prototype Name                       | Description                                    |
|--------------------------------------|------------------------------------------------|
| ComputeAverageWeightedScoreForUser   | Computes and stores the average weighted score for a student. |
| ComputeAverageWeightedScoreForUsers  | Computes and stores the average weighted score for all students. |

## How to Use
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/<your-username>/alx-backend-storage.git
   cd alx-backend-storage/0x00-MySQL_Advanced
   ```
2. **MySQL Server**: Make sure you have MySQL installed on your computer. You can download it from [MySQL's official website](https://dev.mysql.com/downloads/mysql/).
3. **MySQL Client**: Use a MySQL client like MySQL Workbench or a terminal with MySQL command-line tools.

4. **Import the SQL Scripts:**
   Use the MySQL command line to execute the scripts, for example:
   ```bash
   mysql -uroot -p holberton < 0-init.sql
   ```

5. **Run Tests:**
   Each script can be tested sequentially to verify the results.

1. **Using Container-on-Demand:**
   - Request a container with Ubuntu 18.04 and Python 3.7.
   - Connect via SSH or WebTerminal.
   
2. **Start MySQL:**
   ```bash
   $ service mysql start
   ```

3. **Access MySQL:**
   ```bash
   $ mysql -uroot -p
   ```
   (Password is `root`)

4. **Import SQL Dump:**
   ```bash
   $ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
   $ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
   ```

- Each SQL script can be executed in a MySQL environment.
- Ensure you have the necessary permissions to create databases and tables.
- If you encounter errors, make sure your SQL syntax is correct and that the necessary tables and procedures have been created successfully.

- Check that you're using the correct database by executing:
  ```sql
  USE your_database_name;
  ```

## Additional Notes

- **Creating Tables with Constraints**: Use primary keys, foreign keys, and unique constraints.
- **Optimizing Queries with Indexes**: Show how to create indexes for faster data retrieval.
- **Stored Procedures and Functions**: Demonstrate how to create and call procedures/functions.
- **Views**: Create views for simplified data access.
- **Triggers**: Set up triggers for actions like insert, update, and delete.

## Tasks

### 0. Initialize Database
Write a SQL script that creates and populates the table `names`.

### 1. Simple SELECT Queries
Write a SQL script that retrieves all the records from the `names` table.

### 2. Filtering Results
Write a SQL script that retrieves all the records from the `names` table where the score is greater than 50.

### 3. Aggregate Functions
Write a SQL script that retrieves the total number of names in the `names` table.

### 4. Grouping Data
Write a SQL script that retrieves the count of names grouped by their score.

### 5. Joining Tables
Write a SQL script that retrieves names and their corresponding scores from two different tables.

### 6. Subqueries
Write a SQL script that retrieves names that have a score higher than the average score.

### 7. Creating Views
Write a SQL script that creates a view that lists the names with scores above 80.

### 8. Triggers
Write a SQL script that creates a trigger to automatically update a field when certain conditions are met.

### 9. Indexing
Write a SQL script that creates an index `idx_name_first_score` on the table `names` and the first letter of name and the score.

### 10. User-Defined Functions
Write a SQL script that creates a function `SafeDiv` that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

### 11. Views with Conditions
Write a SQL script that creates a view `need_meeting` that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.

### 12. Stored Procedures for Weighted Scores
Write a SQL script that creates a stored procedure `ComputeAverageWeightedScoreForUser` that computes and store the average weighted score for a student.

### 13. Compute Average Weighted Scores for All Users
Write a SQL script that creates a stored procedure `ComputeAverageWeightedScoreForUsers` that computes and store the average weighted score for all students.
