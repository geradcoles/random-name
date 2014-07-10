random-name
===========

Python script and sample data for generating random names
Try using this script to generate random people names, machine hostnames,
or other combinations of random words based on lists.

This checkout includes both the script, which requires python docopt, and
several sample data files, which may be used for various purposes.

## Examples

### Generate twenty random american women's full names

    ./random-name \
      --component=sample_lists/female_names \
      --component=sample_lists/female_names \
      --component=sample_lists/surnames_american \
      --separator=' ' 20

### Generate a random machine hostname (fun)

    ./random-name \
      --component=sample_lists/personalities \
      --component=sample_lists/animals

