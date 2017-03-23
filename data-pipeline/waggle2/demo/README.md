# How to Use Waggle Data
Get the programs wag.py and wag2.py Using
```
wget https://raw.githubusercontent.com/waggle-sensor/beehive-server/master/data-pipeline/waggle2/demo/wag.py
wget https://raw.githubusercontent.com/waggle-sensor/beehive-server/master/data-pipeline/waggle2/demo/wag2.py

```
wag.py works with data in version 1 format - and will soon be deprecated.
wag2.py works with data in version 2 ("v2") format.

The documentation below will assume the user wants to work with v2 data.  To work with v1 data, simply substitute wag2.py with wag.py.

Using pip3, import the necessary libraries for python3:
```
pip3 install pandas
pip3 install bokeh
```
Open a terminal window (in linux) and start the *bokeh* server by typing:
```
bokeh serve
```
Leave that terminal running.  
Open a browser and navigate to
http://beehive1.mcs.anl.gov/
to see the list of all the nodes that ever sent data to the beehive server.
Click on the id of the node to see all the data that a node ever sent - grouped by date and version.
Choose the node(s) and date(s) whose data you would like to download and/or plot.

## Downloading Data into a CSV File
To download the data from the specified node(s) and specified date(s), type:
```
python3 wag2.py -id <node id list> -date <date list> -csv_out <csv filename>
```
where ```<node id list>``` is one or more node_id's from the beehive website;
```<date list>``` is the list of dates;
and ```csv filename``` is the name of the CSV file that will be created.
Note that the 1st line of the CSV file will contain a header, which is a
comma-separated list of columns.
The following lines will contain the comma-separated data.
For example, to save the data from the CDOT node named 00F, and id
0000001e0610b9fd, into a file named ```cdot00F.csv```, type:
```
python3 wag2.py -id 0000001e0610b9fd -date 2016-09-18 -csv_out cdot00F.csv
```
An example of multiple nodes and dates is:
```
python3 wag2.py -id 0000001e0610b9fd 	0000001e0610b9e7 -date 2016-09-17 2016-09-18 -csv_out cdot00F_028_Sept17_18.csv
```


## Plotting Data
To plot the data, simply omit the ```--csv_out <csv filename>``` parameter.  
NOTE: Only the 1st node in the list will have its data plotted,
due to resource limitations.

The plots will appear in a new tab in your browser.  Select the parameter you would like to see plotted (eg. "Concentration").  All sensors that store the selected parameter are plotted on the same graph.  Hide or show each sensor's data by toggling the button above the graph with the sensor's name.  Adjust the view/scope of the plot by using the tool buttons to the right of the plot.
