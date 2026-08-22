---
title: "Previewing Reports"
id: 1500010070941
section: "Creating Datasets and Designing Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010070941-Previewing-Reports
updated_at: 2021-07-24T10:37:43Z
---

# Previewing Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010034882-Saving-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010070821-Editing-Reports)

# Previewing Reports

In the process of designing a report, you can preview it at any time. Logi JReport Designer supports previewing reports in Logi JReport format. For page reports and web reports, you can also preview them in formats such as HTML, PDF, Excel and so on.

When previewing a report,

* If it contains parameters, you will be prompted to [specify values for the parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500010033422-Specifying-Parameter-Values).
* If it is developed with [National Language Support](https://devnet.logianalytics.com/hc/en-us/articles/1500010033362-Applying-National-Language-Support), you can specify the language in which you want the report to display by selecting the language from the Language drop-down menu on the Home or View menu tab.
* If it [applies a style group](https://devnet.logianalytics.com/hc/en-us/articles/1500010034922-Applying-Styles), you will be prompted to select the style group to use.

Below is a list of the sections covered in this topic:

* [Previewing a Report in JReport Format](#jrfmt)
* [Previewing a Report in Other Formats](#other)

## Previewing a Report in JReport Format

To preview a report in Logi JReport format, just select the **View** tab, which will cause Logi JReport Engine to run the report (for details about the options in the View tab, see [Design/View Area](https://devnet.logianalytics.com/hc/en-us/articles/1500010071021-Design-View-Area)). The result is then shown in the viewer. To optimize performance, Logi JReport Designer displays report pages before they have been completely generated.

**Previewing web reports**

When previewing a web report in Logi JReport format, if the [Prefetch](https://devnet.logianalytics.com/hc/en-us/articles/1500010069061-Business-View-Properties#Prefetch) property of at least one business view used by the report is set to true, you will find the View Result Without Prefetch checkbox at the top right corner of the design/view area. By default this option is unchecked and the view result is that when Prefetch=true works. If you check this option and then select the View tab you can preview the scheduled result of the report which ignores Prefetch=true and therefore may be different from the default view result.

**Previewing library components**

When previewing a library component in Logi JReport format, by default only the result of the data component in the library component is displayed. The other parts like the configuration panel cannot be previewed. If you want to preview the effect when the library component is published to Logi JReport Server and inserted into a dashboard, check the **As Dashboard Component** checkbox on the top-right corner of the View tab, then the title bar of the library component will be shown and you can select ![Show button](https://devnet.logianalytics.com/hc/article_attachments/4404901123223/btn_show.gif) on the title bar to display the configuration panel of the library component and preview the objects in it.

![Preview Library Component](https://devnet.logianalytics.com/hc/article_attachments/4404909119511/rpt_prvw_lc.gif)

**Previewing 2-D bar, bench, line, area and stock charts**

When previewing a 2-D chart of the Bar, Bench, Line, Area or Stock type in Logi JReport format, you can select the values you are interested in to have them zoomed.

1. Drag the mouse from the start value to the end value you want to select.

   ![Preview Bar Chart](https://devnet.logianalytics.com/hc/article_attachments/4404901123479/rpt_prvw_cht1.gif)
2. Release the mouse. The selected values will be zoomed in. If the chart is equipped with a [scrollbar](https://devnet.logianalytics.com/hc/en-us/articles/1500010063661-Creating-Scrollable-Charts), the bar will be adjusted automatically at the same time.

   ![Zoomed Chart](https://devnet.logianalytics.com/hc/article_attachments/4404909119767/rpt_prvw_cht2.gif)
3. To go back to the initial state of the chart, select the arrow at the upper right corner of the chart paper.

**Previewing banded objects in page reports**

When previewing a banded object in a page report in Logi JReport format, you are able to dynamically sort the records and show details of aggregate level fields.

* **Dynamic sort**  
   You can sort the records in a banded object dynamically in the View area. To do this, point to the field you want to sort, then right-click the field and select the option **Sort Ascending** or **Sort Descending** from the shortcut menu.
* **Showing aggregation detail**  
   If the banded object is created using a query resource, you can show details of aggregate level fields in the banded object. Showing detail is made possible where there is a summary for a group. For example, if a banded object is grouped by City, and applies a summary on the group. When previewing the banded object, if you point the mouse at the total sales for a city, it turns into a small hand. Select on the total, and the detail report for the selected city is displayed.

  ![Preview Banded Object](https://devnet.logianalytics.com/hc/article_attachments/4404909120023/rpt_prvw_bdobj1.gif)![Show Aggregation Detail](https://devnet.logianalytics.com/hc/article_attachments/4404901123735/rpt_prvw_bdobj2.gif)

  By default, in cases like the above, Logi JReport's convention is to hide the detail panel of each group and only show it in a detail report. To do this, select the detail panel, go to the Report Inspector and set its Invisible property to **true** (make sure the Suppress property is false). Then view the banded object again, and it will be shown without details. If you want to see the details of a certain city, point the mouse at the city's total sales, when the mouse turns into a small hand, select on the total, and the detail report for the city will be displayed.

  ![Preview Banded Object](https://devnet.logianalytics.com/hc/article_attachments/4404901123991/rpt_prvw_bdobj3.gif)![Show Aggregation Detail](https://devnet.logianalytics.com/hc/article_attachments/4404901123735/rpt_prvw_bdobj2.gif)

**Tip:** After some modifications in the design area, if you find the report is shown very quickly and the changes are not applied in view mode, this means you need to select the Refresh Data button ![Refresh Data button](https://devnet.logianalytics.com/hc/article_attachments/4404909116183/btn_refresh.gif) on the toolbar to re-run your report.

## Previewing a Report in Other Formats

For page reports and web reports, Logi JReport also allows you to preview them in the following formats: Page Report Result/Web Report Result, HTML, PDF, Excel, Text, RTF, XML and PostScript. To do this, select **View** > **Preview As** and then select a format from the drop-down menu. If Page Report Result/Web Report Result is selected, the report will be opened in Page Report Studio/Web Report Studio. When any of the other formats is selected, the report will be exported to a temporary file of the selected format which will then be automatically opened with the appropriate application. The temporary file will be removed when you exit Logi JReport Designer. If you want the file to be saved so that you can review it at any time, use the [Export](https://devnet.logianalytics.com/hc/en-us/articles/1500010068401-Exporting-Report-Result) feature instead.

You should pay attention to the following when using the Preview As feature:

* The function of previewing a report in Page/Web Report Result format is enabled only if you have checked the option Server for Previewing Reports when installing Logi JReport Designer.
* Previewing a web report in Web Report Result or a page report creating using business views in Page Report Result requires that you have a Logi JReport Live license for your Logi JReport Server.
* The first time when you preview a report in Page/Web Report Result, the preview server that is included with Logi JReport Designer has to be started so it will be slow. After the first time the preview will be much faster.
* The preview server is a web ad hoc disabled server, and it supports only one user and one report concurrently. Therefore, when you close the report you are previewing, you should use the exit button of Web/Page Report Studio instead of the browser's. In this way, you can release the user session you occupy at the same time, so that you are able to previewing another report later.
* Logi JReport Designer and the preview server are running in two separated JVMs. The preview server applies `-Djreport.url.encoding=UTF-8` in the startup batch file and this setting covers URL encoding/decoding. Therefore, when you preview a report in Page/Web Report Result format, if the name of the report or its report or catalog file contains non-Latin characters, you need add `-Djreport.url.encoding=UTF-8` into the startup batch file of Logi JReport Designer as well; otherwise the preview will fail.
* Make sure the JDBC driver's class path has been appended to setenv.bat in `<install_root>\server\bin.`
* If the report contains [user defined objects](https://devnet.logianalytics.com/hc/en-us/articles/1500010063981-UDOs) (UDO), to have them work correctly in the preview server, you need to compile your Java files again using report.jar and JREngine.jar in the `<install_root>\server\lib` directory, modify the udo.ini file in `<install_root>\server\lib` and append the classes to the class path of JRServer.bat in `<install_root>\server\bin` (make sure that the path of the file JREngine.jar is before that of the file report.jar).
* If the report contains [user defined data sources](https://devnet.logianalytics.com/hc/en-us/articles/1500010064481-User-Defined-Data-Sources) (UDS) or [user defined formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010033242-User-Defined-Formula-Functions) (UDF), you can use the classes you have compiled for using in Designer, but remember to append the classes to the class path of setenv.bat in `<install_root>\server\bin`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010034882-Saving-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010070821-Editing-Reports)
