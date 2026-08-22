---
title: "Editing the Display Sequence of Parameters"
id: 1500009590101
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590101-Editing-the-Display-Sequence-of-Parameters
updated_at: 2021-07-24T05:54:30Z
---

# Editing the Display Sequence of Parameters

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590141-Using-Built-in-Functions-to-Set-Date-and-Time-Parameter-Values)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568622-Controlling-Multiple-Parameters)

# Editing the Display Sequence of Parameters

When you run reports with parameters, you will need to specify the values of the parameters. By default the parameters are displayed in ascending alphabetic order in the parameter value specifying dialog or page, thus the parameter pEndDate appears before pStartDate which would be very confusing to users. Logi JReport allows you to customize the display order of the parameters so that they could be shown in a more reasonable sequence. The order will not affect the display sequence of the parameters in the resource tree, which is determined by the [Sort setting](https://devnet.logianalytics.com/hc/en-us/articles/1500009588081-Options-Dialog#Sort) in the Options dialog.

The display order of parameters can be customized at two levels: catalog and specific report. When the order of parameters in a catalog is specified, the order will be applied to all reports using the catalog. When both levels of orders are configured, the report level order has higher priority than the catalog level one.

**To adjust the parameter order for a catalog:**

1. Open the catalog containing parameters for which you would like to adjust the order.
2. In the Catalog Manager, expand a data source, select the **Parameters** node or any parameter in the node, then select **Parameter Order**  on the Catalog Manager toolbar. The [Parameter Order](https://devnet.logianalytics.com/hc/en-us/articles/1500009588201-Parameter-Order-Dialog) dialog appears.

   ![Parameter Order dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889301527/prmodr.gif)
3. Make use of the Move Up and Move Down buttons to adjust the order of the parameters, or simply drag and drop the parameters in the Parameters box.
   When a catalog contains a lot of parameters, it might be much easier by dragging and dropping.
4. When done, select **OK** to accept the changes.

**To adjust the parameter order for a specific report:**

1. Open the report containing parameters for which you would like to adjust the order, then select **Report** > **Parameter Order**. The Parameter Order dialog appears, listing only the parameters used in the currently open report.
2. Make use of the Move Up and Move Down buttons to adjust the order of the parameters, or simply drag and drop a parameter. The parameter order specified in the report will override the one in the catalog if they are different.
3. Select **OK** to apply the specified order.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590141-Using-Built-in-Functions-to-Set-Date-and-Time-Parameter-Values)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568622-Controlling-Multiple-Parameters)
