---
title: "Setting Up Data Container Links in Banded Objects"
id: 1500010028662
section: "Working with Components in Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010028662-Setting-Up-Data-Container-Links-in-Banded-Objects
updated_at: 2021-07-24T10:39:29Z
---

# Setting Up Data Container Links in Banded Objects

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010028622-Obtaining-Detailed-Information-from-a-Banded-Object) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063821-Maps)

# Setting Up Data Container Links in Banded Objects

For banded objects in page reports, if there are other data components inserted inside them, you can use data container links to set up the relationship between the banded objects and their child data components.

A data container link includes:

* A set of link conditions which are used to dynamically filter out data of the child data component.
* A set of parameter links (if the child data component has parameters) which are used to assign some fixed values to the child component parameters so that at runtime, you do not need to enter values for them.

Assume that you have created a banded object showing the customer information. Then, you [insert a table](https://devnet.logianalytics.com/hc/en-us/articles/1500010063941-Inserting-Tables-in-a-Report-) into the detail panel of the banded object, which displays the order information. Now you want to set up some link conditions between these two components, so that when you view the report, a table will be generated according to the ID of the customer as follows:

![Table](https://devnet.logianalytics.com/hc/article_attachments/4404909289111/cmpnt_table_link.gif)

To achieve this, select the table and right-click it. On the shortcut menu, select **Data Container Link**, then specify the settings as required in the [Link Data Container](https://devnet.logianalytics.com/hc/en-us/articles/1500010067061-Link-Data-Container-Dialog) dialog.

![Link Data Container](https://devnet.logianalytics.com/hc/article_attachments/4404901199767/lnkdtcntnr_cndtn.gif)

Generally, a data container link functions the same as a subreport link. The only difference is that you do not need to specify a specific component that is linked with the parent data component, since you have selected the child as the target of the link. For additional information about how to set up the link, refer to [Subreports](https://devnet.logianalytics.com/hc/en-us/articles/1500010029222-Subreports).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010028622-Obtaining-Detailed-Information-from-a-Banded-Object) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063821-Maps)
