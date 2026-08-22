---
title: "Previewing Reports"
id: 1500010101341
section: "Creating Datasets and Designing Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010101341-Previewing-Reports
updated_at: 2021-07-23T19:16:50Z
---

# Previewing Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101381-Saving-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062762-Editing-Reports)

# Previewing Reports

In the process of designing a report, you can preview it at any time. Designer supports previewing reports in Logi Report format. For page reports and web reports, you can also preview them in formats such as HTML, PDF, and Excel. This topic describes how you can preview a report in different formats.

When previewing a report,

* If it contains parameters, Designer prompts you to [specify values for the parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500010061282-Specifying-Parameter-Values).
* If you design it with [National Language Support](https://devnet.logianalytics.com/hc/en-us/articles/1500010099641-Applying-National-Language-Support), you can specify the language in which you want the report to display by selecting the language from the **Language** drop-down menu on the **Home** or **View** menu tab.
* If it [applies a style group](https://devnet.logianalytics.com/hc/en-us/articles/1500010062802-Applying-Styles-to-Reports), Designer prompts you to select the style group to use.

This topic contains the following sections:

* [Previewing a Report in Logi Report Format](#LogiFormat)
  + [Previewing Web Reports](#Web)
  + [Previewing Library Components](#LC)
  + [Previewing 2-D Bar, Bench, Line, Area, and Stock Charts](#Chart)
  + [Previewing Banded Objects in Page Reports](#Banded)
* [Previewing a Report in Other Formats](#Other)

## Previewing a Report in Logi Report Format

To preview a report in the Logi Report format, just select the **View** tab, which causes Logi Report Engine to run the report (for more information about the options in the View tab, see [Design/View Area](https://devnet.logianalytics.com/hc/en-us/articles/1500010062862-Design-View-Area)). Designer then shows the result in the viewer. To optimize performance, Designer displays the report pages before Logi Report Engine completely generates them.

You can make use of the following features when previewing different types of reports in the Logi Report format.

### Previewing Web Reports

When previewing a web report in the Logi Report format, if you have set the [Prefetch](https://devnet.logianalytics.com/hc/en-us/articles/1500010099841-Business-View-Properties#Prefetch) property of at least one business view used by the report to true, the **View Result Without Prefetch** checkbox is available at the top right corner of the Design/View area. By default this option is unselected and the view result is that when Prefetch=true works. If you select this option and then select the View tab, you can preview the scheduled result of the report which ignores Prefetch=true and therefore may be different from the default view result.

### Previewing Library Components

When previewing a library component in the Logi Report format, by default, Designer only displays the result of the data component in the library component. You cannot preview the other parts like the configuration panel. If you want to preview the effect when the library component is published to Server and inserted into a dashboard, select the **As Dashboard Component** checkbox on the top-right corner of the View tab, then the title bar of the library component displays and you can select ![Show button](https://devnet.logianalytics.com/hc/article_attachments/4404856820503/btn_show.gif) on the title bar to open the configuration panel of the library component and preview the objects in it.

![Preview Library Component](https://devnet.logianalytics.com/hc/article_attachments/4404856820759/rpt_prvw_lc.gif)

### Previewing 2-D Bar, Bench, Line, Area, and Stock Charts

When previewing a 2-D chart of the Bar, Bench, Line, Area, or Stock type in the Logi Report format, you can select the values you are interested in to zoom them.

1. Drag the mouse from the start value to the end value you want to select.

   ![Preview Bar Chart](https://devnet.logianalytics.com/hc/article_attachments/4404848398487/rpt_prvw_cht1.gif)
2. Release the mouse. Designer zooms in the selected values. If you equip the chart with a [scrollbar](https://devnet.logianalytics.com/hc/en-us/articles/1500010057142-Creating-Scrollable-Charts), Designer adjusts the bar automatically at the same time.

   ![Zoomed Chart](https://devnet.logianalytics.com/hc/article_attachments/4404856821015/rpt_prvw_cht2.gif)
3. To go back to the initial state of the chart, select the arrow at the upper right corner of the chart paper.

### Previewing Banded Objects in Page Reports

When previewing a banded object in a page report in the Logi Report format, you are able to dynamically sort the records and show details of aggregate level fields.

* **Dynamic sort**  
  You can sort the records in a banded object dynamically in the View tab. To do this, point to the field you want to sort, then right-click the field and select the option **Sort Ascending** or **Sort Descending** from the shortcut menu.
* **Showing aggregation detail**  
  If the banded object uses a query resource, you can show details of aggregate level fields in it. Showing detail is possible where there is a summary for a group. For example, if a banded object is grouped by City, and applies a summary on the group. When previewing the banded object, if you point the mouse at the total sales for a city, it turns into a small hand. Select on the total, and Designer displays the detail report for the selected city.

  ![Preview Banded Object](https://devnet.logianalytics.com/hc/article_attachments/4404856821271/rpt_prvw_bdobj1.gif)![Show Aggregation Detail](https://devnet.logianalytics.com/hc/article_attachments/4404848402071/rpt_prvw_bdobj2.gif)

  By default, in cases like the above, Logi Report's convention is to hide the detail panel of each group and only show it in a detail report. To do this, select the detail panel, go to the Report Inspector and set its **Invisible** property to **true** (make sure the Suppress property is false). Then view the banded object again, and it shows without details. If you want to see the details of a certain city, point the mouse at the city's total sales, when the mouse turns into a small hand, select on the total, and the detail report for the city displays.

  ![Preview Banded Object](https://devnet.logianalytics.com/hc/article_attachments/4404856821783/rpt_prvw_bdobj3.gif)![Show Aggregation Detail](https://devnet.logianalytics.com/hc/article_attachments/4404848402071/rpt_prvw_bdobj2.gif)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) After some modifications in the design area, if you find Designer displays the report result very quickly and does not apply the changes in view mode, this means you need to select the **Refresh Data** button ![Refresh Data button](https://devnet.logianalytics.com/hc/article_attachments/4404848383767/btn_refresh.gif) on the toolbar to re-run your report.

## Previewing a Report in Other Formats

For page reports and web reports, Designer also enables you to preview them in the following formats: Page Report Result/Web Report Result, HTML, PDF, Excel, Text, RTF, XML, and PostScript. To do this, select **View** > **Preview As** and then select a format from the drop-down menu. If you select Page Report Result/Web Report Result, Designer opens the report in Page Report Studio/Web Report Studio. When you select any of the other formats, Designer exports the report to a temporary file of the selected format which is then automatically opened by the appropriate application. Designer removes the temporary file when you exit it. If you want to save the file so that you can review it at any time, use the [Export](https://devnet.logianalytics.com/hc/en-us/articles/1500010060902-Exporting-Report-Result) feature instead.

You should pay attention to the following when using the Preview As feature:

* The function of previewing a report in the Page/Web Report Result format is enabled only if you have selected the option "Server for Previewing Reports" when installing Designer.
* Previewing a web report in Web Report Result or a page report that uses business views in Page Report Result requires that you have a Live license for your Server.
* The first time when you preview a report in Page/Web Report Result, the preview Server that is included with Designer has to be started so it is slow. After the first time, the preview is much faster.
* The preview Server is a web ad hoc disabled Server. It supports only one user and one report concurrently. Therefore, when you close the report you are previewing, you should use the exit button of Web/Page Report Studio instead of the browser's. In this way, you can release the user session you occupy at the same time, so that you are able to preview another report later.
* Designer and the preview Server are running in two separated JVMs. The preview Server applies `-Djreport.url.encoding=UTF-8` in the startup batch file and this setting covers URL encoding/decoding. Therefore, when you preview a report in Page/Web Report Result format, if the name of the report or its report or catalog file contains non-Latin characters, you need to add `-Djreport.url.encoding=UTF-8` into the startup batch file of Designer as well; otherwise, the preview fails.
* Make sure you have append the JDBC driver's class path to setenv.bat in `<install_root>\server\bin.`
* If the report contains [user-defined objects](https://devnet.logianalytics.com/hc/en-us/articles/1500010057462-Working-with-UDOs) (UDO), to have them work correctly in the preview Server, you need to compile your Java files again using report.jar and JREngine.jar in the <install\_root>\server\lib directory, modify the udo.ini file in <install\_root>\server\lib and append the classes to the class path of JRServer.bat in `<install_root>\server\bin` (make sure that the path of the file JREngine.jar is before that of the file report.jar).
* If the report contains [user-defined data sources](https://devnet.logianalytics.com/hc/en-us/articles/1500010095301-Using-User-Defined-Data-Sources) (UDS) or [user-defined formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010099441-Using-User-Defined-Formula-Functions) (UDF), you can use the classes you have compiled for using in Designer, but remember to append the classes to the class path of setenv.bat in `<install_root>\server\bin`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101381-Saving-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062762-Editing-Reports)
