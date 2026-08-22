---
title: "Select Values Dialog Box Properties"
id: 5741446661015
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741446661015-Select-Values-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:43Z
---

# Select Values Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741460010519-Select-Value-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741459816727-Series-Options-Dialog-Box-Properties)

# Select Values Dialog Box Properties

You can use the Select Values dialog box to select one or more values of a field. This topic describes the properties in the dialog box.

Server displays the dialog box when you do either of the following:

* Right-click any value of a detail field in a table or banded object, and then select **Filter** > **Select Values** from the shortcut menu.
* In the [Edit Dataset Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/7985329714327-Edit-Dataset-Filter-Dialog-Box-Properties) or [Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741449994391-Filter-Dialog-Box-Properties), select **More** in a value list.

![Select Values dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905679038999/slctvalue.gif)

**Available Values**

Select the values you want to filter data with. You can select multiple values at a time.

When there are more than 300 values, Server uses the Big Data Loading logic. In this case, the Shift Key for multiple selection does not work.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/9905577660311/btn_srch.gif)**Search button**

Select to launch the search bar to search for values.

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/9905619099031/btn_srchtlbr.gif)

* **Text box**  
   Type the text you want to search for. Server lists the values containing the matched text.
* **X****Close button**  
   Select to close the search bar.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/9905631409303/btn_srchtlbr_adv.gif)**More button**  
   Select to show more search properties.
  + **Highlight All**  
     Select to highlight all matched text.
  + **Match Case**  
     Select to search for text that meets the case of the typed text.
  + **Match Whole Word**  
     Select to search for text that looks the same as the typed text.
  + **Advanced**  
     Select to display the search bar in the advanced mode. Then, you can customize the value range as you want.

    The advanced properties available on the search bar vary with field types:

    - **For a field of the String type**

      ![Advanced - String Fields](https://devnet.logianalytics.com/hc/article_attachments/9905717629079/btn_srchtlbr_string.gif)

      There are two search conditions. Select one and type characters, then select **OK** to start searching. To clear the characters, select **X**. Select **Cancel** to close the search bar.

      * **Start with**  
         Select to search for the first characters among the values.
      * **End with**  
         Select to search for the last characters among the values.
    - **For a field of Numeric type**  

      ![Advanced - Numeric Fields](https://devnet.logianalytics.com/hc/article_attachments/9905717661463/btn_srchtlbr_num.gif)

      You can use five operators for composing the search condition. Select one from the operator list, type value in the text box, then select **OK** o start searching. To clear the value, select **X** in the text box. Select **Cancel** to close the search bar.

      * **>**  
         Greater than
      * **>=**  
         Greater than or equal to
      * **<**  
         Less than
      * **<=**  
         Less than or equal to
      * **between**  
         Server locates the data values between a range of values indicated by a start value and an end value. The second value should not be smaller than the first value, otherwise the search result will be null.
    - **For a field of Date/Time type**

      ![Advanced - Date/Time Fields](https://devnet.logianalytics.com/hc/article_attachments/9905717695255/btn_srchtlbr_date.gif)

      You can use five [operators](#Operator) for composing the search condition. Select one from the operator list, select the **Calendar** icon ![](https://devnet.logianalytics.com/hc/article_attachments/9905617212951/btn_clndr.gif) to select a value from the calendar, then select **OK** to start searching. Select **Cancel** to close the search bar.
* ![Previous button](https://devnet.logianalytics.com/hc/article_attachments/9905631449623/btn_srchtlbr_prv.gif)  
   When you selected **Highlight All**, you can use this button to go to the previous matched text.
* ![Next button](https://devnet.logianalytics.com/hc/article_attachments/9905619191959/btn_srchtlbr_nxt.gif)  
   When you selected **Highlight All**, you can use this button to go to the next matched text.

![Clear button](https://devnet.logianalytics.com/hc/article_attachments/9905617258903/btn_clear.gif)**Clear button**

Select to cancel the selection of values.

**OK**

Select to apply the values you specified here.

**Cancel**

Select to cancel the selection of field values and close the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to cancel the selection of field values and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741460010519-Select-Value-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741459816727-Series-Options-Dialog-Box-Properties)
