Microformats parser in Python
======
This is a microformats parser in Python.

    import microformats as ufs
    fp = open('index.html')
    data = ufs.parse(fp)

`data` now contains the microformats data.

Specs come from [here](https://github.com/G5/microformats2).
