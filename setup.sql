-- setup.sql

CREATE DATABASE StudentDB;
USE StudentDB;

CREATE TABLE Students (
    name VARCHAR(100),
    age INT,
    email VARCHAR(100),
    gender VARCHAR(10),
    student_id INT PRIMARY KEY,
    class INT
);
