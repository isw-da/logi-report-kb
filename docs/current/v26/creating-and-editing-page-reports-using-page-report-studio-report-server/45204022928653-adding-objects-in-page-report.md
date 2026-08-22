---
title: "Adding Objects in Page Report"
id: 45204022928653
section: "Creating and Editing Page Reports Using Page Report Studio Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204022928653-Adding-Objects-in-Page-Report
updated_at: 2026-04-30T14:10:37Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Adding Objects in Page Report 

You can add labels, images, banded objects, tables, crosstabs, charts, special fields, and web controls to page reports. This topic describes how you can insert objects in page reports and where you can place the objects.

However, for page reports that you created in Report Designer, you can add objects to them only when the corresponding catalog contains business views.

You need a Report Live license for Server to use this feature. For more product information, including new purchases and upgrades, contact US Sales or UK Sales.
    

Object placement

You can place objects within banded objects, tables, tabulars, as well as onto an empty area of a report. The following table lists the report areas that are valid targets for the various objects, listed on the left.

|  | Report Layout Area |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Object | Page Header/Footer | Report Header/Footer | Report Body | Banded Detail | Banded Page Header/Footer | Banded Header/Footer | Banded Group Header/Footer | Table Cell | Tabular Cell |
| Banded object | Y | N | Y | Y | Y | Y | Y | N | Y |
| Chart | Y | Y | Y | Y | Y | Y | Y | N | Y |
| Crosstab | Y | Y | Y | Y | Y | Y | Y | N | Y |
| Table | Y | Y | Y | Y | Y | Y | Y | N | Y |
| Group object | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Detail object | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Aggregation object | N | N | Y | N | N | Y | Y | N | N |
| Formula | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Label | Y | N | Y | Y | Y | Y | Y | Y | Y |
| Special field | Y | N | Y | Y | Y | Y | Y | Y | Y |
| Image | Y | N | Y | Y | Y | Y | Y | Y | Y |
| Web control | Y | Y | Y | Y | Y | Y | Y | N | Y |

To add an object into a report:

- Navigate to Menu > Insert, then select the object you want to add.  

- Select the destination in the report where you want to add the object.
    
- If you specify to add a label, Server inserts a label there. Edit the text of the label and format it.

- If you specify to add a banded object, table, crosstab, or chart, Server displays the corresponding component wizard. Specify the settings in the wizard. For more information, see the specific topic in Creating Page Reports.When you insert a table, crosstab, chart, or banded object into the banded header panel, banded footer panel, group header panel, or group footer panel of a banded object, you can make it inherit the dataset of the parent banded object by selecting Inherit from the Parent instead of a business view or dataset. By inheriting the parent's dataset, the report becomes powerful. For example, if you want to automatically filter a chart by the group of the parent banded object, you can put it in the group panel in the banded object and make it inherit the dataset of its parent, then Server replicates the chart for each group in the parent. In addition, having data components inherit the dataset of the parent banded objects whenever possible will have a dramatic effect on the performance of your reports.

- If you specify to add a special field, Server inserts the special field there. For more information, see Special Fields in the Report Designer Guide.

- If you specify to add a parameter control, parameter form control, or filter control, Server displays the corresponding insert control dialog box. For more information, see Applying Web Controls in Page Report. 

- If you specify to add a navigation control, Server inserts a navigation control there. For more information, see Applying Web Controls in Page Report.

- 
If you specify to add an image, Server displays the Insert Image dialog box.
	 Specify the source of the image file and the image you want, then select OK. 
        

- 
Local File
Select this option if you want to use an image in the local disk. Then in the File Name text box, type the path and name of the image file in the local file system, or select Browse to locate the image file.

- 
Web URL
          Select this option if you want to use an image via URL. Then in the Image URL text box, type the URL of the image file. Server stores the latest 10 typed URLs in the drop-down list.
If your Report Server is in an intranet, to access the image via URL, you need to add the parameters -Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX to the server's startup file JRServer.bat in <install_root>\bin. 

- 
Library
          Select this option if you want to use an image in the server image library. Then select an image from the My Images box, which lists the images you have once inserted into reports.

Alternatively, you can also use the Toolbox panel to add objects other than special fields into a report by dragging them from the panel to the destination.
