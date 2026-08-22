---
title: "Web Report Object Property Reference"
id: 1500009649522
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009649522-Web-Report-Object-Property-Reference
updated_at: 2021-07-24T20:53:52Z
---

# Web Report Object Property Reference

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009672881-Others)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649542-Chart)

# Web Report Object Property Reference

This topic is an overall introduction to the properties of the web report objects in Web Report Studio. Keep in mind the following while browsing each object for its properties:

* You will start off from a table listing all the properties for an object and what can be achieved with each property.
* Some properties are just used to show related information and cannot be edited.
* Some properties can be controlled by a formula or expression. If a formula is selected to control a property, it will be automatically generated as an expression prefixed by an @ sign. Also, some properties must be known by Logi JReport Engine before a page break, so that it can lay out the object. In a formula or expression, the special field PageNumber is the switch for setting the page break calculation time. If PageNumber is used in the formula or expression, then the calculation time will be after the page break, if PageNumber is not used, the calculation time will be before the page break. For this reason, Logi JReport will set the calculation time for controlling whether the formula or expression will be marked as before page break or after page break. For most properties, the property can be controlled by formula or expression at any time without concern about the page break.
* The same property for different objects usually means the same thing, unless otherwise stated.

The following are object properties for web report included in the Inspector panel, listed in alphabetical order:

* [Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009649542-Chart)
* [Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009649582-Crosstab)
* [DBField](https://devnet.logianalytics.com/hc/en-us/articles/1500009649642-DBField)
* [Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009674281-Filter-Control)
* [Formula Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009674301-Formula-Field)
* [Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009674321-Image)
* [KPI Component](https://devnet.logianalytics.com/hc/en-us/articles/1500009674341-KPI-Component)
* [Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009649662-Label)
* [Multimedia Object (OLE Object)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649682-Multimedia-Object-OLE-Object-)
* [Navigation Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009674361-Navigation-Control)
* [Page Panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009649702-Page-Panel)
* [Parameter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009649742-Parameter-Control)
* [Parameter Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009674461-Parameter-Field)
* [Parameer Form Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009674481-Parameter-Form-Control)
* [Report Body](https://devnet.logianalytics.com/hc/en-us/articles/1500009649762-Report-Body)
* [Special Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009649782-Special-Field)
* [Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009674501-Table)
* [Tabular](https://devnet.logianalytics.com/hc/en-us/articles/1500009674621-Tabular)
* [Web Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009674641-Web-Report)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009672881-Others)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649542-Chart)
