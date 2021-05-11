```
Remote Procedure Call
```
Build a Simple Middleware System. That allows dynamically adding a service into the system and allows accessing the service from a client program.

Desing a RPC protocol consisting of Server Stub and Client Stub, responsible to run any given function present in server machine as shared library on client side. Communication protocol can be either Flask API / WebSocket.

Protocol should be able to adapt any generic function and these functions should be usable from client machine using import functions.

## A Simple walk through:
- Server (third party) hosting some function like (fun1()), Client will agree with some Agreement* (RPC protocol) with server and follows the steps provided by server.
- After communication client will be able to use the library without getting the complete code from server side.
- Agreement: Design a process which will help client to use the functions. (Do not directly copy the functions from server to client), also server functions will not be changed during run time.

## Test Samples:
Once the RPC model is ready, TAs will provide functions that will be hosted in Server side and could be used at the client side.

## STEPS FOR RUNNING : 
1. server.PY and client.py files just have the defintions and calls, similar to a text file
2. Run server_stub.py, then rpc.py, then client_stub.py
3. Your required answer will be printed on client_stub.py
