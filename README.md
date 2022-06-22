# A simple software to send data through audio using Morse (only, for now)
Send data and receive it through speaker and microphone.

# Setup:

You must have git installed and python3.

```
git clone https://github.com/Fran6nd/SimpleDataOverAudio.git
cd SimpleDataOverAudio
python3 -m pip install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
```
# Run:

* Activate the virtualenv: `source venv/bin/activate`
* Run the receiver: `python recv.py`
* Exit the receiver: press `q`
* Send some text: `python emit.py "this is my text"`
* Exit the virtualenv: `deactivate`