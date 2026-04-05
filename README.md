# CSE 5324 - Assignment 5: Task Management API Testing
**Author:** Mikhael Prashant Uzagare (1002273528)  
**Instructor:** Dr. Elizabeth Diaz

## Project Overview
This repository contains a RESTful Task Management API built with Flask and SQLAlchemy, featuring a comprehensive multi-tiered testing suite. [cite_start]The primary focus of this project is to demonstrate professional software testing practices, including Unit, Integration, and System testing [cite: 11-12, 63].

## Features
- [cite_start]**User Authentication:** Secure registration and login using JWT tokens and password hashing [cite: 16, 35-39].
- [cite_start]**Task Management:** Full CRUD operations for managing user tasks [cite: 18, 41-43].
- [cite_start]**Input Validation:** Robust sanitization and regex-based validation for emails and passwords [cite: 19, 50-54].
- [cite_start]**CI/CD Integration:** Automated testing via GitHub Actions [cite: 83-84, 156-159].

## Testing Suite
[cite_start]The project utilizes `pytest` to verify 10 distinct test scenarios[cite: 82, 128, 142]:
- [cite_start]**Unit Tests:** Isolated logic checks for models and utility functions [cite: 64-68, 148-151].
- [cite_start]**Integration Tests:** Verifying route communication with the SQLite database [cite: 69-75, 152-153].
- [cite_start]**System Tests:** End-to-end user lifecycle simulation [cite: 76-79, 154-155].

### Running Tests Locally
1. Initialize virtual environment: `python -m venv venv`
2. Install dependencies: `pip install -r requirements.txt`
3. Run all tests: `pytest tests/`
4. [cite_start]Generate coverage report: `pytest --cov=app tests/` [cite: 104, 197-199]

## Results
- [cite_start]**Total Tests:** 10 Passed (100% Pass Rate) [cite: 128, 194]
- [cite_start]**Code Coverage:** 90% [cite: 104, 130, 236]
- [cite_start]**CI/CD Status:** Passing (GitHub Actions) [cite: 131, 191]
