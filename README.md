# TTRPG dynamic weather system
A dynamic weather system designed to shift through weather patterns naturally, day by day.

Is this the most autistic thing I've done? Potentially.

## General function
The base weather states which can be generated are given in *tables/states.csv*. The table doesn't have headers as it relies on numerical indexes to extract the day's weather cell. Rows represent a humidity scale (from arid to humid), while columns represent temperature (from extreme heat to arctic cold).

The model takes an input region temperature and humidity (inspired by the biome pyramid model) which defines the climate.These define the area of the *states* table which weather is pulled from. This selection is then modified by a selected season, and an underlying relative pressure/humidity model.

![How region humidity/temperature defines potential weather states](Assets/methodology_1.png?raw=true "Method to determine possible weather states")

## Inputs
Valid inputs for each variable are given below:

**SEASON**
- spring
- summer
- autumn
- winter

**TEMPERATURE**
- tropical
- subtropical
- temperate
- subpolar
- polar

**HUMIDITY**
- humid
- subhumid
- semiarid
- arid
- hyperarid