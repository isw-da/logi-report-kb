---
title: "Chart Definition Dialog Box Properties"
id: 1500009744102
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744102-Chart-Definition-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:20Z
---

# Chart Definition Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771981-Button-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772001-Chart-Wizard-Properties)

# Chart Definition Dialog Box Properties

You can use the Chart Definition dialog box to [modify the definition of a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009749022-Manipulating-Data-Components-in-Page-Report#Chart). This topic describes the options in the dialog box.

This topic contains the following sections:

* [Chart Type Tab Properties](#Type)
* [Display Tab Properties](#Display)
* [Style Tab Properties](#Style)

**OK**

Applies the settings and closes the dialog box.

**Cancel**

Cancels the settings and closes the dialog box.

**Help**

Displays the help document about this feature.

## Chart Type Tab Properties

You can set the type of the chart in this tab.

![Chart Definition dialog - Chart Type tab](https://devnet.logianalytics.com/hc/article_attachments/4404880252567/chtdef_type.gif)

**Chart Type**

Chart types in Logi Report.

**Subtype**

Shows the subtypes of the selected chart type in thumbnail form.

**Chart Type Groups**

Lists the subtypes defined for the chart.

To replace a chart type with another one, first select it, then select the chart type you want and a sub type.

If you want to create a combo chart, select **<Add Combo Type>** of Primary Axis or Secondary Axis in the Chart Type Groups box. Studio adds an additional subtype. To replace the additional subtype, select it, then specify the required type and subtype respectively. To add more subtypes, repeat the procedure.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)

Removes the selected subtype. At least one type should remain for the Primary Axis to create the chart.

## Display Tab Properties

You can set the fields to display in the chart.

![Chart Definition dialog - Display tab](https://devnet.logianalytics.com/hc/article_attachments/4404880252823/chtdef_dsply.gif)

**Resources**

Displays all the group objects and aggregation objects in the chart.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif)

Adds the selected view element to the chart.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif)

Removes the selected view element.

**Category**

Lists the group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) you want to display on the category axis of the chart.

**Series**

Lists the group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) you want to display on the series axis of the chart.

**Show Values**

Lists the aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151959/btn_bvaggrgtn.gif) and additional values ![Additional Value](https://devnet.logianalytics.com/hc/article_attachments/4404880175511/btn_wbrpt_adtnl.gif) you want to display on the value axis of the chart.

* ![Edit Additional Values](https://devnet.logianalytics.com/hc/article_attachments/4404880196759/btn_pgrpt_edit.gif)  
   Opens the [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009772081-Edit-Additional-Values-Dialog-Box-Properties) dialog box to edit an additional value. Available only when you select an additional value in the **Show Values** box.

**Order/Select N**

Opens the [Order/Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009772821-Order-Select-N-Dialog-Box-Properties) dialog box to define the sort order and Select N condition in the chart.

## Style Tab Properties

You can select a style for the chart. Studio hides this tab when there is only one style available.

![Chart Definition dialog - Style tab](https://devnet.logianalytics.com/hc/article_attachments/4404885599511/chtdef_style.gif)

**Style**

Lists the styles applicable to the component.

* **Custom**  
   There is no style information in this style. Logi Report only uses it to support reports that were created in previous versions when they did not bind any style or their bound styles are not in the style list.

**Preview**

Displays a diagram to illustrate the effect of the selected style on the component.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771981-Button-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772001-Chart-Wizard-Properties)
