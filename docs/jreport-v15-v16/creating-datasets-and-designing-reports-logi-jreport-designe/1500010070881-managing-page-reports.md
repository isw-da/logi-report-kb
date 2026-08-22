---
title: "Managing Page Reports"
id: 1500010070881
section: "Creating Datasets and Designing Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010070881-Managing-Page-Reports
updated_at: 2021-07-24T10:37:44Z
---

# Managing Page Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070841-Making-High-Efficiency-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063261-Working-with-Components-in-Reports-)

# Managing Page Reports

This topic shows managing the page reportsas follows:

* [Managing Page Reports in a Catalog](#Report)
* [Importing Report Tabs into a Page Report](#Import)
* [Managing Report Tabs in a Page Report](#Tab)

## Managing Page Reports in a Catalog

All created page report files are physically placed in the same directory where the catalog file resides. Due to this, you will not be able to get detailed information about a page report until it is opened in Logi JReport Designer. For example, if you want to find a page report with a special condition, you will have to load each page report. For just a few page reports, this is not a problem. However the case is different when there are many reports.

Logi JReport provides you with the Page Report Manager for managing page reports by means of adding them into folders. You can divide the page reports into different types and work on them just like processing files in a file system: add, open, delete, move, rename and search items.

To manage page reports, select **Report** > **Manage Page Reports** to display the Page Report Manager.

![Manage Page Reports](https://devnet.logianalytics.com/hc/article_attachments/4404909123991/rpt_mng.gif)

You can then manage the page reports in the current catalog as shown below:

* **Adding a folder**
  1. Select a folder and select **New Folder** on the toolbar or right-click a folder and select **New Folder** from the shortcut menu.

     Now, a new folder is added as a sub node, and the default name for the folder is Folder1, Folder2.... You can rename the folder as required.
  2. Select the folder and select **Rename** on the toolbar or right-click it and select **Rename** from the shortcut menu.
  3. Type a new name in the name box, and then select outside the box (or just press **Enter** on the keyboard).
* **Adding reports to a folder**
  1. Select the folder to which you want to add the page reports and select **Add Page Reports** on the toolbar, or right-click the folder and select **Add Page Reports** from the shortcut menu.
  2. In the [Choose Page Report](https://devnet.logianalytics.com/hc/en-us/articles/1500010064901-Choose-Page-Report-Dialog) dialog, all the page reports in the current catalog are listed. Select the required ones.

     ![Choose Page Report](https://devnet.logianalytics.com/hc/article_attachments/4404901129495/chspgrpt.gif)
  3. Select the **Add** button to add the selected page reports to the folder. The default names of the report items are the file names of the reports. You can rename the reports as you would with a folder.

     A report can be added to multiple folders in case you want to include it in multiple categories. You can double-click any report in the Page Report Manager to open the report.
* **Moving a folder/report to another folder**
  1. Select the folder/report that you want to move and right-click it.
  2. Select **Move To** from the shortcut menu. The Move Report/Folder dialog is then displayed, which lists all the available folders.

     ![Move Report](https://devnet.logianalytics.com/hc/article_attachments/4404901129751/rpt_mng_move.gif)
  3. Select the folder you want the folder/report to be moved to, then select **OK**.

  You can also move a folder/report to another folder by simply dragging the folder/report to the destination folder.
* **Searching for a report or folder**  
   Wildcard searches for report name or folder name in the Page Report Manager are supported.
  1. Select a folder and right-click it.
  2. Select **Search** on the shortcut menu to display the [Search Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010032822-Search-Reports-Dialog) dialog.

     ![Search Reports](https://devnet.logianalytics.com/hc/article_attachments/4404901130007/srchrpt.gif)
  3. In the Find what text box, input the report or folder name, or report keywords you have specified for the Keywords property of the report in the Properties sheet, then select the corresponding search criteria from the By drop-down list, which can be by name, by keywords or by name or keywords.

     If you just input part of the report or folder name, or report keywords, use \* to replace the other part of the name or keywords. For example, if you want to search for the report EmployeeInformation, you should input *\*Info\** instead of *info* in the text box.
  4. Specify what you want to find: a folder, a report or both.
  5. Enter the search path in the Look in text box.
  6. Specify whether to limit the search to text that exactly matches the case of the search text.
  7. Specify whether to find the folder or report also in the sub folders of the search path.
  8. Select the **Search Now** button to start searching. Matched results will be listed in the search result box.
  9. If you want to start another search, select the **New Search** button and set the condition using the method described above.
* **Exporting the report information to a table**  
   You can export report information in the Page Report Manager to a table in a DBMS. The default name of the table is ReportsInfo. You can change the name as required. Each row of the table is a report description.
  1. Select the root folder **Reports** and right-click it.
  2. On the shortcut menu, select **Export**. The [Get JDBC Connection Information](https://devnet.logianalytics.com/hc/en-us/articles/1500010031562-Get-JDBC-Connection-Information-Dialog) dialog appears.
  3. Fill in the required fields for connecting to the DBMS, and then select the **OK** button.
  4. Give a name for the table, and then select **OK** in the Input dialog. The report information is added to the table in the DBMS.

  You can then [set up a JDBC connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010064401-Setting-Up-JDBC-Connections-in-a-Catalog) in a catalog to connect with the DBMS and [add the table](https://devnet.logianalytics.com/hc/en-us/articles/1500010064361-Tables-Views-Synonyms#Add) to the catalog via the JDBC connection for use.

  **Note:** If a table already exists, it will be replaced. So you must be sure that there are no duplicate names in the DBMS.
* **Deleting folders/reports**
  1. Select the folders/reports in the Reports tree, and then take either of the following ways:
     + Press the **Delete** key on the keyboard.
     + Select **Delete** on the toolbar.
     + Right-click and select **Delete** from the shortcut menu (it works when only one object is selected).
  2. A Warning message box is displayed. Check the option **Also delete report files from file system** if you want to remove them from your local directory permanently. Otherwise leave the option unchecked and only remove them from the virtual tree in the Page Report Manager.
  3. Select **Yes** in the box. If folders are selected, the folders and all their contents will be removed.

  If a report is deleted manually from the local file system, later when you open the Page Report Manager, you will see the node icon that represents the report is marked with a red cross. You can use the above method to remove the invalid node.
* **Editing the properties of a folder/report**   
   Select the folder/report the properties of which you want to edit, select **Show Properties** on the toolbar, then edit its property values in the Properties sheet. After editing a value, press **Enter** on the keyboard to confirm the change.

  A folder has the following properties:

  + **Description**: Specifies the description of the folder.
  + **Name**: Specifies the name of the folder.

  A report has the following properties:

  + **Author**: Specifies the author of the report.
  + **Description**: Specifies the description of the report.
  + **File Name**: Specifies the name of the report.
  + **Keywords**: Specifies the keywords of the report.
  + **Last Modified Time**: Specifies the last time at which the report was modified.
  + **Last Print Time**: Specifies the last time at which the report was printed.
  + **Last Run Time**: Specifies the last time at which the report ran.
  + **Name**: Specifies the display name of the report.
  + **Query Name**: Specifies the query used by the report.
  + **Value Type**: Specifies the type of the report.You can make use of the search bar to search for the desired properties (to display the search bar, select the **Search** button ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404909114647/btn_srch.gif) at the upper right corner of the Properties sheet). The search bar is closed when you select another object.

  ![Qiuck Search Toolbar button](https://devnet.logianalytics.com/hc/article_attachments/4404901130263/btn_srchtlbr.gif)

  + **Text box**  
     Type in the text you want to search for and the properties containing the matched text will be listed.
  + ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404901130519/btn_close1.gif)  
     Clear the text in the text box.
  + ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4404909124247/btn_srchtlbr_adv.gif)  
     Lists more search options.
    - **Highlight All**   
       Specifies whether to highlight all matched text.
    - **Match Case**   
       Specifies whether to search for text that meets the case of the typed text.
    - **Match Whole Word**   
       Specifies whether to search for text that looks the same as the typed text.

## Importing Report Tabs into a Page Report

Logi JReport enables you to import report tabs to a page report from another page report in the same catalog, and specify [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500010070661-Creating-and-Managing-Datasets) for the data components in the to be imported report tabs.

1. Select **File** > **Import From** > **JReport Page Report**.
2. In the Open Report dialog, specify the page report that contains the report tabs you want to import, then select **Open**.

   The [Select Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/1500010032622-Select-Report-Tab-Dialog) dialog appears.

   ![Select Report Tab](https://devnet.logianalytics.com/hc/article_attachments/4404901130775/slctrpt.gif)
3. Select the report tabs you want to import.
4. If you want to customize datasets used by data components within the to be imported report tabs, check the **Customize Dataset for Components** option. Select **OK** and the [Customize Dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500010030222-Customize-Dataset-Dialog) dialog appears.

   ![Customize Dataset](https://devnet.logianalytics.com/hc/article_attachments/4404901131031/cstmzdtst.gif)
5. All data components in the selected report tabs, which have self-bound datasets, will be listed in the dialog. Specify which dataset you want a data component to use by selecting its Dataset Name cell and choosing from the drop-down list.
6. Select **OK** to import the report tabs with specified datasets to their data components. The imported report tabs will be listed after the existing report tabs in the page report.

## Managing Report Tabs in a Page Report

This topic presents how to manage report tabs in a page report with the report tab bar.

![Page Report Tab Bar](https://devnet.logianalytics.com/hc/article_attachments/4404901131287/rpt_crt_tab.gif)

* **Copying a report tab**To copy a report tab, on the report tab bar, right-click the report tab you want to copy and select **Copy** on the shortcut menu. Then,

  + If you want to make a copy of the report tab within the current report, right-click any report tab and select **Paste** from the shortcut menu. You will then be prompt to give the report tab a new name. Specify the name as required.
  + If you want to copy the report tab to another page report of the same catalog, open the report to which the report tab will be copied, then right-click any report tab and select **Paste** from the shortcut menu. The report that you are copying from must still be open in Designer.
* **Moving a report tab to another page report**
  1. On the report tab bar, right-click the report tab you want to move and select **Cut** on the shortcut menu.
  2. Open the page report where the report tab will be moved.
  3. Right-click any report tab and select **Paste** on the shortcut menu.
* **Renaming a report tab**
  1. On the report tab bar, right-click the report tab with the name you want to change and select **Rename** on the shortcut menu.
  2. In the Input Report Tab Name dialog, enter a new name for the report tab and select **OK**.
* **Duplicating a report tab**  
   To make a duplicate report tab in the current page report, right-click the report tab on the report tab bar, and then select **Duplicate** on the shortcut menu.
* **Removing a report tab**  
  Right-click the report tab on the report tab bar, and then select **Remove** on the shortcut menu. Since a page report cannot be empty, you will not be able to remove all of the report tabs in the page report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070841-Making-High-Efficiency-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063261-Working-with-Components-in-Reports-)
