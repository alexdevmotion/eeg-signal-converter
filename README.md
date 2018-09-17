# eeg-signal-converter
Filters and extracts a specified band from a single channel EEG signal

```
usage: converter.py [-h] --inout INOUT [--incol INCOL] [--outcol OUTCOL]
                    [--lowcut LOWCUT] [--highcut HIGHCUT]
                    [--sampling SAMPLING] [--delimiter DELIMITER]
                    [--quotechar QUOTECHAR]

optional arguments:
  -h, --help            show this help message and exit
  --inout INOUT         The CSV input&output file
  --incol INCOL         The name of the column to be converted (defaults to
                        "Electrode")
  --outcol OUTCOL       The name of the new column (will be generated if
                        missing)
  --lowcut LOWCUT       The lower bound of the band filter (defaults to 1)
  --highcut HIGHCUT     The upper bound of the band filter (defaults to 70)
  --sampling SAMPLING   Sampling rate in Hz (defaults to 512)
  --delimiter DELIMITER
                        The CSV delimiter character (defaults to ,)
  --quotechar QUOTECHAR
                        The CSV quote character (defaults to ")
```