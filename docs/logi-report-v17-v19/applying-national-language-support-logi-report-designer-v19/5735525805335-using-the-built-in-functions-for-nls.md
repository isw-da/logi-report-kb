---
title: "Using the Built-in Functions for NLS"
id: 5735525805335
section: "Applying National Language Support - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735525805335-Using-the-Built-in-Functions-for-NLS
updated_at: 2022-11-02T08:07:47Z
---

# Using the Built-in Functions for NLS

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735568330007-Creating-NLS-Property-Files)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735525819287-Localizing-Page-Navigation-Links-in-HTML-Output)

# Using the Built-in Functions for NLS

Logi Report provides two built-in Translate functions for applying NLS to the formula result. This topic introduces the two functions briefly and presents an example to show the usage of the functions.

This topic contains the following sections:

* [The Translate Functions](#Function)
* [Example: Calling the Translate Functions in a Formula](#Example)

## The Translate Functions

You can call the following Translate functions in formulas to display the formula result in another language.

* **Translate(String a)**  
  This function searches for the NLS translation of the current field values in the bound data mapping file.
* **Translate(String a, String b)**  
  This function accesses the corresponding data mapping file dynamically according to the language you select from the language drop-down list on the NLS language toolbar and searches for the NLS translation of "String b" in it.

## Example: Calling the Translate Functions in a Formula

This example shows how you can call a Translate function in a formula to display the formula result in Chinese.

1. Navigate to **Home** > **Open** to open the page report **List of Customer Contact Cards.cls** in the catalog file **SampleReports.cat** saved in `<install_root>\Demo\Reports\SampleReports`.
2. Select the **View** tab to preview the report.

   ![View the report](https://devnet.logianalytics.com/hc/article_attachments/9898476415127/nls_rpt_fctn_vw.gif)
3. Select the **Design** tab to return to design mode.
4. Navigate to **View** > **Language** > **NLS Editor**.
5. In the NLS Editor dialog box, select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) above the **Language** box.
6. In the Add Language dialog box, select **Chinese (China)** from the **Available Languages** list and select **OK** to add it to the Language box of the NLS Editor dialog box.

   ![Add Language to NLS Editor](https://devnet.logianalytics.com/hc/article_attachments/9898459406871/nls_rpt_fctn_nlsedtr.gif)
7. Select **OK** in the NLS Editor dialog box.
8. Open the Catalog Manager and select **Data Mapping Editor** on its toolbar.
9. In the Data Mapping Editor dialog box, select **New**.
10. In the Create Data Mapping File dialog box, type **DataMapping** in the **File Name** text box and select **Chinese (China)** from the **Language** drop-down list. Select **OK** to go back to the Data Mapping Editor dialog box.

    ![Create Data Mapping File](https://devnet.logianalytics.com/hc/article_attachments/9898476470679/nls_rpt_fctn_dtmp.gif)
11. Select **Import Key**.
12. In the Import Key dialog box, select the **City** and **State** fields in the **Customers** table and select **OK**.

    ![Import Key dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898476478615/nls_rpt_fctn_imptkey.gif)
13. In the Data Mapping Editor dialog box, double-click cells in the **Map to Value** column to specify the mapping values for the two fields in Chinese. Select **OK**.
14. Navigate to the **Data Source 1** > **jdbc connection** > **Tables** > **Customers** node in the Catalog Manager, select the **City** column, select **Show Properties** to expand the Properties sheet on the right, then select **DataMapping** from the **Data Mapping File** property value drop-down list.
15. Repeat the preceding step to set the Data Mapping File property of the **State** column in the same table to DataMapping.
16. Select **Save Catalog** on the Catalog Manager toolbar to save the changes.
17. Right-click the **CustomerCityStateZip** formula field in the report and select **Edit** from the shortcut menu. The formula expression is:

    ![CustomerCityStateZip Formula](https://devnet.logianalytics.com/hc/article_attachments/9898459469335/nls_rpt_fctn_fmla.gif)
18. Edit the formula to **`Translate(@City) + ", " + Translate(@State) + "  " + Translate(@"Postal Code")`**, then select **Save** on the toolbar to save the formula. Close the Formula Editor dialog box.

    ![Rewrite CustomerCityStateZip Formula](https://devnet.logianalytics.com/hc/article_attachments/9898459479063/nls_rpt_fctn_fmla1.gif)

    If you have not set the data mapping file of the two table columns, you can also edit the formula as follows to apply the NLS feature:

    `Translate("DataMapping", @City)+ ", " +Translate("DataMapping", @State) + "  " + Translate("DataMapping", @"Postal Code")`.

To completely display the Chinese characters in the report, next we need to edit the font properties for the CustomerCityStateZip formula field.

1. Select **CustomerCityStateZip** in the report again, then set its **Font Face** property to **SimSun** and **Font Size** property to **12** in the Report Inspector.
2. Save the report.
3. Navigate to **View** > **Language** > **Chinese (China)**.
4. Preview the report again. Designer displays the formula result in Chinese.

   ![View Translated Report](https://devnet.logianalytics.com/hc/article_attachments/9898476521879/nls_rpt_fctn_vw1.gif)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* When you call either of the two Translate functions in a formula, you should not use the formula to perform further calculation unless you can make sure it is correct.
* When a formula references a parameter and the parameter's Allow Multiple Values property is "true", the two Translate functions are not available in the Formula Editor dialog box. In this case, if you want to apply NLS in the formula result, you can bind the data mapping file to the formula directly.
* You can also call the two Translate functions in formulas on Server, but they take effect only when the bound data mapping file exists on Server. Moreover, only when you have applied the data mapping file in Designer, you can publish it to Server together with the object it is bound to.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735568330007-Creating-NLS-Property-Files)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735525819287-Localizing-Page-Navigation-Links-in-HTML-Output)
