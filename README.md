random-name
===========

Python script and sample data for generating random names.

Possible uses include creating fake people names for application testing,
generating unique, memorable machine hostnames, generating first/middle
name combinations when choosing baby names, and other combinations of
random words based on lists.

This checkout includes both the script, which requires python _docopt_, and
several sample data files, which may be used for various purposes.

## Examples

Generate twenty random american women's full names

    ./random-name \
      --component=sample_lists/female_names \
      --component=sample_lists/female_names \
      --component=sample_lists/surnames_american \
      --separator=' ' 20

Generate a random machine hostname (fun)

    ./random-name \
      --component=sample_lists/personalities \
      --component=sample_lists/animals

## Installation

    pip install docopt
    git clone https://github.com/geradcoles/random-name.git
    cd random-name
    # run commands from here, or copy random-name to your system's /bin dir

## Performance

This script loads all the names in the specified name lists into memory, so really
large name lists will result in a lot of memory usage.

The method used to get random names from the lists is inefficient, as this tool
was never intended to be used for large amounts (millions) of names. If you really
need this functionality, consider forking this code and updating it, then issue me
a pull request.

