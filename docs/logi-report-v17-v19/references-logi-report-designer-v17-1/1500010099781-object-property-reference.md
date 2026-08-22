---
title: "Object Property Reference"
id: 1500010099781
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010099781-Object-Property-Reference
updated_at: 2021-07-23T19:16:19Z
---

# Object Property Reference

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060862-XML-Option-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061682-Report-Object-Properties)

# Object Property Reference

This topic introduces the properties of objects in Designer. It explains the [report object properties](https://devnet.logianalytics.com/hc/en-us/articles/1500010061682-Report-Object-Properties) shown in the Report Inspector and [catalog data object properties](https://devnet.logianalytics.com/hc/en-us/articles/1500010061302-Catalog-Data-Object-Properties) in the Catalog Manager respectively.

Keep in mind the following while browsing each object for its properties:

* You will start off from a table listing all the properties for an object and what can be achieved with each property.
* Some properties are just used to show related information and cannot be edited.
* Some properties can be [controlled by a formula or expression](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties). If a formula is selected to control a property, Designer generate it automatically as an expression prefixed by the "@" symbol. Also, some properties must be known by Logi Report Engine before a page break, so that it can lay out the object. In a formula or expression, the special field "PageNumber" is the switch for setting the page break calculation time. If the formula or expression uses "PageNumber", the calculation time is after the page break; otherwise, the calculation time is before the page break. For this reason, Logi Report sets the calculation time for controlling whether the formula or expression is marked as before page break or after page break. For most properties, you can control the property by formula or expression at any time without concerning about the page break.
* The same property for different objects usually means the same thing, unless otherwise stated.
* Designer determines the unit of the measurement properties like Width, Height, Thickness, and so on, by the [Units](https://devnet.logianalytics.com/hc/en-us/articles/1500010098161-Options-Dialog-Box#Display) setting in the Options dialog box, which can either be inch or centimeter.
* You can use the search box to easily locate the desired property of an object (to display the search box, select the **Search** icon ![Search icon](https://devnet.logianalytics.com/hc/article_attachments/4404856807959/btn_srch.gif) at the upper right corner of the Properties sheet). Designer closes the search box when you select another object.

  ![Qiuck Search Toolbar button](https://devnet.logianalytics.com/hc/article_attachments/4404848443543/btn_srchtlbr.gif)

  + **Text box**  
    Type the text you want to search for in the text box and Designer lists the properties containing the matched text.
  + ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404856816535/btn_close1.gif)**Delete icon**  
    Select to clear the text in the text box.
  + ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4404856853911/btn_srchtlbr_adv.gif)**Drop-down icon**  
    Select to list more search options.
    - **Highlight All**   
      Select to highlight all matched text.
    - **Match Case**   
      Select to search for text that meets the case of the typed text.
    - **Match Whole Word**   
      Select to search for text that looks the same as the typed text.
    - **Include Sub-Node**   
      Designer displays this option only for the search box in the Report Inspector. Select it if you want to perform the property searching within the property list of the selected object as well as those of its child objects.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) When you hover the mouse on any property, Designer displays a tip showing a brief description about the property. You can select the question mark icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404848443927/btn_tiphelp.gif) on the tip to open the corresponding help document or select the **Close** icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404848444183/btn_tipcls.gif) to close the tip. If you do not want to display the property tips, clear **Show tips** in the Options dialog box (File > Options > General > Show tips).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060862-XML-Option-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061682-Report-Object-Properties)
