---
title: "Setting Up Data Container Links in Banded Objects"
id: 4405664367511
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664367511-Setting-Up-Data-Container-Links-in-Banded-Objects
updated_at: 2022-01-27T20:34:22Z
---

# Setting Up Data Container Links in Banded Objects

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661346583-Obtaining-the-Group-Details-in-a-Banded-Object)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661384599-Working-with-Maps)

# Setting Up Data Container Links in Banded Objects

For banded objects in page reports, if there are other data components inserted inside them, you can use data container links to set up the relationship between the banded objects and their child data components. This topic describes how you can create data container links in a banded object.

A data container link includes:

* A set of link conditions which dynamically filter out data of the child data component.
* A set of parameter links (if the child data component has parameters) which assign some fixed values to the child component parameters, so that at runtime, users do not need to specify values for them.

Assume that you have created a banded object showing the customer information, then you [insert a table](https://devnet.logianalytics.com/hc/en-us/articles/4405661401239-Inserting-Tables-in-a-Report) into the detail panel of the banded object, which displays the order information. Now you want to set up some link conditions between these two components, so that when you view the report, you can get a table according to the ID of the customer.

![Table](https://devnet.logianalytics.com/hc/article_attachments/4420556267799/cmpnt_table_link.gif)

To achieve this, select the table and right-click it. On the shortcut menu, select **Data Container Link**, then specify the settings as required in the [Link Data Container dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661638423-Link-Data-Container-Dialog-Box).

![Link Data Container](https://devnet.logianalytics.com/hc/article_attachments/4420556147735/lnkdtcntnr_cndtn.gif)

Generally, a data container link functions the same as a subreport link. The only difference is that you do not need to specify a specific component to link with the parent data component, because you have selected the child as the target of the link. For more information about how to set up the link, refer to [Subreports](https://devnet.logianalytics.com/hc/en-us/articles/4405664401431-Working-with-Subreports).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661346583-Obtaining-the-Group-Details-in-a-Banded-Object)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661384599-Working-with-Maps)
