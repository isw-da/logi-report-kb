---
title: "Web Report Object Property Reference"
id: 1500009691822
section: "Web Report Object Property Reference"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009691822-Web-Report-Object-Property-Reference
updated_at: 2021-11-03T06:56:46Z
---

# Web Report Object Property Reference

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009689342-Sort)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009691842-Banded-Object)

# Web Report Object Property Reference

This topic is an overall introduction to the properties of the web report objects in Web Report Studio. Keep in mind the following while browsing each object for its properties:

* You will start off from a table listing all the properties for an object and what can be achieved with each property.
* Some properties are just used to show related information and cannot be edited.
* Some properties can be controlled by a formula or expression. If a formula is selected to control a property, it will be automatically generated as an expression prefixed by an @ sign. Also, some properties must be known by Logi JReport Engine before a page break, so that it can lay out the object. In a formula or expression, the special field PageNumber is the switch for setting the page break calculation time. If PageNumber is used in the formula or expression, then the calculation time will be after the page break, if PageNumber is not used, the calculation time will be before the page break. For this reason, Logi JReport will set the calculation time for controlling whether the formula or expression will be marked as before page break or after page break. For most properties, the property can be controlled by formula or expression at any time without concern about the page break.
* The same property for different objects usually means the same thing, unless otherwise stated.

The following lists the objects that a web report may contain in alphabetical order:

* [Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009691842-Banded-Object)
* [Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009718301-Chart)
* [Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009718381-Crosstab)
* [DBField](https://devnet.logianalytics.com/hc/en-us/articles/1500009718401-DBField)
* [Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009718421-Filter-Control)
* [Formula Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009718441-Formula-Field)
* [Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009692082-Image)
* [KPI](https://devnet.logianalytics.com/hc/en-us/articles/1500009692102-KPI)
* [Line](https://devnet.logianalytics.com/hc/en-us/articles/1500009692142-Line)
* [Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009692122-Label)
* [Multimedia Object (OLE Object)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692182-Multimedia-Object-OLE-Object-)
* [Navigation Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009692162-Navigation-Control)
* [Page Panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009692202-Page-Panel)
* [Parameter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009718541-Parameter-Control)
* [Parameter Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009718521-Parameter-Field)
* [Parameter Form Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009692282-Parameter-Form-Control)
* [Report Body](https://devnet.logianalytics.com/hc/en-us/articles/1500009718561-Report-Body)
* [Special Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009718581-Special-Field)
* [Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009692302-Table)
* [Tabular](https://devnet.logianalytics.com/hc/en-us/articles/1500009692422-Tabular)
* [Web Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009718661-Web-Report)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009689342-Sort)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009691842-Banded-Object)
