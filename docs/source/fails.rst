Common fails
============

This documents describes the most common fails and issues you can find while using Patton and possibles solutions.

SSLError
--------

If when you try to run Patton you get a message similar like that:

.. code-block:: python

   Using data directory: /Users/chad/.bokeh/data
   Traceback (most recent call last):
     File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/urllib/request.py", line 1318, in do_open
       encode_chunked=req.has_header('Transfer-encoding'))
     File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/http/client.py", line 1239, in request
       self._send_request(method, url, body, headers, encode_chunked)
     File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/http/client.py", line 1285, in _send_request
       self.endheaders(body, encode_chunked=encode_chunked)
     File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/http/client.py", line 1234, in endheaders
       self._send_output(message_body, encode_chunked=encode_chunked)
     File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/http/client.py", line 1026, in _send_output
       self.send(msg)
     File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/http/client.py", line 964, in send
       self.connect()
     File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/http/client.py", line 1400, in connect
       server_hostname=server_hostname)
     File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/ssl.py", line 401, in wrap_socket
       _context=self, _session=session)
     File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/ssl.py", line 808, in __init__
       self.do_handshake()
     File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/ssl.py", line 1061, in do_handshake
       self._sslobj.do_handshake()
     File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/ssl.py", line 683, in do_handshake
       self._sslobj.do_handshake()
   ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:749)


Try to do the fix that proposes in `cdotson blog <http://www.cdotson.com/2017/01/sslerror-with-python-3-6-x-on-macos-sierra/>`_. In summary:

- Install the `certifi package <https://pypi.python.org/pypi/certifi >`_.
- Run the download script provided with the installer – /Applications/Python 3.6/Install Certificates.command.

