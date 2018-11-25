# README for A/D API

## Background

This project provides a simple interface to interact with a MCP3008 A/D in Python on a Raspberry Pi. It is built on top of the adafruit-mcp3008 driver and thus is dependent on that package being installed on the platform.

The simplification this project makes is to collect and report the samples from each of the 8 channels in one query.

## Installation Instructions

- Install adafruit-mcp3008
- Install this

## Examples of Basic Use

```python
from ad_interface import AD
from ad_fake import AdFake

actual_ad = AdFake()
ad = AD(actual_ad, 8)
samples = ad.get_samples()

for sample in samples:
    print(sample)
```
## Getting more info

Source code in this repository. Maybe use Sphinx.