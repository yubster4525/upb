A bot that plays [Universal Paperclips](http://decisionproblem.com/paperclips/index2.html).

Intended for learning about reinforcement learning.

# Dependencies

## General
- Python 3
- MPI implementation (e.g., OpenMPI or MPICH) for `mpirun`

## Game Handler
- Python modules:
	- Selenium
	- lxml
- One of the following webdrivers:
	- Chromium
		- e.g. On Ubuntu: sudo apt install chromium-browser chromium-chromedriver
	- PhantomJS built with ghostdriver support
		- The binary distribution from http://phantomjs.org/ is best.

## Game Emulation
- Python modules:
	- py\_mini\_racer

## Learning
- Python modules:
        - Numpy
        - [OpenAI Gym](https://github.com/openai/gym)
        - [OpenAI Baselines](https://github.com/openai/baselines)
        - mpi4py

## Plotting
- Python modules:
	- matplotlib

## Documentation
- Python modules:
	- Sphinx

# Installation
~~~~
git clone https://github.com/mmalahe/upb.git
cd upb
pip install -e .
~~~~

# Usage

## Training an agent

After installing the dependencies, you can train the provided PPO agent on the
training version of the game. The training script uses MPI so you can run it
with multiple processes:

Ensure that both an MPI implementation and the `mpi4py` Python package are
installed before running the examples.

~~~~
mpirun -np 4 python examples/train.py
~~~~

Checkpoints will be saved under `data/`. Edit `examples/train.py` if you need to
adjust the path to your PhantomJS or Chromium driver.

To see training progress in a browser, pass the ``--progress-port`` option to
``examples/train.py`` and open ``http://localhost:<port>``. For example:

~~~~
mpirun -np 4 python examples/train.py --progress-port 8080
~~~~

## Running a trained agent

To watch the agent play the standard game, use the rollout script:

~~~~
mpirun -np 4 python examples/rollout.py
~~~~

The script loads the most recent saved policy and opens a browser window. Change
the webdriver path inside `examples/rollout.py` if necessary.
