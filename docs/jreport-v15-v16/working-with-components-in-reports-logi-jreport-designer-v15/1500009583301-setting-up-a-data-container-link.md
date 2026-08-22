---
title: "Setting Up a Data Container Link"
id: 1500009583301
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583301-Setting-Up-a-Data-Container-Link
updated_at: 2021-07-24T05:56:11Z
---

# Setting Up a Data Container Link

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583261-Embedding-Data-Components-in-a-Banded-Object)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584061-Maps)

# Setting Up a Data Container Link

In a page report that is created using query resources, when a data component is inserted into another data component, you can use data container link to set up a relationship between the parent and child data components.

A data container link includes:

* A set of link conditions which are used to dynamically filter out data of the child data component.
* A set of parameter links (if the child data component has parameters) which are used to assign some fixed values to the child component parameters so that at runtime, you do not need to enter values for them.

Assume that you have created a banded object showing the customer information. Then, you [insert a table](https://devnet.logianalytics.com/hc/en-us/articles/1500009563682-Inserting-a-Table) into the detail panel of the banded object, which displays the order information. Now you want to set up some link conditions between these two components, so that when you view the report, a table will be generated according to the ID of the customer as follows:

![](https://devnet.logianalytics.com/hc/article_attachments/4404894006295/cmpnt_table_link.gif)

To achieve this, select the table and right-click it. On the shortcut menu, select **Data Container Link**, then specify the settings as required in the [Link Data Container](https://devnet.logianalytics.com/hc/en-us/articles/1500009566642-Link-Data-Container-Dialog) dialog.

![Link Data Container](https://devnet.logianalytics.com/hc/article_attachments/4404889331095/lnkdtcntnr_cndtn.gif)

Generally, a data container link functions the same as a subreport link. The only difference is that you do not need to specify a specific component that is linked with the parent data component, since you have selected the child as the target of the link. For additional information about how to set up the link, refer to [Subreports](https://devnet.logianalytics.com/hc/en-us/articles/1500009563582-Subreports).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583261-Embedding-Data-Components-in-a-Banded-Object)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584061-Maps)
