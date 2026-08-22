---
title: "Using Navigation Control to Undo/Redo Value Selection in Filter Controls"
id: 1500009563862
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563862-Using-Navigation-Control-to-Undo-Redo-Value-Selection-in-Filter-Controls
updated_at: 2023-05-14T03:37:54Z
---

# Using Navigation Control to Undo/Redo Value Selection in Filter Controls

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584601-Using-Filter-Control-to-Filter-Data)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583961-Images)

# Using Navigation Control to Undo/Redo Value Selection in Filter Controls

A navigation control can be considered as an accessorial control for filter controls and is used to deal with the value selection operations in all the filter controls in the same report.

To insert a navigation control into a report, do either of the following:

* Drag the **Navigation Control** button ![Navigation Control button](https://devnet.logianalytics.com/hc/article_attachments/4404893975063/btn_instnvgtncmtrl.gif) from the Components panel to the destination.
* Select **Insert** > **Web Controls** > **Filter Control**, then point to the destination where you want to add the navigation control and select the mouse button.

A navigation control is a combination of three buttons:

* **Back**  
   Goes back to the previous value selection status and refreshes the report data accordingly.
* **Clear**  
   Removes all the value selection histories and all the filter conditions based on the selections, and refreshes the report data accordingly.
* **Forward**  
   Goes forward to the next value selection status and refreshes the report data accordingly.

By default, these three buttons are displayed as normal buttons, however, you can change their button type to be image button if necessary. To do this:

1. Select the target button, right-click it and select **Button Type** > **Image Button** from the shortcut menu.
2. In the Image Button dialog, select **Browse** to specify the path or input the URL of the image source directly in the text field.
3. Select **OK** to confirm.

If you want to get back the normal button type, you just need to right-click the target image button, and select **Normal Button** from the Button Type submenu.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584601-Using-Filter-Control-to-Filter-Data)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583961-Images)
