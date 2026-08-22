---
title: "Getting Editing Information"
id: 1500009582801
section: "Working with APIs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009582801-Getting-Editing-Information
updated_at: 2021-07-24T05:56:18Z
---

# Getting Editing Information

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562482-Getting-Objects-and-Object-Information)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582821-Exiting-from-the-Editing-Status)

# Getting Editing Information

The following methods are used to get editing information:

* **getWarning()**  
   Gets and returns the warning message. If the operation is successful, it will return null.
* **clearWarning()**  
   Clears the warning message.
* **getError()**  
   Gets and returns the error message. If the operation is successful, it will return null.
* **clearError()**  
   Clears the error message.
* **clearMsg()**  
   Clears all warning and error messages.
* **setLog(OutputStream log, String encoding)**  
   Sets the log to get error, debug and other information.
* **writeLog(String msg)**  
   Writes all messages to the log.
* **closeLog() throws IOException**  
   Closes the log.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562482-Getting-Objects-and-Object-Information)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582821-Exiting-from-the-Editing-Status)
