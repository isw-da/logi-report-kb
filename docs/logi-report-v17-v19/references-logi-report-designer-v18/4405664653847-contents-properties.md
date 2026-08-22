---
title: "Contents Properties"
id: 4405664653847
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664653847-Contents-Properties
updated_at: 2022-01-27T20:36:18Z
---

# Contents Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664652823-Configuration-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664654871-Crosstab-Properties)

# Contents Properties

This topic describes the properties of the Contents object in a library component.

| Property Name | Description |
| --- | --- |
| General | |
| Click Priority | Specifies the priority of the actions to be triggered at runtime when users select certain objects which are bound with some actions in the library component. Select the ellipsis Ellipsis button in the value cell to set the priority in the [Click Priority dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664434455-Click-Priority-Dialog-Box). Data type: String |
| Height | Specifies the normal height of the contents. Type a numeric value to change the height. Data type: Float |
| Horizontal Auto Fit | Specifies whether to change the width of the components in the library component automatically to fit the width of the contents when users resize the components in JDashboard. Data type: Boolean |
| Minimum Height | Specifies the minimum auto fit height of the contents in JDashboard. This property takes effect when you set Vertical Auto Fit of the object to "true". Type a numeric value to change the height. Data type: Float |
| Minimum Width | Specifies the minimum auto fit width of the contents in JDashboard. This property takes effect when you set Horizontal Auto Fit of the object to "true". Type a numeric value to change the width. Data type: Float |
| Scroll Bar | Specifies whether to show the scroll bar when the minimum size of the library component is larger than its actual size in JDashboard. Data type: Boolean |
| Vertical Auto Fit | Specifies whether to change the height of the components in the library component automatically to fit the height of the contents when users resize the components in JDashboard. Data type: Boolean |
| Width | Specifies the normal width of the library component. Type a numeric value to change the width. Data type: Float |
| CSS | |
| Class | Shows the CSS class the object applies. This property is read only. The style of the object is controlled by the JDashboard theme, which you can edit in the CSS file only. Data type: String |
| Other | |
| On Parameter Value Change | Specifies the formulas for validating the parameter values in the library component. After you specify the formulas, when users change the parameter values at runtime, Logi Report Engine passes the values to the formulas first for validation: if the values are valid, Logi Report Engine applies them to the parameters; otherwise, it displays the messages you define in the formulas. Choose the formulas from the drop-down list (to select multiple formulas, use the Ctrl or Shift key on the keyboard, then select outside of the value cell to confirm). For example, for a String type parameter which requires a value that is of 4-7 characters, you can define a formula like this:  `if(length(@P_String) > 8 ) "The value is too long."  else if (length(@P_String) < 3 ) "The value is too short."   else ""`  Then, when users specify a string value of 9 characters to the parameter, Logi Report Engine displays the message "The value is too long.".  Note icon When you define the formula, you need to make it return a blank string for valid parameter values.  Data type: Object Array |
| Suppress Object Space If Not Exported | Specifies whether to suppress the space for holding the objects in the output of the library component, if you have specified to exclude them from exporting. Data type: Boolean |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664652823-Configuration-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664654871-Crosstab-Properties)
