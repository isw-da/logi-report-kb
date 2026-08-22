---
title: "Exporting to Applet"
id: 1500009589241
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589241-Exporting-to-Applet
updated_at: 2021-07-24T05:54:43Z
---

# Exporting to Applet

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568062-Exporting-to-Fax)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592601-Publishing-and-Downloading-Resources)

# Exporting to Applet

Logi JReport Designer can collaborate with a web server by exporting a report as an applet to a server. After publishing it to the server, you can then retrieve it by accessing the server.

Below is a list of the sections covered in this topic:

> * [Exporting the Report Results as an Applet to a Server](#Export)
> * [Viewing the Exported Result File](#View)

## Exporting the Report Results as an Applet to a Server

To export the results of a report as an applet to a server, follow the steps below:

1. In Logi JReport Designer, open the report you want to export.
2. When a page report is opened, on the report tab bar, select the tab that represents the required report tab. Only the active report tab in a page report can be exported.
3. Select **File** > **Export**  > **To****Applet**.
4. In the Applet Setting dialog, key in the server name and port number in the Server Name and Port text boxes.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893843351/apltsting.gif)
5. Check **Run Linked Report** if you want to include the reports that is linked with the report (not including the detail reports) in the exported applet result. If you are only interested in the primary report, leave this option unchecked. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.
6. Select **OK**. Then in the Export to Applet dialog, specify the directory and file name respectively.

   For example, browse to the location where you want to save the file, type exapplet.htm as the file name, and then select **Save**. The file exapplet.htm and the report result exapplet.rst will then be generated.

## Viewing the Exported Result File

Before viewing the exported result file of Logi JReport using a web browser, you first need to make sure that your web server supports applets. Then,

1. Copy the file viewer12.jar in `<se``rver_install_root>\lib` to the document root directory of the web server.
2. Copy the result file \*.rst and \*.html generated when exporting to any directory of the web server. For example, copy A.rst and A.html into `<webserver_install_root>\test`.
3. Edit A.html (with a text editor) to make sure that all paths are valid. For example, change:
   * codebase="/" (which refers to the location of viewer12.jar)
   * value="/test/A.rst" (since we copied A.rst in `<webserver_install_root>\test`.)
   * width=800 height=600
4. Run the web browser with the web server to view the results.

**Notes:**

* Before you can view the results in a web browser, make sure you have enabled Additional Unsigned Permissions for the web browser and NPAPI is enabled for Google Chrome if you use this web browser. To do this, you need to type **chrome://flags/** in the address bar of the web browser, then scroll down and set Enable NPAPI Mac, Windows to **Enable**.
* Logi JReport Server also supports requesting the report result in an applet from a web browser.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568062-Exporting-to-Fax)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592601-Publishing-and-Downloading-Resources)
