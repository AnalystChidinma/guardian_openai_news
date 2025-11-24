# Guardian API Extraction Project

## Project Overview 
This project demonstrates a complete workflow for extracting news articles from **The Guardian Open API**, handling pagination, cleaning the response, and exporting the data into a structured JSON file.  
Beyond the API extraction itself, the main objective of this project was to **practice Continuous Integration (CI)** to ensure that the code remains clean, consistent, and production-ready.
The script interacts with **The Guardian API** to retrieve articles based on a **OpenAI**.

***The main goal of this project is to Integrate CI workflows to enforce code quality before merging into `main***.

## Continuous Integration (CI) — My Main Focus

This project places heavy emphasis on **Continuous Integration**, an engineering practice that ensures all n code are tested and validated before reaching production.

### Why CI?

- Ensures code consistency  
- Prevents production-breaking commits  
- Enforces teamwork-friendly coding styles  
- Guarantees that all branches meet quality standards  
- Automates the review process using tools instead of people  

I implemented CI using **GitHub Actions**:

- I created a new branch 
-  made a Pull Request (PR) 
- The `main` branch receives an update  

Before merging, CI checks **must pass**.

The CI workflow includes:

**flake8** — Linting  
- flake8 checks for:

  * PEP 8 violations  
  * unused variables  
  * Syntax and indentation errors  
  * Complexity issues  

If flake8 fails, **the PR cannot be merged** : ensuring that all code entering the repository is clean and compliant.

 **isort** — Import Sorting  
- isort automatically organizes import statements to maintain:

* Readability  
* Consistency

Both tools run automatically inside the CI job.


To follow best practices, I:

1. Created a feature branch  
2. Wrote and updated code there  
3. Ensured that all CI checks passed (flake8 + isort)  
4. Opened a Pull Request to merge into **main**  
5. Only merged **after CI passed successfully**

This workflow simulates a real-world team environment where no direct pushes are done to **main**.

## What I Learned

### Through this project, I learned:

- How to integrate CI into a Python project

- How to automate code quality checks

- How to work with a branching strategy

- How to test and validate code like a real production workflow

- How CI helps teams maintain clean & scalable codebases

<img width="1048" height="535" alt="image" src="https://github.com/user-attachments/assets/b711bccb-3c91-42cf-ad99-953f551e0b3e" />












