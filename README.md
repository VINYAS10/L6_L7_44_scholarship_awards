
# Scholarship Awards – Lab 6

## Project Information

**Project:** Scholarship Awards  
**Lab:** Lab 6 – Code and Branch Coverage Analysis  
**Repository:** L6_L7_44_scholarship_awards

## About the Project

This project focuses on testing a Python scholarship awards application using pytest and the coverage.py tool.

The application contains three main functions:

- `award_amount()` – Calculates scholarship award amounts.
- `is_eligible()` – Checks applicant eligibility.
- `application_status()` – Determines application status.

## Tools Used

- Python 3.13
- pytest
- coverage.py
- Git and GitHub
- Visual Studio Code

## Installation

Install the required packages:

```bash
python -m pip install pytest coverage
```

## Running Tests

Run the code coverage tests:

```bash
python -m pytest -v Lab\ 6/CodeCoverageTest_44_application.py
```

Run the branch coverage tests:

```bash
python -m pytest -v Lab\ 6/BranchCoverageTest_44_application.py
```

## Coverage Results

| Coverage Type | Achieved | Required |
|---|---:|---:|
| Code Coverage | 100% | 90% |
| Branch Coverage | 100% | 90% |

### Code Coverage

- Total statements: 37
- Missed statements: 0
- Coverage achieved: 100%

### Branch Coverage

- Total statements: 37
- Missed statements: 0
- Total branches: 26
- Partial branches: 0
- Coverage achieved: 100%

## Project Structure

```text
L6_L7_44_scholarship_awards/
│
├── README.md
│
└── Lab 6/
    ├── README.md
    ├── scholarship_awards.py
    ├── test_scholarship_awards.py
    ├── CodeCoverageTest_44_application.py
    ├── BranchCoverageTest_44_application.py
    ├── CodeCoverage_44.png
    └── BranchCoverage_44.png
```

## Deliverables

1. Code coverage test cases.
2. Branch coverage test cases.
3. Code coverage terminal screenshot.
4. Branch coverage terminal screenshot.
5. Git commits for both coverage test files.

## Conclusion

The scholarship awards application achieved 100% code coverage and 100% branch coverage using pytest and coverage.py.

All required coverage targets were successfully achieved.
