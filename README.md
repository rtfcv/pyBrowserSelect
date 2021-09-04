# pyBrowserSelection

A simple interface to let you choose which browser you would like
to open your links with.
Intended for use in windows but should work in other if you manage
to figure out how to configure it as a default browser

## Dependencies

- python3
- tkinter
- cx_freeze

## installation

```sh
python setup.py install
```

Default installation location is `%HOMEPATH%\AppData\Local\pyBrowserSelection\bin`

If you would like to set this program as a default browser, you
will need to additionary write some key/value-s to the registry
Sample configuration is in `regentries-sample.reg`.
Make sure you edit the content to suite your system.
Usually replacing `PATH_TO_YOUR_INSTALLATION_OF` to your actual
installation path should be enough.
