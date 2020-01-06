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

[DEFAULT]
LogFileDirectory = ./data/
LogFormat = apache
Fitting = least-square
