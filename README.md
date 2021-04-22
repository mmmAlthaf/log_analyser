# Log Analyser

Start the script including the log file you want to analyse 

```python3 analyser.py "testFile.log"```

You will come to this menu. Select an option via the number

What analysis do you want?
1) Action
2) LANG SERVER
3) Error Logs
4) Every action after USER LOGIN
5) All Actions till Error
6) Readable format

1 - Only the logs of only the actions made by the user. Such as (API_LIST_FETCH_START, APP_TERMINATE_SUCCESS, etc) will be saved in the output.log file
2 - Only the payloads of the LANG CLIENT will be saved in the output.log file
3 - Only the Error logs will be saved in the output.log file
4 - Every Action since the user first logged in will be saved in the output.log file
5 - All actions made by the user till the first error faced
6 - This format will contain the Actions, Lang client messages, Errors and Interventions. 

