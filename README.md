# Dhoordarshan

Automation tool to automatically connect to a video call with python based interface. 

## Project Setup

**Step 1)** Create python virtual environment
```
pip install virtualenv
python3 -m venv env
source env/bin/activate
...
deactivate
pip freeze > requirements.txt
```

**Step 2)** Install dependencies

To get the packages from requirements.txt
```
pip install -r /path/to/requirements.txt
```

also download appropriate chrome driver and add to PATH
```
echo 'export PATH="$HOME/Documents/Python/ChromeDriver:$PATH"' >> ~/.profile
source ~/.profile
```

**Step 3)** Update utils.py file with your details

**Step 4)** Setup a virtual camera

Use the below commands to setup a virtual camera for the first time

```
sudo apt install v4l2loopback-dkms
sudo modprobe -r v4l2loopback
sudo modprobe v4l2loopback devices=1 video_nr=20 card_label="v4l2loopback" exclusive_caps=1
```

## Running the project

### Test the various modules

Run the following test files one by one and make sure everything works as expected.

```
python3 testCameras.py
python3 testFPS.py
python3 testLag.py
python3 testSelenium.py
python3 testHandTracking.py
python3 testFaceTime.py
```

### Running the code

```
source env/bin/activate
sudo modprobe -r v4l2loopback
sudo modprobe v4l2loopback devices=1 video_nr=20 card_label="v4l2loopback" exclusive_caps=1
python3 main.py
```