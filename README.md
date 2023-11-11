# ANPR-Model-For-License-Plate-Detection

The use of vehicles is increasing in today’s era, making traffic control challenging. Manually storing and maintaining vehicle records is difficult. An Automatic Number Plate Recognition (ANPR) System can be used for better control of vehicles and for storing and maintaining vehicle records automatically.

## How to Run

In our solution, we are using WiFi and Raspberry Pi to send photos back to the model from anywhere in the campus. The main motive behind this is to set up the model on the server, and we just need to install a camera connected to WiFi to run ANPR on each camera connected to the Raspberry Pi.
<img src="/img/architecture.jpg" alt="architecture" width="500" height="300">

1. **Install Requirements:**
   - Navigate to the `Code` folder.
   - Install the requirements using the following command:

     ```bash
     pip install -r requirements.txt
     ```

   - Note: You may need our version of the `builder.py` if the newer version is not compatible.

2. **Setting up Raspberry Pi:**
   - Put the server code on your Raspberry Pi.
   - Map the WiFi IP address on your Raspberry Pi.

3. **Get Live Video Feed:**
   - Use the IP address obtained in the previous step to access the live video feed from the Raspberry Pi.
   - The video feed is then passed to our model for processing.

<p>First run the server on Raspberry Pi then run 'Automatic Number Plate Detection.ipynb' to run</p>
## Additional Notes
  -  Read PPT and paper for more information

## Testing
 <!-- adding testing img -->
   <img src="/img/testing.jpg" alt="testing" width="500" height="300">

## Results
   <!-- adding results img -->
   <img src="/img/results.jpg" alt="results" width="500" height="300">


