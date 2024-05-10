# streaming-02-multiple-processes
Name: Jake Rood

Date: 05-10-2024

> Multiple processes accessing a shared resource concurrently

## Overview

In this project:

1. You'll review how one multiprocessing example behaves when tasks are quick and sharing goes well (generally).
1. You'll change to using longer-running concurrent tasks and explore what happens.
1. You'll implement a scaffolded process that streams from a csv file. 
1. You'll write your own streaming process that reads from a unique csv data source of your choice.

## Prerequisites

1. Git
1. Python 3.7+ (3.11+ preferred)
1. VS Code Editor
1. VS Code Extension: Python (by Microsoft)

## Set Up Repository
Perform the following tasks to correctly set up your repository:

### Fork 

Fork this [repository](https://github.com/denisecase/streaming-02-multiple-processes) ("repo") into **your own** GitHub account. 

### Clone

Clone **your** new GitHub repo down to the Documents folder on your local machine. 

### Execute About Script

Execute about.py to generate information about your local machine and Python setup.

```shell
python3 about.py
```

The resulting information should write to about.txt

### Execute Check Script

Execute 00_check_core.py to generate useful information.

```shell
python3 00_check_core.py
```

The resulting information should write to 00_report_core.txt

## Task 1. Execute Multiple Processes Project Script (quick processes)

Open the multiple_processes.py file.

Set TASK_DURATION_SECONDS to 0.

Execute multiple_processes.py.

```shell
python3 multiple_processes.py
```

Use out0.txt to document the results after running the script.
Paste all of the terminal contents into the output file.

Use the following hotkeys to select all, copy, and paste:

- Command a
- Command c
- Command v

## Task 2. Execute Multiple Processes Script with Longer Tasks

For the second run, modify the task duration to make each task take 3 seconds.

First, clear the terminal in the terminal window by typing clear and hitting return.

`clear`

Set TASK_DURATION_SECONDS to 3.

Run the script again.

```shell
python3 multiple_processes.py
```

Use out3.txt to document the results after running the script.
Paste all of the terminal contents into the output file.

## Task 3. Stream Processing Example

Simulate a stream processing example.

Copy process_streaming_0.py from the [Module 1 repository](https://github.com/jakerood/streaming-01-getting-started).

Copy the batchfile_0_farenheit.csv file from the same repository.

Run the script.

```shell
python3 process_streaming_0.py
```

The streaming process will run continuously for quite a while. Use CTRL-c to stop the process.

## Task 4. Custom Stream from CSV Script

Stream your own unique CSV data by modifying the example approach provided.

Create a new Python script in the repository called process_streaming_jakerood.py (Replace "jakerood" with your own name).

Create a new CSV file in the repository. In this case, we will use the CSV file provided in the [Microsoft Corporation Stock Price Dataset](https://www.kaggle.com/datasets/olegshpagin/microsoft-corporation-stock-price-dataset?select=H1)

Stream from the CSV file into a new file named out9.txt

Execute the script to perform the custom streaming process and write to the output file.

```shell
python3 process_streaming_jakerood.py
```

## Sync Changes to GitHub

Now it's time to get the local work you did on your machine back up to your cloud repo in GitHub:

1. On the VS Code side panel, click the source control icon (look for a blue bubble with an number in it).
1. Important! Above the Commit button, it will say "Message".
1. You MUST include a commit message.
1. Click the down arrow on the blue "Commit" button to "Commit and Push" to your GitHub repo.

Verify: Open a browser to your GitHub repo and verify the files have appeared.

Note: You can either sync all your changes at once at the end of the project **OR** you can sync your changes after completing each task individually.