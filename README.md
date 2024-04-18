# Role Policy Verifier
The Role Policy Verifier is a Python script designed to validate the format of AWS IAM (Identity and Access Management) role policies and verify the content of the "Resource" field in each "Statement", returning False if it's a single "*" and True otherwise.

# Installation
Requirements:

* python==3.11
* jsonschema==4.21.1

Installation:

1. Clone the Repository
   
    ```bash
   git clone https://github.com/AgnikAm/RolePolicyVerifier.git
    ```
    
2. Set Up Virtual Environment (Optional but Recommended)
   
    ```bash
    # Create a virtual environment named 'venv'
    python -m venv venv

    # Activate the virtual environment (Windows)
    venv\Scripts\activate

    # Activate the virtual environment (macOS/Linux)
    source venv/bin/activate
    ```

3. Install Dependencies
   
    ```bash
    pip install -r requirements.txt
    ```

How to run:
* Run the app
   
    ```bash
    #(Windows)
    python src/main.py <path to JSON>

    #(macOS/Linux)
    python3 src/main.py <path to JSON>
    ```

* Run format tests
   
    ```bash
    #(Windows)
    python src/test_format.py

    #(macOS/Linux)
    python3 src/test_format.py
    ```

* Run resource tests
   
    ```bash
    #(Windows)
    python src/test_resources.py

    #(macOS/Linux)
    python3 src/test_resources.py
    ```

# Features

* Method to validate JSON format - validate_iam_role_policy_format
* Method to verify if Resource contains single Asterisk - verify_asterisk_absence
* Unit tests for validating format and verifying resources
* Covering edge cases such as:
  
  * Invalid JSON format
  * Invalid PolicyName:
 
    * Length of name smaller than 1 or bigger than 128
    * Name does not meet the pattern [\w+=,.@-]+
  
  * Invalid PolicyDocument
  
    * No Version
    * No Statement
    * No Sid
    * No Effect
    * No Action
    * Null resource
  
  * Empty list in Resource (return True)
  * Multiple statements (return list of bools)

# Structure

  * src

    * file_input - provides function for loading JSON data from file
   
    * format_validation - provides functions to validate format of AWS IAM Role Policy like is_valid_policy_name, is_of_length, is_of_pattern, is_valid_policy_document and validate_iam_role_policy_format
  
    * resource_verification - provides function that checks each statement in policy document for the presence of single "*" in resource
  
    * main - entry point of application that contains logic for loading JSON file and performing verification
 
    * test_format - unit tests for format validation
    * test_resource - unit tests for resource verification

  * assets

    * schema - folder with PolicyDocument schema that I found here: https://gist.github.com/jstewmon/ee5d4b7ec0d8d60cbc303cb515272f8a
    * format test - folder with test JSON files containing valid and invalid formats
    * asterisk test - folder with test JSON files containing different versions of Statements and Resource content
