# encview - Easily View Encrypted Files

`encview` is a basic 50 line python wrapper around `gpg` to make viewing encrypted files easier.
It decrypts files to the RAM backed temporary filesystem `/dev/shm`, and launches
the system viewer for that filetype with `xdg-open`. CTRL-C will then delete the decrypted file.

Ideally, the decrypted file would automatically be deleted when the viewing program is closed.
However, I haven't been able to figure out how to get the PID of the launched viewer from `xdg-open`.
If anyone's figured out how to make `xdg-open` block or somehow find the launched process, let me know!

## Usage and Installation

This is only going to work on linux computers, but could likely be ported to OSX with minimal effort.

- Usage: `encview <filename>`
- Installation: `cp encview.py /usr/local/bin/encview`
