---
title: "Edit Link Dialog"
id: 1500009607902
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009607902-Edit-Link-Dialog
updated_at: 2021-07-24T16:04:46Z
---

# Edit Link Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607922-Edit-Line-Style-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607942-Edit-Node-Style-Dialog)

# Edit Link Dialog

The Edit Link dialog helps you to [edit the link](https://devnet.logianalytics.com/hc/en-us/articles/1500009613322-Adding-Links-in-Reports#Edit) on an object. It appears when you select an object in a report which is defined with a link, right-click it and select Edit Link from the shortcut menu.

**Conditional Link**

Specifies whether it is a conditional link. If the option is selected, the object can be linked to different targets based on different conditions.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)  
   Adds a new condition in the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009607862-Edit-Conditions-Dialog) dialog.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404911588375/btn_edit.gif)  
   Edits the selected condition.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)  
   Removes the selected condition.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)  
   Moves the selected condition one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)  
   Moves the selected condition one step down.
* **Others**  
   If the option is selected, you can define to which target the object will be linked when none of the conditions you have specified is met.

**Link Type**

Specifies the type of the link target for the object if it is not a conditional link or for the object under the selected condition if it is a conditional link. It can be one of the following: [Report](#Report), [Master/Detail Report](#Detail), [URL](#URL), [E-mail](#Mail), [Content](#Content) (some types are available to specific report types).

**More**

Displays more link options. Available only for the Report, Master/Detail Report and Content link types.

**OK**

Accepts the link editing result and closes the dialog.

**Cancel**

Cancels the link editing process and exits the dialog.

**Help**

Displays the help document about this feature.

### Report

It helps you to link the object to a report.

![Edit Link dialog for Report](https://devnet.logianalytics.com/hc/article_attachments/4404904348055/edtlnk_rpt.gif)

**Report**

Specifies the target report. Select the Browse button to modify the desired report in the [Select a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009610142-Select-a-Report-Dialog) dialog.

**Report Tab**

Specifies the linked report tab. Available to page report only.

**Target**

Specifies the window or frame in which to load the linked report. Applied only when the link is triggered in Page Report Studio and Web Report Studio; when triggered in JDashboard, except for Same Frame, all the other targets are treated as New Window.

* **<Server Setting>**  
   Loads the linked report according to setting on Logi Report Server. For page report, you can set the Pop Up New Window for Links option in the Profile > Configure Profile > Page Report Studio > Properties > Default; for web report and library component, you can set the Target of Detail Table Report and Links option in the Profile > Configure Profile > Web Report Studio > Properties.
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
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)  
     Adds a component in the linked report to be interlinked with the primary report.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404911588375/btn_edit.gif)  
     Edits the component in the linked report to be interlinked with the primary report.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)  
     Removes the selected component.
* **Default Linked Component**  
   Specifies the component that is displayed by default in the linked report when the link is triggered in exported result.
* **Field Conditions**   
   Lists the filter conditions between the primary report and the linked report.
  + **Fields (Primary)**  
     Lists the selected fields in the data resource used by the selected component in the primary report.
  + **OP**  
     Specifies the operator to compose the condition. It can be "=", "<>", "<", ">", "<=", ">=" or "IN".
  + **Fields (Linked)**  
     Lists the fields in the data resource of the linked report which are of the same data type as the selected fields in the primary report.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)  
     Adds a new condition line.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)  
     Removes the selected conditions.
* **Pass on-screen filters to the linked components**  
  Specifies whether to apply the on-screen filters which refer to the filters created via filter controls in the primary report to the selected components of the linked report.
  + **Mapping Table**   
     Opens the [Mapping Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009609102-Mapping-Table-Dialog) dialog to define the mapping relationship based on which the on-screen filters in the primary report are passed to the linked report. Activated when the trigger component in the primary report and the selected component in the linked report use different datasets.

**Parameters tab**

This tab is available when the linked report uses parameters. It helps you to assign values to the parameters of the linked report automatically.

* **Parameter from Linked Report**  
   Lists all parameters contained in the data resources of the linked report.
* **Field from Primary Report**  
   Lists all the fields in the data resources of the primary report which are of the same data type as the parameters of the linked report. Select the field the value of which you want to assign to parameter of the linked report from the drop-down list. If the selected field is a parameter field, you can choose to assign its current value or initial value to the parameter of the linked report.
  + **Current Value**  
     If selected, the most recently specified value of the primary report parameter will be assigned to the parameter of the linked report.
  + **Initial Value**  
     If selected, the original value of the primary report parameter will be assigned to the parameter of the linked report.

**Advanced tab**

Specifies to pass the values of the filter objects such as filter controls in the primary report to those in the linked report. Not available for library component.

