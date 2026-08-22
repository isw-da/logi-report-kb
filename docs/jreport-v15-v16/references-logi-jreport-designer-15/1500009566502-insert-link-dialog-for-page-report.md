---
title: "Insert Link Dialog (for Page Report)"
id: 1500009566502
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009566502-Insert-Link-Dialog-for-Page-Report
updated_at: 2021-07-24T05:55:06Z
---

# Insert Link Dialog (for Page Report)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587621-Insert-Group-Column-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566482-Insert-Link-Dialog-for-Web-Report-and-Library-Component-)

# Insert Link Dialog (for Page Report)

The Insert Link dialog for page report differs according to the data resource type that the page report use: [query resource](#Query) or [business view](#BV).

## When using a Query Resource

The dialog appears when you select a specified object in the design area in a page report based on query, right-click it and select Link from the shortcut menu, or select the button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) in the value cell of the Link property or Detail Report property in the Report Inspector. It helps you to [link the object to a specified target](https://devnet.logianalytics.com/hc/en-us/articles/1500009563442-Binding-a-Link-to-a-Label).

**Conditional Link**

Specifies whether it is a conditional link. If checked, the object can be linked to different targets based on different conditions.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
   Adds a new condition in the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009586381-Edit-Conditions-Dialog) dialog.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif)  
   Edits the selected condition.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
   Removes the selected condition.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)  
   Moves the selected condition one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)  
   Moves the selected condition one step down.
* **Others**  
   If checked, you can define to which target the object will be linked when none of the conditions you have specified is met.

**Link Type**

Specifies the type of the link target for the object if it is not a conditional link or for the object under the selected condition if it is a conditional link. It can be one of the following:

