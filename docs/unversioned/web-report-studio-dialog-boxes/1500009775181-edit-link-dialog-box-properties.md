---
title: "Edit Link Dialog Box Properties"
id: 1500009775181
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009775181-Edit-Link-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:29Z
---

# Edit Link Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009775161-Edit-Image-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747022-Edit-Multimedia-Dialog-Box-Properties)

# Edit Link Dialog Box Properties

This topic describes how you can use the Edit Link dialog box to [edit the link](https://devnet.logianalytics.com/hc/en-us/articles/1500009778801-Adding-Links-in-Web-Report) on the selected object. Server displays the dialog box when you select an object which contains the defined link, right-click it, and select **Edit Link** on the shortcut menu.

**Conditional Link**

Specifies whether it is a conditional link. If the option is selected, the object can be linked to different targets based on different conditions.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif)  
   Adds a new condition in the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009746942-Edit-Conditions-Dialog-Box-Properties) dialog box.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404880163863/btn_wbrpt_edit.gif)  
   Edits the selected condition.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)  
   Removes the selected condition.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)**Move Up button**  
   Moves the selected condition higher in the list.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)**Move Down button**  
   Moves the selected condition lower in the list.
* **Others**  
   If the option is selected, you can define to which target the object will be linked when none of the conditions you have specified is met.

**Link Type**

Specifies the type of the link target for the object if it is not a conditional link or for the object under the selected condition if it is a conditional link. It can be one of the following:

* [Report](#Report)
* [URL](#URL)
* [E-mail](#Mail)
* [Content](#Content)

**More**

Displays more link options. Available only for the Report and Content link types.

**OK**

Applies the settings and closes the dialog box.

**Cancel**

Cancels the changes and exits the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

## Report

It helps you to link a specified object to a report.

![Edit Link dialog - Report](https://devnet.logianalytics.com/hc/article_attachments/4404885487255/edtlnk_rpt.gif)

**Report**

Specifies the target linked report. Select the Browse button to select the desired report in the [Select a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009776281-Select-a-Report-Dialog-Box-Properties) dialog box.

**Target**

Specifies the window or frame in which to load the linked report.

* **New Window**  
   Loads the linked report into a new window. This window is not named.
* **Parent Frame**  
   Loads the linked report into the parent frame of the frame that contains the link. Not available for link in chart.
* **Same Frame**  
   Loads the linked report into the same frame as the link.
* **Whole Window**  
   Loads the linked report into the full browser window. Not available for link in chart.
* **<Server Setting>**  
   Loads the linked report according to setting of the [Target of Detail Table Report and Links](https://devnet.logianalytics.com/hc/en-us/articles/1500009750242-Customizing-Web-Report-Studio-Profile#Target) option in the Web Report Studio profile.
* **Other Frame**  
   Loads the linked report into some other specified frame. If the frame name does not exist, the linked file will be loaded into a new window.

**Filter tab**

Specifies the filter conditions based on which the link relationship between the primary report and the linked report is set up.

* **Components**  
   Specifies the components in the linked report that will be interlinked with the primary report.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif)  
     Adds a component in the linked report to be interlinked with the primary report.
  + ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)  
     Removes the selected component.
* **Default Linked Component**  
   Specifies the component that is displayed by default in the linked report when the link is triggered in exported result.
* **Field Conditions**  
   Lists the link conditions between the primary report and the linked report.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif)  
     Adds a new condition line.
  + ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)  
     Removes the selected condition lines.
  + **Fields (Primary)**  
     Lists the selected fields in the business view used by the selected component in the primary report.
  + **OP**  
     Specifies the operator to compose the condition. It can be "=", "<>", "<", ">", "<=", ">=" or "IN".
  + **Fields (Linked)**  
     Lists the fields in the business views of the linked report which are of the same data type as the selected fields in the primary report.
* **Pass on-screen filters to the linked components**  
  Specifies whether to apply the on-screen filters which refer to the filters created via the Filter panel and filter controls in the primary report to the selected components of the linked report.
  + **Mapping Table**   
     Opens the [Mapping Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009776081-Mapping-Table-Dialog-Box-Properties) dialog box to define the mapping relationship based on which the on-screen filters in the primary report are passed to the linked report. Activated when the trigger component in the primary report and the selected component in the linked report use different business views.

**Parameters tab**

This tab is available when the linked report uses parameters. It helps you to assign values to the parameters of the linked report automatically.

* **Parameter from Linked Report**  
   Lists all parameters contained in the linked report.
* **Field from Primary Report**  
   Lists all the DBFields, formulas, summaries and parameters in the primary report which are of the same data type as the parameters of the linked report. Select the field the value of which you want to assign to parameter of the linked report from the drop-down list. If the selected field is a parameter field, you can choose to assign its current value or initial value to the parameter of the linked report.
  + **Current Value**  
     If selected, the most recently specified value of the primary report parameter will be assigned to the parameter of the linked report.
  + **Initial Value**  
     If selected, the original value of the primary report parameter will be assigned to the parameter of the linked report.

**Advanced tab**

Specifies to pass the values of the filter objects such as filter controls in the primary report to those in the linked report.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif)  
   Adds a new line to pass values between the filter objects in the primary report and the linked report.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)  
   Removes the selected lines.
