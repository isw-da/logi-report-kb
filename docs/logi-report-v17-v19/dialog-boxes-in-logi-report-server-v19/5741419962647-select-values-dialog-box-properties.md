---
title: "Select Values Dialog Box Properties"
id: 5741419962647
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741419962647-Select-Values-Dialog-Box-Properties
updated_at: 2022-10-31T17:16:47Z
---

# Select Values Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741432374807-Select-Parameter-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741413207447-Send-Sync-Dialog-Box-Properties)

# Select Values Dialog Box Properties

You can use the Select Values dialog box to select one or more values of a field. This topic describes the properties in the dialog box.

Server displays the dialog box when you do either of the following:

* Right-click any value of a table detail field and select **Filter** > **Select Values** from the shortcut menu.
* In the [Incremental Condition dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741419595031-Incremental-Condition-Dialog-Box-Properties), select **More** in a value list.

![Select Values dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905759428247/slctvlu.gif)

**Available values**

Select the values you want to filter data with.

When there are more than 300 values, Server uses the Big Data Loading logic. In this case, the Shift Key for multiple selection does not work.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/9905577660311/btn_srch.gif)**Search button**

Select to open the search bar to search for values.

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/9905619099031/btn_srchtlbr.gif)

* **Text box**  
   Type the text you want to search for in the text box, and Server lists the values that contain the matched text.
* **X****Close button**  
   Select to close the search bar.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/9905631409303/btn_srchtlbr_adv.gif)**More button**  
   Select to see more search properties.
  + **Highlight All**   
    Select to highlight all matched text.
  + **Match Case**   
    Select to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Select to search for text that looks the same as the typed text.
  + **Advanced**  
    Select to display the search bar in the advanced mode. You can customize the value range using the advanced properties.

    The advanced properties on the search bar vary with field types:

    - **For fields of String type**

      ![Advanced Options - String Type](https://devnet.logianalytics.com/hc/article_attachments/9905717629079/btn_srchtlbr_string.gif)

      Server provides two search conditions. Select one and specify characters in the text box, then select **OK** to start searching. To clear the text you enter, select the Remove button **X** in the text box. Select **Cancel** to close the search bar.

      * **Start with**  
         First characters among the values.
      * **End with**  
         Last characters among the values.
    - **For fields of Numeric type**  

      ![Advanced Options - Numeric Type](https://devnet.logianalytics.com/hc/article_attachments/9905717661463/btn_srchtlbr_num.gif)

      Server provides five operators for composing the search condition. Select one from the operator list and type value in the text box to compose the condition, then select **OK** to start searching. To clear the value you enter, select **X** in the text box. Select **Cancel** to close the search bar.

      * **>**  
         Greater than
      * **>=**  
         Greater than or equal to
      * **<**  
         Less than
      * **<=**  
         Less than or equal to
      * **between**  
         The data values are between a range of values indicated by a start value and an end value. If you select **between**, the second input value should not be smaller than the first one, otherwise the search result will be null.
    - **For fields of Date/Time type**

      ![Advanced Options - Date/Time Type](https://devnet.logianalytics.com/hc/article_attachments/9905717695255/btn_srchtlbr_date.gif)

      Server provides five [operators](#Operator) for composing the search condition. Select an operator from the operator list and select the Calendar icon ![](https://devnet.logianalytics.com/hc/article_attachments/9905617212951/btn_clndr.gif) to select a value from the calendar to compose the condition, then select **OK** to start searching. Select **Cancel** to close the search bar.
* ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/9905631449623/btn_srchtlbr_prv.gif)**Previous button**  
   Select to go to the previous matched text if you did not clear **Highlight All**.
* ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/9905619191959/btn_srchtlbr_nxt.gif)**Next button**  
   Select to go to the next matched text if you did not clear **Highlight All**.

![Clear button](https://devnet.logianalytics.com/hc/article_attachments/9905617258903/btn_clear.gif)**Clear button**

Select to cancel the selection of values.

**OK**

Select to filter the field with the values you specified here.

**Cancel**

Select to close the dialog box without filtering the field.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the Select Values dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without filtering the field.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741432374807-Select-Parameter-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741413207447-Send-Sync-Dialog-Box-Properties)
