---
title: "Geo Map Properties"
id: 1500010100421
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010100421-Geo-Map-Properties
updated_at: 2021-07-23T19:16:34Z
---

# Geo Map Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062122-Formula-Field-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010100441-Geo-Area-Properties)

# Geo Map Properties

This topic lists the properties of a Geo Map object.

Geographic maps in web reports and library components are labeled Geo Map objects in the Report Inspector. It contains the following properties and the availabilities of its properties vary for the two report types.

| Property Name | Available For | Description |
| --- | --- | --- |
| Geography | | |
| Display As | Web Report, Library Component | Specifies the display type of the map location. Choose an option from the drop-down list.  * **Marker** - Displays the map location as marker. * **Area** - Displays the map location as area. * **Marker and Area** - Displays the map location as marker and area.   Data type: Enumeration |
| Geometry | | |
| Height | Web Report, Library Component | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Web Report, Library Component | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Web Report, Library Component | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Y | Web Report, Library Component | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Others | | |
| Auto Scale in Number | Web Report, Library Component | Specifies whether to automatically scale the values that are of the Number data type in the object when the values fall into the two ranges:  * When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.   Data type: Boolean |
| Default for Filter | Web Report | Specifies whether to show the data component as the default component in the Apply To drop-down list of the Filter dialog box in Web Report Studio. Data type: Boolean  Note icon In a report, you can only set one data component's Default for Filter property to true. |
| Export to Excel | Web Report, Library Component | Specifies whether to include the object in the Excel output of the report. Data type: Boolean |
| Export to HTML | Web Report, Library Component | Specifies whether to include the object in the HTML output of the report. Data type: Boolean |
| Export to PDF | Web Report, Library Component | Specifies whether to include the object in the PDF output of the report. Data type: Boolean |
| Export to PostScript | Web Report, Library Component | Specifies whether to include the object in the PostScript output of the report. Data type: Boolean |
| Export to Report Result | Web Report, Library Component | Specifies whether to include the object when previewing the report in Web Report Result and running the report in Web Report Studio, or when the library component is used in JDashboard. Data type: Boolean |
| Export to RTF | Web Report, Library Component | Specifies whether to include the object in the RTF output of the report. Data type: Boolean |
| Invisible | Web Report, Library Component | Specifies whether to show the object in the design area and in the results. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Invisible for Filter Dialogs | Web Report | Specifies whether to show the data component in the Apply To drop-down list of the Filter dialog box in Web Report Studio. This property cannot be edited when [Default for Filter](#DFilter) is set to true. Data type: Boolean |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500010062762-Editing-Reports#Position) | Web Report, Library Component | Specifies the position of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Suppress | Web Report, Library Component | Specifies whether to show the object in the design area and in the results. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  Note icon When you set both the Invisible and Suppress properties of an object to true, Suppress has the higher priority. |
| Suppress When No Records | Web Report, Library Component | Specifies whether to display the object in the results when no record is returned to its parent data component. Data type: Boolean |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500010061722-Banded-Object-Properties#TOC) | | |
| Anchor Display Value | Web Report | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Web Report | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062122-Formula-Field-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010100441-Geo-Area-Properties)
