# echonotes - summarize lectures with AI

When installing you can chose to use the OpenAI API to create a transcription, or you can optionally install whisper locally (you would still need an OpenAI API key for summarization) This program uses GPT-4o-mini initially but can be changed in the aiSummarizer.py under model="". 

__Python3 with pip installed is mandatory__

[Requirements](#Requirements)

[Basic installation](#Basic-installation)

[Usage](#Usage)

[Install-with-local-whisper](#Install-with-local-whisper)

[Local-whisper-usage](#Local-whisper-usage)

## Requirements

You need to have Python3 with pip installed to run this on your machine

The requirements for the basic installation are listed below:

```python
openai==1.42.0

PyAudio==0.2.14

pydub==0.25.1
```

You can either manually install them or use the command (after installtion):

```bash
pip install -r requirements.txt
```

## Basic-installation

First off, clone the repo using: 

```bash
git clone https://github.com/KaiStephens/echonotes
```
Proceed into the 'echonotes' directory, edit apiInputs.py

```python
openAPIKey = "HERE"
```

replace "HERE" with your openAI API key. 

while in the echonotes directory run:

```bash
pip install -r requirements.txt
```
to install the requirements with pip.



## Usage

While in the echonotes directory run

```bash
python3 apiRun.py
```

If working correctly you should see something like this:

```bash
[kai@archlinux echonotes]$ python3 connectorScript.py
ALSA lib pcm_dsnoop.c:567:(snd_pcm_dsnoop_open) unable to open slave
ALSA lib pcm_dmix.c:1000:(snd_pcm_dmix_open) unable to open slave
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib pcm_dmix.c:1000:(snd_pcm_dmix_open) unable to open slave
Recording... Press Enter to stop.
```

Once you are ready to stop your recording press **Enter** to stop

It will than process the audio and summarize with ai. printing the AI summary.

After the process is completed it will save a file with the current %Y-%m-%d-%H-%M so your files are easily located. the file will contain somthing like this: 

```
[Summary]

The lesson appears to focus on the concept of repetition, as the teacher emphasizes the phrase "This is a test" multiple times. The repeated statement suggests it may be part of an exercise or demonstration intended to reinforce attention or illustrate a point, though the lack of additional context makes it hard to determine the specific educational objectives. Background sounds are noted but are not relevant to the main content.

[Transcript]

Hello, this is a test. This is a test. This is a test. This is a test. I've said this is a test four times. This is a test.
```

**This file is located in the recordings folder**

## Install-with-local-whisper

To use this program locally you need to install whisper. I highly recommened running this locally because whisper from OpenAI starts to cost up to a dollar per transcription when the mp3 files are a couple of hours longs. The API also maxes out at 25 megabytes which in some cases is not enough, there compression already baked into this program but it might not be enough for longer lectures.

It's also super simple to install.

### Install on Linux

```bash
sudo pacman -S ffmpeg
```

### Debian based system

```bash
sudo apt install ffmpeg
```

Install the whisper package (~2gb for full installation of whisper and all dependancies)

```bash
pip install -U openai-whisper
```

Now go through the [Basic installation](#Basic-installation) steps

## Local-whisper-usage

While in the echonotes directory run

```bash
python3 localRun.py
```

If working correctly you should see something like this:

```bash
[kai@archlinux echonotes]$ python3 connectorScript.py
ALSA lib pcm_dsnoop.c:567:(snd_pcm_dsnoop_open) unable to open slave
ALSA lib pcm_dmix.c:1000:(snd_pcm_dmix_open) unable to open slave
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2722:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib pcm_dmix.c:1000:(snd_pcm_dmix_open) unable to open slave
Recording... Press Enter to stop.
```

Once you are ready to stop your recording press **Enter** to stop

It will than process the audio and summarize with ai. printing the AI summary.

After the process is completed it will save a file with the current %Y-%m-%d-%H-%M so your files are easily located. the file will contain somthing like this: 

```
[Summary]

The lesson appears to focus on the concept of repetition, as the teacher emphasizes the phrase "This is a test" multiple times. The repeated statement suggests it may be part of an exercise or demonstration intended to reinforce attention or illustrate a point, though the lack of additional context makes it hard to determine the specific educational objectives. Background sounds are noted but are not relevant to the main content.

[Transcript]

Hello, this is a test. This is a test. This is a test. This is a test. I've said this is a test four times. This is a test.
```

**This file is located in the recordings folder**