* [Report](#Report)
* [Master/Detail Report](#Detail)
* [URL](#URL)
* [E-mail](#Mail)
* [Content](#Content)

**More**

Displays more link options. Available only for the Report, Master/Detail Report and Content link types.

**OK**

Accepts the linking result and closes the dialog.

**Cancel**

Cancels the linking process and exits the dialog.

**Help**

Displays the help document about this feature.

### Report

It helps you to link the object to a report. [See the dialog](javascript:%20void(null)).

![Insert Link dialog - Report](https://devnet.logianalytics.com/hc/article_attachments/4404893872407/instlnk_rpt.gif)

**Report**

Specifies the report in which the linked report tab is. Select the Browse button to select the desired report in the [Select a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009588561-Select-a-Report-Dialog-for-Page-Report-) dialog.

**Report Tab**

Specifies the linked report tab.

**Target**

Specifies the window or frame in which to load the linked report. Applied only when the link is triggered in Page Report Studio.

* **<Server Setting>**  
   Loads the linked report according to setting of the Pop Up New Window for Links option in the Profile > Configure Profile > Page Report Studio > Properties > Default tab on Logi JReport Server.
* **Same Frame**  
   Loads the linked report into the same frame as the primary report.
* **Whole Window**  
   Loads the linked report into the full browser window.
* **New Window**  
   Loads the linked report into a new window. This window is not named.
* **Parent Frame**  
   Loads the linked report into the parent frame of the frame in which the primary report is.
* **Other Frame**  
   Loads the linked report into some other specified frame. If the frame name does not exist, the linked report will be loaded into a new window.

**Filter tab**

Specifies the filter conditions based on which the link relationship between the primary report and the linked report is set up.

* **Components**  
   Specifies the components in the linked report that will be interlinked with the primary report.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
     Adds a component in the linked report to be interlinked with the primary report.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif)  
     Edits the component in the linked report to be interlinked with the primary report.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
     Removes the selected component.
* **Default Linked Component**  
   Specifies the component that is displayed by default in the linked report when the link is triggered in exported result.
* **Field Conditions**   
   Lists the filter conditions between the primary report and the linked report.
  + **Fields (Primary)**  
     Lists the selected fields in the dataset used by the selected component in the primary report.
  + **OP**  
     Specifies the operator to compose the condition. It can be "=", "<>", "<", ">", "<=", ">=" or "IN".
  + **Fields (Linked)**  
     Lists the DBFields in the datasets of the linked report which are of the same data type as the selected fields in the primary report.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
     Adds a new condition line.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
     Removes the selected conditions.
* **Pass on-screen filters to the linked components**  
   Specifies whether to apply the on-screen filters which refer to the filters created via filter controls in the primary report to the selected components of the linked report.
  + **Mapping Table**   
     Opens the [Mapping Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009587841-Mapping-Table-Dialog) dialog to define the mapping relationship based on which the on-screen filters in the primary report are passed to the linked report. Activated when the trigger component in the primary report and the selected component in the linked report use different datasets.

**Parameters tab**

This tab is available when the linked report uses parameters. It helps you to assign values to the parameters of the linked report automatically.

* **Parameters**  
   Lists all parameters contained in the datasets of the linked report.
* **Value**  
   Lists all the DBFields, formulas, summaries and parameters in the datasets of the primary report which are of the same data type as the parameters of the linked report. Select the field the value of which you want to assign to parameter of the linked report from the drop-down list.

**Advanced tab**

Specifies to pass the values of the filter objects such as filter controls in the primary report to those in the linked report.

* **Primary Report Property/Object**  
   Displays the filter objects in the primary report the values of which will be passed to those in the linked report. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) to select a filter object in the primary report in the [Select Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009567562-Select-Value-Dialog) dialog.
* **Linked Report Property/Object**  
   Displays the filter objects in the linked report which will adopt the values passed from filter objects in the primary report. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) to select a filter object in the linked report in the Select Value dialog. You need to make sure that values of the filter object in the primary report can be applied to the filter object in the linked report in the same line.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
   Adds a new line to pass values between the filter objects in the primary report and the linked report.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
   Removes the selected lines.

**Pass style group information down to linked report**

Specifies whether or not to apply the style group of the primary report to the linked report.

### Master/Detail Report

It helps you to link the object to a detail report. [See the dialog](javascript:%20void(null)).

![Insert Link dialog - Master/Detail Report](https://devnet.logianalytics.com/hc/article_attachments/4404889333783/instlnk_dtl.gif)

**Report**

Specifies the report in which the detail report tab is. Select the Browse button to select the desired report in the [Select a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009588561-Select-a-Report-Dialog-for-Page-Report-) dialog.

**Report Tab**

Specifies the target detail report tab.

**Component**

Specifies the component in the detail report tab that will be interlinked with the master report. Select the Browse button to add the components. You can add more than one component as long as the components are based on the same dataset.

**Target**

Specifies the window or frame where to load the detail report.

* **<Server Setting>**  
   Loads the detail report according to setting of the Pop up New Window for Links option in the Profile > Configure Profile > Page Report Studio > Properties > Default tab on Logi JReport Server.
* **Same Frame**  
   Loads the detail report into the same frame as the master report.
* **Whole Window**  
   Loads the detail report into the full browser window.
* **New Window**  
   Loads the detail report into a new window, which is not named. If this is selected, the detail report will be opened independently when you select the trigger in Page Report Studio, that is to say the join and filter conditions you set between the master report and detail report will not be applied.
* **Parent Frame**  
   Loads the detail report into the parent frame of the frame in which the master report is.
* **Other Frame**  
   Loads the detail report into some other specified frame. If the frame name does not exist, the detail report will be loaded into a new window.

**Anchor**

Specifies the relationships between the master report and the detail report.

* **Column in Detail****Report**   
   Specifies the field in the detail report which will be used to link the detail report with the master.
* **OP**  
   Specifies the operator. It can be "=", "<>", "<", ">", "<="or ">=".
* **Column in Master****Report**   
   Specifies the field in the master report.

**Conditions tab**

Specifies the filter conditions between the master report and the detail report.

* **Field Conditions**  
   Lists all the filter conditions.
  + **Fields (MasterReport)**  
     Lists the selected fields of the master report.
  + **OP**  
     Specifies the operator to compose the condition. It can be "=", "<>", "<", ">", "<="or ">=".
  + **Fields (DetailReport)**  
     Lists the DBFields in the datasets of the detail report which are of the same data type as the selected fields in the master report.
  + **More**  
     Specifies relations between two conditions. Can be AND or OR.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
     Adds a new condition line.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
     Removes the selected conditions.

**Parameters tab**

This tab is only available when there is at least one parameter applied in the filters of the queries that the detail report uses. It helps you to assign values to the parameters of the detail report automatically.

* **Parameters (Detail Report)**  
   Lists all parameters contained in the datasets of the detail report.
* **Column (Master Report)**  
   Lists all the DBFields, formulas and summaries in the datasets of the master report which are of the same data type as the parameters of the detail report. Select the field the value of which you want to assign to parameter of the detail report from the drop-down list.

**Use the same encoding and DB setting for the detail report as that of the master report**

Specifies whether the detail report uses the same encoding and DB settings as per the master report.

### URL

It helps you to link the object to a location specified by a URL. [See the dialog](javascript:%20void(null)).

![Insert Link dialog - URL](https://devnet.logianalytics.com/hc/article_attachments/4404893872663/instlnk_url.gif)

**Hyperlink**

Specifies the URL of the location that the object will be linked to. Fields can work in the hyperlink only when they are inserted via the Add Dynamic Field option.

* **Add Dynamic Field**   
  Opens the [Select Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009588681-Select-Field-Dialog) dialog to insert a field into the URL.

**Target**

Specifies the window or frame in which to load the location specified by the URL. Applied only when the link is triggered in Page Report Studio.

* **<Server Setting>**  
   Loads the linked file according to setting of the Pop Up New Window for Links option in the Profile > Configure Profile > Page Report Studio > Properties > Default tab on Logi JReport Server.
* **Same Frame**  
   Loads the linked file into the same frame as the link.
* **Whole Window**  
   Loads the linked file into the full browser window.
* **New Window**  
   Loads the linked file into a new window. This window is not named.
* **Parent Frame**  
   Loads the linked file into the parent frame of the frame that contains the link.
* **Other Frame**  
   Loads the linked file into some other specified frame. If the frame name does not exist, the linked file will be loaded into a new window.

### E-mail

It helps you to link the object to an e-mail address. [See the dialog](javascript:%20void(null)).

![Insert Link dialog - E-mail](https://devnet.logianalytics.com/hc/article_attachments/4404889334039/instlnk_mail.gif)

**Hyperlink**

Specifies the [e-mail address](https://devnet.logianalytics.com/hc/en-us/articles/1500009563442-Binding-a-Link-to-a-Label#MailSyntax) that the object will be linked to. Then after you select the trigger object, an e-mail will be popped with the information specified in the Hyperlink box. You can then further customize the e-mail and send it.

* **Add Dynamic Field**  
   Opens the [Select Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009588681-Select-Field-Dialog) dialog to insert a field into the e-mail address.

### Content

It helps you to link the object to a Blob data type field. The Blob data type field will be bound to the object and displayed as a hyperlink. You can download the Blob content by selecting this hyperlink. In Logi JReport, Blob could be image, Binary, Blob, Clob, LongBlob, LongClob, Varbinary, Longvarbinary, and so on. [See the dialog](javascript:%20void(null)).

![Insert Link dialog - Content](https://devnet.logianalytics.com/hc/article_attachments/4404893872919/instlnk_cntnt.gif)

**Query**

Specifies the query which contains the required Blob data type field. Only queries from the same data source connection as the current report are listed.

When you set the link type to Content, Logi JReport will check whether there are such kind of queries available. If not, options for this link type will be disabled.

**Content Type**

Specifies the content type for the Blob type data. You can select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif) to bind it with a field column or a record level pass one formula in the selected query.

**File Name**

Specifies the file name for the linked Blob type data. You can select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif) to bind it with a field column or a record level pass one formula in the selected query.

**Content**

Specifies the Blob data type field in the selected query.

**Filter tab**

Specifies the link conditions between the query used by the current report and the query that contains the linked Blob content.

* **Field Conditions**   
   Lists the filter conditions between the two queries.
  + **Fields (Primary)**  
     Lists the selected fields of the query used by the current report.
  + **OP**  
     Specifies the operator to compose the condition. It can be "=", "<>", "<", ">", "<=", ">=" or "IN".
  + **Fields (Linked)**  
     Lists the DBFields in the datasets of the query that contains the linked Blob content, which are of the same data type as the selected fields in the query used by the current report.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
     Adds a new condition line.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
     Removes the selected conditions.

**Parameters tab**

This tab is available when the query that contains the linked Blob content uses parameters. It helps you to assign values to the parameters automatically.

* **Parameters**  
   Lists all the parameters the query that contains the linked Blob content uses.
* **Value**  
   Lists all the DBFields, formulas, summaries and parameters in the query used by the current report, which are of the same data type as the parameters the query that contains the linked Blob content uses. Select the field the value of which you want to assign to a parameter from the drop-down list.

## When using a Business View

The dialog appears when you select a specified object in the design area in a page report based on business view, right-click it and select Link from the shortcut menu, or select the button ![More button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) in the value cell of the Link property in the Report Inspector. It helps you to [link the object to a specified target](https://devnet.logianalytics.com/hc/en-us/articles/1500009563442-Binding-a-Link-to-a-Label).

**Conditional Link**

Specifies whether it is a conditional link. If checked, the object can be linked to different targets based on different conditions.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
   Adds a new condition in the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009586381-Edit-Conditions-Dialog) dialog.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif)  
   Edits the selected condition.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
   Removes the selected condition.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)  
   Moves the selected condition one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)  
   Moves the selected condition one step down.
* **Others**  
   If checked, you can define to which target the object will be linked when none of the conditions you have specified is met.

**Link Type**

Specifies the type of the link target for the object if it is not a conditional link or for the object under the selected condition if it is a conditional link. It can be one of the following:

* [Report](#Report-bv)
* [URL](#URL-bv)
* [E-mail](#Mail-bv)

**More**

Displays more link options. Available only for the Report link type.

**OK**

Accepts the linking result and closes the dialog.

**Cancel**

Cancels the linking process and exits the dialog.

**Help**

Displays the help document about this feature.

### Report

It helps you to link the object to a report. [See the dialog](javascript:%20void(null)).

![Insert Link - Report dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893872407/instlnk_rpt.gif)

**Report**

Specifies the report in which the linked report tab is. Select the Browse button to select the desired report in the [Select a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009588561-Select-a-Report-Dialog-for-Page-Report-) dialog.

**Report Tab**

Specifies the linked report tab.

**Target**

Specifies the window or frame in which to load the linked report. Applied only when the link is triggered in Page Report Studio.

* **<Server Setting>**  
   Loads the linked report according to setting of the Pop Up New Window for Links option in the Profile > Configure Profile > Page Report Studio > Properties > Default tab on Logi JReport Server.
* **Same Frame**  
   Loads the linked report into the same frame as the primary report.
* **Whole Window**  
   Loads the linked report into the full browser window.
* **New Window**  
   Loads the linked report into a new window. This window is not named.
* **Parent Frame**  
   Loads the linked report into the parent frame of the frame in which the primary report is.
* **Other Frame**  
   Loads the linked report into some other specified frame. If the frame name does not exist, the linked report will be loaded into a new window.

**Filter tab**

Specifies the filter conditions based on which the link relationship between the primary report and the linked report is set up.

* **Components**  
   Specifies the components in the linked report that will be interlinked with the primary report.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
     Adds a component in the linked report to be interlinked with the primary report.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif)  
     Edits the component in the linked report to be interlinked with the primary report.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
     Removes the selected component.
* **Default Linked Component**  
   Specifies the component that is displayed by default in the linked report when the link is triggered in exported result.
* **Field Conditions**   
   Lists the filter conditions between the primary report and the linked report.
  + **Fields (Primary)**  
     Lists the selected fields in the dataset used by the selected component in the primary report.
  + **OP**  
     Specifies the operator to compose the condition. It can be "=", "<>", "<", ">", "<=", ">=" or "IN".
  + **Fields (Linked)**  
     Lists the DBFields in the datasets of the linked report which are of the same data type as the selected fields in the primary report.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
     Adds a new condition line.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
     Removes the selected conditions.
* **Pass on-screen filters to the linked components**  
   Specifies whether to apply the on-screen filters which refer to the filters created via filter controls in the primary report to the selected components of the linked report.
  + **Mapping Table**   
     Opens the [Mapping Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009587841-Mapping-Table-Dialog) dialog to define the mapping relationship based on which the on-screen filters in the primary report are passed to the linked report. Activated when the trigger component in the primary report and the selected component in the linked report use different datasets.

**Parameters tab**

This tab is available when the linked report uses parameters. It helps you to assign values to the parameters of the linked report automatically.

* **Parameters**  
   Lists all parameters contained in the datasets of the linked report.
* **Value**  
   Lists all the DBFields, formulas, summaries and parameters in the datasets of the primary report which are of the same data type as the parameters of the linked report. Select the field the value of which you want to assign to parameter of the linked report from the drop-down list.

**Advanced tab**

Specifies to pass the values of the filter objects such as filter controls in the primary report to those in the linked report.

* **Primary Report Property/Object**  
   Displays the filter objects in the primary report the values of which will be passed to those in the linked report. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) to select a filter object in the primary report in the [Select Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009567562-Select-Value-Dialog) dialog.
* **Linked Report Property/Object**  
   Displays the filter objects in the linked report which will adopt the values passed from filter objects in the primary report. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) to select a filter object in the linked report in the Select Value dialog. You need to make sure that values of the filter object in the primary report can be applied to the filter object in the linked report in the same line.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
   Adds a new line to pass values between the filter objects in the primary report and the linked report.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
   Removes the selected lines.

**Pass style group information down to linked report**

Specifies whether or not to apply the style group of the primary report to the linked report.

### URL

It helps you to link the object to a location specified by a URL. [See the dialog](javascript:%20void(null)).

![Insert Link - URL dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893872663/instlnk_url.gif)

**Hyperlink**

Specifies the URL of the location that the object will be linked to. Fields can work in the hyperlink only when they are inserted via the Add Dynamic Field option.

* **Add Dynamic Field**   
   Opens the [Select Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009588681-Select-Field-Dialog) dialog to insert a field into the URL.

**Target**

Specifies the window or frame in which to load the location specified by the URL. Applied only when the link is triggered in Page Report Studio.

* **<Server Setting>**  
   Loads the linked file according to setting of the Pop Up New Window for Links option in the Profile > Configure Profile > Page Report Studio > Properties > Default tab on Logi JReport Server.
* **Same Frame**  
   Loads the linked file into the same frame as the link.
* **Whole Window**  
   Loads the linked file into the full browser window.
* **New Window**  
   Loads the linked file into a new window. This window is not named.
* **Parent Frame**  
   Loads the linked file into the parent frame of the frame that contains the link.
* **Other Frame**  
   Loads the linked file into some other specified frame. If the frame name does not exist, the linked file will be loaded into a new window.

### E-mail

It helps you to link the object to an e-mail address. [See the dialog](javascript:%20void(null)).

![Insert Link - E-mail dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889334039/instlnk_mail.gif)

**Hyperlink**

Specifies the [e-mail address](https://devnet.logianalytics.com/hc/en-us/articles/1500009563442-Binding-a-Link-to-a-Label#MailSyntax) that the object will be linked to. Then after you select the trigger object, an e-mail will be popped with the information specified in the Hyperlink box. You can then further customize the e-mail and send it.

* **Add Dynamic Field**  
   Opens the [Select Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009588681-Select-Field-Dialog) dialog to insert a field into the e-mail address.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587621-Insert-Group-Column-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566482-Insert-Link-Dialog-for-Web-Report-and-Library-Component-)
