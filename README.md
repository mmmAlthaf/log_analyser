# Log Analyser

Start the script including the log file you want to analyse 

```python3 analyser.py "testFile.log"```

A menu will be shown asking for which filter you need. Select an option via the number


1) **Action** - Only the logs of only the actions made by the user. Such as (API_LIST_FETCH_START, APP_TERMINATE_SUCCESS, etc) will be saved in the output.log file
2) **LANG SERVER** - Only the payloads of the LANG CLIENT will be saved in the output.log file
3) **Error Logs** - Only the Error logs will be saved in the output.log file
4) **Every action after USER LOGIN** - Every Action since the user first logged in will be saved in the output.log file
5) **All Actions till Error** - All actions made by the user till the first error faced
6) **Readable Format** - This format will contain the Actions, Lang client messages, Errors and Interventions. 

