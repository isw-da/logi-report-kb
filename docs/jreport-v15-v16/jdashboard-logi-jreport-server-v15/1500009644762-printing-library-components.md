---
title: "Printing Library Components"
id: 1500009644762
section: "JDashboard Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644762-Printing-Library-Components
updated_at: 2021-07-24T20:55:17Z
---

# Printing Library Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669241-Exporting-Library-Components)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644682-Setting-a-Dashboard-as-the-Server-Home-Page)

# Printing Library Components

Library components visible in the page panel can be printed, for example, library components that were created using Logi JReport Designer and inserted into dashboards via the Resources panel.

To print the library components in a dashboard, select the ****Print**** button **![](https://devnet.logianalytics.com/hc/article_attachments/4404926628503/btn_print.gif)**on the toolbar, or select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926748951/btn_dshbrd_optn.gif) on the toolbar and select **Print** from the option list. Then in the [Print](https://devnet.logianalytics.com/hc/en-us/articles/1500009646202-Print) dialog, choose whether to use system layout or customize the layout. In the system layout, Logi JReport will calculate the positions of the library components in the dashboard following defined rules. If you are not satisfied with the system layout, you can customize the layout by yourself to determine the position of each library component and specify whether to print all the data of a table/crosstab or just the current page of the table/crosstab displayed in the dashboard. The customized layout can be saved for all users who can access the dashboard.

**To print using system layout:**

1. In the Print dialog, select **System Layout** from the Layout drop-down list.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926780439/prnt_sys.gif)

   The preview of the layout appears in the preview panel on the right. Sometimes you may find that the layout is a little different from what you see in the dashboard.
2. In the Resources box, select the library components you want to print. By default all printable library components are listed and selected.
3. The order of the library components in the Resources box determines the order in which they will be printed. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif) and ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif) to adjust the printing order if necessary.
4. Check the **Show Component Title** option if you want to show the library component titles in the printed result.
5. From the Printer drop-down list, select the printer to use to print the library component result. All the printers the web browser can access will be listed here. If you want to download the result to a PDF or HTML file and then use your local printer to print the file, select **Save as PDF** or **Save as HTML**.
6. If a printer is selected, select the **Properties** link to specify the printing properties in the [Printer Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009646222-Printer-Properties) dialog.
7. Define the number of copies you want to print accordingly.
8. Specify the page orientation and paper type for the printed result file. If necessary, select the **More Settings**  link to set more page properties such as paper size and margins in the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009670381-Page-Setup#Print) dialog.
9. Select the page navigation buttons on the toolbar of the preview panel to browse the pages if you want.
10. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926628503/btn_print.gif) on the toolbar to start printing. If Save as PDF or Save as HTML is selected in the Printer drop-down list, the result file of the library components is then opened in an associated program with which you can print the result to a printer.

**To customize the layout:**

1. In the Print dialog, select **Customize Layout** from the Layout drop-down list. You can also select an existing customized layout to modify it.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920585495/prnt.gif)
2. Do the same as described in steps 4 to 8 of the above system layout procedure.
3. In the Design tab, customize the layout of the library components, then preview it in the View tab. For how to customize the layout, refer to [Exporting by customizing layout](https://devnet.logianalytics.com/hc/en-us/articles/1500009669241-Exporting-Library-Components#Layout).
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926628503/btn_print.gif) on the toolbar to start printing. If Save as PDF or Save as HTML is selected in the Printer drop-down list, the result file of the library components is then opened in an associated program with which you can print the result to a printer.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669241-Exporting-Library-Components)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644682-Setting-a-Dashboard-as-the-Server-Home-Page)
