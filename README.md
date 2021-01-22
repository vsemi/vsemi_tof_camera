# Sentinel ToF Camera python SDK

### Pre-requisites

  #### pyserial, use to connect to Sentinel ToF Camera via serial port

    #pip install pyserial
    or
    #pip3 install pyserial

### Before run the examples, make sure your Sentinel ToF Camera plugged in, and current user has permission to read the serial port. 

To grant serial port permission for Linux system:

    #sudo chmod a+rw /dev/ttyACM0
    
# Examples

Sample programs that use the Sentinel ToF Camera.

## `server.py`

### What this demonstrates

The sample program demonstrates acquiring and displaying point cloud, depth map and grayscale image in a browser based interface.

### Pre-requisites

  #### websockets

    #pip install websockets
    or
    #pip3 install websockets

### How to Run

Command to run the program:

```    
#python server.py
or
#python3 server.py
```
You will have following output in your console:

```    
ToF camera opened successfully:
    model:      4.0
    firmware:   3.1
    uid:        50004B
    resolution: 160x60
    port:       /dev/ttyACM0
    IP address: 127.0.0.1
    URL:  http://127.0.0.1:8080
```    
Copy the URL into your browser address bar.

## `distance.py`

### What this demonstrates

The sample program demonstrates acquiring frames with distance / depth information only.

### Pre-requisites

Pre-requisites/dependencies:

  #### OpenCV python module

    #pip install opencv-python


### How to Run

Command to run the program:

```    
#python distance.py
```

A depth map will be showing.

## `distancePlusAmplitude.py`

### What this demonstrates

The sample program demonstrates acquiring frames with both distance / depth and amplitude image.

### Pre-requisites

Pre-requisites/dependencies:

  #### OpenCV python module

    #pip install opencv-python

### How to Run

Command to run the program:

```    
#python distancePlusAmplitude.py
```

Depth map and amplitude image will be showing in separate windows.

## `distancePlusGrayscale.py`

### What this demonstrates

The sample program demonstrates acquiring frames with both distance / depth and grayscale image.

### Pre-requisites

Pre-requisites/dependencies:

  #### OpenCV python module

    #pip install opencv-python

### How to Run

Command to run the program:

```
#python distancePlusGrayscale.py
```  

Depth map and grayscale image will be showing in separate windows.
