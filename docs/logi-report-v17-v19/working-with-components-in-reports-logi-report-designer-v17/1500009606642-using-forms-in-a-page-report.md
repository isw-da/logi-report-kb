---
title: "Using Forms in a Page Report"
id: 1500009606642
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009606642-Using-Forms-in-a-Page-Report
updated_at: 2021-07-24T16:05:10Z
---

# Using Forms in a Page Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606662-Using-Basic-Web-Controls-in-the-Configuration-Panel-of-a-Library-Component) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629421-Using-Advanced-Web-Controls)

# Using Forms in a Page Report

In order to make web controls accept user inputs and submit requests to Logi Report Server, you can add the web controls to a form and then define properties of the form.

This topic includes the following sections:

* [Creating Forms in a Page Report](#Create)
* [Adding Objects to a Form](#Add)
* [Making Web Controls Work in a Form](#Make)

## Creating Forms in a Page Report

To create a form in a page report, you can do either of the following:

* Drag ![Form button](https://devnet.logianalytics.com/hc/article_attachments/4404916826519/btn_instfrm.gif) from the Components panel to the report.
* Select **Insert** > **Web Controls > Form**.

The following are commands on the shortcut menu of a form:

* **Unmark Form**  
  Deselects this form.
* **Delete Form**  
   Deletes this form.
* **Remove All Controls**  
  Removes all the objects added to the form.
* **Properties**  
  Shows the properties of the form in the Report Inspector.
* **Save Style**   
  [Creates a CSS style](https://devnet.logianalytics.com/hc/en-us/articles/1500009636241-CSS-Styles#Create) for the form.

## Adding Objects to a Form

To add an object to a form, right-click the object, and on the shortcut menu, select the target form from the Add to Form submenu. The object can be added to a new form or an existing one. In Logi Report Designer, the icon ![Form icon](https://devnet.logianalytics.com/hc/article_attachments/4404904421271/btn_form.gif) represents a form. If you select the icon, you will find that the form and all the objects added to it are enclosed by a red dashed outline.

After an object has been added to a form, if you want to remove it from the form, you can right-click the object and select **Remove from Form** from the shortcut menu. You can remove all the objects that are added to a form simply by right-clicking the form and then selecting **Remove All Controls**.

## Making Web Controls Work in a Form

After adding web controls to a form, you need to make the web controls cooperate, that is, you must set some properties of the form so as to organize the web controls and define their working mode. To do this, select the form, go to the Report Inspector, and then edit the properties of the form.

Here is an example illustrating the use of form. In this example, a text field and a button in a report enable the report user to search for a particular string with Google.

1. Create a report which contains a blank flow report tab.
2. In the report tab, insert two web controls: a Text Field and a Button.
3. Right-click the text field, select **Display Type** from the shortcut menu, then in the Display Type dialog, set the following options (leave other options to the default values):

   **Name:** q  
   **Value:** "" (null)  
   **Max Length:** 30
4. Right-click the button, select **Display Type** on the shortcut menu and set the following options in the Display Type dialog:

   **Value:** Google  
   **Action:** Submit Form
5. Select the two web controls, then right-click and select **Add to Form** > **Add to New Form** from the shortcut menu.
6. Set the properties of the form in the Report Inspector as follows:

   **Form Action:** http://www.google.com/search  
   **Form Method:** get  
   **Form Target:** blank
7. Save the report and preview it in Page Report Studio.

   Now you can type a string up to 30 characters in the text field, and then select the button **Google** to search for that string. The search result will be displayed in a new browser window.

**Note:** For a table, if you add a field to a new form, the form will be created in the first cell of the table row which contains the field, and fields in the previous table rows cannot be added to this newly-created form. If you add columns before the first cell, then fields in these columns of the same table row also cannot be added to the form.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606662-Using-Basic-Web-Controls-in-the-Configuration-Panel-of-a-Library-Component) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629421-Using-Advanced-Web-Controls)
