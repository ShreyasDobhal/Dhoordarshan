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

Setup a virtual camera
```
sudo apt install v4l2loopback-dkms
sudo modprobe -r v4l2loopback
sudo modprobe v4l2loopback devices=1 video_nr=20 card_label="v4l2loopback" exclusive_caps=1
```

Download webdrivers and add to PATH
```
echo 'export PATH="$HOME/Documents/Python/ChromeDriver:$PATH"' >> ~/.profile
source ~/.profile
```