* **Primary Report Property/Object**  
   Displays the filter objects in the primary report the values of which will be passed to those in the linked report. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) to select a filter object in the primary report.
* **Linked Report Property/Object**  
   Displays the filter objects in the linked report which will adopt the values passed from filter objects in the primary report. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) to select a filter object in the linked report. You need to make sure that values of the filter object in the primary report can be applied to the filter object in the linked report in the same line.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)  
   Adds a new line to pass values between the filter objects in the primary report and the linked report.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)  
   Removes the selected lines.

**Pass style group information down to linked report**

Specifies whether or not to apply the style group of the primary report to the linked report.

### Master/Detail Report

It helps you to link the object to a detail report. Available to report that uses query resource as the data resource only.

![Edit Link dialog for Master/Detail Report](https://devnet.logianalytics.com/hc/article_attachments/4404904348311/edtlnk_dtl.gif)

**Report**

Specifies the report in which the detail report tab is. Select the Browse button to modify the desired report in the [Select a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009610142-Select-a-Report-Dialog) dialog.

**Report Tab**

Specifies the target detail report tab.

**Component**

Specifies the component in the detail report tab that will be interlinked with the master report. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) to add the components. You can add more than one component as long as the components are based on the same dataset.

**Target**

Specifies the window or frame where to load the detail report.

* **<Server Setting>**  
   Loads the detail report according to setting of the Pop up New Window for Links option in the Profile > Configure Profile > Page Report Studio > Properties > Default tab on Logi Report Server.
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

* **Column in Detail**  
   Specifies the field in the detail report which will be used to link the detail report with the master.
* **OP**  
   Specifies the operator. It can be "=", "<>", "<", ">", "<=" or ">=".
* **Column in Master**  
   Specifies the field in the master report.

**Conditions tab**

Specifies the filter conditions between the master report and the detail report.

* **Field Conditions**  
   Lists all the filter conditions.
  + **Fields (Master Report)**  
     Lists the selected fields of the master report.
  + **OP**  
     Specifies the operator to compose the condition. It can be "=", "<>", "<", ">", "<=" or ">=".
  + **Fields (Detail Report)**  
     Lists the DBFields in the datasets of the detail report which are of the same data type as the selected fields in the master report.
  + **More**  
     Specifies relations between two conditions. Can be AND or OR.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)  
     Adds a new condition line.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)  
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

It helps you to link the object to a location specified by a URL.

