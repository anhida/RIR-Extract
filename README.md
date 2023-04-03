# rir-analysis
A repository for processing and analyzing room impulse response (RIR)

## How To run script

### Invert Sweep

For Inverting Sweep, you need
- reference sweep
- upper and lower limit of sweep's frequency

Then you can run shell command:

```sh
python inversfilter.py reference_sweep.wav lower_freq upper_freq
```

example of result:

![images](images/inversfilter.png?raw=true)

### Extract RIR

For Extract RIR, you need:
- measurement sweep
- inverted of reference sweep

Then you can run shell command:

```sh
python exractRIR.py measurement_sweep.wav inverted_reference_sweep.wav
```

example of result:

![images](images/extractRIR.png?raw=true)

### Fix data chunk error

If the chunk data not understandable by WAVRead in Scipy, maybe because RIFF format inconsistency, you can re-process using **sox** tool

For example:

```sh
sox original_sweep.wav soxed_sweep.wav
```

Then use it as input

```sh
python inversfilter.py soxed_sweep.wav lower_freq upper_freq
```

