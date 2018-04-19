# CTF multitool cheat sheet

A quick summary of common tools

## File-related tools

| tool | what it does | when to use it | example | more info |
| ---- | ------------ | -------------- | ------- | --------- |
| **file** | recognize (guess) the type of data in a file | when given a file of unkinown/dubious type | `file program` command returns: `program: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), stripped` | |
| **readelf -l**| Display's the program headers and entry point of an ELF executable | when given an ELF executable that is stripped in order to find entry point | `readelf -l program` returns a bunch of information, most importantly `Entry point 0x<address>` | |
| **find** | search for files in a directory hierarchy | when you have many files (and/or directories) to search | `find . -name filename` searches for `filename` in the current directory (and any subdirectores). There are many, many more options and commands. |  |
| **grep** | search within a file for certain text/pattern | finding out if a file contains a flag (in text) or something else you are looking for | `grep apple fruitlist.txt` | [lesson](https://swcarpentry.github.io/shell-novice/07-find/) |
| **strings** | prints all printable (text) strings within a program or other binary file | you want to extract all strings from something that might be unreadable otherwise | `strings program` | |
| **caesar** | performs a simple rotation on its input text by the number specified as an argument | when you have an input you believe is a Caesar cipher | <code>echo abcdefg &#124; caesar 5</code> | included in the bsdgames package | 
| **diff** | shows the difference between two files | you want to see what changed | `diff file1 file2` (`-u` for unified diff can be nice) | |
| **xxd** | display data as hexadecimal values | you want to analyze binary data (and possibly search the output with `grep`) | `xxd filename` or use a pipe: <code>cat file &#124; xxd &#124; grep searchterm</code> |  |
| **binwalk** | carves files with a thorough default configuration; can decompress archives and recursively carve | you have a disk image with likely deleted files or you think a file has a second file hidden within it | `binwalk file` (`-e` for automatic file extraction, places files in folder named `_file`) | |
| **base64** | encode to or decode from base64 encoding | you want to encode or decode base64 data | `base64 -i inputfile -o outputfile` to encode inputfile, `--decode` to decode; uses stdin and stdout by default without `-i` and `-o` | |
| **radamsa** | general purpose fuzzer, a tool that sends arbitrary input meant to crash a program | you want to quickly and easily generate a bunch of random text | <code>echo abcdefg &#124; radamsa</code> | https://github.com/aoh/radamsa |

## network-related tools

| tool | what it does | when to use it | example | more info |
| ---- | ------------ | -------------- | ------- | --------- |
| **netcat** | network swiss-army knife |
| **wget** | fetch web pages via HTTP |
| **curl** | similar to wget |
| **nmap** | network port scanner |
| **wireshark** | sniff/analyze network traffic (pcap) |

## password / hashing related tools

| tool | what it does | when to use it | example | more info |
| ---- | ------------ | -------------- | ------- | --------- | 
| **hashcat** | advanced password recovery | you have a password hash | [nice example from uiuctf](https://tylerkerr.ca/b/2017/04/uiuctf-2017-crackme) | https://hashcat.net/hashcat/ |
| **john** | John the Ripper - old school but powerful | brute-force passwords | `john -w:password.lst pass.txt` | [homepage with wordlists](http://www.openwall.com/john/) |

## database tools
| tool | what it does | when to use it | example | more info |
| ---- | ------------ | -------------- | ------- | --------- |
| **sqlmap** | automated SQL injection flaw detection and exploitation| you have a web challenge that you suspect is vulnerable to SQL injection and want to access the database | `python sqlmap.py -u "https://www.test.url/"` | |

## steganography tools
| tool | what it does | when to use it | example | more info |
| ---- | ------------ | -------------- | ------- | --------- |
| **stegsolve** | extracts hidden data from images | when a steganography challenge presents you with an image that may contain hidden data | | | |
| **audacity** | audio editor useful for audio challenges | when a steganography challenge gives you an audio file | | don't forget to check the spectrogram view for visual clues! |

## debuggers

| tool | what it does | when to use it | example | more info |
| ---- | ------------ | -------------- | ------- | --------- |
| **gdb** | GNU Debugger |
| **IDA Pro** | Interactive Disassembler |
| **radare2** | Free Interactive Disassembler |

## debugger plugins

| tool | what it does | when to use it | example | more info |
| ---- | ------------ | -------------- | ------- | --------- |
| **pwndbg** | GDB add-on for exploitation assistance with features such as in-depth process context at breakpoints, ROP gadget finding and chain building, etc. | Use it for easy viewing of current register contents, nearby instructions, nearby stack contents; use it for finding ROP gadgets in a running process' memory; etc. | `pwndbg> ropgadget` or `pwndbg> context`, etc. | [pwndbg GitHub](https://github.com/pwndbg/pwndbg) |

## web browser tools/tricks

| tool | what it does | when to use it | example | more info |
| ---- | ------------ | -------------- | ------- | --------- |
| **view source** | |
| **inspect** | |
| **setting (spoofing) user-agent** | |
| **postman** | chrome plugin for interacting with web APIs | |
