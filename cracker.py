#! /usr/bin/python3

import sys
import optparse
import subprocess
from termcolor import colored

# Function to crack WPA2 hashes from a file using hashcat with subprocess
def crack_wpa2_hashes(hash_file, wordlist):
    try:
        # Example hashcat command to crack WPA2 hashes from file with specified wordlist
        cmd = ["hashcat", "-m", "22000", "-a", "0", "-w", "4", "--force", hash_file, wordlist]

        print(colored(f"Cracking WPA2 hashes in {hash_file} with wordlist {wordlist}", "yellow"))

        # Execute hashcat command using subprocess
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        # Print the output
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        if e.stderr:
            print(f"Error output:\n{e.stderr}")
        sys.exit(1)

# Function to convert hash file to pcap using hcxdumptool with subprocess
def convert_to_pcap(input_file):
    try:
        # Example hcxdumptool command to convert to pcap
        cmd = ["hcxpcapngtool", "-o", f"{input_file}.pcapng", input_file]

        print(colored(f"Converting {input_file} to pcap using hcxdumptool", "yellow"))

        # Execute the command using subprocess
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        # Print the output
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        if e.stderr:
            print(f"Error output:\n{e.stderr}")
        sys.exit(1)


# Main function to parse arguments and initiate actions
def main():
    parser = optparse.OptionParser(usage="%prog -f <hash_file> | -C <input_file> [-w <wordlist_file>]")
    parser.add_option("-f", dest="hash_file", help="Crack WPA2 hashes from a file")
    parser.add_option("-C", dest="convert_file", help="Convert file to pcap using hcxdumptool")
    parser.add_option("-w", dest="wordlist", help="Specify wordlist file for cracking")

    (options, args) = parser.parse_args()

    if options.hash_file:
        if options.wordlist:
            crack_wpa2_hashes(options.hash_file, options.wordlist)
        else:
            print("Error: Wordlist file (-w) must be specified for cracking hashes from a file (-f)")
            sys.exit(1)
    elif options.convert_file:
        convert_to_pcap(options.convert_file)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
