---
title: "Previewing a Page Report"
id: 1500009592961
section: "Creating Datasets and Designing Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592961-Previewing-a-Page-Report
updated_at: 2021-07-24T05:53:47Z
---

# Previewing a Page Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592941-Managing-Report-Tabs-in-a-Page-Report)

# Previewing a Page Report

In the process of designing a page report, you can preview the report tabs in it at any time in Logi JReport format or other formats.

When previewing a page report tab,

* If it contains parameters, you will be prompted to specify values for the parameters in the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009586681-Enter-Parameter-Values-Dialog) dialog.
* If it is developed with [National Language Support](https://devnet.logianalytics.com/hc/en-us/articles/1500009589921-Applying-National-Language-Support), you can specify the language in which you want the report tab to display by selecting the language from the Language drop-down menu on the Home or View menu tab.

Below is a list of the sections covered in this topic:

> * [Previewing a Report Tab in Logi JReport Format](#jrfmt)
> * [Previewing a Report Tab in Other Formats](#other)

## Previewing a Report Tab in Logi JReport Format

To preview a report tab in Logi JReport format, just select the **View** tab, which then causes Logi JReport Engine to run the report tab. The result is then shown in the viewer. To optimize performance, Logi JReport Designer displays report pages before they have been completely generated. For details about the options in the View tab, see [Design/View area](https://devnet.logianalytics.com/hc/en-us/articles/1500009571082-Design-View-Area).

In addition, when previewing a banded object, you are able to dynamically sort the records and show details of aggregate level fields.

**Dynamic sort**

You can sort the records in a banded object dynamically in the View area. To do this, point to the field you want to sort, then right-click the field and select the option **Sort Ascending** or **Sort Descending** from the shortcut menu.

**Showing aggregation detail**

You can show details of aggregate level fields in a banded object. Showing detail is made possible where there is a summary for a group. For example, if a banded object has been grouped by City, and the group summary is on Cost. When previewing the banded object, if you point the mouse at the total cost sales for a city, it will turn into a small hand. Select on the total, and the detail report for the selected city will be displayed.

![Preview a report](https://devnet.logianalytics.com/hc/article_attachments/4404889287191/rpt_pgrpt_prvw1.gif)![Aggregation detail](https://devnet.logianalytics.com/hc/article_attachments/4404893806615/rpt_pgrpt_prvw2.gif)

By default, in cases like the above, Logi JReport's convention is to hide the detail panel of each group and only show it in a detail report. To do this, select the detail panel, go to the Report Inspector and set its Invisible property to **true** (make sure the Suppress property is false). Then view the banded object again, and it will be shown without details. If you want to see the details of a certain city, point the mouse at the city's total annual sales, when the mouse turns into a small hand, select on the total, and the detail report for the city will be displayed.

![Preview a report](https://devnet.logianalytics.com/hc/article_attachments/4404889287447/rpt_pgrpt_prvw3.gif)![Aggregation detail](https://devnet.logianalytics.com/hc/article_attachments/4404893806615/rpt_pgrpt_prvw2.gif)

**Note:** After some modifications in the design area, if you find the report tab is shown very quickly and the changes are not applied in view mode, this means you need to select the Refresh Data button ![](https://devnet.logianalytics.com/hc/article_attachments/4404893802519/btn_refresh.gif) on the toolbar to re-run your report tab.

## Previewing a Report Tab in Other Formats

Logi JReport also allows you to preview your report tab in the following formats: Page Report Result, HTML, PDF, Excel, Text, RTF, XML and PostScript. To do this, select **View** > **Preview As** and the select a format from the drop-down menu. If Page Report Result is selected, the report tab will be opened in Page Report Studio. When any of the other formats is selected, the report tab will be exported to a temporary file which will automatically be opened in the format with the appropriate application. The temporary file will be removed when you exit Logi JReport Designer. If you want the file to be saved so that you can review it at any time, use the [Export](https://devnet.logianalytics.com/hc/en-us/articles/1500009589221-Exporting-Report-Results) feature instead.

**Notes:**

* The function of previewing a report tab in Page Report Result format is enabled only if you have checked the option Server for Previewing Reports when installing Logi JReport Designer.
* The first time when you preview a report tab in Page Report Result, the preview server that is included with Logi JReport Designer has to be started so it will be slow. After the first time the preview will be much faster.
* The preview server is a web ad hoc disabled server, and it supports only one user and one report concurrently. Therefore, when you close the report you are previewing, you should use the exit button of Page Report Studio instead of the browser's. In this way, you can release the user session you occupy at the same time, so that you are able to previewing another report later.
* Logi JReport Designer and the preview server are running in two separated JVMs. The preview server applies `-DLogi JReport.url.encoding=UTF-8` in the startup batch file and this setting covers URL encoding/decoding. Therefore, when you preview a report tab in Page Report Result format, if the name of the report tab or its report or catalog file contains non-Latin characters, you need add `-DLogi JReport.url.encoding=UTF-8` into the startup batch file of Logi JReport Designer as well; otherwise the preview will fail.
* When previewing a report tab in Page Report Result format,
  + Make sure the JDBC driver's class path has been appended to setenv.bat in `<install_root>\server\bin.`
  + If the report tab contains some user defined objects (UDO), to have them work correctly in the preview server, you need to compile your Java files again using report.jar and JREngine.jar in the `<install_root>\server\lib` directory, modify the udo.ini file in `<install_root>\server\lib` and append the classes to the class path of JRServer.bat in `<install_root>\server\bin` (make sure that the path of the file JREngine.jar is before that of the file report.jar). For details, see [Creating a UDO Manually](https://devnet.logianalytics.com/hc/en-us/articles/1500009584501-Creating-a-UDO-Manually).
  + If the report tab contains some user defined data sources (UDS) or user defined formulas (UDF), you can use the classes you have compiled for using in Designer, but remember to append the classes to the class path of setenv.bat in `<install_root>\server\bin`.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592941-Managing-Report-Tabs-in-a-Page-Report)
