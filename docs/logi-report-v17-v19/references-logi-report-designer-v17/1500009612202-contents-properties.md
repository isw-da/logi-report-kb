---
title: "Contents Properties"
id: 1500009612202
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009612202-Contents-Properties
updated_at: 2021-07-24T16:03:38Z
---

# Contents Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009612182-Configuration-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009635301-Crosstab-Properties)

# Contents Properties

This topic lists the properties of the Contents object in a library component.

| Property Name | Description |
| --- | --- |
| General | |
| Select Priority | Specifies the priority of the actions that will be triggered at runtime when you select on certain objects in the library component which are bound with some actions. Select  in the value cell to set the priority in the [Select Priority](https://devnet.logianalytics.com/hc/en-us/articles/1500009630041-Click-Priority-Dialog) dialog. Data type: String |
| Height | Specifies the normal height of the contents. Type a numeric value to change the height. Data type: Float |
| Horizontal Auto Fit | Specifies whether to change the width of the component in the contents automatically to fit the content width when the component is resized in JDashboard. Data type: Boolean |
| Minimum Height | Specifies the minimum auto fit height of the contents. The property works only when Vertical Auto Fit is set to true. Type a numeric value to change the height. Data type: Float |
| Minimum Width | Specifies the minimum auto fit width of the contents. The property works only when Horizontal Auto Fit is set to true. Type a numeric value to change the width. Data type: Float |
| Scroll Bar | Specifies whether to show the scrollbar when the minimum size of the library component is larger than its actual size at runtime in JDashboard. Data type: Boolean |
| Vertical Auto Fit | Specifies whether to change the height of the component in the contents automatically to fit the content height when the component is resized in JDashboard. Data type: Boolean |
| Width | Specifies the normal width of the contents. Type a numeric value to change the width. Data type: Float |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009635501-Label-Properties#CSS) | Indicates the CSS class that will be applied to the object. This property is read only. The style of the contents is controlled by the JDashboard theme, which can only be edited in the CSS file. Data type: String |
| Other | |
| On Parameter Value Change | Specifies to use formulas to validate values of the parameters used by the library component, then when the parameter values are changed at runtime, the values will be passed to the formulas first for validation. If the values are valid, they will be applied to the parameters; if not, you can make messages returned. Note that when you define the formula, you need to make it return a blank string for valid parameter values. Choose the view elements in the business view the library component uses which are mapped to the required formulas from the drop-down list (to select multiple view elements, make use of the Ctrl or Shift keys on the keyboard, after selecting the elements, select outside of the value cell to confirm). For example, for a string type parameter which requires a value that is of 4-7 characters, you can define a formula like this:  `if(length(@P_String) > 8 ) "The value is too long."  else if (length(@P_String) < 3 ) "The value is too short."   else ""`  Then, when a string value of 9 characters is specified to the parameter, you will be prompted with the "The value is too long." message.  Data type: Object Array |
| Suppress Object Space If Not Exported | Specifies whether to suppress the space used for holding the object in the exported report result when you have specified not to include it for exporting. Data type: Boolean |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009612182-Configuration-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009635301-Crosstab-Properties)
