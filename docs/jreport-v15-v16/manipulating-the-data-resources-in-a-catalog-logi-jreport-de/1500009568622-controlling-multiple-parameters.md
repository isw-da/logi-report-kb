---
title: "Controlling Multiple Parameters"
id: 1500009568622
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568622-Controlling-Multiple-Parameters
updated_at: 2021-07-24T05:54:30Z
---

# Controlling Multiple Parameters

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590101-Editing-the-Display-Sequence-of-Parameters)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590201-Importing-Parameter-Values)

# Controlling Multiple Parameters

When multiple parameters are used in a report, but you only want to show some of them when running it, you can group them and then select the parameter you want for the report. The parameter values not entered will use their default value. See the example below:

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, expand **Data Source 1**, then right-click the **Parameters** node and select **New Parameter**.
3. In the New Parameter dialog, enter **GroupParam** in the Name field, select **Parameters** from the Value Type drop-down list, then add three parameters as the default values of GroupParam as shown in the following image:

   ![New Parameter](https://devnet.logianalytics.com/hc/article_attachments/4404893828375/prmtr_app_cntrl1.gif)
4. Open an existing page report. Insert the parameters P\_Category, P\_Month, P\_Country, and GroupParam into a report tab of the report.
5. View the report, and the Enter Parameter Values dialog appears. You can select the parameter you want from the GroupParam drop-down list.

   ![Enter Parameter Values](https://devnet.logianalytics.com/hc/article_attachments/4404893828759/prmtr_app_cntrl2.gif)

   Select @P\_Category, the P\_Category parameter is displayed in the dialog and you can select or type in a value for the parameter. If you select @P\_Month,@P\_Country, then both the parameters P\_Month and P\_Country will be displayed for you to specify values with which to run the report.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590101-Editing-the-Display-Sequence-of-Parameters)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590201-Importing-Parameter-Values)
