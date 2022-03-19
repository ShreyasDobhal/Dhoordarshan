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

To get the packages from requirements.txt
```
pip install -r /path/to/requirements.txt
```

Other packages
```
sudo apt install v4l2loopback-dkms
sudo modprobe v4l2loopback devices=1
v4l2-ctl --list-devices -d4 # it should NOT say 'Cannot open device /dev/video4'
# Set the (same) device for pyvirtualwebcam
```