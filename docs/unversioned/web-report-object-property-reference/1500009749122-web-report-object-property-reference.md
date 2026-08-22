---
title: "Web Report Object Property Reference"
id: 1500009749122
section: "Web Report Object Property Reference"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009749122-Web-Report-Object-Property-Reference
updated_at: 2021-07-24T00:47:49Z
---

# Web Report Object Property Reference

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009774841-Sort-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777721-Banded-Object-Properties)

# Web Report Object Property Reference

This topic is an overall introduction to the properties of the web report objects in Web Report Studio. It describes general information about the properties.

Keep in mind the following while browsing each object for its properties:

* You will start off from a table listing all the properties for an object and what you can achieve with each property.
* Some properties only show related information and you cannot edit them.
* You can control some properties by a formula or expression. If you select a formula to control a property, Logi Report automatically generates an expression with the prefix @. Also, you must let Logi Report Engine know some properties before a page break, so that it can lay out the object. In a formula or expression, the special field **PageNumber** is the switch for setting the page break calculation time. If you use PageNumber in the formula or expression, then the calculation time will be after the page break, if you do not use PageNumber, the calculation time will be before the page break. For this reason, Logi Report will set the calculation time for controlling whether to mark the formula or expression as before page break or after page break. For most properties, you can control the property by formula or expression at any time without concern about the page break.
* The same property for different objects usually means the same thing, unless otherwise stated.

This topic contains the following sections:

* [Banded Object Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009777721-Banded-Object-Properties)
* [Chart Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009777861-Chart-Properties)
* [Crosstab Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009749242-Crosstab-Properties)
* [DBField Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009777981-DBField-Properties)
* [Filter Control Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009778001-Filter-Control-Properties)
* [Formula Field Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009778021-Formula-Field-Properties)
* [Image Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009778041-Image-Properties)
* [KPI Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009778061-KPI-Properties)
* [Line Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009749282-Line-Properties)
* [Label Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009749262-Label-Properties)
* [Multimedia Object (OLE Object) Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009778141-Multimedia-Object-OLE-Object-Properties)
* [Navigation Control Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009778081-Navigation-Control-Properties)
* [Page Panel Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009778161-Page-Panel-Properties)
* [Parameter Control Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009778181-Parameter-Control-Properties)
* [Parameter Field Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009749382-Parameter-Field-Properties)
* [Parameter Form Control Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009778201-Parameter-Form-Control-Properties)
* [Report Body Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009749402-Report-Body-Properties)
* [Special Field Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009749422-Special-Field-Properties)
* [Table Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009778221-Table-Properties-Properties)
* [Tabular Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009778321-Tabular-Properties)
* [Web Report Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009749522-Web-Report-Properties)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009774841-Sort-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777721-Banded-Object-Properties)
