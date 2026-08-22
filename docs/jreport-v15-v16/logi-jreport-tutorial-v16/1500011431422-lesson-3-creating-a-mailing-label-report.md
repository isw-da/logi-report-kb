---
title: "Lesson 3: Creating a Mailing Label Report"
id: 1500011431422
section: "Logi JReport Tutorial v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011431422-Lesson-3-Creating-a-Mailing-Label-Report
updated_at: 2021-07-24T10:39:40Z
---

# Lesson 3: Creating a Mailing Label Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011431442-Lesson-2-Creating-a-Horizontal-Banded-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011431402-Lesson-4-Creating-a-Chart-Report)

# Lesson 3: Creating a Mailing Label Report

In this lesson, we develop a Customer Contact Card report using the mailing label layout. This report can be used to print rolodex cards as well as mailing labels. On each card, the following information needs to be shown:

![Report Sketch](https://devnet.logianalytics.com/hc/article_attachments/4404909095575/rpt_lsn3_card.gif)

The data source for this report is our built-in XML data, predefined as Data Source 2 in the catalog.

Follow the tasks below to finish creating the report:

* [Task 1: Define the Query the Report Uses](#Task1)
* [Task 2: Add Objects to the Report](#Task2)
* [Task 3: Edit Object Properties and Print the Report](#Task3)

## Task 1: Define the Query the Report Uses

1. In Logi JReport Designer select **File** > **New** > **Page Report**.
2. In the Select Component for Page Report dialog, select **Mailing Label**, then select **OK**.

   Be sure that JinfonetGourmetJava.cat is specified as the current catalog because it is the catalog we use in this track. For information about specifying this catalog, see [Task 1, Step 2 and 3](https://devnet.logianalytics.com/hc/en-us/articles/1500011431462-Lesson-1-Creating-a-Standard-Banded-Report#SelectCat) of Lesson 1.
3. In the Data screen of the Mailing Label Wizard, select **<New Query...>** in the Queries node of Data Source 2, input **CustomerContactCard** in the Enter Query Name dialog and then select **OK**.

   ![New Query](https://devnet.logianalytics.com/hc/article_attachments/4404909095831/rpt_lsn3_qrynm.gif)
4. In the Add Tables/Views/Queries dialog, expand the XML connection node and then the **Tables** node, then select the table **Customer** and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901075351/btn_addarw.gif) to add it to the query. select **OK** to close the dialog.
5. In the Query Editor, select all columns in the Customer table by choosing **\*,** then uncheck the **NodePrimaryKey**  and **NodeForeignKey** columns.

   ![Select Columns in Table](https://devnet.logianalytics.com/hc/article_attachments/4404901089687/rpt_lsn3_clmn.gif)
6. Select **OK** at the bottom of the Query Editor to create the query.
7. Select **Style** to switch to the screen in the Mailing Label Wizard and select **Simple** as the report style, then select **Finish** to create the report.

The report with an empty banded object is created. The panels in the banded object are identified on the left side by their abbreviations: a banded header panel (BH), a banded page header panel (BPH), a detail panel (DT), a banded page footer panel (BPF) and a banded footer panel (BF).

## Task 2: Add Objects to the Report

1. Select and resize the DT panel of the banded object, to make it similar to the one below:

   ![Resize Detail Panel](https://devnet.logianalytics.com/hc/article_attachments/4404909096087/rpt_lsn3_rszpnl.gif)

We will use a simple formula to create a single value out of the customer's last and first names, and similarly to the address.

1. In the Data panel, select **<New Formula...>** in the Formulas node.

   ![New Formula](https://devnet.logianalytics.com/hc/article_attachments/4404901090071/rpt_lsn3_addfmla.gif)
2. Input the formula name **CustomerContactName** in the Enter Formula Name dialog, select **OK**, define the formula in the Formula Editor as **`@ContactFirstName + " " + @ContactLastName`** (you can copy the formula to the formula editing area directly), select **Save** on toolbar, then close the editor.

   ![Edit Formula Expression](https://devnet.logianalytics.com/hc/article_attachments/4404901090327/rpt_lsn3_dfnfmla.gif)
3. Create another formula named **CustomerContactAddress** using the same way and define it as follows:

   `@Address1 + ", " + @City + ", " + @State + " " + @PostalCode`

Now we will use one of the Logi JReport Designer's customizations that can simplify the creation of this report.

1. Select **File** > **Options**.
2. In the Options dialog, select **Component**, remove the checkmark from the **Insert field name label with field** checkbox and select **OK**.

We don't want to show the name labels of the DBFields in this report. Now we can add our formulas and DBFields to the report.

1. From the Data panel, drag the **CustomerContactName** formula in the Formulas node to the DT panel of the banded object, and then the **ContactPosition** DBField in the Customer table to the right of it.

   ![Add Fields](https://devnet.logianalytics.com/hc/article_attachments/4404901090583/rpt_lsn3_drgfld.gif)
2. Use the same way to add the following fields:

   ![Add More Fields](https://devnet.logianalytics.com/hc/article_attachments/4404909096343/rpt_lsn3_addfld.gif)
3. Add two labels ahead of the Phone and Fax DBFields to identify them by dragging ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404901080471/btn_label.gif) from the Basic group in the Components panel. Resize the labels and edit their text to "**Phone:**" and "**Fax:**" respectively, , then the report displays as follows.

   ![Add Labels](https://devnet.logianalytics.com/hc/article_attachments/4404909096599/rpt_lsn3_lbl.gif)
4. Insert a Line drawing object just above the CustomerName DBField by selecting **Insert** > **Drawing Objects** > **Line**.

   ![Insert Line](https://devnet.logianalytics.com/hc/article_attachments/4404901090839/rpt_lsn3_line.gif)
5. Select the DT panel of the banded object and add a Box drawing object to enclose all the objects in the panel by selecting **Insert** > **Drawing Objects** > **Box**.   

   ![Insert Box](https://devnet.logianalytics.com/hc/article_attachments/4404901091095/rpt_lsn3_box.gif)
6. Resize the BPH panel, drag ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404901080471/btn_label.gif) from the Basic group in the Components panel to add a label in it, then resize the label and edit its text to **Customer Contact Card** as the title of the report.

   ![Add Report Title](https://devnet.logianalytics.com/hc/article_attachments/4404901091351/rpt_lsn3_title.gif)

## Task 3: Edit Object Properties and Print the Report

1. Select the label in the BPH panel and change its Font Size to 14 and Foreground to Red in the Report Inspector.
2. Select all the objects in the DT panel except the Line and the Box drawing objects by holding the Ctrl key on the keyboard, then select **10** from the Format > Font Size drop-down list ![Font Size button](https://devnet.logianalytics.com/hc/article_attachments/4404909097111/btn_fontsz.gif).
3. Select the **CustomerContactName** formula and select **Format** > **Bold**![Bold button](https://devnet.logianalytics.com/hc/article_attachments/4404901085975/btn_bold.gif).
4. In the Report Inspector, select the **Box** node from the report structure tree and change its Border Color property to **Lightgray**.

   ![Edit Border Color](https://devnet.logianalytics.com/hc/article_attachments/4404901091607/rpt_lsn3_color.gif)
5. Select the **Line** node and edit its Line Color property to **Lightgray** and Line Thickness to **0.02**.
6. Resize the fields horizontally if data is truncated.

   ![Report in Design View](https://devnet.logianalytics.com/hc/article_attachments/4404901091863/rpt_lsn3_dsgn.gif)
7. Hide the BH, BPF and BF panels that don't hold any data by right-clicking the panel and select **Hide** from the shortcut menu.
8. On the report tab bar, right-click the report tab and select **Rename** to rename it to  **CustomerInformation**.

   ![Rename Report Tab](https://devnet.logianalytics.com/hc/article_attachments/4404901076631/renmrpttb.gif)
9. Select **File** > **Save** to save the report as **CustomerContactCard.cls**.
10. Select the **View** tab to preview the report. The report appears similar as follows:

    ![Preview Report](https://devnet.logianalytics.com/hc/article_attachments/4404901092247/rpt_lsn3_prvw.gif)

    The report displays as expected. We can print it to make the customer contact card now.
11. Select **File** > **Print** and then specify the settings in the Print dialog according to your requirements.
12. Select **File** > **Options** again to enable the **Insert field name label with field** option in the Component category, so that later when you add fields to reports, their name labels can be added automatically.

**Note:** If the report does not look correct, you can compare it to the final version of the report provided by Logi JReport. To do so, you will need to save and close this catalog and then open the JinfonetGourmetJava.cat catalog file located at `<install_root>\Demo\Reports\TutorialReports`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011431442-Lesson-2-Creating-a-Horizontal-Banded-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011431402-Lesson-4-Creating-a-Chart-Report)
