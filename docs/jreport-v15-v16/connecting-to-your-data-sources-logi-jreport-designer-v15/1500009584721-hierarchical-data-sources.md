---
title: "Hierarchical Data Sources"
id: 1500009584721
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584721-Hierarchical-Data-Sources
updated_at: 2021-07-24T05:55:51Z
---

# Hierarchical Data Sources

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564282-EnterpriseDB-Stored-Procedure-UDS)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563962-Hierarchical-Data-Source-API)

# Hierarchical Data Sources

Logi JReport Designer supports hierarchical data sources (HDS). This feature uses the hierarchical data source API provided by Logi JReport.

As the XML technology has become a popular standard for data interchange on the web, Logi JReport Designer directly supports XML format data source by wrapping the provided HDS API. Logi JReport Designer's built-in classes can implement the XML format hierarchical data source interface. You can directly import an XML data source to a catalog using the Catalog Manager.

Hierarchical data sources with a parallel structure are also supported by Logi JReport Designer, and are hence called parallel HDS. The difference between the general HDS and the parallel HDS is that the parallel HDS contains more than one parallel branch, which will be presented in different Parallel Detail (PDT) panels in a banded object in Logi JReport Designer.

Data in a parallel HDS is organized in a tree structure, which contains branches and leaves. Among these branches, there are some parallel branch nodes that split the trunk of the data source tree into deeper and more complex branches. The following is a figure illustrating the parallel HDS structure.

![](https://devnet.logianalytics.com/hc/article_attachments/4404889399575/cnctn_hds_prlel1.gif)

**Leaf**

A leaf in parallel HDS refers to a column (DBField), nodes that contain no sub-nodes.

**Branch**

A branch in parallel HDS is a special table that contains leaves or sub-branches.

![](https://devnet.logianalytics.com/hc/article_attachments/4404893971991/cnctn_hds_prlel2.gif)

**Parallel branches**

If the contents of two branches have no parental relationships, these branches are called parallel branches.

The way of using a parallel HDS is the same as with general HDS in Logi JReport Designer. There are however, some key points that you should be aware of when you use a parallel HDS to develop reports. For details, see [Example 2: Developing a report from a parallel HDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009584761-Developing-Reports-from-HDS#Example2).

The following topics discuss working with hierarchical data sources in a catalog:

> * [Hierarchical Data Source API](https://devnet.logianalytics.com/hc/en-us/articles/1500009563962-Hierarchical-Data-Source-API)
> * [Adding an HDS to a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009584741-Adding-an-HDS-to-a-Catalog)
> * [Developing Reports from HDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009584761-Developing-Reports-from-HDS)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564282-EnterpriseDB-Stored-Procedure-UDS)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563962-Hierarchical-Data-Source-API)
