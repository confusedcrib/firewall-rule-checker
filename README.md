# firewall-rule-checker
Checks AWS FMS for excluded rules

This Python script iterates through AWS Firewall Manager Security Policies and looks for any overridden individual rules within managed rule groups that may be turned off.

## Installation

1. Make sure you're authenticated into whatever account you orchestrate AWS Firewall Manager from

2. `pip install boto3`

3. `python3 excludedrulecheck.py`