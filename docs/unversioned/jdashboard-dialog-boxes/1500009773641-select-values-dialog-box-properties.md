---
title: "Select Values Dialog Box Properties"
id: 1500009773641
section: "JDashboard Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009773641-Select-Values-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:53Z
---

# Select Values Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745642-Select-Parameter-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745662-Send-Sync-Dialog-Box-Properties)

# Select Values Dialog Box Properties

Use the Select Values dialog box to specify one or more values to apply a filter criterion. This topic describes how to select filter values.

JDashboard displays the dialog box when you right-click on any value of a table detail field and select Filter > Select Values from the shortcut menu.

![Select Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880437271/slctvlu.gif)

**Available values**

Select the values to filter data with.

When there are more than 300 values, Logi Report uses Big Data Loading logic. In this case, the Shift Key for multiple selection does not work.

**Search**

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif)

Select to open the search bar to search for values.

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4404880162071/btn_srchtlbr.gif)

* **Text box**  
   Type the text you want to search for in the text box and Logi Report lists the values that contain the matched text.
* **X**  
   Select to close the search bar.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4404885330071/btn_srchtlbr_adv.gif)  
   Select to see more search options.
  + **Highlight All**   
    Select **Highlight All** to highlight all matched text.
  + **Match Case**   
    Select **Match Case** to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Select **Match Whole Word** to search for text that looks the same as the typed text.
  + **Advanced**  
    Select **Advanced** to display the search bar in the advanced mode. You can customize the value range with the advanced options.

    The advanced options on the search bar vary with field types:

    - **For fields of String type**

      ![Advanced Options - String Type](https://devnet.logianalytics.com/hc/article_attachments/4404880335255/btn_srchtlbr_string.gif)

      There are two search conditions. Select one and specify characters in the text box, then select **OK** to start searching. To clear the characters you enter, select **X** in the text box. Select **Cancel** to close the search bar.

      * **Start with**  
         First characters among the values.
      * **End with**  
         Last characters among the values.
    - **For fields of Numeric type**  

      ![Advanced Options - Numeric Type](https://devnet.logianalytics.com/hc/article_attachments/4404880335767/btn_srchtlbr_num.gif)

      There are five operators for composing the search condition. Select one from the operator drop-down list and type value in the text box to compose the condition, then select **OK** to start searching. To clear the value you enter, select **X** in the text box. Select **Cancel** to close the search bar.

      * **>**  
         Greater than
      * **>=**  
         Greater than or equal to
      * **<**  
         Less than
      * **<=**  
         Less than or equal to
      * **between**  
         The data values are between a range of values indicated by a start value and an end value. If you select **between**, the second input value should not be smaller than the first input value, otherwise the search result will be null.
    - **For fields of Date/Time type**

      ![Advanced Options - Date/Time Type](https://devnet.logianalytics.com/hc/article_attachments/4404885444759/btn_srchtlbr_date.gif)

      There are five [operators](#Operator) for composing the search condition. Select an operator from the operator drop-down list and select the **Calendar** icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404885317143/btn_clndr.gif) to select a value from the calendar to compose the condition, then select **OK** to start searching. Select **Cancel** to close the search bar.
* ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/4404880162711/btn_srchtlbr_prv.gif)  
   Select this button to go to the previous matched text if you did not clear **Highlight All**.
* ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/4404880162967/btn_srchtlbr_nxt.gif)  
   Select this button to go to the next matched text if you did not clear **Highlight All**.

![Clear button](https://devnet.logianalytics.com/hc/article_attachments/4404880145431/btn_clear.gif)**Clear**

Select to cancel the selection of values.

**OK**

Select **OK** to filter the field with the values you specified here.

**Cancel**

Select **Cancel** to close the dialog box without filtering the field.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select to view information about the Select Values dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select to close the dialog box without filtering the field.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745642-Select-Parameter-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745662-Send-Sync-Dialog-Box-Properties)
