---
title: "Managing Page Reports"
id: 1500010101281
section: "Creating Datasets and Designing Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010101281-Managing-Page-Reports
updated_at: 2021-07-23T19:16:49Z
---

# Managing Page Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101221-Making-High-Efficiency-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports)

# Managing Page Reports

Designer places all the page report files physically in the same directory where the catalog file resides. Due to this, you are not able to get detailed information about a page report until you open it in Designer. For example, if you want to find a page report with a special condition, you have to load each page report. For just a few page reports, this is not a problem; however, the case is different when there are many reports. To ease the work for you, Designer provides you with the Page Report Manager for managing page reports by means of adding them into folders. Designer also enables you to manage the report tabs in a specific page report, for example, you can import report tabs from another page report into it, and move, duplicate, rename, and delete the report tabs via the report tab bar. This topic describes how you can manage the page reports in a catalog as well as the report tabs in a page report.

This topic contains the following sections:

* [Managing the Page Reports in a Catalog](#Report)
  + [Adding a Folder](#Add)
  + [Adding Reports to a Folder](#AddRpt)
  + [Moving a Folder/Report to Another Folder](#Move)
  + [Editing the Properties of a Folder/Report](#Edit)
  + [Searching for a Report or Folder](#Search)
  + [Exporting the Report Information to a Table](#Export)
  + [Deleting Folders/Reports](#Delete)
* [Managing the Report Tabs in a Page Report](#Tab)
  + [Importing Report Tabs into a Page Report](#Import)
  + [Managing Report Tabs with the Report Tab Bar](#TabBar)

## Managing the Page Reports in a Catalog

To manage the page reports using the Page Report Manager, first select **Report** > **Manage Page Reports** to open it. You can categorize the page reports into different folders and work on them just like processing files in a file system: add, open, delete, move, rename, and search items.

![Manage Page Reports](https://devnet.logianalytics.com/hc/article_attachments/4404848409495/rpt_mng.gif)

### Adding a Folder

1. Select a folder and select **New Folder** on the toolbar or right-click a folder and select **New Folder** from the shortcut menu.

   Designer then adds a new folder as a sub node, and the default name for the folder is Folder1, Folder2.... You can rename the folder.
2. Select the folder and select **Rename** on the toolbar or right-click it and select **Rename** from the shortcut menu.
3. Type a new name in the name box, and then select outside the box (or just press **Enter** on the keyboard).

### Adding Reports to a Folder

1. Select the folder to which you want to add the page reports and select **Add Page Reports** on the toolbar, or right-click the folder and select **Add Page Reports** from the shortcut menu. Designer displays the [Choose Page Report dialog box.](https://devnet.logianalytics.com/hc/en-us/articles/1500010058162-Choose-Page-Report-Dialog-Box)
2. All the page reports in the current catalog are available in the report box. Select the required ones.

   ![Choose Page Report](https://devnet.logianalytics.com/hc/article_attachments/4404856828055/chspgrpt.gif)
3. Select the **Add** button to add the selected page reports to the folder. The default names of the report items are the file names of the reports. You can rename the reports as you would with a folder.

You can add a report to multiple folders in case you want to include it in multiple categories. You can double-click any report in the Page Report Manager to open the report.

### Moving a Folder/Report to Another Folder

1. Select the folder/report and right-click it, then select **Move To** from the shortcut menu. Designer displays the Move Report/Folder dialog box.
2. The Move To box lists all the available folders. Select the folder to which you want to move the folder/report.

   ![Move Report](https://devnet.logianalytics.com/hc/article_attachments/4404856828311/rpt_mng_move.gif)
3. Select **OK** to apply the setting.

You can also move a folder/report to another folder by simply dragging the folder/report to the destination folder.

### Editing the Properties of a Folder/Report

Select the folder/report, select **Show Properties** on the toolbar, then edit its property values in the **Properties** sheet. After editing a value, press **Enter** on the keyboard to confirm the change.

A folder has the following properties:

* **Description**: Specify the description of the folder.
* **Name**: Specify the name of the folder.

A report has the following properties:

* **Author**: Specify the author of the report.
* **Description**: Specify the description of the report.
* **File Name**: Specify the name of the report.
* **Keywords**: Specify the keywords of the report.
* **Last Modified Time**: Specify the last time at which the report was modified.
* **Last Print Time**: Specify the last time at which the report was printed.
* **Last Run Time**: Specify the last time at which the report ran.
* **Name**: Specify the display name of the report.
* **Query Name**: Specify the query used by the report.
* **Value Type**: Specify the type of the report.

You can make use of the search box to search for the desired properties (to display the search box, select the **Search** icon ![Search icon](https://devnet.logianalytics.com/hc/article_attachments/4404856807959/btn_srch.gif) at the upper right corner of the Properties sheet). To start searching, type the text you want to search for in the search box and Designer lists the properties containing the matched text. Designer closes the search box when you select another object.

You can make use of the following options in the search box:

* ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4404848393111/btn_srchbox_adv.gif)**Drop-down icon**  
  Select to list more search options.
  + **Highlight All**   
    Select to highlight all matched text.
  + **Match Case**   
    Select to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Select to search for text that looks the same as the typed text.
* ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404856816535/btn_close1.gif)**Delete icon**  
  Select to close the search box and cancel the search.

### Searching for a Report or Folder

You can perform wildcard searches for report names or folder names in the Page Report Manager.

1. Select a folder and right-click it, then select **Search** on the shortcut menu. Designer displays the [Search Reports dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098901-Search-Reports-Dialog-Box).

   ![Search Reports](https://devnet.logianalytics.com/hc/article_attachments/4404856828567/srchrpt.gif)
2. In the **Find what** text box, type the report or folder name, or report keywords you have specified for the **Keywords** property of the report in the Properties sheet, then select the corresponding search criteria from the **By** drop-down list, which can be by name, by keywords, or by name or keywords.

   If you just type in part of the report or folder name, or report keywords, use \* to replace the other part of the name or keywords. For example, if you want to search for the report EmployeeInformation, you should type *\*Info\** instead of *info* in the text box.
3. Specify what you want to find: a folder, a report, or both.
4. Type the search path in the **Look in** text box.
5. Specify whether to limit the search to text that exactly matches the case of the search text.
6. Specify whether to find the folder or report also in the sub folders of the search path.
7. Select the **Search Now** button to start searching. Designer lists the matched results in the search result box.
8. If you want to start another search, select the **New Search** button and set the condition using the method described above.

### Exporting the Report Information to a Table

You can export report information in the Page Report Manager to a table in a DBMS. The default name of the table is "ReportsInfo". You can change the name as required. Each row of the table is a report description.

1. Select the root folder **Reports** and right-click it.
2. On the shortcut menu, select **Export**. Designer displays the [Get JDBC Connection Information dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097761-Get-JDBC-Connection-Information-Dialog-Box).
3. Fill in the required text boxes for connecting to the DBMS, and then select the **OK** button.
4. Give a name for the table and select **OK** in the Input dialog box. Designer adds the report information to the table in the DBMS.

   You need to make sure there are no duplicate name in the DBMS; otherwise, Designer replaces the same name table directly.

You can then [set up a JDBC connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010057702-Setting-Up-JDBC-Connections-in-a-Catalog) in a catalog to connect with the DBMS and [add the table](https://devnet.logianalytics.com/hc/en-us/articles/1500010057682-Using-Tables-Views-Synonyms#Add) to the catalog via the JDBC connection for use.

### Deleting Folders/Reports

1. Select the folders/reports in the Reports tree, and then do any of the following:
   * Press the **Delete** key on the keyboard.
   * Select **Delete** on the toolbar.
   * Right-click and select **Delete** from the shortcut menu (it works when only one object is selected).

   Designer displays a Warning message box.
2. Select the option **Also delete report files from file system** if you want to remove them from your local directory permanently; otherwise, leave the option unselected to only remove them from the virtual tree in the Page Report Manager.
3. Select **Yes** in the box. If you select folders, Designer removes the folders and all their contents.

If you delete a report manually from the local file system, later when you open the Page Report Manager, you can see that the node icon representing the report is marked with a red cross. You can use the above method to remove the invalid node.

## Managing the Report Tabs in a Page Report

You can also manage the report tabs in a specific page report, for example, import report tabs from another page report into it, and insert, duplicate, and delete the report tabs via the report tab bar.

### Importing Report Tabs into a Page Report

Designer enables you to import report tabs to a page report from another page report in the same catalog, and specify [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500010062542-Creating-and-Managing-Datasets) for the data components in the to be imported report tabs.

1. Select **File** > **Import From** > **Logi Report Page Report**.
2. In the Open Report dialog box, specify the page report that contains the report tabs you want to import, then select **Open**.

   Designer displays the [Select Report Tab dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098741-Select-Report-Tab-Dialog-Box).

   ![Select Report Tab](https://devnet.logianalytics.com/hc/article_attachments/4404848410007/slctrpt.gif)
3. Select the report tabs you want to import.
4. If you want to customize datasets used by data components within the to be imported report tabs, select the **Customize Dataset for Components** checkbox.
5. Select **OK**. Designer displays the [Customize Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096041-Customize-Dataset-Dialog-Box).

   ![Customize Dataset](https://devnet.logianalytics.com/hc/article_attachments/4404848410263/cstmzdtst.gif)
6. Designer lists all the data components in the selected report tabs, which have self-bound datasets, in the dialog box. Specify which dataset you want a data component to use by selecting its **Dataset Name** cell and choosing from the drop-down list.
7. Select **OK** to import the report tabs with specified datasets to their data components. Designer displays the imported report tabs after the existing report tabs in the page report.

### Managing Report Tabs with the Report Tab Bar

You can use the report tab bar to duplicate, move, rename, and delete the report tabs in a specific page report.

![Page Report Tab Bar](https://devnet.logianalytics.com/hc/article_attachments/4404848410647/rpt_crt_tab.gif)

* **Copying a report tab**  
  On the report tab bar, right-click the report tab and select **Copy** on the shortcut menu. Then,
  + If you want to make a copy of the report tab within the current report, right-click any report tab and select **Paste** from the shortcut menu. Designer then prompts you to give the report tab a new name. Specify the name as required.
  + If you want to copy the report tab to another page report of the same catalog, open the report to which to copy the report tab, then right-click any report tab and select **Paste** from the shortcut menu. The report that you are copying from must still be open in Designer.
* **Moving a report tab to another page report**
  1. On the report tab bar, right-click the report tab and select **Cut** on the shortcut menu.
  2. Open the page report in the same catalog where to put the report tab.
  3. Right-click any report tab and select **Paste** on the shortcut menu.
* **Renaming a report tab**
  1. On the report tab bar, right-click the report tab and select **Rename** on the shortcut menu.
  2. In the Input Report Tab Name dialog box, specify a new name for the report tab and select **OK**.
* **Duplicating a report tab**  
  To make a duplicate report tab in the current page report, right-click the report tab on the report tab bar, and then select **Duplicate** on the shortcut menu.
* **Removing a report tab**  
  Right-click the report tab on the report tab bar, and then select **Remove** on the shortcut menu. Since a page report cannot be empty, you are not able to remove all of the report tabs in the page report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101221-Making-High-Efficiency-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports)
