---
title: "Using Parameter Control to Specify a Parameter to a Report"
id: 1500009563882
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563882-Using-Parameter-Control-to-Specify-a-Parameter-to-a-Report
updated_at: 2021-07-24T05:55:52Z
---

# Using Parameter Control to Specify a Parameter to a Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584581-Using-Advanced-Web-Controls)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584621-Using-Parameter-Form-Control-to-Run-Reports)

# Using Parameter Control to Specify a Parameter to a Report

A parameter control is a web control that is bound with a parameter used by the current report. By specifying values to the parameter in a parameter control at runtime, end users can pass the parameter values to Logi JReport and run the report with the specified values.

Parameter controls do not support inserting cascading parameters. If you want to do this, use [parameter form controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009584621-Using-Parameter-Form-Control-to-Run-Reports) instead.

**To insert a parameter control into a report**:

1. Do one of the following:
   * Drag the button of **Parameter Control**![Parameter Control](https://devnet.logianalytics.com/hc/article_attachments/4404893871895/btn_paramcntrl.gif) from the Components panel to the destination.
   * Select **Insert** > **Web Controls** > **Parameter****Control**, then select the mouse button in the destination.

   The [Insert Parameter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009566522-Insert-Parameter-Control-Dialog) dialog appears.

   ![Insert Parameter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893872151/instprmtrctrl.gif)
2. In the dialog, specify the parameter you want to add to the parameter control from the Select a Parameter box, which lists all the parameters except cascading parameters used in the current report. For a report created using business views, you can also use [a local parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Param).
3. When done, select **OK** to insert the parameter control into the desired destination.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584581-Using-Advanced-Web-Controls)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584621-Using-Parameter-Form-Control-to-Run-Reports)