![Edit Link dialog for URL](https://devnet.logianalytics.com/hc/article_attachments/4404904348567/edtlnk_url.gif)

**Hyperlink**

Specifies the URL of the location that the object will be linked to.

* **Add Dynamic Field**   
   Opens the [Select Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009610322-Select-Field-Dialog) dialog to insert a field into the URL.

**Target**

Specifies the window or frame in which to load the location specified by the URL. Applied only when the link is triggered in Page Report Studio and Web Report Studio; when triggered in JDashboard, except for Same Frame, all the other targets are treated as New Window.

* **<Server Setting>**  
   Loads the linked file according to setting on Logi Report Server. For page report, you can set the Pop Up New Window for Links option in the Profile > Configure Profile > Page Report Studio > Properties > Default; for web report and library component, you can set the Target of Detail Table Report and Links option in the Profile > Configure Profile > Web Report Studio > Properties.
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

**IE Navigate2 Flags**

Specifies to use the IE Navigate2 method and its flags to control the behavior of IE when loading the linked file with Internet Explorer. Available only when the link is triggered in a table in Web Report Studio. This option applies to web report only, and it is available only when the link is triggered in a table in Web Report Studio.

**Flags**

Lists all the flags of the IE Navigate2 method. This option applies to web report only.

To make sure the navigate2 flags work well, clear the option **Enable Protected Mode** in Internet Options dialog > Security tab of the Internet Explorer browser, then select the **Custom level** button, in the Security Settings dialog, enable all ActiveX relative options under the ActiveX controls and plug-ins.

You can see that multiple flags can be selected at a time. Some of them may conflict with each other. The conflict relationship between the flags strictly follows the Microsoft MSDN specification. Logi Report loyally delivers the user state to the Microsoft interface and does not present or check the conflict.

When you create a new link to a URL, with none of the Navigate2 flags being selected, the linked file will be opened in the specified window if a window name is provided via the "Other Frame or Window" setting in the Target field. If the window name is not given, the linked file will be opened in a new window.

* **navOpenInNewWindow**  
   Opens the resource or file in a new window.
* **navNoHistory**  
   Does not add the resource or file to the history list. The new page replaces the current page in the list.
* **navNoReadFromCache**  
   Not implemented.
* **navNoWriteToCache**  
   Not implemented.
* **navAllowAutosearch**  
   If the navigation fails, the auto search functionality attempts to navigate common root domains (.com, .edu, and so on). If this also fails, the URL is passed to a search engine.
* **navHyperlink**  
   Internet Explorer 6 for Windows XP SP2 and later. If the navigation fails when a hyperlink is being followed, this constant specifies that the resource should then be bound to the moniker using the BINDF\_HYPERLINK flag.
* **navEnforceRestricted**  
   Internet Explorer 6 for Windows XP SP2 and later. Forces the URL into the restricted zone.
* **navNewWindowsManaged**  
   Internet Explorer 6 for Windows XP SP2 and later. Uses the default Popup Manager to block pop-up windows.
* **navUntrustedForDownload**  
   Internet Explorer 6 for Windows XP SP2 and later. Blocks files that normally trigger a file download dialog box.
* **navTrustedForActiveX**  
   Internet Explorer 6 for Windows XP SP2 and later. Prompts for the installation of ActiveX controls.
* **navKeepWordWheelText**  
   For Internet Explorer 7. Maintains state for dynamic navigation based on the filter string entered in the search band text box (wordwheel). Restores the wordwheel text when the navigation completes.
* **navVirtualTab**  
   For Internet Explorer 8. Opens the resource as a replacement for the current or target tab. The existing tab is closed while the new tab takes its place in the tab bar and replaces it in the tab group, if any. Browser history is copied forward to the new tab. On Windows Vista, this flag is implied if the navigation would cross integrity levels and navOpenInNewTab, navOpenInBackgroundTab, or navOpenInNewWindow is not specified.
* **navBlockRedirectsXDomain**  
   For Internet Explorer 8. Blocks cross-domain redirect requests. The navigation triggers the DWebBrowserEvents2::RedirectXDomainBlocked event if blocked.

### E-mail

It helps you to link the object to an e-mail address.

![Edit Link dialog for E-mail](https://devnet.logianalytics.com/hc/article_attachments/4404904348823/edtlnk_mail.gif)

**Hyperlink**

Specifies the [e-mail address](https://devnet.logianalytics.com/hc/en-us/articles/1500009613322-Adding-Links-in-Reports#MailSyntax) that the object will be linked to. Then after you select the trigger object, an e-mail will be popped with the information specified in the Hyperlink box. You can then further customize the e-mail and send it.

* **Add Dynamic Field**  
   Opens the [Select Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009610322-Select-Field-Dialog) dialog to insert a field into the e-mail address.

### Content

It helps you to link the object to a Blob data type field. The Blob data type field will be bound to the object and displayed as a hyperlink. You can download the Blob content by selecting this hyperlink. In Logi Report, Blob could be image, Binary, Blob, Clob, LongBlob, LongClob, Varbinary, Longvarbinary, and so on. Not available to page report that uses business view as the data resource.

![Edit Link dialog for Content](https://devnet.logianalytics.com/hc/article_attachments/4404904349079/edtlnk_cntnt.gif)

**Query**

Specifies the data resource which contains the required Blob data type field. Only data resources from the same data source connection as the current report are listed.

When you set the link type to Content, Logi Report will check whether there are such kind of data resources available. If not, options for this link type will be disabled.

**Content Type**

Specifies the content type for the Blob type data. You can select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404904189591/btn_fmla.gif) to bind it with a field column or a record level pass one formula in the selected query, or with a dynamic formula in the current report (available to web report and library component only).

**File Name**

Specifies the file name for the linked Blob type data. You can select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404904189591/btn_fmla.gif) to bind it with a field column or a record level pass one formula in the selected query.

**Content**

Specifies the Blob data type field in the selected query.

**Filter tab**

Specifies the link conditions between the data resource used by the current report and the data resource that contains the linked Blob content.

* **Field Conditions**   
   Lists the filter conditions between the two data resources.
  + **Fields (Primary)**  
     Lists the selected fields of the data resource used by the current report.
  + **OP**  
     Specifies the operator to compose the condition. It can be "=", "<>", "<", ">", "<=", ">=" or "IN".
  + **Fields (Linked)**  
     Lists the fields in the data resource that contains the linked Blob content, which are of the same data type as the selected fields in the data resource used by the current report.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)  
     Adds a new condition line.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)  
     Removes the selected conditions.

**Parameters tab**

This tab is available when the data resource that contains the linked Blob content uses parameters. It helps you to assign values to the parameters automatically.

* **Parameters**  
   Lists all the parameters the data resource that contains the linked Blob content uses.
* **Value**  
   Lists all the fields in the data resource used by the current report, which are of the same data type as the parameters the data resource that contains the linked Blob content uses. Select the field the value of which you want to assign to a parameter from the drop-down list.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607922-Edit-Line-Style-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607942-Edit-Node-Style-Dialog)
