---
title: "Exporting to HTML"
id: 1500009568082
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568082-Exporting-to-HTML
updated_at: 2021-07-24T05:54:40Z
---

# Exporting to HTML

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568122-Exporting-to-Logi-JReport-Result)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589381-Exporting-to-PDF)

# Exporting to HTML

To export the results of a report to an HTML file, follow the steps below:

1. Open the report that you want to export.
2. Select **File** > **Export**  > **To HTML**.
3. In the [Web Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009565542-Web-Wizard-Dialog), specify the settings as required.
4. When done, select **Finish** to generate the file.

The following example shows you how to export the results of a report to HTML format and view the exported file via a web browser, taking the sample report Banded\_Link.cls in SampleReports.cat as an example:

1. Select **File** > **Open**.
2. In the Open Report dialog, select the **Browse** button to open the catalog file **SampleReports.cat** in `<install_root>\Demo\Reports\SampleReports`, then open **Banded\_Link.cls** in the catalog.
3. Select **File** > **Export**  > **To****HTML** to open the Web Wizard.
4. In the Report tab, check the **Multiple Files** radio button.
5. Specify the web page name as required. Here we use the default one Banded\_Link\_Product Sales by Country. Make sure that Drilldown and TOC are checked.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893841815/frmt_expt_html1.gif)
6. In the Directory tab, specify where the exported result files will be saved. Here we save them in the default directory `C:\Logi JReport\Designer\Demo\Reports\SampleReports\`.
7. In the Chart Applet tab, select **Image Chart** > **GIF**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893842071/frmt_expt_html2.gif)
8. Select **Finish**.
9. In the Enter Parameter Values dialog, select **Default** to generate the results using the default parameter values.
10. Open the directory `C:\Logi JReport\Designer\Demo\Reports\SampleReports\` and find the exported files.
11. Open the file **Banded\_Link\_Product Sales by Country\_1.html**.
12. The Table of Contents (TOC) is displayed in the left panel, including the names of groups and subgroups. If you select a group, the relative contents will be shown in the right panel.
13. Since Drilldown is checked when exporting the report, you can drill down on a summary by placing the mouse pointer over the summary and selecting it when the mouse pointer becomes a hand.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404893842327/frmt_expt_html3.gif)

    Note that summaries should be inserted into your report in advance. They cannot be hidden or suppressed; otherwise you will not be able to get drilldown files.

**Notes:**

* When exporting a multi-page report to HTML, you can localize the page navigation link names. For detailed information, refer to [Localizing the Page Navigation Links in HTML Report Outputs](https://devnet.logianalytics.com/hc/en-us/articles/1500009568542-Localizing-Page-Navigation-Links-in-HTML-Report-Outputs).
* Multimedia and shapes (except for straight lines and boxes) in reports cannot be exported to HTML.
* For mainly meeting the requirements from voice agents used by people with eyesight disabilities, Logi JReport supports exported tables/crosstabs in the HTML data table format with SCOPE=Row/Column to get a section 508 compliant result. For detailed descriptions, refer to [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/1500009562542-Accessibility).
* After you export a report to an HTML file, you may view it with charts in a web browser. If that, you must ensure that the chart can be displayed correctly, make sure that you have enabled Additional Unsigned Permissions in the web browser.
  Moreover, if Applet Chart in the Web Wizard is checked and you use Google Chrome, it can be viewed only when NPAPI is enabled for the web browser. To do this, you need to type **chrome://flags/** in the address bar of the web browser, then scroll down and set Enable NPAPI Mac, Windows to **Enable**.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568122-Exporting-to-Logi-JReport-Result)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589381-Exporting-to-PDF)
