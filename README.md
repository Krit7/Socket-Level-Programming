# Socket-Level-Programming

The idea here is to be able to use a server to process a file, and to return the file to the client once the processing is complete. In this application processing by server is limited to compressing the file and returning the compressed version of the file (only) using compression algorithm called Lempel‐Ziv compression. 

1. There are inbuilt functions copied in this code for compression and decompression of Lempel‐Ziv compression for processing the file.

2. You can use the same code to run the application (server and client) on the same machine by running both of them on differnet terminal using command :-
python server.py/client.py

3. For running on different machines you need to replace the host address by the address of the system on which you are running server.py

4. The "file.txt" contains the content that is being sent by the client to the server for compression and the "decompressed.txt" contains the uncompressed text received by the client from server.
