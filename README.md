# Challenge Natixis : website monitoring

## Python script that monitors the website of "Banque Populaire" for availability.

Information about the project and installations

## Configuration & prerequisites:

Configuration used:

- Windows 10
- Python 3.9
- Browsers used: Latest versions of Chrome and Edge

Libraries: Mainly Lackey for image recognition, Selenium, logging and many others...  
For more details about the libs, please check out the "requirements.txt" file, for a complete list of the libs used to run the project.

## Contents of the project:

- `main_script.py`: main code that contains the different steps of the script (using Lackey and Selenium);
- `utils.py`: some utility functions;
- Folder `images_folder_lackey` which contains 2 images that are useful for the image recognition process (the map and the number 4 image);
- Folder `videos_obtained_simulation`, where the recordings of the runs are stored.
- Text file `requirements.txt` with the libs required.
- XML FILE `param.xml` with some configurations for the script.
- Folder `dist`: inside you can find the executable to run the script (without requirements).

## How to run the project and install:

### Step 1: Clone/download the repository to your machine.

### Step 2: Navigate to the project folder in the terminal.

### Step 3: Install the packages (check below for Anaconda).

Using the `requirements.txt` file where I put all the packages required to run the project.

Just run the following command:


> pip install -r requirements.txt



-----------
Tips (for Anaconda users):
- To avoid problems or conflicts in packages, you can create a new environment to run the project:
Run the following commands:

>conda create --name NewEnvironmentName
>conda activate NewEnvironmentName

-Then, import the packages (requirements.txt file):

> pip install -r requirements.txt




### Step 4: Run the web monitoring script
To execute the monitoring of the website https://www.banquepopulaire.fr/, just run the Python file main_script.py. This will launch the process for two browsers: Chrome and Edge.

Multiple files are created during the process such as:

LOGS: execution.log, which contains the logs of the script, this includes error logs and success logs.
RECORDING: in the folder videos_obtained_simulation, you can find at the end of the run the different recordings for both executions (Chrome and Edge).
SCREENSHOTS: when an error appears, screenshots are taken such as lackey_error_screenshot.


### Step 5 (optional): run the executable
In order to avoid installations, you can also just run the executable generated with PyInstaller. You can find the executable in the folder dist.


---------------------------------------


Thanks! And in case of any problem with the code or any issue to run it, feel free to contact me!

Email: gustavo.p.gama@gmail.com






