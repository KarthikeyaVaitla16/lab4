# This program prints Hello, world!

print('Hello, world!')
trigger:
- main

pool:
  vmImage: ubuntu-latest
strategy:
  matrix:
    Python27:
      python.version: '2.7'
    Python35:
      python.version: '3.5'
    Python36:
      python.version: '3.6'
    Python37:
      python.version: '3.7'

steps:
- task: UsePythonVersion@0
  inputs:
    versionSpec: '$(python.version)'
  displayName: 'Use Python $(python.version)'

- script: | python "helloworld.py"
    python -m pip install --upgrade pip
    pip install -r requirements.txt
  displayName: 'Install dependencies'

- script: |helloworld.py
    pip install pytest pytest-azurepipelines
    pytest
  displayName: 'pytest'
