---
title: "Contents Properties"
id: 28898505458829
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898505458829-Contents-Properties
updated_at: 2024-09-30T09:10:56Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Contents Properties

This topic describes the properties of the Contents object in a library component.

| Property Name | Description |
| --- | --- |
| General |  |
| Click Priority | Specifies the priority of the actions to be triggered at runtime when users select certain objects which are bound with some actions in the library component. Select the ellipsis in the value cell to set the priority in the Click Priority dialog box. Data type: String |
| Height | Specifies the normal height of the contents object. Type a numeric value to change the height. Data type: Float |
| Horizontal Auto Fit | Specifies whether to change the width of the components in the library component automatically to fit the width of the contents object when users resize the components in JDashboard. Data type: Boolean |
| Minimum Height | Specifies the minimum auto fit height of the contents object in JDashboard, when you set Vertical Auto Fit of the object to "true". Type a numeric value to change the height. Data type: Float |
| Minimum Width | Specifies the minimum auto fit width of the contents object in JDashboard, when you set Horizontal Auto Fit of the object to "true". Type a numeric value to change the width. Data type: Float |
| Scroll Bar | Specifies whether to show the scroll bar when the minimum size of the library component is larger than its actual size in JDashboard. Data type: Boolean |
| Vertical Auto Fit | Specifies whether to change the height of the components in the library component automatically to fit the height of the contents object when users resize the components in JDashboard. Data type: Boolean |
| Width | Specifies the normal width of the library component. Type a numeric value to change the width. Data type: Float |
| CSS |  |
| Class | Shows the CSS class the object applies. Read only. The style of the object is controlled by JDashboard theme, which you can edit in the corresponding CSS file only. Data type: String |
| Other |  |
| On Parameter Value Change | Specifies the formulas for validating the parameter values in the library component. After you specify the formulas, when users change the parameter values at runtime, Report Engine passes the values to the formulas first for validation: if the values are valid, Report Engine applies them to the parameters; otherwise, it displays the messages you define in the formulas. Choose the formulas from the drop-down list (to select multiple formulas, use the Ctrl or Shift key on the keyboard, then select outside the value cell to confirm). For example, for a String type parameter which requires a value that is of 4-7 characters, you can define a formula like this: if(length(@P_String) > 8 ) "The value is too long." else if (length(@P_String) Previous Topic  Next Topic
