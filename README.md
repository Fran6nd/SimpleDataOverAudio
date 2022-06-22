# A simple software to send data through audio using Morse (only, for now)
Send data and receive it through speaker and microphone.

# Setup:

```
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