---
title: "Lesson 3: Creating a Mailing Label Report"
id: 4405683496343
section: "Logi Report Tutorial v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683496343-Lesson-3-Creating-a-Mailing-Label-Report
updated_at: 2022-01-27T07:58:19Z
---

# Lesson 3: Creating a Mailing Label Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453376919/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683495191-Lesson-2-Creating-a-Horizontal-Banded-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420461444759/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683497367-Lesson-4-Creating-a-Chart-Report)

# Lesson 3: Creating a Mailing Label Report

In this lesson, we develop a Customer Contact Card report using the mailing label layout. The report users can use it to print rolodex cards and mailing labels. On each card, the following information needs to be shown:

![Report Sketch](https://devnet.logianalytics.com/hc/article_attachments/4420453741335/rpt_lsn3_card.gif)

The data source for this report is our built-in XML data, predefined as Data Source 2 in the catalog.

Follow these tasks to create the report:

* [Task 1: Define the Query the Report Uses](#Task1)
* [Task 2: Add Objects to the Report](#Task2)
* [Task 3: Edit Object Properties and Print the Report](#Task3)

## Task 1: Define the Query the Report Uses

1. In Designer, navigate to **File** > **New** > **Page Report**.
2. In the Select Component for Page Report dialog box, select **Mailing Label**, then select **OK**.

   Be sure that JinfonetGourmetJava.cat is the current catalog because it is the catalog we use in this track. For information about specifying this catalog, see [Task 1, Step 2 and 3](https://devnet.logianalytics.com/hc/en-us/articles/4405690446871-Lesson-1-Creating-a-Standard-Banded-Report#SelectCat) of Lesson 1.
3. In the **Data** screen of the Mailing Label Wizard dialog box, select **<New Query...>** in the Queries node of Data Source 2, type **CustomerContactCard** in the Enter Query Name dialog box and then select **OK**.

   ![New Query](https://devnet.logianalytics.com/hc/article_attachments/4420447418263/rpt_lsn3_qrynm.gif)
4. In the Add Tables/Views/Queries dialog box, expand the XML connection node and then the **Tables** node, then select the table **Customer** and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447410583/btn_addarw.gif) to add it to the query. Select **OK** to close the dialog box.
5. In the Query Editor dialog box, select all columns in the Customer table by choosing **\***, then clear the **NodePrimaryKey** and **NodeForeignKey** columns.

   ![Select Columns in Table](https://devnet.logianalytics.com/hc/article_attachments/4420453741591/rpt_lsn3_clmn.gif)
6. Select **OK** to create the query.
7. Select **Style** on the screen navigation bar to switch to the screen in the Mailing Label Wizard dialog box and select **Simple** as the report style.
8. Select **Finish** to create the report.

Designer creates the report with an empty banded object, and identifies the panels in the banded object on the left side by their abbreviations: a banded header panel (BH), a banded page header panel (BPH), a detail panel (DT), a banded page footer panel (BPF), and a banded footer panel (BF).

## Task 2: Add Objects to the Report

1. Select and resize the DT panel of the banded object, to make it similar to this:

   ![Resize Detail Panel](https://devnet.logianalytics.com/hc/article_attachments/4420447418519/rpt_lsn3_rszpnl.gif)

We want to use a simple formula to create a single value out of the customer's last and first names, and similarly to the address.

1. In the **Data** panel, select **<New Formula...>** in the Formulas node.

   ![New Formula](https://devnet.logianalytics.com/hc/article_attachments/4420447418775/rpt_lsn3_addfmla.gif)
2. Type the formula name **CustomerContactName** in the Enter Formula Name dialog box, select **OK**, define the formula in the Formula Editor dialog box as **`@ContactFirstName + " " + @ContactLastName`** (you can copy the formula to the formula editing area directly), select **Save** on toolbar, then close the editor.

   ![Edit Formula Expression](https://devnet.logianalytics.com/hc/article_attachments/4420447419031/rpt_lsn3_dfnfmla.gif)
3. Create another formula named **CustomerContactAddress** using the same way and define it as follows:

   `@Address1 + ", " + @City + ", " + @State + " " + @PostalCode`

We do not want to show the name labels of the DBFields in this report, so we can use one of the Designer's customizations that can simplify the creation of this report.

1. Navigate to **File** > **Options**.
2. In the Options dialog box, select **Component**, clear **Insert field name label with field** and select **OK**.

Now we can add our formulas and DBFields to the report.

1. From the **Data** panel, drag the **CustomerContactName** formula in the Formulas node to the DT panel of the banded object, and then the **ContactPosition** DBField in the Customer table to the right of it.

   ![Add Fields](https://devnet.logianalytics.com/hc/article_attachments/4420447419287/rpt_lsn3_drgfld.gif)
2. Use the same way to add the following fields:

   ![Add More Fields](https://devnet.logianalytics.com/hc/article_attachments/4420453741847/rpt_lsn3_addfld.gif)
3. Add two labels ahead of the **Phone** and **Fax** DBFields to identify them by dragging the **Label** icon ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4420447412375/btn_label.gif) from the **Components** panel. Resize the labels and edit their text to "**Phone:**" and "**Fax:**" respectively.

   ![Add Labels](https://devnet.logianalytics.com/hc/article_attachments/4420453742103/rpt_lsn3_lbl.gif)
4. Navigate to **Insert** > **Drawing Objects** > **Line** to insert a Line object above the CustomerName DBField.

   ![Insert Line](https://devnet.logianalytics.com/hc/article_attachments/4420447419543/rpt_lsn3_line.gif)
5. Select the DT panel of the banded object, then navigate to **Insert** > **Drawing Objects** > **Box** to add a Box object to enclose all the objects in the panel.  

   ![Insert Box](https://devnet.logianalytics.com/hc/article_attachments/4420453742487/rpt_lsn3_box.gif)
6. Resize the BPH panel, drag the **Label** icon ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4420447412375/btn_label.gif) from the **Components** panel to it to add a label in the panel, then resize the label and edit its text to **Customer Contact Card** as the title of the report.

   ![Add Report Title](https://devnet.logianalytics.com/hc/article_attachments/4420461798295/rpt_lsn3_title.gif)

## Task 3: Edit Object Properties and Print the Report

1. Select the label in the BPH panel and change its **Font Size** property to **14** and **Foreground** to **Red** in the Report Inspector.
2. Select all the objects in the DT panel except the Line and the Box drawing objects, then select **10** from the **Font Size** drop-down list ![Font Size button](https://devnet.logianalytics.com/hc/article_attachments/4420461798551/btn_fontsz.gif) on the **Format** menu tab.
3. Select the **CustomerContactName** formula and navigate to **Format** > **Bold**![Bold button](https://devnet.logianalytics.com/hc/article_attachments/4420453739159/btn_bold.gif).
4. In the Report Inspector, select the **Box** node from the report structure tree and change its **Border Color** property to **Lightgray**.

   ![Edit Border Color](https://devnet.logianalytics.com/hc/article_attachments/4420453742871/rpt_lsn3_color.gif)
5. Select the **Line** node and edit its **Line Color** property to **Lightgray** and **Line Thickness** to **0.02**.
6. Resize the fields horizontally to display the data completely.

   ![Report in Design View](https://devnet.logianalytics.com/hc/article_attachments/4420453743127/rpt_lsn3_dsgn.gif)
7. Hide the BH, BPF, and BF panels that do not hold any data by right-clicking the panel and selecting **Hide** from the shortcut menu.
8. On the report tab bar, right-click the report tab and select **Rename** to rename it to  **CustomerInformation**.

   ![Rename Report Tab](https://devnet.logianalytics.com/hc/article_attachments/4420447410839/renmrpttb.gif)
9. Navigate to **File** > **Save** to save the report as **CustomerContactCard.cls**.
10. Select the **View** tab to preview the report. Designer displays the report similar as follows:

    ![Preview Report](https://devnet.logianalytics.com/hc/article_attachments/4420447419799/rpt_lsn3_prvw.gif)

    The report displays as expected. We can print it to make the customer contact card now.
11. Navigate to **File** > **Print** and then specify the settings in the Print dialog box.
12. Navigate to **File** > **Options** again and select **Insert field name label with field** in the Component category, so that later when you add fields to reports, Designer adds their name labels automatically.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) If the report does not look correct, you can compare it to the final version of the report included in Designer. To do this, save and close your current catalog, and then open the **JinfonetGourmetJava.cat** catalog file in `<install_root>\Demo\Reports\TutorialReports`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453376919/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683495191-Lesson-2-Creating-a-Horizontal-Banded-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420461444759/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683497367-Lesson-4-Creating-a-Chart-Report)
