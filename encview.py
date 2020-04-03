#!/usr/bin/python3

import sys
import os
import uuid
import subprocess
import signal

secure_dir = "/dev/shm"

def main(f):
    if not os.path.isfile(f):
        print("Error:", f, "is not a file.")
    if not os.path.isdir(secure_dir):
        print("Error:", secure_dir, "is not a directory.")
        print("No secure location to store decrypted files.")
        return


    o = secure_dir + "/" + str(uuid.uuid4().hex)

    # attempt to discren true extension by stripping gpg from end of string and checking extension
    fname = f
    if fname.endswith(".gpg"):
        fname = fname[:-4]

    _, fext = os.path.splitext(fname)
    if fext:
        o = o + fext


    print("Decrypting", f, "to", o)
    os.umask(0o77) # prevent groups and others from reading file
    p = subprocess.Popen(["gpg", "--output", o, "--decrypt", f], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()

    # automatically open decrypted file
    p = subprocess.Popen(["xdg-open", o], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()

    print("Viewer launched, delete decrypted file with CTRL-C...")

    try:
        signal.pause()
    except KeyboardInterrupt:
        pass

    os.remove(o)
    print("Output file", o, "deleted.")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("usage: encview <filename>")
        print("Automatically decrypt to secure temporary location, then delete when file is closed")
        sys.exit(1)
    main(sys.argv[1])
