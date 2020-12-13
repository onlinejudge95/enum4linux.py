1. Create CLI module
    * ~~Create a CLI entrypoint to the module (better to use click)~~
    * This step needs thinking as to what all options are we providing,
    ideally all the individual enumeration should be coupled into buckets(up to the extent that makes sense) and provided as individual commands.
    * ~~There should be a command to run all the enumerations in one pass.~~
2. Check for dependencies(system)
    * This module should make sure that you have all the required system dependencies installed.
    * This should run as the first thing, and the code should die if this check fails
3. Port all perl `sub`s to corresponding methods
    * For time being simply port the `sub`s to python methods in a separate module.
    * Later see if we can abstract out common code and if we can use Object-Oriented approaches here.
