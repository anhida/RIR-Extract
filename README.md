# rir-analysis
A repository for processing and analyzing room impulse response (RIR)

## How To run script

For Extract RIR, you need:
- original sweep
- inverted sweep

Then you can run shell command:

```sh
python ./exractRIR.py original_sweep.wav inverted_sweep.wav
```

For Inverting Sweep, you need
- Original Sweep
- Upper and Lower limit of sweep's frequency

Then you can run shell command:

```sh
python ./inversfilter.py original_sweep.wav lower_freq upper_freq
```

Currently, inversing wav array still not working

