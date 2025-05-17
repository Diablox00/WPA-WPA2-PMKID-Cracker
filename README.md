# WPA2 Hash Cracker & PCAP Converter

## Description
This project provides a Python script that allows users to:
- Crack WPA2 hashes using **hashcat** and a specified wordlist.
- Convert captured network files to **PCAP** format using **hcxdumptool**.

## Features
- WPA2 hash cracking with **hashcat**
- PCAP file conversion using **hcxdumptool**
- Command-line interface for ease of use

## Requirements
- Python 3
- **hashcat** (installed and configured)
- **hcxdumptool** (installed and configured)
- **termcolor** (install via `pip install termcolor`)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/faizanzohaib/WPA2-Hash-Cracker.git
   cd WPA2-Hash-Cracker
   ```
2. Install dependencies:
   ```sh
   pip install termcolor
   ```

## Usage

### Crack WPA2 Hashes
```sh
python3 script.py -f <hash_file> -w <wordlist_file>
```
Example:
```sh
python3 script.py -f handshake.hccapx -w rockyou.txt
```

### Convert File to PCAP Format
```sh
python3 script.py -C <input_file>
```
Example:
```sh
python3 script.py -C capture.22000
```

## License
This program is free software: you can redistribute it and/or modify it under the terms of the **GNU General Public License** as published by the **Free Software Foundation**, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but **WITHOUT ANY WARRANTY**; without even the implied warranty of **MERCHANTABILITY** or **FITNESS FOR A PARTICULAR PURPOSE**. See the **GNU General Public License** for more details.


## Author
**Faizan Zohaib**  
Email: [faizanzohaib00@protonmail.com](mailto:faizanzohaib00@protonmail.com)

