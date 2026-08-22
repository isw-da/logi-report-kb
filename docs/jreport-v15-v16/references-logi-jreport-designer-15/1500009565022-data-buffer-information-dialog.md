---
title: "Data Buffer Information Dialog"
id: 1500009565022
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009565022-Data-Buffer-Information-Dialog
updated_at: 2021-07-24T05:55:30Z
---

# Data Buffer Information Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586201-Customized-Function-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565042-Data-Format-Dialog)

# Data Buffer Information Dialog

The Data Buffer Information dialog appears when you select View > Data Buffer. It helps you to view the information of data buffer in the current report and its subreports (make sure the report is viewed successfully once at least). You can adjust the performance and footprint for the reports according to the data buffer information. [See the dialog](javascript:%20void(null)).

![Data Buffer Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893930135/dtbfinfo.gif)

The following are details about options in the dialog:

**Report List**

Lists the current report and its subreports' instance names.

**Template Resources**

Displays the data components and datasets of the report and its subreports.

**Detailed Information** (for data component)

Shows information of a report's latest successful running.

* **Total memory for**  
   Displays the total buffer size in the current report and its subreports. It is the sum of the Maximum Used Buffer Size for all of data components in the current report and its subreports.
* **Maximum Used Buffer Size**  
   Displays the maximum buffer size which the specified data component occupies. It is the sum of Records Buffer Size and Groups Buffer Size.
* **Records Buffer Size**  
   Displays the maximum usage size for all the records’ buffers in running memory.
* **Records Buffer Number**  
   Displays the number of all the records’ buffers after running memory.
* **Groups Buffer Size**  
   Displays the maximum usage size for all the groups’ buffers in running memory.
* **Groups Buffer Number**  
   Displays the number of all the groups’ buffers after running memory.
* **Records per Page**  
   Displays the number of records in each page in the data buffer. You can [set it in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500009591461-Properties-of-Dataset-in-Page-Report#DataBuffer) to improve the report performance.
* **Maximum Page Number**  
   Displays the maximum number of pages in the data buffer. You can set it in the Report Inspector to improve the report performance.
* **Dataset**  
   Displays the name of the dataset which the specified data component uses.
* **Data Inherit**  
   Indicates whether the datasets for this component is inherited from another component.

**Detailed Information** (for dataset)

Shows information of a report's latest successful running.

* **Total memory for**  
   Displays the total buffer size in the current report and its subreports. It is the sum of the Maximum Used Buffer Size for all of data components in the current report and its subreports.
* **Maximum Used Buffer Size**  
   Displays the maximum buffer size which the specified dataset occupies. It is the sum of Records Buffer Size and Groups Buffer Size.
* **Records Buffer Size**  
   Displays the maximum usage size for all the records' buffers in running memory.
* **Records Buffer Number**  
   Displays the number of all the records' buffers after running memory.
* **Groups Buffer Size**  
   Displays the maximum usage size for all the groups' buffers in running memory.
* **Groups Buffer Number**  
   Displays the number of all the groups' buffers after running memory.
* **Records per Page**  
   Displays the number of records in each page in the data buffer. You can set it in the Report Inspector to improve the report performance.
* **Maximum Page Number**  
   Displays the maximum number of pages in the data buffer. You can set it in the Report Inspector to improve the report performance.

**Save As**

Saves the data buffer information in the specified directory with XML format.

**Close**

Exits the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586201-Customized-Function-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565042-Data-Format-Dialog)
