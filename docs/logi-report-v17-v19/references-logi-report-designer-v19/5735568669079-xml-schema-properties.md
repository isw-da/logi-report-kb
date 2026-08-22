---
title: "XML Schema Properties"
id: 5735568669079
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735568669079-XML-Schema-Properties
updated_at: 2022-11-02T08:09:58Z
---

# XML Schema Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532825111-XML-Connection-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735484068887-Appendices)

# XML Schema Properties

This topic describes the properties of an Element (![](https://devnet.logianalytics.com/hc/article_attachments/9898458858647/btn_elmnt.gif))/Attribute (![](https://devnet.logianalytics.com/hc/article_attachments/9898475903639/btn_atrbt.gif))/Reference of Element (![](https://devnet.logianalytics.com/hc/article_attachments/9898458877207/btn_elmntref.gif)) object in an XML schema in an XML connection.

| Property Name | Description |
| --- | --- |
| Data Type | Specifies the data type of the element or attribute. Designer imports the data type when importing the XML schema from XSD file or provides it when parsing from the XML source. This property on the reference of element is read only. |
| Default Value | Specifies the default value of the element or attribute. If the element or attribute has no specific value in the XML schema, Designer applies the default value you specify; otherwise, Designer applies the value in the XML schema for the element or attribute. This property on the reference of element is read only. |
| Fixed Value | Specifies the fixed value of the element or attribute, which Designer applies no matter there is a value for the element or attribute. This property on the reference of element is read only. |
| Format Pattern | Designer enables this property when you set Format Pattern Type to "Customize". Select the ellipsis Ellipsis button in the value cell to open the [Format Pattern dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735542973719-Format-Pattern-Dialog-Box) to specify the pattern to format the Date, Time, or DateTime data in the XML schema. |
| Format Pattern Type | Designer enables this property when the object is Date, Time, or DateTime data type. You can use it to specify the format pattern type for the data of the object. Choose an option from the drop-down list.  * **Default** Select to apply the lexical formats inspired by [ISO 8601](http://www.w3.org/TR/xmlschema-2/#ISO8601) for the data following the specification [XML Schema Part 2: Datatypes Second Edition](http://www.w3.org/TR/xmlschema-2/#isoformats). * **Customize** Select to use customized pattern to format the data in the XML schema. |
| Is Multiple | Shows whether the object occurs more than once in the XML instance. Read only. The default value of this property is affected by the object's maxOccurs property in the XSD. When the value of maxOccurs is greater than 1 or unbounded, the default value for Is Multiple is "true"; otherwise, it is "false". |
| List | Specifies whether to set the data type of an element or attribute as List. This property on the reference of element is read only. |
| List Delimiter | Designer enables this property when you set List to "true". You can use it to specify the delimiter to separate the items in a list. Choose an option from the drop-down list. |
| Name | Shows the name of the object in the XML instance. Read only. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532825111-XML-Connection-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735484068887-Appendices)