* **Primary Report Property/Object**  
   Displays the filter objects in the primary report the values of which will be passed to those in the linked report. Select ![Select Value](https://devnet.logianalytics.com/hc/article_attachments/4404885320983/btn_chsr.gif) to select a filter object in the primary report in the [Select Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009776301-Select-Value-Dialog-Box-Properties) dialog box.
* **Linked Report Property/Object**  
   Displays the filter objects in the linked report which will adopt the values passed from filter objects in the primary report. Select ![Select Value](https://devnet.logianalytics.com/hc/article_attachments/4404885320983/btn_chsr.gif) to select a filter object in the linked report in the Select Value dialog box. You need to make sure that values of the filter object in the primary report can be applied to the filter object in the linked report in the same line.

**Pass style group information down to linked report**

Specifies whether to apply the style group of the primary report to the linked report.

## URL

It helps you to link a specified object to a location specified by a URL.

![Edit Link dialog - URL](https://devnet.logianalytics.com/hc/article_attachments/4404885487767/edtlnk_url.gif)

**Hyperlink**

Specifies the URL for the hyperlink that is to be used to link the object.

* **Add Dynamic Field**  
   Opens the [Select Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009776241-Select-Field-Dialog-Box-Properties#Link) dialog box to insert a field into the URL.

**Target**

Specifies the window or frame in which to load the location specified by the URL.

* **New Window**  
   Loads the linked file into a new window. This window is not named.
* **Parent Frame**  
   Loads the linked file into the parent frame of the frame that contains the link.
* **Same Frame**  
   Loads the linked file into the same frame as the link.
* **Whole Window**  
   Loads the linked file into the full browser window.
* **<Server Setting>**  
   Loads the linked file according to setting of the [Target of Detail Table Report and Links](https://devnet.logianalytics.com/hc/en-us/articles/1500009750242-Customizing-Web-Report-Studio-Profile#Target) option in the Web Report Studio profile.
* **Other Frame**  
   Loads the linked file into some other specified frame. If the frame name does not exist, the linked file will be loaded into a new window.

## E-Mail

It helps you to link the specified object to an e-mail address.

![Edit Link dialog - E-mail](https://devnet.logianalytics.com/hc/article_attachments/4404880394391/edtlnk_mal.gif)

**Hyperlink**

Specifies the [e-mail address](https://devnet.logianalytics.com/hc/en-us/articles/1500009778801-Adding-Links-in-Web-Report#MailSyntax) that the object will be linked to. Then after you trigger the link, an e-mail will be popped with the information specified in the Hyperlink box. You can then further customize the e-mail and send it.

* **Add Dynamic Field**  
   Opens the [Select Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009776241-Select-Field-Dialog-Box-Properties#Link) dialog box to insert a field into the e-mail address.

## Content

It helps you to link the object to a Blob data type field. The Blob data type field will be bound to the object and displayed as a hyperlink, you can download the Blob content by triggering the link. In Logi Report, Blob could be image, Binary, Blob, Clob, LongBlob, LongClob, Varbinary, Longvarbinary, and so on.

![Edit Link dialog - Content](https://devnet.logianalytics.com/hc/article_attachments/4404885488151/edtlnk_cntnt.gif)

**Query**

Specifies the business view which contains the required Blob data type field.

When you set the link type to Content, Logi Report will check whether there are such kind of business views available in the current catalog. If not, options for this link type will be disabled.

**Content Type**

Specifies the content type for the Blob type data. You can select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404880159895/btn_wbrpt_fmla.gif) to bind it with a string type business view element, or a dynamic formula in the current report.

**File Name**

Specifies the file name for the linked Blob type data. You can select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404880159895/btn_wbrpt_fmla.gif) to bind it with a string type business view element, or a dynamic formula in the current report.

**Content**

Specifies the Blob data type field in the selected business view.

**Filter tab**

Specifies the link conditions between the business view used by the current report and the business view that contains the linked Blob content.

* **Field Conditions**   
  Lists the filter conditions between the two business views.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif)  
     Adds a new condition line.
  + ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)  
     Removes the selected condition lines.
  + **Fields (Primary)**  
     Lists the selected fields of the business view used by the current report.
  + **OP**  
     Specifies the operator to compose the condition. It can be "=", "<>", "<", ">", "<=", ">=" or "IN".
  + **Fields (Linked)**  
     Lists the fields in the business view that contains the linked Blob content, which are of the same data type as the selected fields in the business view used by the current report.

**Parameters tab**

This tab is available when the business view that contains the linked Blob content uses parameters. It helps you to assign values to the parameters automatically.

* **Parameters**  
   Lists all parameters the business view that contains the linked Blob content uses.
* **Value**  
   Lists all the view elements in the business view as well as formulas, aggregations and parameters used by the current report, which are of the same data type as the parameters the business view that contains the linked Blob content uses. Select the field the value of which you want to assign to a parameter from the drop-down list.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009775161-Edit-Image-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747022-Edit-Multimedia-Dialog-Box-Properties)
