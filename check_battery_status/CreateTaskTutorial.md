# How to create an automation with Task Scheduler on Win11

### 1. Search "Task Scheduler" in the search bar and open it
<image src="check_battery_status/assets/img1.png" width="600">

### 2. On the right side, press "Create basic task"
<image src="check_battery_status/images/img2.png" width="300">

### 3. Give the task a name and, optionally, a description, then press "Next"
<image src="check_battery_status/images/img3.png" width="350">

### 4. In this section, set the task trigger to "When the computer starts", in this way, your task will run as soon as you turn on the PC, executing the loop inside the code
<image src="check_battery_status/images/img4.png" width="350">

### 5. Here, set to "Start a program"
<image src="check_battery_status/images/img5.png" width="350">

### 6. The most important section:
#### 1. In the "Program/script" box put your pythonw.exe path (should be like "C:\Users\user_name\AppData\Local\Programs...)
#### 2. In "Add argument" box put check_battery.pyw
#### 3. In "Start in" box put the file path where you downloaded the script
<image src="check_battery_status/images/img6.png" width="450">

### 7. At the end, press "Finish". Ta daa, you made a new task :)

## Now your task will run daily and give you a message according to you battery percentage, enjoy!


