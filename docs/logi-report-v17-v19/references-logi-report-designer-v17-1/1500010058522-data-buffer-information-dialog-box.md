---
title: "Data Buffer Information Dialog Box"
id: 1500010058522
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010058522-Data-Buffer-Information-Dialog-Box
updated_at: 2021-07-23T19:15:13Z
---

# Data Buffer Information Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096021-Customized-Function-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096081-Data-Format-Dialog-Box)

# Data Buffer Information Dialog Box

You can use the Data Buffer Information dialog box to view the information of the data buffer for the current report and its subreports (make sure you have previewed the report successfully once at least). You can adjust the performance and footprint for the reports according to the data buffer information. This topic describes the options in the dialog box.

Designer displays the Data Buffer Information dialog box when you select View > Data Buffer.

![Data Buffer Information dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848590999/dtbfinfo.gif)

You see the following options in the dialog box:

**Report List**

The box shows the current report and its subreports' instance names.

**Template Resources**

The box displays the data components and datasets of the report and its subreports. Select a data component or dataset to view the detail information.

**Detailed Information**

The box shows the information of the current report's latest successful running.

* **Total memory for**  
  The option shows the total buffer size for the current report and its subreports. It is the sum of the Maximum Used Buffer Size for all the data components in the report and its subreports.
* **Maximum Used Buffer Size**  
  The option shows the maximum buffer size which the specified data component/dataset occupies. It is the sum of Records Buffer Size and Groups Buffer Size.
  + **Records Buffer Size**  
    The option shows the maximum usage size for all the records’ buffers in running memory.
  + **Records Buffer Number**  
    The option shows the number of all the records’ buffers after running memory.
  + **Groups Buffer Size**  
    The option shows the maximum usage size for all the groups’ buffers in running memory.
  + **Groups Buffer Number**  
    The option shows the number of all the groups’ buffers after running memory.
* **Records per Page**  
  The option shows the number of records in each page in the data buffer. You can [set it in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010062082-Dataset-Properties#DataBuffer) to improve the report performance.
* **Maximum Page Number**  
  The option shows the maximum number of the pages in the data buffer. You can set it in the Report Inspector to improve the report performance.
* **Dataset**  
  The option shows the name of the dataset which the specified data component uses.
* **Data Inherit**  
  The option shows whether the specified data component inherits the dataset from another component.

**Save As**

Select to save the data buffer information to the specified directory in XML.

**Close**

Select to exit the dialog box.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096021-Customized-Function-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096081-Data-Format-Dialog-Box)
