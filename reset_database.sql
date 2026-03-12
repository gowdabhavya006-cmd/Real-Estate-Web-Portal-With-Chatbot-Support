-- Reset Database Script
-- Run this in MySQL to drop and recreate tables

USE real_estate_portal;

-- Drop tables in correct order (respecting foreign keys)
DROP TABLE IF EXISTS contacts;
DROP TABLE IF EXISTS properties;
DROP TABLE IF EXISTS users;

-- Note: After running this SQL script, run: python init_db.py
-- Or restart your Flask app which will create tables automatically

