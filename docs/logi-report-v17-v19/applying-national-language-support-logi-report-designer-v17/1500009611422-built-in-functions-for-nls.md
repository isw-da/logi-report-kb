---
title: "Built-in Functions for NLS"
id: 1500009611422
section: "Applying National Language Support - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009611422-Built-in-Functions-for-NLS
updated_at: 2021-07-24T16:03:51Z
---

# Built-in Functions for NLS

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611442-Creating-NLS-Property-Files) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009634441-Localizing-Page-Navigation-Links-in-HTML-Report-Outputs)

# Built-in Functions for NLS

Two built-in [Translate functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009605182-Appendix-1-Formula-Functions#Translate) are available in formulas for applying the NLS feature to the formula result.

* **Translate(String a)**  
  This function searches for the NLS translation of the current field values in the bound data mapping file.
* **Translate(String a, String b)**  
   This function accesses the corresponding data mapping file dynamically according to the language selected from the language drop-down list on the NLS language toolbar and searches for the NLS translation of String b in it.

The following example shows the usage of the two functions. It is based on the page report List of Customer Contact Cards.cls in the SampleReports.cat catalog file.

1. Select **Home** > **Open** to open the page report List of Customer Contact Cards.cls in the catalog SampleReports.cat saved in `<install_root>\Demo\Reports\SampleReports`.
2. Preview the report and it displays as follows:

   ![View the report](https://devnet.logianalytics.com/hc/article_attachments/4404904217751/nls_rpt_fctn_vw.gif)
3. Select the **Design** tab to return to the design mode.
4. Select **View** > **Language** > **NLS Editor**.
5. In the NLS Editor, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) above the Language box.
6. In the Add Language dialog, select **Chinese (China)** from the Available Languages list and select **OK** to add it to the Language box of the NLS Editor.

   ![Add Language to NLS Editor](https://devnet.logianalytics.com/hc/article_attachments/4404911661079/nls_rpt_fctn_nlsedtr.gif)
7. select **OK** in the NLS Editor.
8. Open the Catalog Manager and select **Data Mapping Editor** on its toolbar.
9. In the Data Mapping Editor, select the **New** button.
10. In the Create Data Mapping File dialog, type **DataMapping** in the File Name text box and select **Chinese (China)** from the Language drop-down list. Select **OK** to go back to the Data Mapping Editor.

    ![Create Data Mapping File](https://devnet.logianalytics.com/hc/article_attachments/4404911661335/nls_rpt_fctn_dtmp.gif)
11. Select the **Import Key** button, select the fields **City** and **State** in the Customers table of the displayed dialog and select **OK**.

    ![Import Key dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904218007/nls_rpt_fctn_imptkey.gif)
12. Double-click cells in the Map to Value column to specify the mapping values for the imported resources in Chinese. Select **OK**.
13. Expand **Data Source 1** > **jdbc connection** > **Tables** > **Customers** node in the Catalog Manager, select the **City** column, select the **Show Properties** button to expand the Properties sheet on the right, then select **DataMapping** from the Data Mapping File property value drop-down list.
14. Repeat the step above to set the Data Mapping File property of the column State in the same table to DataMapping.
15. Select **Save Catalog** on the Catalog Manager toolbar to save the changes.
16. Right-click the formula field **CustomerCityStateZip** in the report and select **Edit** from the shortcut menu. The formula is written as below in the Formula Editor:

    ![CustomerCityStateZip Formula](https://devnet.logianalytics.com/hc/article_attachments/4404904218263/nls_rpt_fctn_fmla.gif)
17. Edit the formula to **Translate(@City) + ", " + Translate(@State) + "  " + Translate(@"Postal Code")**, then select **Save** on the toolbar to save the formula. Close the Formula Editor.

    ![Rewrite CustomerCityStateZip Formula](https://devnet.logianalytics.com/hc/article_attachments/4404911662103/nls_rpt_fctn_fmla1.gif)

    If you have not set the data mapping file of the table columns, you can also edit the formula as follows to apply the NLS feature: Translate("DataMapping", @City)+ ", " +Translate("DataMapping", @State) + "  " + Translate("DataMapping", @"Postal Code").

To make the Chinese characters displayed completely in the report, next we need to edit the font properties for the formula field CustomerCityStateZip.

1. Select the formula **CustomerCityStateZip** in the report, then set its Font Face property to **SimSun** and Font Size property to **12** in the Report Inspector.
2. Select **File** > **Save** to save the report.
3. Select **View** > **Language** > **Chinese (China)**.
4. Preview the report and you can find the formula result is displayed in Chinese:

   ![View Translated Report](https://devnet.logianalytics.com/hc/article_attachments/4404911662359/nls_rpt_fctn_vw1.gif)

**Notes:**

* When either of the two functions is called in a formula, you are suggested not to use the formula to do further calculation unless you can make sure it is correct.
* When a formula references a parameter and the parameter's Allow Multiple Values property is true, the two functions are not available in the Formula Editor for editing the formula. In this case, if you want to apply NLS in the formula result, you can bind the data mapping file to the formula directly.
* The two functions can also be called in formulas on Logi Report Server, but they take effect only when the bound data mapping file exists in Logi Report Server. Moreover, only when the data mapping file is used in Logi Report Designer, can it be published to Logi Report Server together with the object it is bound to.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611442-Creating-NLS-Property-Files) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009634441-Localizing-Page-Navigation-Links-in-HTML-Report-Outputs)
