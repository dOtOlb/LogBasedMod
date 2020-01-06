# Generation of Realistic Server Load using MMLS Tool and Server Log

The generation would be useful for commonly seen purposes such as stress test, QoS assurance, etc.

This is a work in progress.  Considering the aforementioned objective, it will have to support multiple output formats in order to be conveniently used for subsequent processing in other applications.  The current plan is to target script generation for JMeter and Catchpoint first. 

This is distributed under MIT license (if the license file has not been added yet).

## LogBasedMod: log-based sample module for MMLS

The module is used on top of MMLS and can produce simulated load based on patterns extracted from a given set of production log files.

This is a work in progress.

## Step 1 Installation

The module can be installed to MMLS by following instructions here.

## Step 2 Usage

First, a configuration file has to be created specifying settings to be used for the module.

```no-highlight
[DEFAULT]
LogFileDirectory = ./data/
LogFormat = apache
Fitting = least-square
ArrivalModel = exponential
PopularityModel = custom
LoadGeneration = 1h
```

The directives are explained as follows:

#### LogFileDirectory
The path to which the example log file(s) is stored.  Both relative and absolute paths are supported.
    
#### LogFormat
The format of the log files.  The common log formats are supported, e.g. w3c, w3c extended, etc.

#### Fitting
The method of curve fitting to be used for parameter estimation.  It should be matching the specified model settings.  In other words, only the supported curve-fitting methods could be chosen to use for a particular arrival distribution specified.

#### ArrivalModel
The name of the statistical model to be fitted into the data.  Currently, only exponential distribution is supported.

#### PopularityModel
The name of the popularity model to be used for the distribution of URLs.  Currently only custom model (custom) is supported.

#### LoadGeneration
The length of duration for the simulated load.
