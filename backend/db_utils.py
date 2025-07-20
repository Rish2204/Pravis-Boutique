#!/usr/bin/env python3
"""
Database utility functions for testing connections and running queries
"""
import os
import sys
from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql

# Load environment variables
load_dotenv()

def get_connection():
    """Get a database connection using environment variables"""
    try:
        # Try DATABASE_URL first
        database_url = os.getenv("DATABASE_URL")
        if database_url:
            return psycopg2.connect(database_url)
        
        # Otherwise use individual components
        return psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            database=os.getenv("DB_NAME", "marketing_analytics"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "")
        )
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def test_connection():
    """Test database connection"""
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT version();")
            version = cursor.fetchone()
            print(f"Successfully connected to PostgreSQL!")
            print(f"PostgreSQL version: {version[0]}")
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Error executing query: {e}")
            return False
    return False

def create_database(db_name):
    """Create a new database"""
    conn = get_connection()
    if conn:
        try:
            conn.autocommit = True
            cursor = conn.cursor()
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(
                sql.Identifier(db_name)
            ))
            print(f"Database '{db_name}' created successfully!")
            cursor.close()
            conn.close()
            return True
        except psycopg2.errors.DuplicateDatabase:
            print(f"Database '{db_name}' already exists.")
            return True
        except Exception as e:
            print(f"Error creating database: {e}")
            return False
    return False

if __name__ == "__main__":
    # Test the connection when script is run directly
    test_connection()
