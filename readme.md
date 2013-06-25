Microformats parser in Python
======
This is a microformats parser in Python.

    import microformats as ufs
    fp = open('index.html')
    data = ufs.parse(fp)

`data` now contains the microformats data.
