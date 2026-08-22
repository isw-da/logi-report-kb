---
title: "Properties of Contents in Library Component"
id: 1500009590741
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590741-Properties-of-Contents-in-Library-Component
updated_at: 2021-07-24T05:54:20Z
---

# Properties of Contents in Library Component

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590701-Properties-of-Configuration-Panel-in-Library-Component)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009569102-Properties-of-Body-in-Library-Component)

# Properties of Contents in Library Component

The library component contents can have the following child objects: [Body](https://devnet.logianalytics.com/hc/en-us/articles/1500009569102-Properties-of-Body-in-Library-Component), [Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009569122-Properties-of-Data-Source-in-Library-Component) and [Page Panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009590801-Properties-of-Page-Panel-in-Library-Component).

The properties of the library component contents are as follows:

| Property Name | Description |
| --- | --- |
| General | |
| Select Priority | Specifies the priority of the actions that will be triggered at runtime when you select on certain objects in the library component which are bound with some actions. Select  in the value cell to set the priority in the [Select Priority](https://devnet.logianalytics.com/hc/en-us/articles/1500009585861-Select-Priority-Dialog) dialog. Data type: String |
| Height | Specifies the normal height of the contents. Enter a numeric value to change the height. Data type: Float |
| Horizontal Auto Fit | Specifies whether to change the width of the component in the contents automatically to fit the content width when the component is resized in JDashboard. Data type: Boolean |
| Minimum Height | Specifies the minimum auto fit height of the contents. The property works only when Vertical Auto Fit is set to true. Enter a numeric value to change the height. Data type: Float |
| Minimum Width | Specifies the minimum auto fit width of the contents. The property works only when Horizontal Auto Fit is set to true. Enter a numeric value to change the width. Data type: Float |
| Scroll Bar | Specifies whether to show the scrollbar when the minimum size of the library component is larger than its actual size at runtime in JDashboard. Data type: Boolean |
| Vertical Auto Fit | Specifies whether to change the height of the component in the contents automatically to fit the content height when the component is resized in JDashboard. Data type: Boolean |
| Width | Specifies the normal width of the contents. Enter a numeric value to change the width. Data type: Float |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | Indicates the CSS class that will be applied to the object. This property is read only. Data type: String |
| Other | |
| On Parameter Value Change | Specifies to use formulas to validate values of the parameters used by the library component, then when the parameter values are changed at runtime, the values will be passed to the formulas first for validation. If the values are valid, they will be applied to the parameters; if not, you can make messages returned. Note that when you define the formula, you need to make it return a blank string for valid parameter values. Choose the view elements in the business view the library component uses which are mapped to the required formulas from the drop-down list (to select multiple view elements, make use of the Ctrl or Shift keys on the keyboard, after selecting the elements, select outside of the value cell to confirm). For example, for a string type parameter which requires a value that is of 4-7 characters, you can define a formula like this:  `if(length(@P_String) > 8 ) "The value is too long."  else if (length(@P_String) < 3 ) "The value is too short."   else ""`  Then, when a string value of 9 characters is specified to the parameter, you will be prompted with the "The value is too long." message.  Data type: Object Array |
| Suppress Object Space If Not Exported | Specifies whether to suppress the space used for holding the object in the exported report result when you have specified not to include it for exporting. Data type: Boolean |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590701-Properties-of-Configuration-Panel-in-Library-Component)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009569102-Properties-of-Body-in-Library-Component)
