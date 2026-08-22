---
title: "Data Buffer Information Dialog Box"
id: 4405661495575
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661495575-Data-Buffer-Information-Dialog-Box
updated_at: 2022-01-27T20:36:08Z
---

# Data Buffer Information Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664448023-Customized-Function-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664452759-Data-Format-Dialog-Box)

# Data Buffer Information Dialog Box

You can use the Data Buffer Information dialog box to view the information of the data buffer for the current report and its subreports (make sure you have previewed the report successfully once at least). You can adjust the performance and footprint for the reports according to the data buffer information. This topic describes the options in the dialog box.

Designer displays the Data Buffer Information dialog box when you navigate to View > Data Buffer.

![Data Buffer Information dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556207127/dtbfinfo.gif)

You see the following options in the dialog box:

**Report List**

This box shows the name of the current report and the instance names of its subreports.

**Template Resources**

This box displays the data components and datasets of the current report and its subreports. Select a data component or dataset to view the detail information.

**Detailed Information**

This box shows the information of the current report's latest successful running.

* **Total memory for**  
  This option shows the total buffer size for the current report and its subreports. It is the sum of the Maximum Used Buffer Size for all the data components in the report and its subreports.
* **Maximum Used Buffer Size**  
  This option shows the maximum buffer size which the specified data component/dataset occupies. It is the sum of Records Buffer Size and Groups Buffer Size.
  + **Records Buffer Size**  
    This option shows the maximum usage size for all the records’ buffers in running memory.
  + **Records Buffer Number**  
    This option shows the number of all the records’ buffers after running memory.
  + **Groups Buffer Size**  
    This option shows the maximum usage size for all the groups’ buffers in running memory.
  + **Groups Buffer Number**  
    This option shows the number of all the groups’ buffers after running memory.
* **Records per Page**  
  This option shows the number of records in each page in the data buffer. You can [set it in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/4405664656919-Dataset-Properties#DataBuffer) to improve the report performance.
* **Maximum Page Number**  
  This option shows the maximum number of pages in the data buffer. You can set it in the Report Inspector to improve the report performance.
* **Dataset**  
  This option shows the name of the dataset that the specified data component uses.
* **Data Inherit**  
  This option shows whether the specified data component inherits dataset from another component.

**Save As**

Select to save the data buffer information to the specified directory in XML.

**Close**

Select to exit the dialog box.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664448023-Customized-Function-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664452759-Data-Format-Dialog-Box)
