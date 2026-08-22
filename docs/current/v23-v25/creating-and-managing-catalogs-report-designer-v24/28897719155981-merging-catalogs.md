---
title: "Merging Catalogs"
id: 28897719155981
section: "Creating and Managing Catalogs - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897719155981-Merging-Catalogs
updated_at: 2024-09-30T09:10:36Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Merging Catalogs

You can make two catalogs that have the same name merged by saving reports of one catalog to another directory in which a catalog of the same name already exists. This topic describes how you can merge two catalogs and deal with the differences between the catalogs.

When merging catalogs,   Designer checks for the differences between the two catalogs, for example, resources that have the same mapping names in the two catalogs may conflict with each other because they have different property values. If there are differences between the two catalogs, based on the Merge Catalog Options setting in the Options dialog box, Designer either identifies them and prompts the Merge dialog box or ignores them and remains them in the target catalog. By default, Designer identifies the critical differences that can cause Report Engine to fail in running reports and marks them in the Merge dialog box. 

To merge catalogs

- Open a report in the catalog that you want to merge with another catalog.

- Navigate to File > Save To.

- In the Save To dialog box, choose a directory to save the report, where a catalog with the same name as the current catalog already exists.

- If you set Merge Catalog Options as Identify All Differences or Identify Critical Differences in the Options dialog box and there are conflicting resources between the two catalogs, Designer displays the Merge dialog box. The dialog box lists all the resources referenced by the report with the conflicting resources marked. 

- Select a conflicting resource, then select Differences to view the differences of the resource between the source catalog and target catalog in the Property Differences dialog box. Designer lists the property values of the conflicting resource from the two catalogs  in the dialog box with any differences highlighted. You can select Previous or Next to go to the previous or next conflicting resource between the two catalogs. 

- To view the parent resources of the selected conflicting resource in the target catalog, select Target Relation. Designer displays the Target Relation dialog box showing the relation. Sometimes, a resource is marked in the Merge dialog box, but  the Property Differences dialog box shows no difference. In this case, you can use the Target Relation dialog box to get its parent resources and check whether the differences exist in the parent resources.   

- Select any of the following buttons to deal with the selected conflicting resource. 
 Designer does not activate certain button for specific resource type.
    
- 
Rename
Select to rename the resource and copies it to the target catalog with the new name.

- 
Replace
Select to use the resource from the source catalog to replace that in the target catalog. This impacts the reports that use this resource in the target catalog.

- 
Skip
Select to keep the values in the target catalog for the resource. This impacts the report that uses this resource in the source catalog.

- Select Merge after you settle all conflicts. Designer then saves the report according to the changes you have made.  

After you merge two catalogs via the Merge dialog box, you may need to test all the reports in both catalogs to ensure they can work properly. 

 Designer checks parameters based on the whole catalog. For example, assume there is a parameter Param1 in Data Source 1 of the source catalog, and there is also a parameter Param1 in Data Source 2 in the target catalog. Designer checks these two parameters in different data sources as a conflicting resource. You must rename the parameter in order to get a correct result.

Previous Topic  Next Topic
