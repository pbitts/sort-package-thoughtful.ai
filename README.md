# Package Sorter

A python tool that classifies packages to the corresponding stack based on its dimensions and mass.

- `REJECTED`
- `SPECIAL`
- `STANDARD`

##  Rules

Sort the packages using the following criteria:

- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
- A package is **heavy** when its mass is greater or equal to 20 kg.

You must dispatch the packages in the following stacks:

- **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
- **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
- **REJECTED**: packages that are **both** heavy and bulky are rejected.

# Usage

~~~bash
Select stack for packages.

options:
  -h, --help            show this help message and exit

  -w WIDTH, --width WIDTH

                        Width (cm)

  -e HEIGHT, --height HEIGHT

                        Height (cm)

  -l LENGHT, --lenght LENGHT

                        Lenght (cm)

  -m MASS, --mass MASS  Mass (cm)
~~~


# Examples

~~~bash
python main.py -w 200 -e 10 -l 10 -m 10
~~~

~~~bash

2025-07-31 11:14:58-0300        [main]  [INFO]  Width:             200.0

2025-07-31 11:14:58-0300        [main]  [INFO]  Height:            10.0

2025-07-31 11:14:58-0300        [main]  [INFO]  Lenght:            10.0

2025-07-31 11:14:58-0300        [main]  [INFO]  Mass:              10.0

2025-07-31 11:14:58-0300        [sort]  [INFO]  Sorting packages...

2025-07-31 11:14:58-0300        [sort]  [INFO]  Package Heavy=False and Bulky=True

2025-07-31 11:14:58-0300        [main]  [INFO]  Stack Selected: SPECIAL
~~~


~~~bash
python main.py -w 200 -e 10 -l 10 -m -10
~~~

~~~bash
usage: main.py [-h] -w WIDTH -e HEIGHT -l LENGHT -m MASS

main.py: error: argument -m/--mass: -10 must be >0.
~~~