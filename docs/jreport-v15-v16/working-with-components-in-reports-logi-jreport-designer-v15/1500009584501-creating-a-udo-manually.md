---
title: "Creating a UDO Manually"
id: 1500009584501
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584501-Creating-a-UDO-Manually
updated_at: 2021-07-24T05:55:54Z
---

# Creating a UDO Manually

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584561-Objects-and-Interfaces-for-Creating-UDOs)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563822-Example-1-Accessing-a-Record-for-a-UDO-and-Registering-the-UDO-with-the-Report-System)

# Creating a UDO Manually

To create a UDO manually, follow the steps:

1. Inherit from the class JROblectTemplate to create a template file.
2. Inherit from the class JRVisiableResult or JRObjectResult to create a result file.
3. Implement JRObjectResultCreator to create a result creator file.
4. Implement interface JRObjectRender to create a result render file. If you want to display a UDO in the Design area, implement interface JRObjectEditor. If your UDO is a group level object, implement interface JRGroupListener.
5. Modify the file udo.ini in `<install_root>\lib` by adding the following:

   |  |
   | --- |
   | ``` Begin  name=MyDbField template=myudo.MyDbFld resultobject=myudo.MyDbFldRst resultcreator=myudo.MyDbFldCreator resultviewer=myudo.MyDbFldRender End ``` |
6. Compile the Java files, add the classes to the ADDCLASSPATH variable of setenv.bat in `<install_root>\bin`.

   **Note:** If you want to use class files for the UDO which have been used in previous versions, you should re-compile the source files.

Following are two specific examples about creating UDOs:

> * [Example 1: Accessing a Record for a UDO and Registering the UDO with the Report System](https://devnet.logianalytics.com/hc/en-us/articles/1500009563822-Example-1-Accessing-a-Record-for-a-UDO-and-Registering-the-UDO-with-the-Report-System)
> * [Example 2: Making a Group Based on a UDO](https://devnet.logianalytics.com/hc/en-us/articles/1500009584521-Example-2-Making-a-Group-Based-on-a-UDO)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584561-Objects-and-Interfaces-for-Creating-UDOs)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563822-Example-1-Accessing-a-Record-for-a-UDO-and-Registering-the-UDO-with-the-Report-System)
