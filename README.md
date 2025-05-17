A bot that plays [Universal Paperclips](http://decisionproblem.com/paperclips/index2.html).

Intended for learning about reinforcement learning.

# Dependencies

## General
- Python 3
- An MPI implementation (e.g., OpenMPI or MPICH) must be installed to use `mpirun`

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
        - mpi4py (required for the training and rollout scripts)

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
with multiple processes. Make sure an MPI implementation and the Python `mpi4py` module are installed before running this command:

~~~~
mpirun -np 4 python examples/train.py
~~~~

Checkpoints will be saved under `data/`. Edit `examples/train.py` if you need to
adjust the path to your PhantomJS or Chromium driver.

## Running a trained agent

To watch the agent play the standard game, use the rollout script:

Ensure that an MPI implementation and `mpi4py` are installed before running the script.

~~~~
mpirun -np 4 python examples/rollout.py
~~~~

The script loads the most recent saved policy and opens a browser window. Change
the webdriver path inside `examples/rollout.py` if necessary.
