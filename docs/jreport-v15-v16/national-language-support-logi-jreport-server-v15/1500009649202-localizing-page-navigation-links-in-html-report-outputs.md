---
title: "Localizing Page Navigation Links in HTML Report Outputs"
id: 1500009649202
section: "National Language Support Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009649202-Localizing-Page-Navigation-Links-in-HTML-Report-Outputs
updated_at: 2021-07-24T20:53:57Z
---

# Localizing Page Navigation Links in HTML Report Outputs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673881-Running-NLS-Reports-Dashboards)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673821-Monitoring-Logi-JReport-Server-Guide-v15-Server)

# Localizing Page Navigation Links in HTML Report Outputs

When you schedule to publish a report to HTML format, or run it in Advanced mode in HTML format, you can localize the names of page navigation links in the HTML report outputs, such as First, Previous, Next, and Last, according to your requirements.

The localizing process is divided into three steps:

1. [Create a property file for the desired language](#Create).
2. [Enable the language for the report](#Enable).
3. [Apply the localized link names to HTML report outputs](#Apply).

## Creating the Property File

To localize the page navigation link names in HTML report outputs, a property file must be created first for the desired language. To do this:

1. Create the sub directories in `<server_install_root>\resources` as follows: `<server_install_root>\resources\report\languages\[language-locale]\properties`. For example, `C:\Logi JReport\Server\resources\report\languages\zh-cn\properties`.

   Select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009673861-NLS-at-Application-Level#Name) for more information about the naming criterion for language package folders.
2. Create a report.properties file in the properties directory.
3. Open the property file and copy the following contents to it:

   |  |
   | --- |
   | ``` # The following is the report properties file format that can localize the link names in HTML. 4000101=First 4000102=Prev 4000103=Next 4000104=Last 4000105=Back 4000106=Refresh 4000107=@CurrentPageNumber; of @TotalPageNumber; ``` |
4. Translate the text after = to the language specified by the folder name.

   **Note:** For the line "`4000107=@CurrentPageNumber; of @TotalPageNumber;`", you just need to translate "of" to the desired language. In the HTML outputs, @CurrentPageNumber will be replaced by the current page number, and @TotalPageNumber by the report total page number.
5. Save the property file with UTF-8 encoding.
6. Copy the property file to the `<jdk_install_root>\bin` directory.

   **Note:** You can just add the <jdk\_install\_root>\bin directory to your PATH instead of copying the file.
7. Convert the contents in the property file into Unicode using native2ascii.exe in `<jdk_install_root>\bin` by running the following command:

   `C:\jdk1.7.0_17\bin>native2ascii -encoding utf-8 report.properties > newreport.properties`

   **Note:** When you convert your property file to the same directory as the original one, you need to give it a new name instead of replacing the original in order to avoid problems.
8. Delete report.properties in `<server_install_root>\resources\report\languages\[language-locale]\properties` and copy newreport.properties in `<jdk_install_root>\bin` to it, then rename the property file back to report.properties.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Enabling the Language for the Report

When the property file is ready, the next step is to enable the language defined in the file for the required report.

1. Start Logi JReport Server and log onto the Logi JReport Administration page.
2. Browse to the row that the report is in, then select the **NLS Editor** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926691351/btn_srv_nlsedtr.gif) in the Control column.
3. In the NLS Editor dialog, specify a report and catalog version as required.
4. Select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) above the Language box, then in the Add Language dialog, choose the specified language and select **OK**.
5. Select **OK** in the NLS Editor dialog to confirm the settings.

Now the language will have been enabled for the report.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Applying the Localized Link Names to HTML Report Outputs

To apply the localized link names to HTML outputs of the specified report, follow the steps below:

1. Log onto the Logi JReport Console page and browse to the report.
2. Put the mouse pointer over the report row and select the **Advanced Run** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920423319/btn_srv_advrun.gif) or **Schedule** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920422295/btn_srv_schdl.gif) on the floating toolbar.
3. In the Format/General tab of the Advanced Run/Schedule dialog, check **Enable NLS** and select the specified language from the Using Language drop-down list.
4. Specify the other settings and finish the task. Then in the generated HTML outputs, you can see that the page navigation links are displayed in the language you defined for the property file.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673881-Running-NLS-Reports-Dashboards)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673821-Monitoring-Logi-JReport-Server-Guide-v15-Server)
