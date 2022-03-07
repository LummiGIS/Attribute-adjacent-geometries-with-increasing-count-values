'''
This script will populate an attribute column with increasing number values based spatial adjacency.
Given an existing user defined attribute (type short or long) and given that one of those records is attributed
with a value of 1 and all other records are 0, this tool will identify the adjacent objects touching 1 and attribute them with a 2.
This process repeats with item 2 until all touching records are populated with number values.  

Author:  Gerry Gabrisch, GISP
Lummi Nation GIS Division
geraldg@lummi-nsn.gov

Use:
1. Create a new attribute in your data as type short or long as needed.
2. Populate your starting line or polygon feature with a value of 1.
3. Change in_fc to the path to your data.
4. Chance in_field to the name of your attribute.
5. Copy and paste the altered code into an ArcGIS Pro Python window or run in your favorite Python IDE which is pointing to the arcpy Python installation.

'''
import sys
import traceback
import arcpy

try:
    
    #The input feature class.  The user must have write permissions to these data.
    in_fc = r'Z:\GISpublic\GerryG\Python3\AttributeAdjacetGeometries\testdata\test_data.shp'
    #The existing attribute (type must be integer)
    in_field = 'adjacent'
    
    
    
    counter = 1
    
    arcpy.AddMessage("Attribute Adjacent Geometries by Gerry Gabrisch, geraldg@lummi-nsn.gov...")
   
    in_fc1 = arcpy.MakeFeatureLayer_management(in_fc)
    
    results = arcpy.management.GetCount(in_fc1).getOutput(0) 
    arcpy.AddMessage('Total objects to attribute =  ' + str(results))
    
    
    def recursive_select(in_fc1, counter, in_field):
        
        arcpy.AddMessage('working, please wait...')
        
        #Make the SQL statement
        query = '\"'+ in_field + '\"' +  ' = ' + str(counter)
        
        #Select by attribute that record with the correct counter value
        arcpy.management.SelectLayerByAttribute(in_fc1, 'NEW_SELECTION', query)
        
        #Once all the records are attributed there will be no more features to
        #select.  If so, end this function by returning nothing...
        if arcpy.management.GetCount(in_fc1).getOutput(0) == '0':
            arcpy.AddMessage("All records are calculated...")  
            return        
        
        #Select the geometries that touch the selected geometry
        arcpy.SelectLayerByLocation_management(in_fc1, "INTERSECT", in_fc1, "", "NEW_SELECTION")

        #Reselect those records with a value of 0
        query0 = '\"'+ in_field + '\"' +  ' = ' + '0'
        arcpy.management.SelectLayerByAttribute(in_fc1, 'SUBSET_SELECTION', query0)
        
        #Calculate the fields to those adjacent objects
        arcpy.CalculateField_management(in_fc1, in_field, counter + 1)
        #Clear the selection...
        arcpy.management.SelectLayerByAttribute(in_fc1, 'CLEAR_SELECTION')
        
        #Up the count by one
        counter +=1
        #Make recursive function call...
        recursive_select(in_fc1,  counter, in_field)
    
    recursive_select(in_fc1,  counter, in_field)
    
   
    arcpy.AddMessage("done")
    
    
except arcpy.ExecuteError: 
    msgs = arcpy.GetMessages(2) 
    arcpy.AddError(msgs)  
    arcpy.AddMessage(msgs)
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
    msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
    arcpy.AddError(pymsg)
    arcpy.AddError(msgs)
    arcpy.AddMessage(pymsg + "\n")
    arcpy.AddMessage(msgs)
