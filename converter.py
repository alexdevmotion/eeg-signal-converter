import argparse
import numpy as np
import pandas as pd
import sys


parser = argparse.ArgumentParser()
parser.add_argument('--inout', type=str, required=True, help='The CSV input&output file')
parser.add_argument('--incol', type=str, required=False, default='Electrode',
                    help='The name of the column to be converted (defaults to "Electrode")')
parser.add_argument('--outcol', type=str, required=False,
                    help='The name of the new column (will be generated if missing)')
parser.add_argument('--lowcut', type=float, required=False, default=0,
                    help='The lower bound of the band filter (defaults to 1)')
parser.add_argument('--highcut', type=float, required=False, default=70,
                    help='The upper bound of the band filter (defaults to 70)')
parser.add_argument('--sampling', type=float, required=False, default=512,
                    help='Sampling rate in Hz (defaults to 512)')
parser.add_argument('--delimiter', type=str, required=False, default=',',
                    help='The CSV delimiter character (defaults to ,)')
parser.add_argument('--quotechar', type=str, required=False, default='"',
                    help='The CSV quote character (defaults to ")')

args = parser.parse_args(sys.argv[1:])

outcol = args.outcol
if not outcol:
    outcol = 'Band %.2f - %.2f' % (args.lowcut, args.highcut)

print('Will add the "%s" column to the "%s" file' % (outcol, args.inout))

csv_data = pd.read_csv(args.inout)
electrode_data = csv_data[args.incol].tolist()
fft_vals = np.absolute(np.fft.fft(electrode_data))
fft_freq = np.fft.fftfreq(len(electrode_data), 1./args.sampling)

filtered_vals = []
for i in range(len(fft_vals)):
    if (fft_freq[i] >= args.lowcut) & (fft_freq[i] <= args.highcut):
        filtered_vals.append(fft_vals[i])
    else:
        filtered_vals.append(0.)

csv_data[outcol] = pd.Series(filtered_vals)
csv_data.to_csv(args.inout)

print('Done.')
