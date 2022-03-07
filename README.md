# Attribute-adjacent-geometries-with-increasing-count-values


This script will populate an attribute column with increasing number values based spatial adjacency.
Given an existing user defined attribute in the feature class (type short or long) and given that one of those records is attributed
with a value of 1 and all other records are 0, this tool will identify the adjacent objects touching 1 and attribute them with a 2.
This process repeats with item 2 until all touching records are populated with number values.  
This script requires and installation of ArcGIS.

Use:
1. Create a new attribute in your data as type short or long as needed.
2. Populate your starting line or polygon feature with a value of 1.
3. Change in_fc to the path to your data.
4. Chance in_field to the name of your attribute.
5. Copy and paste the altered code into an ArcGIS Pro Python window or run in your favorite Python IDE which is pointing to the ArcPro Python interpreter.



Here is a river feature class divided into 1000m sections and attributed with increasing values from the start feature.
![image](https://user-images.githubusercontent.com/68295520/157117516-f60d6d96-107d-42a7-95b6-44f87e39fa60.png)


The tool will handle branches as well where each branch values is the count away from the source feature.
![image](https://user-images.githubusercontent.com/68295520/157117861-a42c1bbe-db7c-40b5-b71c-2d202da28ae9.png)
