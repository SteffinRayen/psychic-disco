Installation
------------

`Sentiment Analysis on Movie Review` works with Python3.3. If you know the drill, this should be enough:

    git clone https://github.com/SteffinRayen/psychic-disco.git
    pip install -e psychic-disco -r psychic-disco/docs/setup/requirements-dev.txt
    download_3rdparty_data.py

If the short instructions are not enough, read on.

### Full instructions for Ubuntu


These instructions will install the development version of Sentiment Analysis on Movie Review inside a virtualenv and were thought for a blank, vanilla Ubuntu 16.04 and tested using [Docker](https://www.docker.com/) (awesome tool btw). They should work more or less unchanged with other Ubuntu versions and Debian-based OSs.

Open a console and 'cd' into an empty folder of your choice. Now, execute the following commands:

Install python 3.3 and compilation requirements for numpy and scipy:

    sudo apt-get update
    sudo apt-get install -y software-properties-common
    sudo add-apt-repository -y ppa:fkrull/deadsnakes
    sudo apt-get update
    sudo apt-get install -y python3.3 python3.3-dev python-scipy gfortran libopenblas-dev liblapack-dev git wget

Create virtualenv and bootstrap pip:

    python3.3 -m venv venv
    source venv/bin/activate
    wget https://bootstrap.pypa.io/get-pip.py
    python3.3 get-pip.py
    echo 'PATH="$VIRTUAL_ENV/local/bin:$PATH"; export PATH' >> venv/bin/activate
    source venv/bin/activate

Clone and install Sentiment Analysis on Movie Review:

    git clone https://github.com/SteffinRayen/psychic-disco.git
    pip install -e psychic-disco -r psychic-disco/docs/setup/requirements-dev.txt
    download_3rdparty_data.py

Optionally run the tests:

    nosetests psychic-disco/tests

The installation is self-contained (within the folder you chose at the start) with
two exceptions:

- Lines starting with `sudo apt-get` made system-wide changes, to uninstall
  those you will to use `sudo apt-get remove`.
- `nltk` downloads data to `~/nltk_data`, once you don't use `nltk` it's safe
  to erase that folder.
