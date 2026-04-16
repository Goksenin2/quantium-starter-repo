#!/bin/bash

echo "1. Activating virtual environment..."
source venv/bin/activate

echo "2. Running the test suite..."
pytest test_app.py

# Capture the exit code (the grade) from the test robot
TEST_RESULT=$?

# 3. Check the grade and return 0 (Pass) or 1 (Fail)
if [ $TEST_RESULT -eq 0 ]; then
  echo "Success! All tests passed. Returning exit code 0."
  exit 0
else
  echo "Error! Tests failed. Returning exit code 1."
  exit 1
fi
