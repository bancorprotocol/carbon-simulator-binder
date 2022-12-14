<p align="center">
<img width="100%" src="https://drive.google.com/uc?export=view&id=10y3NKbbk7yt7cZDMszMt04g6NquTEa4p" alt="Carbon Logo" />
</p>

# Carbon Simulator for Binder

[![PyPI version](https://badge.fury.io/py/carbon-simulator.svg)](https://badge.fury.io/py/carbon-simulator)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Binder](https://img.shields.io/badge/binder-main-blue)][binderlab]


This is the [Binder][binder] repo for the [Carbon simulator][repo]. The permament github URL for this repo is [bancorprotocol/carbon-simulator-binder][repob]. Please refer to the simulator repo at [bancorprotocol/carbon-simulator][repo] and the Carbon project website [carbondefi.xyz][carbon] for more information. On the site you will find in particular the [litepaper][litepaper], [whitepaper][whitepaper] and the [patent application][patent]. 

## Usage

This repo is mostly designed to be used with [Binder][binder], a web-based service for hosting Jupyter notebooks and labs. If you want to run the simulator locally, we recommend cloning the [main repo][repo] instead, and following the installation instructions there. This gives you access to not only the stable `main` branch of the simulator that is available in [PyPi][pypi], but also to the full source code and the `beta` branch that contains the latest code.

To launch this repo on binder, you can use the badge above to launch the lab. You can also

- go to the [lab environment here][binderlab], or 
- to the [litepaper example sheet here][binderlab_lpex].



Note that the launch process can be slow at times: if the repo has been recently changed and you are the first one use it then the docker images may have to be built. Even if the docker images are available, it may take a moment to transfer the required images to the [federation server][binderfed]

[binderlab]:https://mybinder.org/v2/gh/bancorprotocol/carbon-simulator-binder/main
[binderlab_lpex]:https://mybinder.org/v2/gh/bancorprotocol/carbon-simulator-binder/main?labpath=CarbonSim-LitepaperExamples.ipynb


## Local usage 

If you nevertheless want to run this repo locally, you can do so by running

````{tab} PyPI
$ pip install -r requirements.txt
````

which in particular will install the carbon simulator from [PyPi][pypi]

````{tab} PyPI
$ pip install carbon-simulator
````

We recommend using a [virtual environment][venv] to ensure that there are no conflicts with other local installations.


[carbon]:https://carbondefi.xyz
[litepaper]:https://carbondefi.xyz/litepaper
[whitepaper]:https://carbondefi.xyz/whitepaper
[patent]:https://carbondefi.xyz/patent
[repo]:https://github.com/bancorprotocol/carbon-simulator/
[repob]:https://github.com/bancorprotocol/carbon-simulator-binder/
[pypi]:https://pypi.org/project/carbon-simulator/
[venv]:https://docs.python.org/3/library/venv.html
[binder]:https://mybinder.org/
[binderfed]:https://mybinder.readthedocs.io/en/latest/about/federation.html



