# Sentinel ToF Camera python SDK

## Before run the examples, make sure your Sentinel ToF Camera plugged in, and current user has permission to read the serial port. For Linux system:

sudo chmod a+rw /dev/ttyACM0

### Pre-requisites

  #### pyserial, use to connect to Sentinel ToF Camera via serial port

    #pip install pyserial
    or
    #pip3 install pyserial

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
```

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
