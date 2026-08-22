---
title: "Data Buffer Information Dialog"
id: 1500010065321
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010065321-Data-Buffer-Information-Dialog
updated_at: 2021-07-24T10:39:02Z
---

# Data Buffer Information Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065221-Customized-Function-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030282-Data-Format-Dialog)

# Data Buffer Information Dialog

The Data Buffer Information dialog helps you to view the information of data buffer in the current report and its subreports (make sure the report is viewed successfully once at least). You can adjust the performance and footprint for the reports according to the data buffer information. It appears when you select View > Data Buffer.

![Data Buffer Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909227799/dtbfinfo.gif)

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
   Displays the number of records in each page in the data buffer. You can [set it in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010069861-Dataset-Properties#DataBuffer) to improve the report performance.
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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065221-Customized-Function-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030282-Data-Format-Dialog)
