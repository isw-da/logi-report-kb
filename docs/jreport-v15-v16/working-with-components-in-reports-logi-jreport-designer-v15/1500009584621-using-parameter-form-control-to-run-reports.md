---
title: "Using Parameter Form Control to Run Reports"
id: 1500009584621
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584621-Using-Parameter-Form-Control-to-Run-Reports
updated_at: 2021-07-24T05:55:52Z
---

# Using Parameter Form Control to Run Reports

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563882-Using-Parameter-Control-to-Specify-a-Parameter-to-a-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584601-Using-Filter-Control-to-Filter-Data)

# Using Parameter Form Control to Run Reports

A parameter form control is a web control that is bound with the parameters used by the current report or other reports. By specifying values to the parameters in a parameter form control at runtime, end users can run the reports with the specified parameter values.

**To insert a parameter form control into a report:**

1. Do one of the following:
   * Drag the **Parameter Form Control** button ![Parameter Form Control button](https://devnet.logianalytics.com/hc/article_attachments/4404893871639/btn_paramfrmcntrl.gif) from the Components panel to the destination.
   * Select **Insert** > **Web Controls** > **Parameter Form Control**, then select the mouse button in the destination.

   The [Insert Parameter Form Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009587641-Insert-Parameter-Form-Control-Dialog) dialog appears.

   ![Insert Parameter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889333527/instprmtrfrmctrl.gif)
2. Specify the target reports to run using the parameter form control.
   * To run the current report, select **Current Report**, then specify the parameters used to run the report from the Select Parameters box. For a report created using business views, you can also use [local parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Param) to run it.
   * To run other reports, select **Others**, then select the reports you want to run. If all the selected reports contain no parameters, you cannot finish the dialog.
3. Specify whether to include the Submit button in the parameter form control. If Submit is included, it is used to submit the parameter values end users specify in the parameter form control. If Submit is not included, once end users change the value of a parameter in the parameter form control, the new value will be applied automatically.
4. When done, select **OK** to insert the parameter form control into the desired destination.

**Note:** If you save a report containing a parameter form to another directory or publish it to local directory or to Logi JReport Server, the reports that you selected in the parameter form in order to run will not be saved or published along with the report. You need to ensure that all the reports are published to the same folder on Logi JReport Server.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563882-Using-Parameter-Control-to-Specify-a-Parameter-to-a-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584601-Using-Filter-Control-to-Filter-Data)
